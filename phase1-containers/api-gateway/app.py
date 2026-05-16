from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'api_gateway_requests_total',
    'Total number of requests to api-gateway',
    ['endpoint']
)

@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint='/').inc()
    return "api-gateway is alive"

@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint='/health').inc()
    return {"status": "ok"}

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)