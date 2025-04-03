from reactpy import componeent, html
from reactpy.backend.Flask import configure

app = Flask(__name__)
app.run(host='0.0.0.0', debug=True)
