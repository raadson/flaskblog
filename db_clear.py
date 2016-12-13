#coding=utf-8
__author__ = 'Ladson'
from www import db
from www.model import models
# users = models.User.query.all()
# for u in users:
#     db.session.delete(u)
posts = models.Post.query.all()
for p in posts:
    db.session.delete(p)
users = models.Role.query.all()
for u in users:
    db.session.delete(u)
db.session.commit()
