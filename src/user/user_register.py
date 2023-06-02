from flask import Blueprint,request, Response
import os
import configparser
from flask import current_app



user_api = Blueprint('userapi', __name__)
config = configparser.ConfigParser() 
dir_path = os.path.dirname(os.path.realpath(__file__))


class UserManagementApi:
    def __init__(self):
        pass

    @user_api.route('/login', methods=['POST'])
    def authenticate_user():
        if not request.json or 'username'  not in  request.json or 'password' not in request.json or 'reenterpassword' not in request.json:
            return Response("Invalid Input", status=400)

        username = request.json['username']
        password = request.json['password']
        reenterpassword = request.json['reenterpassword']

        current_app.logger.info('Received login request by '+username)

        # return UserManagementServiceFactory().get_authentication_service(config['user_management_module']['auth_service']).authenticate_user(username,password)
        #return Response("Login successful", status=200)