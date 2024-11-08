import json
import os
from datetime import datetime

from flask import url_for, request, redirect, flash, Blueprint, jsonify, current_app
from app import db
from app.models import *
from werkzeug.utils import secure_filename

participants_routes = Blueprint('participants', __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@participants_routes.route('/', methods=['GET'])
def index():
    return "Hello"


@participants_routes.route('/create', methods=['POST'])
def create_participant():
    """
    Create participant
    """
    # Handle photo upload
    if request.method == 'POST':
        if 'profile_photo' not in request.files:
            flash('No file part')
            return jsonify({
                "status": "error",
                "message": "No file part"
            }), 400

        file = request.files['profile_photo']
        if file.filename == '':
            flash('No selected file')
            return jsonify({
                "status": "error",
                "message": "No selected file"
            }), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        else:
            return jsonify({
                "status": "error",
                "message": "File type not allowed"
            }), 400

        try:
            first_names = request.form['first_names']
            middle_name_initial = request.form['middle_name_initial']
            last_names = request.form['last_names']
            gender = request.form['gender']
            date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
            legal_status = request.form['legal_status']
            maid_number = int(request.form['maid_number'])
            ssn = int(request.form['ssn'])
            phone_number = int(request.form['phone_number'])
            address_1 = request.form['address_1']
            address_2 = request.form['address_2']
            city_state = request.form['city_state']
            zip_code = int(request.form['zip_code'])
            profile_photo = request.files['profile_photo']

            new_participant = Participant(
                first_names=first_names,
                middle_name_initial=middle_name_initial,
                last_names=last_names,
                gender=gender,
                date_of_birth=date_of_birth,
                legal_status=legal_status,
                maid_number=maid_number,
                ssn=ssn,
                phone_number=phone_number,
                address_1=address_1,
                address_2=address_2,
                city_state=city_state,
                zip_code=zip_code,
                profile_photo=filename
            )

            db.session.add(new_participant)
            db.session.commit()

            return jsonify({
                "status": "success",
                "message": "Participant successfully created!",
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 400
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid request"
        }), 400


@participants_routes.route('/list', methods=['GET'])
def view_all_participants():
    """
    View all participants.
    Sends out only name, DOB, email, and phone number of participants.
    """
    try:
        participants = Participant.query.all()
        participants_list = [
            {
                "Name": participant.first_names + " " + participant.last_names,
                "Date of Birth": participant.date_of_birth,
                "Phone": participant.phone_number,
                "Address": participant.address_1,

            } for participant in participants
        ]

        return jsonify({
            "status": "success",
            "participants": participants_list,
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


@participants_routes.route('/details', methods=['GET'])
def view_all_participant_details():
    try:
        participants = Participant.query.all()
        participants =participants_schema.dump(participants)

        return jsonify({
            "status": "success",
            "count": len(participants),
            "participant_details": participants
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


@participants_routes.route('/delete/<string:participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    if request.method == 'DELETE':
        try:
            participant = Participant.query.get(participant_id)
            if participant is None:
                return jsonify({
                    "status": "error",
                    "message": "Participant not found"
                }), 404

            db.session.delete(participant)
            db.session.commit()

            return jsonify({
                "status": "success",
                "message": f"Participant with ID {participant_id} deleted"
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 400
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid method"
        }), 405


@participants_routes.route('/update/<string:participant_id>', methods=['PATCH'])
def edit_participant_details(participant_id):
    """
    Edit participant details
    """
    if request.method == 'PATCH':
        try:
            participant = Participant.query.get(participant_id)
            if participant is None:
                return jsonify({
                    "status": "error",
                    "message": "Participant not found"
                }), 404

            info = request.form

            if 'legal_status' in info:
                participant.legal_status = info['legal_status']
            if 'maid_number' in info:
                participant.maid_number = info['maid_number']
            if 'phone_number' in info:
                participant.phone_number = info['phone_number']
            if 'email' in info:
                participant.email = info['email']
            if 'address_1' in info:
                participant.address_1 = info['address_1']
            if 'address_2' in info:
                participant.address_2 = info['address_2']
            if 'city_state' in info:
                participant.city_state = info['city_state']
            if 'zip_code' in info:
                participant.zip_code = info['zip_code']

            if 'profile_photo' in info:
                file = request.files['profile_photo']
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                    participant.profile_photo = filename

            db.session.commit()

            return jsonify({
                "status": "success",
                "message": "Participant details updated"
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 400