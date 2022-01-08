import flask
from flask import jsonify

app = flask.Flask(__name__)


# test data
tpe = {
    "id": 0,
    "name":"黃小明",
    "age":"21歲",
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "name":"陳凱高",
    "age":"25歲",
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "name":"李和珅",
    "age":"35歲",
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
cities = [tpe, nyc, ldn]


@app.route('/', methods=['GET'])
def home():
    return jsonify(cities)# "<h1>Hello Flask!</h1>"


@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()
