import datetime
import sqlalchemy
from sqlalchemy import orm, Table, Column, ForeignKey
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash

colab_table = Table("Colab", SqlAlchemyBase.metadata,
                    Column('job_id', ForeignKey('job.id')),
                    Column('user_id', ForeignKey('user.id')))

colab_table_2 = Table("Colab_2", SqlAlchemyBase.metadata,
                      Column('dep_id', ForeignKey('department.id')),
                      Column('user_id', ForeignKey('user.id')))

jobs_to_category = Table('jobs_to_category', SqlAlchemyBase.metadata,
                         Column('job_id', ForeignKey('job.id')),
                         Column('category_id', ForeignKey('category.id')))


class Category(SqlAlchemyBase):
    __tablename__ = 'category'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Job(SqlAlchemyBase):
    __tablename__ = 'job'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('user.id'))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = orm.relationship("User", secondary=colab_table, back_populates="job")
    categories = orm.relation("Category", secondary="jobs_to_category", backref="job")
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=None)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    user = orm.relation('User')

    def __repr__(self):
        return f"Job {self.job}"


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    addres = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    collaborators = orm.relationship("Job", secondary=colab_table, back_populates="user", overlaps="collaborators")
    members = orm.relationship("Department", secondary=colab_table_2, back_populates="user", overlaps="members")
    job = orm.relation("Job", overlaps='user')
    department = orm.relation("Department", overlaps='user')

    def __repr__(self):
        return f"Colonist {self.id} {self.surname} {self.name}"

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Department(SqlAlchemyBase):
    __tablename__ = 'department'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    chief = sqlalchemy.Column(sqlalchemy.Integer,
                              ForeignKey('user.id'))

    members = orm.relationship("User", secondary=colab_table_2, back_populates="department")

    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)

    user = orm.relation('User')
