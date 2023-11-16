from flask import Flask, render_template

# create an instance of Flask
app = Flask(__name__)

# create routes


@app.route("/jinja")
def demo(fullname, times):
    username = "Amy Smith"
    return render_template("jinja_demo.html", username=username)


@app.route("/products/<color>")
def cart(color):
    products = ["smartphone", "TV", "Earbuds", "mouse pad"]

    return render_template("products.html", products_list=products, color=color)


@app.route("/students/<name>")
def students(name):
    students = [
        {"name": "joe", "email": "joe@gmail.com"},
        {"name": "Amy", "email": "Amy@gmail.com"},
        {"name": "Lauren", "email": "Lauren@icloud.com"},
    ]
    # email = ""
    # for el in students:
    #     if name == el["name"].lower():
    #         email = el["email"]
    #         break
    #     else:
    #         email = "Not Found"
    return render_template("products.html", students=students, name=name)


if __name__ == "__main__":
    app.run(debug=True)
