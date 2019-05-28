from app.errors import errors
from flask import render_template

from app import login_manager


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('403.html'), 403


@errors.app_errorhandler(404)
def not_found_error_404(error):
    return render_template('404.html'), 404


@errors.app_errorhandler(500)
def internal_server_error_500(error):
    return render_template('500.html'), 500
