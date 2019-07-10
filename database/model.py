from datetime import datetime
from . import db

class Customers(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip = db.Column(db.String(5), nullable=False)
    email_sent = None

    def __init__(self, first_name, last_name, email, address, city, state, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_time(self):
        self.email_sent = datetime.utcnow()
