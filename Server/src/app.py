from flask import Flask, request, render_template
from routes import (
    TempRoute,
)
import os

# Configuration
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static",
    template_folder= "templates",
)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


app.register_blueprint(TempRoute.router)

# Start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT',5000)), debug=True)
