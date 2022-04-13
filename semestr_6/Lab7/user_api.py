from flask import Blueprint, jsonify, request

from data import db_session
from data.tables import Job, User, Category

blueprint = Blueprint('user_api', __name__,
                      template_folder='templates')


@blueprint.route('/api/user', methods=['GET'])
def get_user():
    session = db_session.create_session()
    user = session.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict(only=('name', 'surname', 'age', 'position', 'email'))
                 for item in user]
        }
    )


@blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=('name', 'surname', 'age', 'position', 'email'))
        }
    )


@blueprint.route('/api/user', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'surname', 'age', 'position', 'email']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    user = User(
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        email=request.json['email']
    )
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
# 'name', 'surname', 'age', 'position', 'email'
    if 'name' in request.json:
        user.name = request.json['name']
    if 'surname' in request.json:
        user.surname = request.json['surname']
    if 'age' in request.json:
        user.age = request.json['age']
    if 'position' in request.json:
        user.position = request.json['position']
    if 'email' in request.json:
        user.email = request.json['email']
    session.commit()
    return jsonify({'success': 'OK'})
