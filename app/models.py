from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    first_names = db.Column(db.String(100), nullable=False)
    middle_name_initial = db.Column(db.String(10), nullable=False)
    last_names = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    legal_status = db.Column(db.String(50), nullable=False)
    maid_number = db.Column(db.Integer, nullable=False)
    ssn = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    address_1 = db.Column(db.String(50), nullable=False)
    address_2 = db.Column(db.String(50), nullable=True)  # An optional field
    city_state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    profile_photo = db.Column(db.String(200), nullable=False)
    #prescriptions = db.relationship('Prescription', backref='participant', lazy=True)

#
# class Prescription(db.Model):
#     __tablename__ = 'prescriptions'