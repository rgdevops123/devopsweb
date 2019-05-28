from app.overview_kubernetes import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/overview-kubernetes')
@login_required
def overview_kubernetes():
    with blueprint.open_resource('overview_kubernetes.txt', "r") as f:
        content = f.read()

    return render_template('overview_kubernetes.html', content=content)
