import os
from datetime import datetime, timedelta

from flask import request, flash, Blueprint, jsonify, current_app
from app.models import *
from werkzeug.utils import secure_filename

participants_routes = Blueprint('participants', __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@participants_routes.route('/create/<string:caregiver_id>', methods=['POST'])
def create_participant(caregiver_id):
    """
    Creates participant
    """
    if request.method == 'POST':
        # Handle photo upload
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
            caregiver = Caregiver.query.get_or_404(caregiver_id)
            first_names = request.form.get('first_names')
            middle_name_initial = request.form.get('middle_name_initial')
            last_names = request.form.get('last_names')
            gender = request.form.get('gender')
            date_of_birth = datetime.strptime(request.form.get('date_of_birth'), '%Y-%m-%d').date()
            legal_status = request.form.get('legal_status')
            maid_number = int(request.form.get('maid_number'))
            ssn = int(request.form.get('ssn'))
            phone_number = int(request.form.get('phone_number'))
            address_1 = request.form.get('address_1')
            address_2 = request.form.get('address_2')
            city_state = request.form.get('city_state')
            zip_code = int(request.form.get('zip_code'))

            required_params = [first_names, last_names, gender, date_of_birth, legal_status, maid_number, ssn,
                               phone_number, address_1, city_state, zip_code]
            if any(params is None for params in required_params):
                raise ValueError("Missing parameter(s)")

            new_participant = Participant(
                caregiver_id=caregiver.id,
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
            "message": f"{request.method} not allowed"
        }), 405


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
    """
    Displays all participant details.
    """
    try:
        participants = Participant.query.all()
        participants = participants_schema.dump(participants)

        return jsonify({
            "status": "success",
            "count": len(participants),
            "participant_details": participants
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@participants_routes.route('/delete/<string:participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    """
    Deletes a specified participant using their user ID
    """
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
    Edit participant details (partial update)
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

            if 'profile_photo' in request.files:
                file = request.files['profile_photo']

                if file.filename == '':
                    return jsonify({
                        "status": "error",
                        "message": "No selected file"
                    }), 400

                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                    participant.profile_photo = filename
                else:
                    return jsonify({
                        "status": "error",
                        "message": "File type not allowed."
                    }), 400

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


@participants_routes.route('/prescribe', methods=['POST'])
def create_prescription():
    """
    Prescribes medication for the participant (patient)
    """
    if request.method == 'POST':
        #caregiver = Caregiver.query.get_or_404(caregiver_id)
        caregiver_id = request.form.get('caregiver_id')
        participant_id = request.form.get('participant_id')
        #participant = Participant.query.get_or_404(participant_id)
        # caregiver = db.session.query(Caregiver).get(caregiver_id)
        # participant = db.session.query(Participant).get(participant_id)
        drug_id = request.form.get('drug_id')
        reason_for_medication = request.form.get('reason_for_medication')
        prescriber = request.form.get('prescriber')
        pharmacy_id = request.form.get('pharmacy_id')
        quantity_dosage = int(request.form.get('quantity_dosage'))
        refills = int(request.form.get('refills'))
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
        expiry_date = start_date + timedelta(days=refills * 30) + timedelta(days=1 * 30)
        dose = int(request.form.get('dose'))
        frequency = int(request.form.get('frequency'))
        comment = request.form.get('comment')

        dose_times = []
        for x in range(dose):
            dose_time_key = f"dose_time_{x+1}"

            if dose_time_key in request.form:
                dose_time = datetime.strptime(request.form.get(dose_time_key), '%H:%M').time()
                dose_times.append(dose_time)
            else:
                return jsonify({
                    "status": "error",
                    "message": f"Dose time {x+1} is missing. Please insert."
                }), 400

        new_prescription = Prescription(
            caregiver_id=caregiver_id,
            participant_id=participant_id,
            drug_id=drug_id,
            reason_for_medication=reason_for_medication,
            prescriber=prescriber,
            pharmacy_id=pharmacy_id,
            quantity_dosage=quantity_dosage,
            refills=refills,
            start_date=start_date,
            expiry_date=expiry_date,
            frequency=frequency,
            dose=dose,
            comment=comment
        )

        db.session.add(new_prescription)
        db.session.commit()

        for dose_time in dose_times:
            new_dose_time = DoseTime(
                prescription_id=new_prescription.id,
                time=dose_time
            )

            db.session.add(new_dose_time)

        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Prescription has been successfully created!"
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid HTTP verb"
        }), 400


@participants_routes.route('/prescriptions/<string:participant_id>')
def list_all_participant_prescriptions(participant_id):
    """
    List all the prescriptions created for a given participant.
    """
    try:
        # participant = Participant.query.get_or_404(participant_id)
        prescriptions = Prescription.query.filter_by(participant_id=participant_id).all()

        prescriptions_list = []
        for prescription in prescriptions:
            prescriptions_list.append({
                "id": prescription.id,
                "name": prescription.drugs.name,
                "dose": prescription.dose,
                "time": [dose_time.time.strftime('%H:%M') for dose_time in prescription.dose_times],
                "instruction": prescription.comment,
                "action": prescription.action
            })

        return jsonify({
            "status": "success",
            "prescriptions_count": len(prescriptions_list),
            "prescriptions": prescriptions_list
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@participants_routes.route('/administer/<string:participant_id>/prescription/<int:prescription_id>', methods=['POST'])
def administer_prescription(participant_id, prescription_id):
    """
    Marks a prescription as either administered or unadministered.
    """
    try:
        prescription = Prescription.query.filter_by(id=prescription_id, participant_id=participant_id).first_or_404()

        prescription.action = True

        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Prescription successfully given.",
            "prescription": {
                "id": prescription.id,
                "name": prescription.drugs.name,
                "dose": prescription.dose,
                "time": [dose_time.time.strftime('%H:%M') for dose_time in prescription.dose_times],
                "instruction": prescription.comment,
                "action": prescription.action
            }
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": f"Database was rolled back\nstr(e)"
        }), 400
