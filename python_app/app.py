from flask import Flask, render_template, Blueprint
from datetime import datetime
import pytz

bp = Blueprint('Time', __name__)

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


@app.route('/')
def example():
    moscow_zone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_zone)
    time_h = moscow_time.strftime("%H")
    time_m = moscow_time.strftime("%M")
    time_s = moscow_time.strftime("%S")
    return render_template('index.html', hour=str(time_h), minute=str(time_m), second=str(time_s))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
