from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_new.db'
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    appointment = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return "Account(username={0}, password={1}, name={2}, appointment = {3})".format(self.username,self.password,self.name,self.appointment)
    
#db.create_all()

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
    def get(self, user_id):
        # if sqldb
        result = Account.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User not found with the given ID")
        return result

    @marshal_with(acc_fields)
    def put(self, user_id):
        args = acc_put_args.parse_args()
        #if sqldb
        result = Account.query.filter_by(id=user_id).first()
        if result:
            abort(409, message ="User ID taken...")
        user = Account(id=user_id, username=args['username'], password=args['password'], name=args['name'], appointment=args['appointment'])
        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(acc_fields)    
    def patch(self, user_id):
        args = acc_update_args.parse_args()
        result = Account.query.filter_by(id=user_id).first()
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
    def delete(self, user_id):
        result = Account.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message ="Video ID doesn't exist, cannot delete")
        else:
            db.session.delete(result)
            db.session.commit()
            return '', 204

api.add_resource(Acc, "/acc/<string:user_id>")

if __name__ == '__main__':
    app.run(debug=True)