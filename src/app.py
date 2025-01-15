from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/app")
def create():
    return render_template("app.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
