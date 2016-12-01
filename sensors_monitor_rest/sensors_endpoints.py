from flask import Flask, jsonify
from ..sensors_monitor_core import DHT11, HCSR501, LightSensor

app = Flask(__name__)

VERSION=1.0
BASE_PATH="/sensors-monitor/api/v{0}/sensors".format(VERSION)

@app.route(BASE_PATH)
def hello():
    return jsonify({'sensors':'all sensors'})

@app.route(BASE_PATH+"/dht11")
def dht11():
    sensor = DHT11(4)
    sensor.read_and_get()
    return jsonify({'dht11':sensor})

@app.route(BASE_PATH+"/hcsr501")
def hcsr501():
    sensor = HCSR501(17)
    sensor.detect_and_get()
    return jsonify({'hcsr501':sensor})

@app.route(BASE_PATH+"/lightsensor")
def lightsensor():
    sensor = LightSensor(27)
    sensor.detect_and_get()
    return jsonify({'lightsensor':sensor})

if __name__ == "__main__":
    app.run()
