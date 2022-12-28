import datetime

from flask import  Flask

app = Flask(__name__)
viewed_counter = 0


@app.route("/")
def welcome():
    return "Welcome to flask flashcards!"


@app.route("/date")
def date():
    return f"Page served at {datetime.datetime.now()}"


@app.route("/viewed")
def viewed():
    global viewed_counter
    viewed_counter += 1
    return f"Page has been viewed {viewed_counter}"
