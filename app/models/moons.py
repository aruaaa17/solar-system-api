from app import db


class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    discovery = db.Column(db.Integer)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="moons")

def to_dict(self):
    return {
        "id": self.id,
        "name":self.name,
        "discovery": self.discovery,
        "planet_id": self.planet_id
    }
    
@classmethod
def from_dict(cls, moon_details):
    new_moon = cls(
        name=moon_details["name"],
        discovery=moon_details["discovery"],
        planet_id=moon_details["planet_id"]
    )
    return new_moon

