from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    hash_password: so.Mapped[None | str] = so.mapped_column(sa.String(256))
    klass_user: so.Mapped[str] = so.mapped_column(sa.String(15))

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Executor(User, db.Model):
    """Класс исполнителя"""
    klass_user = 'executor'
    def __repr__(self):
        return f'<Исполнитель {self.username}>'


class Customer(User, db.Model):
    """Класс заказчика"""
    klass_user = 'customer'
    def __repr__(self):
        return f'<Заказчик {self.username}>'
