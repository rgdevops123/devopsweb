from app.home import  blueprint
from flask import render_template
from flask_login import login_required

import platform


@blueprint.route('/home')
@login_required
def home():
    hostname = platform.node()
    osdistribution = platform.linux_distribution()[0]
    osversion = platform.version()
    osrelease = platform.release()
    sysprocessor = platform.processor()
    sysarchitecture = platform.architecture()[0]
    pythonversion = platform.python_version()
    return render_template('home.html',
                           hostname=hostname,
                           osdistribution=osdistribution,
                           osversion=osversion,
                           osrelease=osrelease,
                           sysprocessor=sysprocessor,
                           sysarchitecture=sysarchitecture,
                           pythonversion=pythonversion)
