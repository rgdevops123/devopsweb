from flask import Blueprint

blueprint = Blueprint('home_blueprint',
                      __name__,
                      template_folder='templates',
                      static_folder='static')
