import json
from flask import Response
from flask_restful import Resource
from twiml_server.persist.models import Message


class Gallery(Resource):
    def get(self, account_sid, phone_number):
        messages = [dict({"MediaUrl": m.MediaUrl, "DateReceived": str(m.DateReceived)}) for m in
            Message.query.filter(Message.AccountSid==account_sid).filter(Message.To=='+12693593295').filter(Message.From==phone_number).filter(Message.MediaUrl!=None).all()]
        return Response(json.dumps(messages),
                        status=200,
                        mimetype='application/json')

