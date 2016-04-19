#!/usr/bin/env python

import logging
from twiml_server import app
from twiml_server.common.util import make_json_app

if __name__ == '__main__':
    if app.config['LOGGING']:
        logging.basicConfig(filename='app/persist/app.log', level=logging.INFO)

    make_json_app()

    app.run(host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'])

