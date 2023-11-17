from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
)  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"
app.secret_key = "it's a secret"  # set a secret key for security purposes

# =================== LOGIN ===================


# * Display Form -> form.html
@app.route("/login")
def login():
    return render_template("form.html")


# ? Action Route
@app.route("/process", methods=["POST"])
def process_form():
    print(f"my email is: {request.form['email']}")
    print(f"my password is: {request.form['pass']}")

    #! NEVER EVER RENDER ON A POST REQUEST
    return redirect("/login")


# =================== PRODUCT ===================
# * Display Route -> product.html
@app.route("/product")
def product():
    return render_template("product.html")


# * ACTION ROUTE
@app.route("/pay", methods=["POST"])
def pay():
    print(request.form)
    session["product_name"] = request.form["pName"]
    session["product_price"] = request.form["price"]
    session["product_unit"] = request.form["units"]
    #! NEVER EVER RENDER ON A POST REQUEST
    return redirect("/success")


# * DISPLAY ROUTE -> success.html
@app.route("/success")
def success():
    # print(request.form)
    return render_template("success.html")


# * Display Route -> success.html
@app.route("/clear")
def clear_session():
    """Clears the session data."""
    session.clear()
    return render_template("success.html")


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
