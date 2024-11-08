from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
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


# Serialization
class ParticipantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Participant
        load_instance = True

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)