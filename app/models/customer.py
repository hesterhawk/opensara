from app import db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    state = db.Column(db.Integer)
    instagram_login = db.Column(db.String(128))    
    fullname = db.Column(db.String(128))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    project = db.relationship("Project", back_populates="customers")
    notes = db.relationship("Note", backref="post", cascade="all, delete-orphan" , lazy='dynamic')

    def __repr__(self):
        return '<Customer {}>'.format(self.instagram_login)