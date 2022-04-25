from flask import jsonify, request
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.tables import Job, User

parser = reqparse.RequestParser()
parser.add_argument('job', required=True)
parser.add_argument('team_leader', required=True)
parser.add_argument('work_size', required=True, type=int)


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(jobs_id)
    if not jobs:
        abort(404, message=f"Jobs {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Job).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('job', 'team_leader', 'work_size'))})

    def put(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Job).get(jobs_id)
        if 'team_leader' in request.json:
            jobs.team_leader = request.json['team_leader']
        if 'job' in request.json:
            jobs.job = request.json['job']
        if 'work_size' in request.json:
            jobs.work_size = request.json['work_size']
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Job).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Job).all()
        return jsonify({'news': [item.to_dict(
            only=('job', 'team_leader', 'work_size')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Job(
            job=args['job'],
            team_leader=args['team_leader'],
            work_size=args['work_size']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})
