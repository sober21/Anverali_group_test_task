from flask import abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app import app, db
from app.models import User

admin = Admin(app)


class Controller(ModelView):
    def is_accessible(self):
        if current_user.is_admin:
            return current_user.is_authenticated
        return abort(404)

    def inaccessible_callback(self, name, **kwargs):
        return 'У вас нет доступа к админке'


admin.add_view(Controller(User, db.session))
