from flask import Flask, render_template, abort, jsonify

from dummy_db import db

app = Flask(__name__)
viewed_counter = 0


@app.route("/")
def welcome():
    """
    Render the welcome/home page. Passes the entire json db (not good practice, demo purposes)
    to show a list of cards.
    """
    return render_template("welcome.html",
                           cards=db)


@app.route("/card/<int:index>")
def card_view(index):
    """
    Retrieve a card by index and use it to render the card page. Also
    passes current index and max list index to the template.
    If index not found, returns a 404.
    """
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route("/api/card/")
def api_card_list():
    """Return a list of all cards"""
    return jsonify(db)


@ app.route('/api/card/<int:index>')
def api_card_detail(index):
    """Return a single card by index"""
    try:
        return db[index]
    except IndexError:
        abort(404)
