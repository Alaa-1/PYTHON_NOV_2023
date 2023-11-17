from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


# The "@" decorator associates this route with the function immediately following
@app.route("/hello")
def hello_world():
    return "Hello, World!"  # Return the string 'Hello World!' as a response


@app.route("/contact")
def contact_us():
    return "<h1>Send an email: a@a.com</h1><hr>"


@app.route("/contact/<name>")
def contact_hello(name):
    return f"You contacted {name} 📩 "


@app.route("/contact/<name>/<times>")
def contact_hello_times(name, times):
    return f"You contacted {name} {times} times. 📩 "


# ------------------------------------------------------------------
@app.route("/index")
def index():
    return render_template("index.html")


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
