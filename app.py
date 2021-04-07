import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
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


@app.route("/get_trainings")
def get_trainings():
    trainings = list(mongo.db.trainings.find())
    return render_template("trainings.html", trainings=trainings)


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
            register = {
                'username': request.form.get('username').lower(),
                'password': generate_password_hash(
                            request.form.get('password'), salt_length=7),
                'alias': request.form.get('alias').lower()
            }
            mongo.db.users.insert_one(register)
            # put the new user into 'session' cookie
            session["user"] = request.form.get('username').lower()
            flash('Registration Successful!')
            return redirect(url_for('profile', username=session['user']))
        else:
            flash("Password doesn't match!")
            return redirect(url_for('register'))
    return render_template("register.html")


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
                    return redirect(url_for('profile', username=session['user']))
            else:
                # invalid password match
                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash('Incorrect Username and/or Password')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/profile/<username>", methods=['GET','POST'])
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
