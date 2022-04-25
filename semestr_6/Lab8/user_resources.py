from flask import jsonify, request
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.tables import User

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('age', required=True, type=int)


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        Users = session.query(User).get(users_id)
        return jsonify({'Users': Users.to_dict(
            only=('surname', 'name', 'age'))})

    def put(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        if 'name' in request.json:
            users.name = request.json['name']
        if 'surname' in request.json:
            users.surname = request.json['surname']
        if 'age' in request.json:
            users.age = request.json['age']
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'news': [item.to_dict(
            only=('name', 'surname', 'age')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
