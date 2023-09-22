from flask import Flask
import os


# test config is tells whether app undergoes testing or under user usage
def create_app(test_config=None):
    app = Flask(__name__,
                instance_relative_config=True)  # instance config tells some configurations are defined in outside here
    if test_config is None:
        app.config.from_mapping(SECRET_KEY= os.environ.get("SECRET_KEY"))  # user config
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    @app.get('/home')
    def home():
        return {"message": "Hello world"}

    return app
