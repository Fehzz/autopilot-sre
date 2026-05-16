from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "auth-service is alive"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/verify")
def verify():
    return {"authenticated": True, "user": "kevin"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)