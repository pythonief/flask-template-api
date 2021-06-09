"""
MyApp module for the application resourses
"""

# Import flask utilities
from flask import Flask

# Import apps utilities like register config and blueprints
from .utils import register_blueprints, load_config

# Import blueprints
# --> from myapp.blueprints.<module_name> import <bluprint_variable> as <name_blueprint>
from myapp.blueprints.home import home as home_blueprint


def create_app(json_file='config.json', db=None):
    app = Flask(__name__)
    try:
        load_config(app, json_file)
    except Exception as e:
        print(e.args[0])

    # Register blueprints --> app.register_blueprint(<blueprint_name>)
    register_blueprints(app, [
        home_blueprint,
    ])

    """
    db initialization:
        Uncomment the line below to initialize the db after configure extension
        if you don't configure the db configuration values in 'secret.json' a sqlite database will be 
        created with the name 'test.sqlite' within myapp folder
    """
    db.init_app(app)

    return app
