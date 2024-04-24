import sqlalchemy as sa
from flask import render_template, flash, url_for, redirect, request
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
    if form.validate_on_submit():
        klass_user = 'executor' if request.form.get('executor') else 'customer'
        query = sa.select(User).where(User.email == form.email.data)
        user = db.session.scalar(query)
        if user is None or not user.check_password(form.password.data) or klass_user != user.klass_user:
            flash('Неправильная почта или пароль')
            return redirect(url_for('login'))
        return redirect(url_for(klass_user))
    return render_template('login.html', form=form, title='Вход')


@app.route('/logout')
def logout():
    db.session.close()
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        klass_user = 'executor' if request.form.get('executor') else 'customer'
        user = User(email=form.email.data, klass_user=klass_user)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Регистрация')


@app.route('/user/executor')
def executor():
    return render_template('executor.html')


@app.route('/user/customer')
def customer():
    return render_template('customer.html')