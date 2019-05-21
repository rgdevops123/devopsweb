from flask import jsonify, render_template, redirect, request, url_for

from app import login_manager
from app.base import blueprint


@blueprint.route('/')
def route_default():
    return redirect(url_for('users_blueprint.login'))
