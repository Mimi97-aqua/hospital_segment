from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.String, primary_key=True)
    first_names = db.Column(db.String(100), nullable=False)
    middle_name_initial = db.Column(db.String(10), nullable=False)
    last_names = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Boolean, nullable=False) # 1 for male and 0 for female
    date_of_birth = db.Column(db.Date, nullable=False)
    legal_status = db.Column(db.String(50), nullable=False)
    maid_number = db.Column(db.Integer(20), nullable=False)
    ssn = db.Column(db.Integer(20), nullable=False)
    phone_number = db.Column(db.Integer(10), nullable=False)
    address_1 = db.Column(db.String(50), nullable=False)
    address_2 = db.Column(db.String(50), nullable=True)  # An optional field
    city_state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer(5), nullable=False)
    profile_photo = db.Column(db.String(200), nullable=True)  # All patients must not have photos
    #prescriptions = db.relationship('Prescription', backref='participant', lazy=True)

#
# class Prescription(db.Model):
#     __tablename__ = 'prescriptions'