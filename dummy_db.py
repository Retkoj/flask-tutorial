import json


def load_db():
    """
    NOTE: not suitable for production environment

    :return:
    """
    with open("data/flashcards_db.json") as file:
        return json.load(file)


db = load_db()
