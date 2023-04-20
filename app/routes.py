from flask import Blueprint, jsonify

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


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planet_list_as_dict = [vars(planet) for planet in planet_list]
    return jsonify(planet_list_as_dict), 200


# class planet():
#     def __init__(self, id, species, name, habitat):
#         self.id = id
#         self.species = species
#         self.name = name
#         self.habitat = habitat

# planet_list = [
#     planet(1, "Anaconda", "Nikki Minaj", "Jungle"),
#     planet(2, "Elephant", "Dumbo", "Our childhood!!!"),
#     planet(3, "Unicorn", "Charlie", "Youtube")
# ]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=['GET'])
# def handle_planets():
#     planet_list_as_dict = [vars(planet) for planet in planet_list]
#     return jsonify(planet_list_as_dict), 200