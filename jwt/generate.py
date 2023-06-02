__author__ = 'Ravi Prasad Sanaboina'

import secrets
import base64

def generate_secrate_key():
    jwt_secret_key = secrets.token_urlsafe(32)
    jwt_secret_key_encoded = base64.b64encode(jwt_secret_key.encode('utf-8')).decode('utf-8')

    return jwt_secret_key_encoded