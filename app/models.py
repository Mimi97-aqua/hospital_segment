from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship


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

    # Relationships
    prescriptions = db.relationship('Prescription', backref='participant', lazy=True)


class Prescription(db.Model):
    __tablename__ = 'prescriptions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Foreign keys
    participant_id = db.Column(db.String, db.ForeignKey('participants.id'), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    pharmacy_id = db.Column(db.Integer, db.ForeignKey('pharmacies.id'), nullable=False)

    reason_for_medication = db.Column(db.String(200), nullable=True)
    prescriber = db.Column(db.String(50), nullable=False)
    quantity_dosage = db.Column(db.Integer, nullable=False)
    refills = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    dose = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)

    # Relationships
    drugs = db.relationship('Drug', backref='prescription', lazy=True)
    pharmacy = db.relationship('Pharmacy', backref='prescription', lazy=True)
    dose_times = db.relationship('DoseTime', backref='prescription', lazy=True)

class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    # Relationships
    participants = db.relationship('Participant', backref='caregiver', lazy=True)
    prescriptions = db.relationship('Prescription', backref='caregiver', lazy=True)

# Dependent Models
class Drug(db.Model):
    __tablename__ = 'drugs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable=False)
    form = db.Column(db.String, nullable=False) # Syrup, Tablet, Capsule, Powder etc

class Pharmacy(db.Model):
    __tablename__ = 'pharmacies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)

class DoseTime(db.Model):
    __tablename__ = 'dose_times'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    prescription_id = db.Column(db.Integer, db.ForeignKey('prescriptions.id'), nullable=False)
    time = db.Column(db.Time, nullable=False)

# Serialization
class ParticipantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Participant
        load_instance = True

class DrugsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Drug
        load_instance = True

class PharmacySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pharmacy
        load_instance = True


participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)

drug_schema = DrugsSchema()
drugs_schema = DrugsSchema(many=True)

pharmacy_schema = PharmacySchema()
pharmacies_schema = PharmacySchema(many=True)