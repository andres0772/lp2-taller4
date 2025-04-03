from reactpy import componeent, html
from reactpy.backend.flask import configure
from flask import flask

@component
def app():
    return html.hl("hello, world!")


app = Flask(__name__)
 configure(app, App)
 app.run(host='0.0.0.0', debug=True)
