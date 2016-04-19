import json
from flask import Response
from flask_restful import Resource
from twiml_server.persist.models import Message


class Messages(Resource):
    def get(self, account_sid, phone_number):
        messages = [m.to_dict() for m in
            Message.query.filter_by(AccountSid=account_sid).filter_by(To=phone_number)]
        return Response(json.dumps(messages),
                        status=200,
                        mimetype='application/json')

