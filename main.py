from reactpy import component, html
from reactpy.backend.Flask import configure
from Flask import Flask

@component
def app():
    return html.hl("hello, world!")


app = Flask(__name__)
 configure(app, App)
 app.run(host='0.0.0.0', debug=True)
