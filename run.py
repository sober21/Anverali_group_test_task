import sqlalchemy
import sqlalchemy.orm
from app import app, db
from app.models import User, Executor, Customer


@app.shell_context_processors
def make_shell_context():
    return {'sa': sqlalchemy, 'so': sqlalchemy.orm, 'db': db, 'User': User, 'Executor': Executor, 'Customer': Customer}