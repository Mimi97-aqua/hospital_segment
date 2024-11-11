from flask import Blueprint, request, jsonify
from app.models import Caregiver, db, caregivers_schema, Participant

caregiver_route = Blueprint('caregiver_route', __name__)


@caregiver_route.route('/create', methods=['POST'])
def create_caregiver():
    """
    Creates a new caregiver
    """
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('email')

            new_caregiver = Caregiver(
                name=name,
                email=email,
                phone=phone
            )

            db.session.add(new_caregiver)
            db.session.commit()

            return jsonify({
                "status": "success",
                "message": "Caregiver successfully created."
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 400
    else:
        return jsonify({
            "status": "error",
            "message": "Method not allowed."
        }), 405


@caregiver_route.route('/details', methods=['GET'])
def view_caregiver_details():
    """
    Displays all caregiver details
    """
    try:
        caregivers = Caregiver.query.all()
        caregivers = caregivers_schema.dump(caregivers)

        return jsonify({
            "status": "success",
            "count": len(caregivers),
            "caregiver_details": caregivers
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@caregiver_route.route('/<string:caregiver_id>/participants', methods=['GET'])
def list_participants_for_caregiver(caregiver_id):
    """
    List all participants associated with a caregiver.
    """
    try:
        caregiver = Caregiver.query.get_or_404(caregiver_id)
        participants = Participant.query.filter_by(caregiver_id=caregiver_id).all()

        participants_list = []
        for participant in participants:
            participants_list.append({
                "id": participant.id,
                "name": participant.first_names + " " + participant.last_names
            })

        return jsonify({
            "status": "success",
            "caregiver": {
                "id": caregiver.id,
                "name": caregiver.name,
                "participants": participants_list
            }
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
