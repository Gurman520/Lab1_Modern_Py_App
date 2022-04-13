from flask import Blueprint, jsonify, request

from data import db_session
from data.tables import Job, User, Category

blueprint = Blueprint('jobs_api', __name__,
                      template_folder='templates')


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'team_leader', 'work_size'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_jobs(job_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('id', 'job', 'team_leader', 'work_size'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    jobs = Job(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        is_finished=request.json['is_finished']
    )
    session.add(jobs)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    session.delete(jobs)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def update_jobs(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})

    if 'team_leader' in request.json:
        jobs.team_leader = request.json['team_leader']
    if 'job' in request.json:
        jobs.job = request.json['job']
    if 'work_size' in request.json:
        jobs.work_size = request.json['work_size']
    if 'collaborators' in request.json:
        coll_str = request.json['collaborators']
        coll_str = coll_str.split()
        for i in coll_str:
            user = session.query(User).filter(User.id == i).first()
            jobs.collaborators.append(user)
    if 'categories' in request.json:
        coll_str = request.json['categories']
        coll_str = coll_str.split()
        for i in coll_str:
            cat = session.query(Category).filter(Category.id == i).first()
            jobs.categories.append(cat)
    if 'is_finished' in request.json:
        jobs.is_finished = request.json['is_finished']
    session.commit()
    return jsonify({'success': 'OK'})
