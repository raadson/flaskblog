#coding=utf-8
__author__ = 'Ladson'

from www import db
import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

sep = os.sep#路径分隔符windows是“\”

class Role(db.Model):
    # __tablename__ = 'Roles'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    #email = db.Column(db.String(120), index=True,unique=True)
    # users = db.relationship('User', backref='role', lazy='dynamic')
    # password = db.Column(db.String(16))
    # def __init__(self,username,password):
    #     self.username = username
    #     self.password = password
    def avatar(self,size):
        return sep + 'static'+sep+'img'+sep+'1.jpg'+' width='+size
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        try:
            return  unicode(self.id)#if pythons so :str(self.id)
        except NameError:
            return str(self.id)
    def __repr__(self):
        return '<User %r>' % self.nickname

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    # user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

# db.Column( )是创建一列
# db.Integer 是整数类型
# db.String 是字符串类型
# primary_key = True 是主键
# index=True 增加索引
# unique=True 整表唯一
# db.relationship( )，第一个参数是类名，第二个backref名字好像是随便(这个参数是在新增数据时user_id 用 authou 代替 )，第三个固定lazy='dynamic'
# db.relationship( )定义主键和外键的联系
# db.ForeignKey( )是外键
# __repr__方法告诉Python如何打印class对象，方便我们调试使用。

class User(UserMixin,db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), index=True,unique=True)
    username = db.Column(db.String(64), index=True, unique=True)

    password_hash = db.Column(db.String(128))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)