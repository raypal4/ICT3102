from flask import Flask, render_template
from routes import (
    BeaconRoutes,
)
from domain.BeaconControl import BeaconControl

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
    data = BeaconControl().retrieve_all_staff()
    return render_template("index.html" , data=data)


app.register_blueprint(BeaconRoutes.router)

if __name__ == "__main__":
    # NGINX ver TODO remove port 80
    app.run(host='0.0.0.0', port=5000)