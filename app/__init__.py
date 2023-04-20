from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from flask import Blueprint
    from .routes import planets_bp
    
    app.register_blueprint(planets_bp)

    return app


# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     #  add our new animals blueprint
#     from flask import Blueprint
#     from .routes.animals import animals_bp

#     app.register_blueprint(animals_bp)

#     return app 