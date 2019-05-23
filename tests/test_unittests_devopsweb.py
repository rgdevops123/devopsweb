from flask_login import current_user
from flask_testing import TestCase
from bcrypt import gensalt, hashpw

from config import config_dict
from app import create_app, db
from app.models import User

import logging
import unittest


# Don't show logging messages while testing.
logging.disable(logging.CRITICAL)


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app = create_app(config_dict['Test'])
        return app

    def setUp(self):
        db.create_all()

        password = "123"
        hashed_password = hashpw(password.encode('utf8'), gensalt())
        admin = User(username="admin",
                     email="admin@test.com",
                     password=hashed_password)
        testuser = User(username="testuser1",
                        email="testuser1@test.com",
                        password=hashed_password)

        db.session.add(admin)
        db.session.add(testuser)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly.
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login.
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Login Form', response.data)

    # Ensure that user goes to home page after login.
    def test_home_page(self):
        response = self.client.post(
            '/login',
            data=dict(email="admin@test.com", password="123"),
            follow_redirects=True)
        self.assertIn(b'System Configuration', response.data)

    # Ensure that the login page redirects to home after login.
    def test_login_page_redirects_to_home(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(email="admin@test.com", password="123"),
                follow_redirects=True)
            response = self.client.get('/login', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Home', response.data)
            self.assertTrue(current_user.username == 'admin')

    # Ensure that register page works correctly.
    def test_register_page(self):
        response = self.client.post(
            '/register',
            data=dict(username='testuser2',
                      email="testuser2@test.com",
                      password="123",
                      confirm_password='123'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your account has been created!', response.data)

    # Ensure that register page works correctly with taken username.
    def test_register_page_with_taken_username(self):
        response = self.client.post(
            '/register',
            data=dict(username='admin',
                      email="testuser3@test.com",
                      password="123",
                      confirm_password='123'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username is already in use.', response.data)

    # Ensure that register page works correctly with taken email.
    def test_register_page_with_taken_email(self):
        response = self.client.post(
            '/register',
            data=dict(username='testuser3',
                      email="admin@test.com",
                      password="123",
                      confirm_password='123'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email is already in use.', response.data)

    # Ensure that the register page redirects to home after login.
    def test_register_page_redirects_to_home(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(email="admin@test.com", password="123"),
                follow_redirects=True)
            response = self.client.get('/register', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Home', response.data)
            self.assertTrue(current_user.username == 'admin')

    # Ensure that the user can get the account page after login.
    def test_account_page(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(email="admin@test.com", password="123"),
                follow_redirects=True)
            response = self.client.get('/account')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Account Info', response.data)
            self.assertTrue(current_user.username == 'admin')

    # Ensure that the user can update account info.
    def test_update_account_page(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(email="admin@test.com", password="123"),
                follow_redirects=True)
            response = self.client.post(
                '/account',
                data=dict(username='admin1',
                          email="admin1@test.com",
                          company="testCompany"),
                follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Account Info', response.data)
            self.assertTrue(current_user.username == 'admin1')

    # Ensure that the reset request page works correctly.
    def test_reset_request_page(self):
        with self.client:
            response = self.client.post(
                '/reset_request',
                data=dict(email="admin@test.com"),
                follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Email sent with instructions', response.data)

   # Ensure that the reset request page works correctly with bad account.
    def test_reset_request_page_with_bad_account(self):
        with self.client:
            response = self.client.post(
                '/reset_request',
                data=dict(email="admin10@test.com"),
                follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Account does not exist.', response.data)

    # Ensure that the reset password page works correctly.
    def test_reset_password_page(self):
        with self.client:
            response = self.client.post(
                '/reset_password/123',
                follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'invalid or expired token', response.data)


if __name__ == '__main__':
    unittest.main()
