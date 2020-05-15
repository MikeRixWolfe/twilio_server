from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)
db = SQLAlchemy(app)

from twiml_server.resources.endpoint import Endpoint
from twiml_server.resources.messages import Messages

api.add_resource(Endpoint, '/twilioendpoint')
api.add_resource(Messages, '/messages/<account_sid>/<phone_number>')

