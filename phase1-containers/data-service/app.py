from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'data_service_requests_total',
    'Total number of requests to data-service',
    ['endpoint']
)

@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint='/').inc()
    return "data-service is alive"

@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint='/health').inc()
    return {"status": "ok"}

@app.route("/records")
def records():
    REQUEST_COUNT.labels(endpoint='/records').inc()
    return {
        "records": [
            {"id": 1, "value": "record-alpha"},
            {"id": 2, "value": "record-beta"},
            {"id": 3, "value": "record-gamma"}
        ]
    }

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)