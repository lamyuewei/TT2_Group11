from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy     # For Database
import app
import pandas as pd

ProjectData = pd.read_json("data/project.json")
#print(ProjectData.head())

# class Project(Resource):
#     def get(self, id):
#         result = Project

if __name__ == "__main__":
    app.app.run(debug=True)