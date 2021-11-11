from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy     # For Database

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
#db.create_all()   ## Only do this once

@app.route("/")

def home():
    return "Hi"


@app.route("/test_login")
def auth(name, pw):
    if name == "name" and pw == "pass":
        return "Authenticated"
    else:
        return "Wrong password"

