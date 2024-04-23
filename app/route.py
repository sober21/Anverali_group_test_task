import sqlalchemy as sa
from flask import render_template, flash, url_for, redirect, request
from app.forms import RegisterForm, LoginForm
from app.models import Executor, Customer
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        klass = Executor if request.form.get('executor') else Customer
        query = sa.select(klass).where(klass.email==form.email.data)
        user = db.session.scalar(query)
        if user is None or not user.check_password(form.password.data):
            flash('Неправильная почта или пароль')
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Вход')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        klass = Executor if request.form.get('executor') else Customer
        user = klass(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Регистрация')

