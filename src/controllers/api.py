from flask import Flask
from ..hollywood.actionmovies.movieslist import movies_management_api
from ..hollywood.horrormovies.horrorlist import horror_lists
from ..jwt_security.generate_secrate_key import jwt_secret
from ..user.user_register import user_api

import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
log_filename=os.path.join(dir_path, '../../demo.log')


def initialize():
    pass

def create_app():
    app = Flask(__name__)
    app.register_blueprint(movies_management_api,url_prefix='/user')
    app.register_blueprint(horror_lists, url_prefix='/list')
    app.register_blueprint(jwt_secret, url_prefix='/jwt')
    app.register_blueprint(user_api, url_prefix='/userlogin')

    logging.basicConfig(filename=log_filename, level=logging.INFO)
    app.logger.info('Blueprints added to the application')
    
    
    return app