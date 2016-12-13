#coding=utf-8
__author__ = 'Ladson'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager



#创建项目对象
app = Flask(__name__)


app.config.from_object('config')

#模块下的setting文件名，不用加py后缀
# www.config.from_object('www.settings')
# www.config.from_envvar('FLASKR_SETTINGS')
#环境变量，指向配置文件setting的路径

db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
#导入login模块
#flask-lonin需要一个LoginManager( )实例
#init_app(应用名)配置到应用中
#login_view 那个视图允许登入

from www.model import models, Category

from www.controller import blog_message
