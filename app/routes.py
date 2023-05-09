from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planets import Planet
from app.models.moons import Moon


def get_valid_item_by_id(model, id):
    try:
        id = int(id)
    except:
        abort(make_response({'msg': f"Invalid id '{id}'"}, 400))

    item = model.query.get(id)

    return item if item else abort(make_response({'msg': f"No {model.__name__} with id {id}"}, 404))

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"msg": f'Invalid id {planet_id}'}, 400))


#     planet = Planet.query.get(planet_id)

#     return planet if planet else abort(make_response({"msg": f'No planet with id {planet_id}'}, 404))
    


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_all_planets():
    name_query = request.args.get("name")
    if name_query:
        all_planets = Planet.query.filter_by(name=name_query)
    else:
        all_planets=Planet.query.all()
    planets_response = []
    for planet in all_planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_single_planet(planet_id):
    planet = get_valid_item_by_id(Planet, planet_id)
    Planet.query.get(planet_id)
    
    return planet.to_dict(), 200


@planets_bp.route("", methods=['POST'])
def create_planet():

    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

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
    planet_to_update = get_valid_item_by_id(Planet, planet_id)
    
    planet_to_update.name = request_body['name'] if 'name'in request_body else planet_to_update.name
    planet_to_update.description = request_body['description'] if 'description'in request_body else planet_to_update.description
    
    db.session.commit()
    return planet_to_update.to_dict(), 200


@planets_bp.route("/<planet_id>",methods=["DELETE"])
def delete_one_planet(planet_id):
    planet_to_delete = get_valid_item_by_id(Planet, planet_id)
    
    db.session.delete(planet_to_delete)
    db.session.commit()
    
    return f'Planet {planet_to_delete.name} is deleted!', 200




moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

@moons_bp.route("", methods=['GET'])
def handle_all_moons():
    name_query = request.args.get("name")
    if name_query:
        all_moons = Moon.query.filter_by(name=name_query)
    else:
        all_moons=Moon.query.all()
    moons_response = []
    for moon in all_moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response), 200

@moons_bp.route("/<moon_id>", methods=["GET"])
def handle_single_moon(moon_id):
    moon = get_valid_item_by_id(Moon, moon_id)
    Moon.query.get(moon_id)
    
    return moon.to_dict(), 200


@moons_bp.route("", methods=['POST'])
def create_moon():

    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return {
        "id": new_moon.id,
        "name": new_moon.name,
        "msg": "Successfully created",
        "discovery": new_moon.discovery
    }, 201
    

@moons_bp.route("/<moon_id>", methods=['PUT'])
def update_one_moon(moon_id):
    request_body = request.get_json()
    moon_to_update = get_valid_item_by_id(Moon, moon_id)
    
    moon_to_update.name = request_body['name'] if 'name'in request_body else moon_to_update.name
    moon_to_update.discovery = request_body['discovery'] if 'discovery'in request_body else moon_to_update.discovery
    
    db.session.commit()
    return moon_to_update.to_dict(), 200


@moons_bp.route("/<moon_id>",methods=["DELETE"])
def delete_one_moon(moon_id):
    moon_to_delete = get_valid_item_by_id(Moon, moon_id)
    
    db.session.delete(moon_to_delete)
    db.session.commit()
    
    return f'Moon {moon_to_delete.name} is deleted!', 200