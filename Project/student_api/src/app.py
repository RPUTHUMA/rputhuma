#src/app.py

from flask import Flask
from .config import app_config
from .views.StudentView import student_api as student_blueprint 
from .models import db

def create_app(env_name):
    """
        create app
    """
    #initialization of the app
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)
    app.register_blueprint(student_blueprint, url_prefix='/api/v1/student')

    @app.route('/',methods=['GET'])
    def index():
        """
            example endpoint
        """
        return 'Congratulations!!!'
    return app
    

