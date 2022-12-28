from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

from dummy_db import db_handler

app = Flask(__name__)
viewed_counter = 0


@app.route("/")
def welcome():
    """
    Render the welcome/home page. Passes the entire json db (not good practice, demo purposes)
    to show a list of cards.
    """
    return render_template("welcome.html",
                           cards=db_handler.get_db())


@app.route("/card/<int:index>", methods=["GET", "POST"])
def card_view(index):
    """
    Retrieve a card by index and use it to render the card page. Also
    passes current index and max list index to the template.
    If index not found, returns a 404.
    """
    show_card = False
    if request.method == "POST":
        show_card = True
    try:
        card = db_handler.get_card_by_index(index)
        return render_template("card.html",
                               card=card,
                               index=index,
                               show_card=show_card,
                               max_index=len(db_handler.get_db()) - 1)
    except IndexError:
        abort(404)


@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        card = {"question": request.form["question"],
                "answer": request.form["answer"]}
        db_handler.add_to_db(card)
        return redirect(url_for("card_view", index=len(db_handler.get_db()) - 1))
    elif request.method == "GET":
        return render_template("add_card.html")


@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    print("call")
    if request.method == "POST":
        print("call post")
        db_handler.remove_from_db(index)
        return redirect(url_for("welcome",
                                cards=db_handler.get_db()))
    elif request.method == "GET":
        print("call get")
        try:
            card = db_handler.get_card_by_index(index)
            return render_template("remove_card.html",
                                   card=card,
                                   index=index)
        except IndexError:
            abort(404)


@app.route("/api/card/")
def api_card_list():
    """Return a list of all cards"""
    return jsonify(db_handler.get_db())


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    """Return a single card by index"""
    try:
        return db_handler.get_card_by_index(index)
    except IndexError:
        abort(404)
