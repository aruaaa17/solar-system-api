from flask import Blueprint, jsonify, abort, make_response

class Planet():
    def __init__(self, id, name, description, distance):
        self.id = id
        self.name = name
        self.description = description
        self.distance = distance


planet_list = [
    Planet(1, "Mercury", "A rocky planet", 1),
    Planet(2, "Venus", "A rocky planet", 2),
    Planet(3, "Earth", "A rocky planet", 3),
    Planet(4, "Mars", "A gas planet", 4),
    Planet(5, "Jupiter", "A gas planet", 5),
    Planet(6, "Saturn", "A gas planet", 6),
    Planet(7, "Uranus", "A ice planet", 7),
    Planet(8, "Neptune", "A ice planet", 8)
]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"msg": f'Invalid id {planet_id}'}, 400))
    for planet in planet_list:
        if planet.id == planet_id:
            return planet
    return abort(make_response({"msg": f'No planet with id {planet_id}'}, 404))
    


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planet_list_as_dict = [vars(planet) for planet in planet_list]
    return jsonify(planet_list_as_dict), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name
    }, 200

