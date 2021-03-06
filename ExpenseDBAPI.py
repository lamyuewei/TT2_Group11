from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import relation

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_new1.db'
db = SQLAlchemy(app)

# db.create_all()

class ExpenseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # project_id = db.Column(db.Integer, nullable = False)
    # category_id = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.String, nullable = False)
    created_by = db.Column(db.String(100), nullable = False)
    updated_at = db.Column(db.String, nullable = False)
    updated_by = db.Column(db.String(100), nullable = False)

    # def __repr__(self):
    #     return "Expense(id={0}, project_id={1}, category_id={2}, name={3}, description={4}, amount={5}, created_at={6}, created_by={7}, updated_at={8}, created_by={9})".format(self.name,self.description,self.amount,self.created_at,self.created_by,self.updated_at,self.updated_by)
        


exp_put_args = reqparse.RequestParser()
exp_put_args.add_argument("name", type=str, help="name required", required = True) 
exp_put_args.add_argument("description", type=str, help="description required", required = True) 
exp_put_args.add_argument("amount", type=int, help="amount required", required = True) 
exp_put_args.add_argument("created_at", type=str, help="created_at required", required = True)
exp_put_args.add_argument("created_by", type=str, help="created_by required", required = True)
exp_put_args.add_argument("updated_at", type=str, help="updated_at required", required = True)
exp_put_args.add_argument("updated_by", type=str, help="updated_by required", required = True)

exp_update_args = reqparse.RequestParser()
exp_update_args.add_argument("name", type=str, help="name required", required = True) 
exp_update_args.add_argument("description", type=str, help="description required", required = True) 
exp_update_args.add_argument("amount", type=int, help="amount required", required = True) 
exp_update_args.add_argument("created_at", type=str, help="created_at required", required = True)
exp_update_args.add_argument("created_by", type=str, help="created_by required", required = True)
exp_update_args.add_argument("updated_at", type=str, help="updated_at required", required = True)
exp_update_args.add_argument("updated_by", type=str, help="updated_by required", required = True)

exp_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'amount' : fields.Integer,
    'created_at': fields.String,
    'created_by': fields.String,
    'updated_at': fields.String,
    'updated_by': fields.String
}

class Expense(Resource):
    @marshal_with(exp_fields)
    def get(self, exp_id):
        result = ExpenseModel.query.filter_by(id=exp_id).first()
        if not result:
            abort(404, message="Could not find expense with that ID")
        return result

    @marshal_with(exp_fields)
    def put(self, exp_id):
        args = exp_put_args.parse_args()
        result = ExpenseModel.query.filter_by(id=exp_id).first()
        if not result:
            abort(409, message="Exp ID taken...")
        expense = ExpenseModel(id=exp_id, name=args['name'], description=args['description'], amount=args['amount'], 
                                created_at=args['created_at'], created_by=args['created_by'], updated_at=args['updated_at'],
                                updated_by=args['updated_by']) 
        db.session.add(expense)
        db.session.commit()
        return expense, 201
    
    @marshal_with(exp_fields)
    def patch(self, exp_id):
        args = exp_update_args.parse_args()
        result = ExpenseModel.query.filter_by(id=exp_id).first()
        if not result:
            abort(404, message ="Expense ID doesn't exist, cannot update")
        if args['name']:
            result.name = args['name']
        if args['description']:
            result.description = args['description']
        if args['amount']:
            result.amount = args['amount']
        if args['created_at']:
            result.created_at = args['created_at']
        if args['created_by']:
            result.created_by = args['created_by']
        if args['updated_at']:
            result.updated_at = args['updated_at']
        if args['updated_by']:
            result.updated_by = args['updated_by']
        return result
    
    @marshal_with(exp_fields)
    def delete(self, exp_id):
        result = ExpenseModel.query.filter_by(id=exp_id).first()
        if not result:
            abort(404, message ="Video ID doesn't exist, cannot delete")
        else:
            db.session.delete(result)
            db.session.commit()
            return '', 204

api.add_resource(Expense, "/exp/<int:exp_id>")


if __name__ == '__main__':
    app.run(debug=True)
    
