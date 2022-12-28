import json


class FlashCardDB:
    def __init__(self):
        self.db = self.load_db()

    def load_db(self):
        """
        NOTE: not suitable for production environment

        :return:
        """
        with open("data/flashcards_db.json") as file:
            return json.load(file)

    def get_db(self):
        return self.db

    def get_card_by_index(self, index):
        return self.db[index]

    def write_db(self):
        with open("data/flashcards_db.json", "w") as file:
            json.dump(self.db, file)

    def add_to_db(self, entry):
        self.db.append(entry)
        self.write_db()

    def remove_from_db(self, index):
        self.db.pop(index)
        self.write_db()


db_handler = FlashCardDB()
