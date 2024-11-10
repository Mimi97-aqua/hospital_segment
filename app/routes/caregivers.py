from flask import Blueprint, request, jsonify
from app.models import Caregiver, db

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