"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/members", methods=["POST"])
def add_one_member():
    data = request.get_json()
    if not data:
         return jsonify({"error": "No se proporcionaron datos"}), 400
    
    nuevo_member = {
         
                "id": jackson_family._generate_id(),
                "first_name": data.get("first_name"),
                "last_name": data.get("last_name"),
                "age": data.get("age"),
                "lucky_numbers": data.get("lucky_numbers")
            
    }

    miembro_agregado = jackson_family.add_member(nuevo_member)

    if miembro_agregado:
        return jsonify(nuevo_member), 200
    else:
        return "El mienmbro no se pudo agregar", 400
    
@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    return jsonify(response_body), 200

@app.route("/members/<int:member_id>", methods=["GET"])
def get_one_member(member_id=None):
    member = jackson_family.get_member(member_id)
    return jsonify(member), 200

@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id=None):
    member_to_delete = jackson_family.delete_member(member_id)

    return jsonify(member_to_delete), 200






# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
