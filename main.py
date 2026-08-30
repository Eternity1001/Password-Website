from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username_or_email = request.form.get("username_or_email")
        password = request.form.get("password")

        print(username_or_email)
        print(password)

        return "Sign in successful!"

    return render_template("signin.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username_or_email = request.form.get("username_or_email")
        password = request.form.get("password")

        print(username_or_email)
        print(password)
        return render_template("signin.html")
    return render_template("signup.html")

@app.route("/forgot-username")
def forgot_username():
    return "Forgot username"


@app.route("/forgot-password")
def forgot_password():
    return "Forgot password"


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)