from bcrypt import gensalt, hashpw
from config import config_dict
from pytest import fixture
from app import create_app, db


@fixture
def base_client():
    app = create_app(config_dict['Test'])
    app_ctx = app.app_context()
    app_ctx.push()
    db.session.close()
    db.drop_all()
    yield app.test_client()
