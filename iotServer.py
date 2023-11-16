from flask import Flask, request, jsonify

"""The minimal application will be used to host a server
for the incomming HTTP requests by the IoT devices"""

app = Flask(__name__)


@app.post("/api/v2/lightstatus")
def light_status():
    data_light = request.get_json()
    print(data_light)
    response = {
        "status": "ok",
        "received_data": data_light
    }
    return jsonify(response)


@app.post("/api/v2/smartwatch")
def smart_watch_data():
    data_smartwatch = request.get_json()
    response = {
        "status": "ok",
        "received_data": data_smartwatch
    }
    return jsonify(response)


app.run("0.0.0.0", 5000)
