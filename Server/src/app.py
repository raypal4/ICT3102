from flask import Flask, render_template
from routes import (
    TempRoute,
)

# # Configuration
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static",
    template_folder= "templates",
)

@app.route("/")
def index():
    return "Hello, World!"
    # return render_template("index.html")


app.register_blueprint(TempRoute.router)

# Start server
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)