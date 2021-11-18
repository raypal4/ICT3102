from flask import Flask, render_template
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
# Configuration
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static",
    template_folder="templates",
)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error")
def index():
    return "Flask Servers Down"

if __name__ == "__main__":
    # NGINX ver TODO remove port 80
    serve(app, host='0.0.0.0', port=4000)
