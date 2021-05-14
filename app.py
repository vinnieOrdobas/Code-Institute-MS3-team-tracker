import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
import bson
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_teams")
def get_teams():
    teams = mongo.db.teams.find()
    return render_template("teams.html", teams=teams)


# --------------------------------User functions---------------------- #
@app.route("/get_trainings")
def get_trainings():
    username = mongo.db.users.find_one(
        {'username': session['user']})
    is_instructor = True if mongo.db.instructors.find_one(
        {'username': session['user']}) else False
    trainings = list(mongo.db.trainings.find())
    students = list(mongo.db.users.find(
        {"student": True}))
    training_types = mongo.db.training_types.find().sort('training_type', 1)
    return render_template("trainings.html",
    trainings=trainings, username=username,
        is_instructor=is_instructor, students=students,
            training_types=training_types)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        password = request.form.get('password')
        check_password = request.form.get('check_password')

        if password == check_password:
            team_leader = "on" if request.form.get('team_leader') else "off"
            instructor = "on" if request.form.get('instructor') else "off"
            register = {
                'username': request.form.get('username').lower(),
                'password': generate_password_hash(
                            request.form.get('password'), salt_length=7),
                'alias': request.form.get('alias'),
                'team_name': request.form.get('team_name'),
                'team_leader': team_leader
            }
            if team_leader and instructor == 'off':
                register['student'] = True
                register['trainings'] = {}
            mongo.db.users.insert_one(register)
            if instructor == "on":
                submit = {
                    "instructor_name": request.form.get('alias'),
                    "username": request.form.get('username').lower()
                }
                mongo.db.instructors.insert_one(submit)
            # put the new user into 'session' cookie
            session["user"] = request.form.get('username').lower()
            flash('Registration Successful!')
            return redirect(url_for('profile', username=session['user']))
        else:
            flash("Password doesn't match!")
            return redirect(url_for('register'))
    teams = mongo.db.teams.find().sort('team_name', 1)
    return render_template("register.html", teams=teams)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                alias = existing_user['alias']
                flash(f'Welcome, {alias}')
                return redirect(url_for(
                    'profile', username=session['user']))
            else:
                # invalid password match
                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash('Incorrect Username and/or Password')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    # grab the session's user's username from db
    username = mongo.db.users.find_one(
        {'username': session['user']})['alias']

    if session['user']:
        return render_template('profile.html', username=username)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # remove user from session cookies
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


# --------------------------------Training functions---------------------- #
@app.route("/add_training", methods=['GET', 'POST'])
def add_training():
    # adds training to the database
    if request.method == 'POST':
        existing_training = mongo.db.users.find_one(
            {'training_name': request.form.get('training_name')})
        if existing_training:
            flash('Training already exists')
            return redirect(url_for('add_training'))
        training = {
            "team_name": request.form.get('training_team'),
            "training_name": request.form.get('training_name'),
            "training_description": request.form.get('training_description'),
            "training_date": request.form.get('due_date'),
            "training_cycle": {},
            "created_by": session['user'],
            "complete_training": "False"
        }
        assigned_to = request.form.getlist('assign_to')
        for user in assigned_to:
            # get students alias from the form
            student = mongo.db.users.find_one({'alias': user})
            # find students on the database
            trainings = student['trainings']
            # appends new training to returning dictionary
            training_schema = {
                request.form.get('training_name'): {}
            }
            trainings.update(training_schema)
            # updates training dictionary to push to student
            mongo.db.users.update_one(
                {'alias': user},
                {'$set': {'trainings': trainings}})
        # push training to database
        mongo.db.trainings.insert_one(training)
        flash("Training Successfully Created")
        return redirect(url_for('get_trainings'))
    # variables to be rendered by the template
    teams = mongo.db.teams.find().sort('team_name', 1)
    students = list(mongo.db.users.find({"student": True}).sort('alias', 1))
    return render_template('add_training.html', teams=teams, students=students)


@app.route("/edit_training/<training_id>", methods=['GET', 'POST'])
def edit_training(training_id):
    # Edit trainings in the database
    if request.method == 'POST':
        training_name = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_name']
        training_cycle = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_cycle']
        training = {
            "team_name": request.form.get('training_team'),
            "training_name": request.form.get('training_name'),
            "training_description": request.form.get('training_description'),
            "training_date": request.form.get('due_date'),
            "training_cycle": training_cycle,
            "created_by": session['user'],
            "complete_training": "False"
        }
        # --> Edits training for enrolled students <--
        # Find students on the database
        students = mongo.db.users.find(
            {f"trainings.{training_name}": {'$exists': "true"}})
        for student in students:
            mongo.db.users.update(
                {'username': student.get("username")},
                {'$rename':
                    {f"trainings.{training_name}":
                        f"trainings.{request.form.get('training_name')}"}})
    # Updates training on database
        mongo.db.trainings.update({'_id': ObjectId(training_id)}, training)
        flash("Training Successfully Edited")
        return redirect(url_for('get_trainings'))
    # variables to be rendered by the template
    training = mongo.db.trainings.find_one({'_id': ObjectId(training_id)})
    teams = mongo.db.teams.find().sort('team_name', 1)
    students = list(mongo.db.users.find({"student": True}).sort('alias', 1))
    return render_template('edit_training.html',
            teams=teams, training=training, students=students)


@app.route("/delete_training/<training_id>")
def delete_training(training_id):
    # finds training name
    training_name = mongo.db.trainings.find_one(
        {'_id': ObjectId(training_id)})['training_name']
    # finds students
    students = mongo.db.users.find(
        {f"trainings.{training_name}": {'$exists': "true"}})
    for student in students:
        user = student['alias']
        training_folder = student['trainings']
        del training_folder[training_name]
        mongo.db.users.update_one(
                {'alias': user},
                {'$set': {'trainings': training_folder}})
    # deletes training from database
    mongo.db.trainings.remove({'_id': ObjectId(training_id)})
    flash("Training successfully removed")
    return redirect(url_for('get_trainings'))


@app.route("/enroll_training/<training_id>", methods=['GET', 'POST'])
def enroll_training(training_id):
    if request.method == 'POST':
        # --> Assigns training for new students <--
        training_name = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_name']
        training_cycle = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_cycle']
        assigned_to = request.form.getlist('assign_to')
        for user in assigned_to:
            # get students alias from the form
            student = mongo.db.users.find_one({'alias': user})
            # find students on the database
            training_folder = student['trainings']
            # appends new training to returning dictionary
            training_schema = {
                training_name: training_cycle
                }
            training_folder.update(training_schema)
            # updates training dictionary to push to student
            mongo.db.users.update_one(
                {'alias': user},
                {'$set': {'trainings': training_folder}})
    flash("Student successfully enrolled")
    return redirect(url_for('get_trainings'))


# --------------------------------Cycle functions---------------------- #
@app.route("/add_cycle/<training_id>", methods=['GET', 'POST'])
def add_cycle(training_id):
    if request.method == 'POST':
        training_folder = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_cycle']
        if request.form.get('training_type') in training_folder.keys():
            flash(f"{request.form.get('training_type')} cycle already exists")
        else:
            training_name = mongo.db.trainings.find_one(
                {'_id': ObjectId(training_id)})['training_name']
            new_cycle = request.form.get('training_type')
            students = list(mongo.db.users.find(
                {f"trainings.{training_name}": {'$exists': "true"}}))
            cycle = {
                request.form.get('training_type'): {
                    "training_link": request.form.get('training_link'),
                    "instructor": request.form.get('instructor_name'),
                    "completed": False,
                    "training_date": request.form.get('due_date')
                    }
                }
            for student in students:
                current_cycle = student['trainings'][training_name]
                current_cycle.update(cycle)
                mongo.db.users.update_one(
                    {'username': student['username']},
                    {'$set': {f'trainings.{training_name}':
                        current_cycle}}, upsert= True)
            training_folder[new_cycle] = cycle[new_cycle]
            mongo.db.trainings.update_one(
                {'_id': ObjectId(training_id)},
                {'$set':
                    {'training_cycle': training_folder}})
            flash("Training Cycle Successfully Created")
            return redirect(url_for('get_trainings'))
    training = mongo.db.trainings.find_one({'_id': ObjectId(training_id)})
    instructors = mongo.db.instructors.find().sort('instructor_name', 1)
    training_types = mongo.db.training_types.find().sort('training_type', 1)
    return render_template('add_cycle.html',
        instructors=instructors, training=training,
        training_types=training_types)


@app.route("/complete_cycle/<training_id>", methods=['GET', 'POST'])
def complete_cycle(training_id):
    # marks training as complete
    if request.method == 'POST':
        # finds training name
        training_name = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_name']
        current_cycle = request.form.get('cycle_name')
        students = mongo.db.users.find(
            {f"trainings.{training_name}": {'$exists': "true"}})
        # finds students
        for student in students:
            user = student['alias']
            mongo.db.users.update_one(
                {'alias': user},
                {'$set':
                    {f'trainings.{training_name}.{current_cycle}.completed':
                        True}})
#       sets training to complete on training's record
        mongo.db.trainings.update_one(
                {'_id': ObjectId(training_id)},
                {'$set':
                    {f'training_cycle.{current_cycle}.completed': True}})
    return redirect(url_for('get_trainings'))


@app.route("/incomplete_training/<training_id>", methods=['GET', 'POST'])
def incomplete_cycle(training_id):
    if request.method == 'POST':
        # finds training name
        training_name = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_name']
        current_cycle = request.form.get('cycle_name_switch')
        students = mongo.db.users.find(
            {f"trainings.{training_name}": {'$exists': "true"}})
        # finds students
        for student in students:
            user = student['alias']
            mongo.db.users.update_one(
                {'alias': user},
                {'$set':
                    {f'trainings.{training_name}.{current_cycle}.completed':
                        False}})
#       sets training to complete on training's record
        mongo.db.trainings.update_one(
                {'_id': ObjectId(training_id)},
                {'$set':
                    {f'training_cycle.{current_cycle}.completed': False}})
    return redirect(url_for('get_trainings'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
