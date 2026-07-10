from flask import Flask, render_template
from modules.weather import get_weather
from modules.water import get_water
import config

app = Flask(__name__)


@app.route("/")
def dashboard():

    weather = get_weather()
    water = get_water()

    return render_template(
        "index.html",
        title=config.TITLE,
        weather=weather,
        water=water
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
