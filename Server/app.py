from flask import Flask, render_template
from routes import (
    BeaconRoutes,
)

app = Flask(__name__)
# Configuration
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static",
    template_folder= "templates",
)

@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(BeaconRoutes.router)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80)