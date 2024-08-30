import hashlib
from flask_jwt_extended import create_access_token, create_refresh_token


def generate_md5_salted(password, salt):
    salted_password = password + salt
    md5_hash = hashlib.md5(salted_password.encode()).hexdigest()
    return md5_hash


def generate_token(user_id):
    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return {
        'access_token': 'Bearer ' + access_token,
        'refresh_token': 'Bearer ' + refresh_token,
    }


def response(data=None, message='ok', success=True, code=200):
    return {"success": success, "data": data, "message": message}, code




