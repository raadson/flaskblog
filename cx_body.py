#coding=utf-8
__author__ = 'Ladson'

from www import db
from www.model import models

u = models.User.query.get(1)
posts = u.posts.all()
print (posts)
e = models.User.query.get(2)
print (e.posts.all())