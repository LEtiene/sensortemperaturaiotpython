from flask import Flask, jsonify
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_sensor_data():
    temperature = sensor.get_temperature()

    if temperature is not None:
        return jsonify({
            'Temperatura': temperature
        }), 200
    else:
        return jsonify({
            'error': 'Error ao ler os dados do sensor.'
        }), 500


@app.route('/')
def home():
    return "Servidor de monitoramento de temperatura"


if __name__ == '__main__':
    app.run(host='192.168.1.105', port=80)