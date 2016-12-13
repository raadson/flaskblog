#coding=utf-8
__author__ = 'Ladson'
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True
# session必须要设置key
SECRET_KEY = 'fdagfdaghfdah'

#mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://root:qaz@localhost:3306/test"