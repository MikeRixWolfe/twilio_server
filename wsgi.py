from twiml_server import app as application
from twiml_server.common.util import make_json_app

if __name__ == '__main__':
    make_json_app()

    application.run(host=application.config['HOST'],
        port=application.config['PORT'],
        debug=application.config['DEBUG'])

