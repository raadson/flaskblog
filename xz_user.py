#coding=utf-8
__author__ = 'Ladson'
from www import db
from www.model import models
#新增用户
def add_com(u):
    db.session.add(u)
    db.session.commit()

u = models.User(email='john@email.com',username='admin',password_hash='zzzzzz')
add_com(u)
# w = models.User(user='susan',email='susan@email.com')
# add_com(w)

#session.add( )添加数据
#session.commit( )提交事务