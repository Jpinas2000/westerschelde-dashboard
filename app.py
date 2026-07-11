from flask import Flask, render_template

import config

from modules.weather import get_weather
from modules.water import get_water

app = Flask(__name__)


@app.route("/")
def dashboard():

    return render_template(

        "dashboard.html",

        title=config.TITLE,

        weather=get_weather(),

        water=get_water()

    )


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
