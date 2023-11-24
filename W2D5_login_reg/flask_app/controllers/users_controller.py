from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

# ========== LOGIN / REGISTER PAGE - VIEW =========
@app.route("/")
def index():
    return render_template("index.html")

# ========= REGISTER - method - ACTION ========
@app.route("/users/register", methods=['post'])
def user_reg():
    print(request.form)
    if not User.validate(request.form):
        return redirect("/")
    
    # 1. hash the pws
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # 2. get the data dict ready with the new hashed pw to create a User 
    data = {
        **request.form,
        'password': pw_hash
    }
    # 3. pass it to the User model
    user_id = User.create(data)
    # how do we keep track if someone is logged in?
    # store the user_id of the created user in session 🎒
    session['user_id'] = user_id
    return redirect("/dashboard")

# ----------- LOGIN - methods - action
@app.route("/users/login", methods=['post'])
def user_login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data) # False or a User
    # if email not found
    if not user_in_db:
        flash("invalid credentials")
        return redirect("/")
    
    # now check the pw
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("invalid credentials")
        return redirect("/")
    
    # * if all is good:
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")


# ------------ DASHBOARD PAGE - RENDER -----------
@app.route("/dashboard")
def dash():
    # ! route guard
    if 'user_id' not in session:
        return redirect("/")
    # grab the user_id from session
    data = {
        'id' : session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template("welcome.html", logged_user=logged_user)


# !------ LOGOUT ------ action
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")