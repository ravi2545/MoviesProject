"""data security"""
__author__ = 'Ravi Prasad Sanaboina'

from flask import Blueprint,request, jsonify
import codecs
import secrets
import base64


jwt_secret = Blueprint('secret', __name__)


@jwt_secret.route('/jwtsecret', methods=['GET'])
def get_jwt_secret_key():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        jwt_secret_key = secrets.token_urlsafe(32)
        jwt_secret_key_encoded = base64.b64encode(jwt_secret_key.encode('utf-8')).decode('utf-8')
        return jsonify({'data': jwt_secret_key_encoded})
    except Exception as e:
        return jsonify({'Message': str(e)})