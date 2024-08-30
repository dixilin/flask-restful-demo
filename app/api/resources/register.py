import uuid
from flask_restful import Resource, reqparse
from ..models.user import UserModel
from ..utils.common import generate_md5_salted, response
from ..schema.register_sha import register_args_valid


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        register_args_valid(parser)
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return response(success=False, message='Username already registered', code=400)
        else:
            try:
                data['salt'] = uuid.uuid4().hex
                data['pwd'] = generate_md5_salted(data['pwd'], data['salt'])
                user = UserModel(**data)
                user.add_user()
                return response(message='User registered', code=200)
            except Exception as e:
                return response(success=False, message=f'error: {e}', code=500)
