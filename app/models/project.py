from app import db
from datetime import datetime
from secrets import token_hex

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer)
    fullname = db.Column(db.String(255))
    token = db.Column(db.String(34), unique=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Project {}>'.format(self.fullname)
    
    def set_random_token(self):
        self.token = token_hex(12)