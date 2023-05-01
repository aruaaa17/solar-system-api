from flask import Flask
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planets import Planet


def create_app():
    app = Flask(__name__)



def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"msg": f'Invalid id {planet_id}'}, 400))


    planet = Planet.query.get(planet_id)

    return planet if planet else abort(make_response({"msg": f'No planet with id {planet_id}'}, 404))
    


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_all_planets():
    all_planets = Planet.query.all() 
    planets_response = []
    for planet in all_planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_single_planet(planet_id):
    planet = validate_planet(planet_id)
    Planet.query.get(planet_id)
    
    # return {
    #     "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description
    # }, 200
    
    return jsonify(vars(planet))


@planets_bp.route("", methods=['POST'])
def create_planet():

    request_body = request.get_json()
    # print("just the request body", request_body)
    # print("HIIII", request_body["name"])
    new_planet = Planet(name=request_body["name"], description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return {
        "id": new_planet.id,
        "name": new_planet.name,
        "msg": "Successfully created",
        "description": new_planet.description
    }, 201
    

@planets_bp.route("/<planet_id>", methods=['PUT'])
def update_one_planet(planet_id):
    request_body = request.get_json()
    planet_to_update = validate_planet(planet_id)
    planet_to_update.name = request_body['name']
    update_one_planet.description = request_body["description"]
    db.session.commit()
    return planet_to_update.to_dict(), 200


@planets_bp.route("/<planet_id>",methods=["DELETE"])
def delete_one_planet(planet_id):
    planet_to_delete = validate_planet(planet_id)
    
    db.session.delete(planet_to_delete)
    db.session.commit()
    
    return f'Planet {planet_to_delete.name} is deleted!', 200