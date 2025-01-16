import secrets
from flask import Flask, render_template, request, redirect, url_for, session

import api

client = Flask(__name__)


@client.route("/")
def index():
    return redirect(url_for("login"))


@client.route("/login")
def login():
    return render_template("login.html")


@client.route("/login-api", methods=["POST"])
def login_api():
    username = request.form.get("username")
    session["username"] = username
    api.createBanana(username)
    session["bananas"] = api.readBananaNum(username)
    return redirect(url_for("app"))


@client.route("/app", methods=["GET", "POST"])
def app():
    username = session.get("username")
    if request.method == "POST":
        session["bananas"] += 1
        # api.addBanana(username, session["bananas"])

    if session["username"]:
        return render_template(
            "app.html", username=username, cloud_bananas=api.readBananaNum(username), local_bananas=session["bananas"]
        )
    else:
        return redirect(url_for("login"))


@client.route("/send-api", methods=["GET", "POST"])
def send_api():
    username = session.get("username")
    api.addBanana(username, session["bananas"])
    session["bananas"] = api.readBananaNum(username)
    return redirect(url_for("app"))


@client.route("/delete-api", methods=["GET", "DELETE"])
def delete_api():
    username = session.get("username")
    api.deleteUser(username)
    session.pop("username")
    session.pop("bananas")
    return redirect(url_for("login"))


if __name__ == "__main__":
    client.secret_key = secrets.token_urlsafe(4)
    client.run(host="0.0.0.0", port=8080, debug=True)
