from flask import render_template
from app.forms import RegisterForm, LoginForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', form=form, title='Вход')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form, title='Регистрация')