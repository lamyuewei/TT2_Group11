from . import db
from flask_login import UserMixin

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    appointment = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return "Account(username={0}, password={1}, name={2}, appointment = {3})".format(self.username,self.password,self.name,self.appointment)

class ProjectModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    budget = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return "Project Model(user_id={0}, name={1}, budget={2}, description = {3})".format(self.user_id,self.name,self.budget,self.description)