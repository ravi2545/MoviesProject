from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
#from flask.ext.script import Manager
import src.controllers.api as flask_app
import configparser
import os


if __name__ == '__main__':
    config = configparser.ConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename=os.path.join(dir_path, 'configuration/server_config.ini')
    config.read(filename)
    application = DispatcherMiddleware(flask_app.create_app())
    run_simple(config['dev_server']['host'], int(config['dev_server']['port']), application, use_reloader=True)