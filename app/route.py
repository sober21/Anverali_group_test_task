from urllib.parse import urlsplit

import sqlalchemy as sa
from flask import render_template, flash, url_for, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import RegisterForm, LoginForm, EditProfileForm
from app.models import User
from app import app, db


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Главная')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        klass_user = 'executor' if request.form.get('executor') else 'customer'
        query = sa.select(User).where(User.email == form.email.data)
        user = db.session.scalar(query)
        if user is None or not user.check_password(form.password.data) or klass_user != user.klass_user:
            flash('Неправильная почта или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form, title='Вход')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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


@app.route('/user/<username>')
def user(username):
    user = db.session.scalar(sa.select(User).where(User.username == username))
    klass_user = user.klass_user
    return render_template(f'{klass_user}.html', user=user)


# @app.route('/user/executor/<username>')
# def executor(username):
#     user = db.first_or_404(sa.select(User).where(User.username == username))
#     return render_template('executor.html', user=user)
#
#
# @app.route('/user/customer/<username>')
# def customer(username):
#     user = db.first_or_404(sa.select(User).where(User.username == username))
#     return render_template('customer.html', user=user)


@app.route('/edit_profile', methods=['POST', 'GET'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Изменения успешно сохранены!')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form, title='Профилье')
