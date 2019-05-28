from app.overview_linux import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/overview-linux')
@login_required
def overview_linux():
    with blueprint.open_resource('overview_linux.txt', "r") as f:
        content = f.read()
    return render_template('overview_linux.html', content=content)
