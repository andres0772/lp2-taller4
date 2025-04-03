from reactpy import component, html
from reactpy.backend.flask import configure
from flask import Flask

@component
def app():
    return html.h1("Hello, world!")

flask_app = Flask(__name__)
configure(flask_app, app)

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True)