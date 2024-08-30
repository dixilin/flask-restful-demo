from flask_restful import Resource, fields, marshal
from ..models.user import UserModel
from ..utils.common import response
from flask_jwt_extended import jwt_required

user_fields = {
    'id': fields.Integer,
    'username': fields.String
}


class User(Resource):
    @jwt_required()
    def get(self):
        users = UserModel.get_all_user()
        if users:
            return response(data=marshal(users, user_fields))
        else:
            return response()
