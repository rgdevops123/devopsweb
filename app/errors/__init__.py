from flask import Blueprint

blueprint = Blueprint('errors_blueprint',
                      __name__,
                      template_folder='templates')

