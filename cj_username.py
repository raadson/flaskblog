#coding=utf-8
__author__ = 'Ladson'
from www import db
from www.model import models
#新增用户
def add_com(u):
    db.session.add(u)
    db.session.commit()

u = models.user_name(username='john',email='john@email.com',password='zzzzzz')
add_com(u)
w = models.user_name(username='susan',email='susan@email.com',password='zzzzzz')
add_com(w)

#session.add( )添加数据
#session.commit( )提交事务