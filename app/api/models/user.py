from . import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'tbl_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(40), nullable=False, default='', comment='用户名')
    pwd = db.Column(db.String(102), comment='密码')
    salt = db.Column(db.String(32), comment='salt')
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.now, onupdate=datetime.now,
                           comment='更新时间')

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def get_pwd(self):
        return {
            "pwd": self.pwd,
            "salt": self.salt,
        }

    @classmethod
    def find_by_username(cls, username):
        return db.session.execute(db.select(cls).filter_by(username=username)).first()

    @classmethod
    def get_all_user(cls):
        return db.session.query(cls).all()

    # def find_all(self):
    #     return self.query.all()


