from flask_mongoengine import MongoEngine

db = MongoEngine()

class Puppy(db.Document):
    name = db.StringField()
    owner = db.StringField()

    def __repr__(self):
        if self.owner:
            return f"My name is {self.name} and my owner is {self.owner}"
        else:
            return f"My name is {self.name} and I don't have an owner yet"
