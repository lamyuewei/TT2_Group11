from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Account, db, app

api = Api(app)
db.create_all()

acc_put_args = reqparse.RequestParser()
acc_put_args.add_argument("username", type=str, help="username required", required = True) 
acc_put_args.add_argument("password", type=str, help="password required", required = True) 
acc_put_args.add_argument("name", type=str, help="name required", required = True) 
acc_put_args.add_argument("appointment", type=str, help="Appointment")

acc_update_args = reqparse.RequestParser()
acc_update_args.add_argument("username", type=str, help="username required") 
acc_update_args.add_argument("password", type=str, help="password required") 
acc_update_args.add_argument("name", type=str, help="name required") 
acc_update_args.add_argument("appointment", type=str, help="Appointment")

acc_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'name' : fields.String,
    'appointment': fields.String
}

class Acc(Resource):
    @marshal_with(acc_fields)
    def get(self, ID):
        result = Account.query.filter_by(id=ID).first()
        if not result:
            abort(404, message="User not found with the given ID")
        return result

    @marshal_with(acc_fields)
    def put(self, ID):
        args = acc_put_args.parse_args()
        result = Account.query.filter_by(id=ID).first()
        if result:
            abort(409, message ="User ID taken...")
        user = Account(id=ID, username=args['username'], password=args['password'], name=args['name'], appointment=args['appointment'])
        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(acc_fields)    
    def patch(self, ID):
        args = acc_update_args.parse_args()
        result = Account.query.filter_by(id=ID).first()
        if not result:
            abort(404, message ="User ID doesn't exist, cannot update")
        if args['username']:
            result.username = args['username']
        if args['password']:
            result.password = args['password']
        if args['name']:
            result.name = args['name']
        if args['appointment']:
            result.appointment = args['appointment']
        db.session.commit()
        return result

    @marshal_with(acc_fields)  
    def delete(self, ID):
        result = Account.query.filter_by(id=ID).first()
        if not result:
            abort(404, message ="User ID doesn't exist, cannot delete")
        else:
            db.session.delete(result)
            db.session.commit()
            return '', 204

api.add_resource(Acc, "/acc/<string:ID>")

if __name__ == '__main__':
    app.run(debug=True)
