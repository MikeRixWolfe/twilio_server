import json
from flask import request, Response
from flask_restful import Resource
from app.persist.models import Message


class Messages(Resource):
    def get(self, account_sid, phone_number):
        messages = [m.to_dict() for m in Message.query \
            .filter_by(AccountSid=account_sid) \
            .filter_by(To=phone_number) \
            .order_by(Message.DateReceived.desc()) \
            .limit(request.args.get('limit', 25))]

        return Response(json.dumps(messages),
                        status=200,
                        mimetype='application/json')

