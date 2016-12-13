#coding=utf-8
__author__ = 'Ladson'
# CSRF_ENABLED配置是为了激活跨站点请求伪造保护
# SECRET_KEY是当CSRF激活后，建立一个加密令牌，用于验证表单
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-geuss'
SQLALCHEMY_TRACK_MODIFICATIONS = True
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#db文件创建在与创建脚本同一目录下
# SQLALCHEMY_DATABASE_URI是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径。
# SQLALCHEMY_MIGRATE_REPO 是用来存储SQLAlchemy-migrate数据库文件的文件夹。
#SQLALCHEMY_TRACK_MODIFICATIONS 不设为True会报错(貌似段代码没有也能正常运行)