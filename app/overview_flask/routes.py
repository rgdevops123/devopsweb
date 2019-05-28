from app.overview_flask import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/overview-flask')
@login_required
def overview_flask():
    with blueprint.open_resource('overview_flask.txt', "r") as f:
        content = f.read()
    return render_template('overview_flask.html', content=content)
