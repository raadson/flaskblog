#coding=utf-8
__author__ = 'Ladson'
import datetime
from www import db
from www.model import models
#新增文章
u = models.User.query.get(1)
p = models.Role(body='my first post!',timestamp=datetime.datetime.utcnow(),author=u)
db.session.add(p)
db.session.commit()
