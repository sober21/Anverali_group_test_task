from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[None | str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    klass_user: so.Mapped[str] = so.mapped_column(sa.String(15))
    hash_password: so.Mapped[None | str] = so.mapped_column(sa.String(256))
    about_me: so.Mapped[None | str] = so.mapped_column(sa.String(512))


    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __repr__(self):
        return f'<{self.klass_user}: {self.username}>'



