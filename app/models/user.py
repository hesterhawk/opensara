from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

users_projects = db.Table('users_projects',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.PrimaryKeyConstraint('user_id', 'project_id')
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    projects = db.relationship('Project', secondary=users_projects, backref='users' ) 

    """
    projects = db.relationship(
        'Project', secondary=users_projects,
        primaryjoin=(users_projects.c.project_id == id),
        secondaryjoin=(users_projects.c.user_id == id),
        backref=db.backref('projects', lazy='dynamic'), lazy='dynamic')
    """

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))