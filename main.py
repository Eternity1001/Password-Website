from flask import Flask, render_template, request, jsonify
from server_side.password import *
from server_side.database import *
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username_or_email = request.form.get("username_or_email")
        password = request.form.get("password")

        return "Sign in successful!"

    return render_template("signin.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return render_template("signin.html")
    return render_template("signup.html")


@app.route("/verify-account", methods=["GET", "POST"])
def verify_account():
    data = request.get_json()

    if data['password'] != data['confirm_password']:
        return jsonify({"error": f"Password"}, 200)

    status = create_account(email=data['email'],username=data['username'],
                             password=data['password'], confirm_password=data['confirm_password'] )

    if status[0]:
        return jsonify({"success": f"Account"}, 200) 

    if status[1][1] == data['email']:
        return jsonify({"error": f"Email"}, 200)

    if status[1][2] == data['username']:
        return jsonify({"error": f"Username"}, 200)

    # status = search_account_entries("account", "")
    # print(username)

    return "hello world"

@app.route("/forgot-username")
def forgot_username():
    return "Forgot username"



@app.route("/forgot-password")
def forgot_password():
    return "Forgot password"


if __name__ == "__main__":
    # print_all_database_enteries('account', 'users')
    # stauts = login("test@test.com", "password")
    # print(stauts)
    # create_account_db("account")
    # create_account(email="test@test.com", username="test", password="password", confirm_password="password")
   
    # status, user = search_account_entries("account", "username = ? AND email = ?", ("test", "test@test.com"))
    # print(status, user)

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)