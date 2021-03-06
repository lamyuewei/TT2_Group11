from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy     # For Database

from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

DB_Name = "new_Db.db"
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.secret_key = 'TEAM_11'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}".format(DB_Name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    return app

# @app.route("/")
# def home():
#     return "Hi"



# @app.route('/auth_test', methods=['GET','POST'])
# def auth():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     if (username == "user" and password == "123"):
#         return 'OK', 200
#     else:
#         return 'Wrong password', 401
    
