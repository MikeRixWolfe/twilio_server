from datetime import datetime
from app import db


class SerializableModel(object):
    def to_dict(self):
        value = {}
        for column in self.__table__.columns:
            attribute = getattr(self, column.name)
            if isinstance(attribute, datetime):
                attribute = str(attribute)
            value[column.name] = attribute
        return value


class Message(db.Model, SerializableModel):
    __tablename__ = 'Message'

    MessageSid = db.Column(db.String, primary_key=True)
    AccountSid = db.Column(db.String)
    ApiVersion = db.Column(db.String)
    Body = db.Column(db.String)
    From = db.Column(db.String)
    To = db.Column(db.String)
    MediaUrl = db.Column(db.String, nullable=True)
    DateReceived = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, MessageSid, AccountSid, ApiVersion,
                 Body, From, To, MediaUrl):
        self.MessageSid = MessageSid
        self.AccountSid = AccountSid
        self.ApiVersion = ApiVersion
        self.Body = Body
        self.From = From
        self.To = To
        self.MediaUrl = MediaUrl

