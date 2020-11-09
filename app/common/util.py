import requests
import types
from boto3.session import Session
from flask import jsonify
from io import BytesIO
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
from app import app


def make_json_app():
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    for code in default_exceptions:
        app.register_error_handler(code, make_json_error)


def s3_upload(media_url):
    print(media_url)
    _session = Session()
    client = _session.client('s3', region_name=app.config['S3_REGION_NAME'], endpoint_url=app.config['SE_ENDPOINT_URL'],
        aws_access_key_id=app.config['S3_ACCESS_ID'], aws_secret_access_key=app.config['S3_SECRET_KEY'])

    r = requests.get(media_url)
    client.upload_fileobj(BytesIO(r.content), app.config['S3_BUCKET_NAME'], media_url.split('/')[-1],
        ExtraArgs={'ACL': 'public-read', 'ContentType': r.headers['Content-Type']})

