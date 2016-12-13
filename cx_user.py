#coding=utf-8
__author__ = 'Ladson'
from www import db
from www.model import models

users = models.User.query.all()
#print users
for u in users:
    print (u.id, u.nickname)
e = models.User.query.get(1)
e = models.User.query.all()
print (e)
print ('===================')
p = models.User.query.filter_by(nickname='john').first()
print (p.id)
print (p.email)
p.email = 'john1@163.com'#更新数据
db.session.add(p)
db.session.commit()
d = models.User.query.filter(models.User.email.endswith('@email.com')).all()
print (d)
select=str(models.User.query.filter_by(nickname='john'))#语句还原成sql语句
print (select)
# filter_by() 方法对查询结果进行过滤，参数是键值对，filter 方法也可以对结果进行过滤，但参数是布尔表达式
#query这个属性是查询，query.all( )是查询所有
#query.get( )是查询主键
#filter_by( )是单条过滤条件，first( )是选择第一条
#query.filter_by(过滤条件).first( )根据过滤条件查询第一条

# users = User.query.limit(1).offset(3)
# 从第 3 条记录开始取(注意是从 0 开开始算起)，并最多取 1 条记录