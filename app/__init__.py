import os
from flask import Flask, jsonify
from .config import config
from .api.models import db
from .api import api_blueprint
from .manage import migrate
from .api.models.user import UserModel
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis


def jwt_custom_handler(jwt):
    @jwt.expired_token_loader
    # 双token返回不同错误码，可进行无感刷新
    def my_expired_token_callback(jwt_header, jwt_payload):
        if jwt_payload['type'] == 'access':
            return jsonify(err_code="50001", err="access_token has expired"), 401
        else:
            return jsonify(err_code="50002", err="refresh_token has expired"), 401

    # token已添加至黑名单自定义
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify(err_code='50000', err='The token has been revoked'), 401

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        token_in_redis = app.redis.get(jti)
        return token_in_redis is not None


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    app.jwt = JWTManager(app)
    app.redis = FlaskRedis(app)

    jwt_custom_handler(app.jwt)

    app.register_blueprint(api_blueprint)
    return app


# 初始化项目
app = create_app(os.getenv('FLASK_ENV', 'development'))
