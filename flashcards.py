from flask import Flask, render_template

from dummy_db import db

app = Flask(__name__)
viewed_counter = 0


@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="Message from view function")


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html",
                           card=card)
