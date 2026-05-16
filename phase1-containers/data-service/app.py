from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "data-service is alive"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/records")
def records():
    return {
        "records": [
            {"id": 1, "value": "record-alpha"},
            {"id": 2, "value": "record-beta"},
            {"id": 3, "value": "record-gamma"}
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)