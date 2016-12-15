__author__ = 'Ladson'
from www import db
from www.model import models

admin_role = models.Role(name='Admin')
mod_role = models.Role(name='Moderator')
user_role = models.Role(name='User')

user_john = models.User(username='john', role=admin_role)
user_susan = models.User(username='susan',role=user_role)
user_david = models.User(username='david', role=user_role)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)
db.session.commit()