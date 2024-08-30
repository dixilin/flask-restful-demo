from flask_restful import Resource
from flask_jwt_extended import get_jwt, jwt_required
from flask import current_app
import time
from ..utils.common import response


class LogOut(Resource):
    @jwt_required(refresh=True)
    def delete(self):
        jti, exp, sub = get_jwt()['jti'], get_jwt()['exp'], get_jwt()['sub']
        ex = int(exp - time.time())
        current_app.redis.set(jti, sub, ex=ex)
        return response(message='Log out successfully')



