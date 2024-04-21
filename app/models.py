from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    hash_password: so.Mapped[None | str] = so.mapped_column(sa.String(256))

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

