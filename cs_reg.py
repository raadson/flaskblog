__author__ = 'Ladson'
from www import db
from www.model import models

user = models.User.query.filter_by(username='adson').first()
if user is None:
    user = models.User(username='adson',email='adaf@163.com',password='zzz')
    db.session.add(user)
    db.session.commit()