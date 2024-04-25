import sqlalchemy as sa
from flask import render_template, flash, url_for, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        klass_user = 'executor' if request.form.get('executor') else 'customer'
        user = db.session.scalar(sa.select(User).where(User.email == form.email.data))
        return redirect(url_for(klass_user, username=user.username))

    if form.validate_on_submit():
        klass_user = 'executor' if request.form.get('executor') else 'customer'
        query = sa.select(User).where(User.email == form.email.data)
        user = db.session.scalar(query)
        if user is None or not user.check_password(form.password.data) or klass_user != user.klass_user:
            flash('Неправильная почта или пароль')
            return redirect(url_for('login'))
        return redirect(url_for(klass_user, username=user.username))
    return render_template('login.html', form=form, title='Вход')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        klass_user = 'executor' if request.form.get('executor') else 'customer'
        try:
            user = User(username=form.username.data, email=form.email.data, klass_user=klass_user)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегистрировались')
        except:
            db.session.rollback()
            flash('Пользователь с такой почтой или именем уже существует')
            return render_template('register.html', form=form, title='Регистрация')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Регистрация')


@app.route('/user/executor/<username>')
@login_required
def executor(username):
    user = db.session.scalar(sa.select(User).where(User.username == username))
    return render_template('executor.html', user=user)


@app.route('/user/customer/<username>')
@login_required
def customer(username):
    user = db.session.scalar(sa.select(User).where(User.username == username))
    return render_template('customer.html', user=user)
