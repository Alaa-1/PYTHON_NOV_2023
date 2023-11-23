from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.quote import Quote
from flask_app.models.user import User


@app.route("/new")
def display_quote_form():
    all_users = User.get_all()
    return render_template("createquote.html", all_users=all_users)


@app.route("/processquote", methods=["POST"])
def create_quote():
    print(request.form)
    Quote.create_quote(request.form)
    return redirect(f"/show/{request.form['user_id']}")
