from app.errors import blueprint
from flask import render_template

from app import login_manager


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('403.html'), 403

