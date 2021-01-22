from flask import Flask
from APIs.charts import charts_api
from APIs.song import song_api
from APIs.album import album_api

app = Flask(__name__)

app.register_blueprint(charts_api, url_prefix="/charts")
app.register_blueprint(song_api, url_prefix="/song")
app.register_blueprint(album_api, url_prefix="/album")


@app.route("/")
def index():
    return "Nothing here."


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)