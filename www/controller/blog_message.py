#coding=utf-8
__author__ = 'Ladson'
from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import  login_user,logout_user,current_user,login_required
from www import app, db,lm
from www.forms import LoginForm,RegistrationForm
from www.model import models
from www.model.models import User,Role

@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))
    # eturn User.query.filter(User.id==userid).first()

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    # user = {'nickname':'Bob'}
    posts = [
        {'author': {'nickname':'John'},
         'body': 'Beautiful day in Portland!'},
        {'author': {'nickname':'Susan'},
         'body': 'The Avengers movie was so cool!'}
    ]
    return render_template(
        "index.html",
        title='Home',
        user=user,
        posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if models.User.query.filter_by(username=form.openid.data).first():
            user = User.query.filter_by(username=form.openid.data).first_or_404()
            if user and user.verify_password(form.password.data):
                login_user(user)
        #flash('login requested for OpenID="'+form.openid.data+'",remember_me='+str(form.remember_me.data))
                return redirect(url_for('index'))
            else:
                return render_template('login.html',
                                   title = 'Sign In',
                                   error = '[NO]',
                                   form = form
                                   )
    return render_template(
        'login.html',
        title = "Sign In",
        form = form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering')
        return redirect(url_for('login'))
        #if form.validate_on_submit():

    return render_template(
         'register.html',
            title = "Register",
         form = form
    )
#登出时
@app.route('/logout')
@login_required#意思是登录以后才能访问看到这个页面
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<nickname>')
@login_required
def get_user(nickname):
    user = User.query.filter_by(username=nickname).first()
    if user ==None:
        flash('user'+nickname+'not found!')
        return redirect(url_for('index'))
    posts = [
        {'author':user,'body':'Test port #1 !!!'},
        {'author':user,'body':'Test post #2 !!!'}
        ]
    return render_template('user.html',
                           user=user,
                           posts=posts
                           )
