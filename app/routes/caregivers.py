from flask import Blueprint, request, jsonify
from app.models import Caregiver, db, caregivers_schema

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
