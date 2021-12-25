""" website package initializer  """

from flask import Flask

def create_app():
    """ create a flask app  """
    app = Flask(__name__)

    app.config['SPOONACULAR_KEY'] = "a8529c104d8749b4a19488d0fd654353"
    app.secret_key = 'ib90rcf42r768bxf67g8t6kn907v0k9n34x'

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
