# from app import db

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
