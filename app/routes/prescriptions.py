from flask import Blueprint, jsonify
from app.models import Drug, drugs_schema, Pharmacy, pharmacies_schema

prescriptions_route = Blueprint('prescriptions', __name__)


@prescriptions_route.route('/drugs', methods=['GET'])
def get_drugs():
    drugs = Drug.query.all()
    drugs = drugs_schema.dump(drugs)

    return jsonify({
        "status": "success",
        "drugs": drugs
    }), 200


@prescriptions_route.route('/pharmacy', methods=['GET'])
def get_pharmacies():
    pharmacies = Pharmacy.query.all()
    pharmacies = pharmacies_schema.dump(pharmacies)

    return jsonify({
        "status": "success",
        "pharmacies": pharmacies
    }), 200
