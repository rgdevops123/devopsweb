from app.overview_postgresql import  blueprint
from flask import render_template, url_for
from flask_login import login_required


@blueprint.route('/overview-postgresql')
@login_required
def overview_postgresql():
    with blueprint.open_resource('overview_postgresql.txt', "r") as f:
        content = f.read()
    return render_template('overview_postgresql.html', content=content)
