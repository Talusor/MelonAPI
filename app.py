from flask import Flask
from charts import charts_api

app = Flask(__name__)

app.register_blueprint(charts_api, url_prefix="/charts")


@app.route("/")
def index():
    return "Nothing here."


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)