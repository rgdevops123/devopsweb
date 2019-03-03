from app.errors import blueprint
from flask import render_template

from app import login_manager


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('403.html'), 403


@blueprint.errorhandler(403)
def access_forbiden(error):
    return render_template('403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
