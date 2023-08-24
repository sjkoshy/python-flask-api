from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase(
    "seinfeld", user="postgres", password="", host="localhost", port=5432
)

app = Flask(__name__)


@app.route("/")
def index():
    app.run(port=5000, debug=True)


@app.route("/endpoint", methods=["GET", "PUT", "POST", "DELETE"])
def endpoint():
    if request.method == "GET":
        return "GET"

    if request.method == "PUT":
        return "PUT"

    if request.method == "POST":
        return "POST"

    if request.method == "DELETE":
        return "DELETE"


@app.route("/json")
def json():
    return jsonify({"key": "value", "listkey": [1, 2, 3], "isbool": True})
