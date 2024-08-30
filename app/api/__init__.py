from flask import Blueprint
from flask_restful import Api
from .resources.register import Register
from .resources.login import Login
from .resources.log_out import LogOut
from .resources.user import User
api_blueprint = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_blueprint)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login', '/refresh_token')
api.add_resource(LogOut, '/log_out')
api.add_resource(User, '/user_all')
