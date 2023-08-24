from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase(
    "seinfeld", user="postgres", password="", host="localhost", port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class Character(BaseModel):
    name = CharField()
    gender = CharField()
    occupation = CharField()
    portrayedby = CharField()


db.connect()
db.drop_tables([Character])
db.create_tables([Character])

Character(
    name="Jerry",
    gender="male",
    occupation="comedian",
    portrayedby="Jerry Seinfeld",
).save()
Character(
    name="George",
    gender="male",
    occupation="architect",
    portrayedby="Jason Alexander",
).save()
Character(
    name="Elaine",
    gender="female",
    occupation="writer",
    portrayedby="Julia Louis-Dreyfus",
).save()
Character(
    name="Kramer",
    gender="male",
    occupation="unemployed",
    portrayedby="Michael Richards",
).save()


app = Flask(__name__)


@app.route("/character", methods=["GET", "POST"])
@app.route("/character/<id>", methods=["GET", "PUT", "DELETE"])
def endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Character.get_by_id(id)))
    else:
        characters = []
        for character in Character.select():
            characters.append(model_to_dict(character))
        return jsonify(characters)

    if request.method == "PUT":
        body = request.get_json()
        Character.update(body).where(Character.id == id).execute()
        return "Character {id} updated."

    if request.method == "POST":
        add_character = dict_to_model(Character, request.get_json())
        add_character.save()
        return "Character {id} added."

    if request.method == "DELETE":
        Character.delete().where(Character.id == id).execute()
        return "Character {id} deleted."


app.run(port=5000, debug=True)
