from bcrypt import gensalt, hashpw
from config import config_dict
from pytest import fixture
from app import create_app, db
from app.models import User


@fixture
def base_client():
    app = create_app(config_dict['Debug'])
    app_ctx = app.app_context()
    app_ctx.push()
    db.session.close()
    db.drop_all()
    yield app.test_client()


@fixture
def init_database():
    db.create_all()
    password = '123'
    hashed_password = hashpw(password.encode('utf8'), gensalt())
    user = User(username='testuser',
                email='testuser@email.com',
                password=hashed_password)
    db.session.add(user)
    db.session.commit()
    yield db

    db.drop_all()


@fixture
def login_disabled_client():
    app = create_app(config_dict['Test'])
    app_ctx = app.app_context()
    app_ctx.push()
    db.session.close()
    db.drop_all()
    yield app.test_client()
