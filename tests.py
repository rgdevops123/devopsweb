import unittest

from flask_login import current_user
from flask_testing import TestCase
from bcrypt import checkpw, gensalt, hashpw

from config import config_dict
from app import create_app, db
from app.models import User


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app = create_app(config_dict['Test'])
        return app

    def setUp(self):
        db.create_all()

        username = "admin"
        email = "admin@test.com"
        password = "admin"
        hashed_password = hashpw(password.encode('utf8'), gensalt())
        user = User(username=username, email=email, password=hashed_password)

        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Login Form', response.data)

    # Ensure that user goes to home page after login
    def test_home_page(self):
        response = self.client.post(
            '/login',
            data=dict(email="admin@test.com", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'System Configuration', response.data)


if __name__ == '__main__':
    unittest.main()
