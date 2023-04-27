from app import db

class Planet(db.Model):
    id = db.Column(db.integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    description = db.Column(db.string)