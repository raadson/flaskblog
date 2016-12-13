#coding=utf-8
__author__ = 'Ladson'
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Required,EqualTo,Email,Regexp
from www.model.models import User

class LoginForm(FlaskForm):
    # 定义一个文本框                   需要验证时候为空
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)
    password = PasswordField('password',validators=[Required()])
    submit = SubmitField('submit')

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email])
    username = StringField('username',validators=[DataRequired()])
    password1 = PasswordField('password',validators=[DataRequired()])
    password2 = PasswordField('确认密码：', validators=[DataRequired(), EqualTo('password1', message="密码不匹配")])
    submit = SubmitField('submit')
    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError(u'邮箱地址已被注册')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError(u'用户名已被注册')