from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    state = db.Column(db.Integer)
    instagram_login = db.Column(db.String(128))    
    fullname = db.Column(db.String(128))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="customers")

    def __repr__(self):
        return '<Customer {}>'.format(self.fullname)