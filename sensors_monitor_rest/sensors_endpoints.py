from flask import Flask, jsonify, Response, stream_with_context, request
from flask.json import JSONEncoder
from ..sensors_monitor_core import DHT11, ConditionSensor

VERSION=1.0
BASE_PATH="/sensors-monitor/api/v{0}/sensors".format(VERSION)

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DHT11):
            return {
                'name': 'dht11',
                'pin_number': obj.pin_num,
                'temperature': obj.temp,
                'humidity': obj.humidity
            }
        elif isinstance(obj, ConditionSensor):
            return {
                'name': obj.name,
                'pin_number': obj.pin_num,
                'state': obj.state,
            }
        return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

@app.route(BASE_PATH)
def sensors():
    dht11 = DHT11(4)
    dht11.read_and_get()
    hcsr501 = ConditionSensor(17, 'hcsr501')
    hcsr501.detect_and_get()
    light = ConditionSensor(27, 'light sensor')
    light.detect_and_get()
    return jsonify({'sensors':[dht11, hcsr501, light]})

@app.route(BASE_PATH+"/dht11")
def dht11():
    sensor = DHT11(4)
    sensor.read_and_get()
    return jsonify({'sensor':sensor})

@app.route(BASE_PATH+"/hcsr501")
def hcsr501():
    sensor = ConditionSensor(17, 'hcsr501')
    sensor.detect_and_get()
    return jsonify({'sensor':sensor})

@app.route(BASE_PATH+"/lightsensor")
def lightsensor():
    sensor = ConditionSensor(27, 'light sensor')
    sensor.detect_and_get()
    return jsonify({'sensor':sensor})

if __name__ == "__main__":
    app.run()
