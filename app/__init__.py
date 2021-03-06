
from flask import Flask
from config import config_options

# Application factory function
def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # setting config
    from .requests import config_request
    config_request(app)

    return app
