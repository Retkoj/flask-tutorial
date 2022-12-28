from flask import Flask, render_template

app = Flask(__name__)
viewed_counter = 0


@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="Message from view function")
