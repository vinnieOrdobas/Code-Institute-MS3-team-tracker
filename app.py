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


# Helper functions
def reset_access(user):
    '''
    Resets user's access in the database
    '''
    access = ['student', 'team_leader', 'instructor']
    for key in access:
        if key in user.keys():
            mongo.db.users.update({
                'username': user['username']
            }, {
                '$set': {key: False}
            })
# Server routes


@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")


# Team endpoints


@app.route("/get_teams")
def get_teams():
    # Finds current user
    username = mongo.db.users.find_one(
        {'username': session['user']})
    if username.get('admin'):
        # Finds staff per team
        teams = list(mongo.db.teams.aggregate([
            {'$lookup': {
                'from': 'users',
                'localField': 'team_name',
                'foreignField': 'team_name',
                'as': 'users'
            }},
            {'$project': {'team_name': 1, 'team_region': 1,
                          'team_description': 1, 'users.alias': 1,
                          'users.team_leader': 1, 'users.student': 1,
                          'users.instructor': 1}}
        ]))
    else:
        # User is not admin, gets user's team staff
        teams = mongo.db.teams.find({
            'team_name': username['team_name']
        })
    students = list(mongo.db.users.find({
        'student': True,
        'team_name': username['team_name']
    }))
    team_leader = list(mongo.db.users.find({
        'team_leader': True,
        'team_name': username['team_name']
    }))
    instructors = list(mongo.db.users.find({
        'instructor': True,
        'team_name': username['team_name']
    }))
    return render_template("teams.html", teams=teams,
                           students=students,
                           team_leader=team_leader, instructors=instructors,
                           username=username)


@app.route("/add_team", methods=['GET', 'POST'])
def add_team():
    # adds team to the database
    if request.method == 'POST':
        existing_team = mongo.db.users.find_one(
            {'team_name': request.form.get('team_name')})
        alias = mongo.db.users.find_one(
            {'username': session['user']})['alias']
        if existing_team:
            flash('Team already exists')
            return redirect(url_for('add_team'))
        team = {
            "team_name": request.form.get('team_name'),
            "team_region": request.form.get('team_region'),
            "team_description": request.form.get('team_description'),
            "created_by": alias
        }
        mongo.db.teams.insert_one(team)
        flash("Team Successfully Created")
        return redirect(url_for('get_teams'))
    # variables to be rendered by the template
    return render_template('add_team.html')


@app.route("/edit_team/<team_id>", methods=['GET', 'POST'])
def edit_team(team_id):
    # Finds team document
    team = mongo.db.teams.find_one(
        {'_id': ObjectId(team_id)})
    if request.method == 'POST':
        alias = mongo.db.users.find_one(
            {'username': session['user']})['alias']
        new_team = {
            "team_name": request.form.get('team_name'),
            "team_region": request.form.get('team_region'),
            "team_description": request.form.get('team_description'),
            "created_by": alias
        }
        # Finds team's users and update their records
        mongo.db.users.update_many({
            'team_name': team['team_name']
        }, {
            '$set': {
                'team_name': request.form.get('team_name')
            }
        })
        # Find team's trainings and update their records
        mongo.db.trainings.update_many({
            'team_name': team['team_name']
        }, {
            '$set': {
                'team_name': request.form.get('team_name')
            }
        })
        # Updates team parameters in the collection
        mongo.db.teams.update({'_id': ObjectId(team_id)}, new_team)
        flash('Team successfully edited')
        return redirect(url_for('get_teams'))
    return render_template('edit_team.html', team=team)


@app.route('/delete_team/<team_id>')
def delete_team(team_id):
    # Finds team document
    team = mongo.db.teams.find_one(
        {'_id': ObjectId(team_id)})
    # finds team's users
    mongo.db.users.delete_many({
        'team_name': team['team_name']})
    # deletes team record in the database
    mongo.db.teams.remove({
        '_id': ObjectId(team_id)
    })
    flash('Team successfully deleted')
    return redirect(url_for('get_teams'))

# --------------------------------User functions---------------------- #


@app.route("/get_trainings")
def get_trainings():
    username = mongo.db.users.find_one(
        {'username': session['user']})
    if username.get('admin'):
        trainings = list(mongo.db.trainings.find())
        students = list(mongo.db.users.find(
            {'student': True}))
    else:
        trainings = list(mongo.db.trainings.find({
            'team_name': username['team_name']
        }))
        students = list(mongo.db.users.find(
            {'student': True,
                'team_name': username['team_name']}))
    training_types = mongo.db.training_types.find().sort('training_type', 1)
    return render_template("trainings.html",
                           trainings=trainings, username=username,
                           students=students, training_types=training_types)


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
            team_leader = True if request.form.get('team_leader') else False
            instructor = True if request.form.get('instructor') else False
            register = {
                'username': request.form.get('username').lower(),
                'password': generate_password_hash(
                            request.form.get('password'), salt_length=7),
                'alias': request.form.get('alias'),
                'team_name': request.form.get('team_name'),
                'team_leader': team_leader,
                'instructor': instructor
            }
            if not team_leader and not instructor:
                register['student'] = True
                register['trainings'] = {}
            mongo.db.users.insert_one(register)
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


@app.route("/profile/<username>")
def profile(username):
    if request.args.get('alias') is not None:
        username = mongo.db.users.find_one({
            'alias': request.args.get('alias')
        })
        access = mongo.db.users.find_one(
            {'username': session['user']})
    else:
        access = None
        # grab the session's user's username from db
        username = mongo.db.users.find_one(
            {'username': session['user']})
    courses = list(mongo.db.trainings.find())
    return render_template('profile.html', username=username,
                           courses=courses, access=access)


@app.route('/logout')
def logout():
    # remove user from session cookies
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/edit_access', methods=['GET', 'POST'])
def edit_access():
    alias = request.args.get('alias')
    if request.method == 'POST':
        user = mongo.db.users.find_one({'alias': alias})
        reset_access(user)
        access = request.form.get('access')
        mongo.db.users.update({
            'username': user['username']
        }, {
            '$set': {access: True}
        })
        flash('Access updated')
    return redirect(url_for('profile',
                            username=session['user'], alias=user['alias']))


# --------------------------------Training functions---------------------- #
@app.route("/add_training", methods=['GET', 'POST'])
def add_training():
    # Finds user
    username = mongo.db.users.find_one(
            {'username': session['user']})
    # If system admin
    if username.get('admin'):
        students = list(mongo.db.users.find(
            {"student": True}).sort('alias', 1))
    else:
        students = list(mongo.db.users.find(
            {"student": True,
                "team_name":
                    username['team_name']}).sort('alias', 1))
    # adds training to the database
    if request.method == 'POST':
        existing_training = mongo.db.users.find_one(
            {'training_name': request.form.get('training_name')})
        if existing_training:
            flash('Training already exists')
            return redirect(url_for('add_training'))
        training = {
            "team_name": username['team_name'],
            "training_name": request.form.get('training_name'),
            "training_description": request.form.get('training_description'),
            "training_date": request.form.get('due_date'),
            "training_cycle": {},
            "created_by": username['alias'],
            "complete_training": False
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
    return render_template('add_training.html', teams=teams, students=students,
                           username=username)


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
            "complete_training": False
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
    flash("Training successfully deleted")
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
    flash("Student enrolled")
    return redirect(url_for('get_trainings'))


@app.route("/complete_training/<training_id>", methods=['GET', 'POST'])
def complete_training(training_id):
    # marks training as complete
    if request.method == 'POST':
        # finds training name
        mongo.db.trainings.update_one({
            '_id': ObjectId(training_id)}, {
                "$set": {
                    "complete_training": True
                }
            }
        )
    flash("Training updated")
    return redirect(url_for('get_trainings'))


@app.route("/incomplete_training/<training_id>", methods=['GET', 'POST'])
def incomplete_training(training_id):
    # marks training as complete
    if request.method == 'POST':
        # finds training name
        mongo.db.trainings.update_one({
            '_id': ObjectId(training_id)}, {
                "$set": {
                    "complete_training": False
                }
            }
        )
    flash("Training updated")
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
                              current_cycle}}, upsert=True)
            training_folder[new_cycle] = cycle[new_cycle]
            mongo.db.trainings.update_one(
                {'_id': ObjectId(training_id)},
                {'$set':
                    {'training_cycle': training_folder}})
            flash("Training Cycle Successfully Created")
            return redirect(url_for('get_trainings'))
    training = mongo.db.trainings.find_one({'_id': ObjectId(training_id)})
    instructors = mongo.db.users.find(
        {'instructor': True}).sort('alias', 1)
    training_types = mongo.db.training_types.find().sort('training_type', 1)
    return render_template('add_cycle.html',
                           instructors=instructors, training=training,
                           training_types=training_types)


@app.route("/edit_cycle/<training_id>", methods=['GET', 'POST'])
def edit_cycle(training_id):
    if request.method == 'POST':
        training_folder = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_cycle']
        training_name = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_name']
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
        cycle_name = request.form.get('training_type')
        for student in students:
            current_cycle = student['trainings'][training_name]
            current_cycle.update(cycle)
            mongo.db.users.update_one(
                {'username': student['username']},
                {'$set': {f'trainings.{training_name}':
                          current_cycle}}, upsert=True)
        training_folder[cycle_name] = cycle[cycle_name]
        mongo.db.trainings.update_one(
            {'_id': ObjectId(training_id)},
            {'$set':
                {'training_cycle': training_folder}})
        flash("Cycle Successfully Edited")
        return redirect(url_for('get_trainings'))
    training = mongo.db.trainings.find_one({'_id': ObjectId(training_id)})
    instructors = mongo.db.users.find(
        {'instructor': True}).sort('alias', 1)
    training_types = mongo.db.training_types.find().sort('training_type', 1)
    cycle = request.args.get('cycle')
    return render_template('edit_cycle.html',
                           instructors=instructors, training=training,
                           training_types=training_types, cycle=cycle)


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
    flash("Cycle updated")
    return redirect(url_for('get_trainings'))


@app.route("/incomplete_cycle/<training_id>", methods=['GET', 'POST'])
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
    flash("Cycle updated")
    return redirect(url_for('get_trainings'))


@app.route("/delete_cycle/<training_id>", methods=['GET', 'POST'])
def delete_cycle(training_id):
    if request.method == 'POST':
        # finds training name
        training_name = mongo.db.trainings.find_one(
            {'_id': ObjectId(training_id)})['training_name']
        current_cycle = request.form.get('cycle_name_delete')
        students = mongo.db.users.find(
            {f"trainings.{training_name}": {'$exists': "true"}})
        # finds students
        for student in students:
            user = student['alias']
            mongo.db.users.update_one(
                {'alias': user},
                {'$unset':
                    {f'trainings.{training_name}.{current_cycle}':
                        ""}})
#       sets training to complete on training's record
        mongo.db.trainings.update_one(
                {'_id': ObjectId(training_id)},
                {'$unset':
                    {f'training_cycle.{current_cycle}': ""}})
    flash("Cycle deleted")
    return redirect(url_for('get_trainings'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
