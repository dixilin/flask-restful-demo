from flask_restful import Resource, reqparse
from ..models.user import UserModel
from flask_jwt_extended import get_jwt_identity,jwt_required,create_access_token
from ..utils.common import response,generate_md5_salted,generate_token
from ..schema.register_sha import register_args_valid


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        register_args_valid(parser)
        data = parser.parse_args()

        user_tuple = UserModel.find_by_username(data['username'])
        if user_tuple:
            try:
                (user, ) = user_tuple
                pwd, salt = user.get_pwd()['pwd'], user.get_pwd()['salt']
                if generate_md5_salted(data['pwd'], salt) != pwd:
                    return response(success=False, message='Password is wrong!', code=403)
                else:
                    return response(data=generate_token(user.id))
            except Exception as e:
                return response(success=False, message=f'Error: {e}', code=500)
        else:
            return response(success=False, message='Unregistered username!', code=400)

    @jwt_required(refresh=True)
    def get(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return response(data={'access_token': 'Bearer ' + access_token})



