from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from models import ProjectModel, db, app
from app import create_app

api = Api(app)
#db.create_all()

pro_put_args = reqparse.RequestParser()
pro_put_args.add_argument("user_id", type=int, help="user_id required", required = True) 
pro_put_args.add_argument("name", type=str, help="name", required = True) 
pro_put_args.add_argument("budget", type=int, help="budget required", required = True) 
pro_put_args.add_argument("description", type=str, help="description")

pro_update_args = reqparse.RequestParser()
pro_update_args.add_argument("user_id", type=int, help="user_id required") 
pro_update_args.add_argument("name", type=str, help="name required") 
pro_update_args.add_argument("budget", type=int, help="budget required") 
pro_update_args.add_argument("description", type=str, help="description")

pro_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'name': fields.String,
    'budget' : fields.Integer,
    'description': fields.String
}

class Pro(Resource):
    @marshal_with(pro_fields)
    def get(self, id):
        result = ProjectModel.query.filter_by(id=id).all()
        if not result:
            abort(404, message="User not found with the given ID")
        return result

    @marshal_with(pro_fields)
    def put(self, id):
        args = pro_put_args.parse_args()
        result = ProjectModel.query.filter_by(id=id).all()
        if result:
            abort(409, message ="User ID taken...")
        project = ProjectModel(id=id, user_id=args['user_id'], name=args['name'], budget=args['budget'], description=args['description'])
        db.session.add(project)
        db.session.commit()
        return project, 201

    @marshal_with(pro_fields)    
    def patch(self, id):
        args = pro_update_args.parse_args()
        result = ProjectModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message ="User ID doesn't exist, cannot update")
        if args['user_id']:
            result.user_id = args['user_id']
        if args['name']:
            result.name = args['name']
        if args['budget']:
            result.budget = args['budget']
        if args['description']:
            result.description = args['description']
        db.session.commit()
        return result

    @marshal_with(pro_fields)  
    def delete(self, id):
        result = ProjectModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message ="User ID doesn't exist, cannot delete")
        else:
            db.session.delete(result)
            db.session.commit()
            return '', 204

api.add_resource(Pro, "/pro/<string:id>")

if __name__ == '__main__':
    app.run(debug=True)
