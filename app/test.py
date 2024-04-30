import os

os.environ['DATABASE_URL'] = 'sqlite://'
from unittest import TestCase, main
from app import app, db
from app.models import User


class ModelUserTests(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_check_password(self):
        user = User(username='Maxim', email='max@mail.ru', klass_user='executor')
        user.set_password('111')
        self.assertTrue(user.check_password('111'))
        self.assertFalse(user.check_password('222'))
        self.assertFalse(user.check_password(''))


if __name__ == '__main__':
    main()
