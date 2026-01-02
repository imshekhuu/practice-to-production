from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_registration", methods=["POST"])
def perform_registration():
    name = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    response = dbo.insert(name, email, password)

    if response:
        return render_template("login.html", massage = 'Register Succesfully Login To processed')
    else:
       return render_template("register.html", massage = 'email already already exist')

@app.route('/perform_login', methods=["POST"])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.search(email, password)

    if response:
        return redirect("/profile")
    else:
        return render_template('login.html', massage = "incorrect email/password")
    


@app.route('/profile')
def profile():
    return render_template("profile.html")



if __name__ == "__main__":
    app.run(debug=True)
