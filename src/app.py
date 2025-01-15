import secrets
from flask import Flask, render_template, request, redirect, url_for, session

client = Flask(__name__)

client.secret_key = secrets.token_urlsafe(4)


@client.route("/")
def index():
    return redirect(url_for("login"))


@client.route("/login")
def login():
    return render_template("login.html")


@client.route("/login-success", methods=["POST"])
def login_api():
    username = request.form.get("username")
    session["username"] = username
    session["clicks"] = 0
    return redirect(url_for("app"))


@client.route("/app", methods=["GET", "POST"])
def app():
    username = session.get("username")
    clicks = session.get("clicks")

    if request.method == "POST":
        session["clicks"] += 1
        clicks += 1

    if username:
        return render_template("app.html", username=username, clicks=clicks)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    client.run(host="0.0.0.0", port=8080, debug=True)
