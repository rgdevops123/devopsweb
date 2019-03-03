from flask import jsonify, render_template, redirect, request, url_for

from app import login_manager
from app.base import blueprint


@blueprint.route('/')
def route_default():
    return redirect(url_for('users_blueprint.login'))


@blueprint.route('/about')
def about():
    pass

### Errors

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
