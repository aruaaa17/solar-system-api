import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planets import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    planet_one = Planet(id=1, name="Mars", description="It's a rocky planet.")
    planet_two = Planet(id=2, name="Jupiter", description="It's a gas planet.")

    db.session.add(planet_one)
    db.session.add(planet_two)

    db.session.commit()