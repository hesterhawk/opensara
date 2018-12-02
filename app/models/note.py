from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    state = db.Column(db.Integer)
    message = db.Column(db.String(4000), nullable=False)
    instagram_post_url = db.Column(db.String(255), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="notes")

    def __repr__(self):
        return '<Note {}>'.format(self.id)