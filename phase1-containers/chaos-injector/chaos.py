import requests
import time
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SERVICES = [
    "http://api-gateway:5000",
    "http://auth-service:5001",
    "http://data-service:5002",
]

ENDPOINTS = {
    "http://api-gateway:5000": ["/", "/health"],
    "http://auth-service:5001": ["/", "/health", "/verify"],
    "http://data-service:5002": ["/", "/health", "/records"],
}

def normal_traffic():
    service = random.choice(SERVICES)
    endpoint = random.choice(ENDPOINTS[service])
    url = f"{service}{endpoint}"
    try:
        response = requests.get(url, timeout=2)
        logging.info(f"NORMAL {url} -> {response.status_code}")
    except Exception as e:
        logging.error(f"FAILED {url} -> {e}")

def spike_traffic():
    service = random.choice(SERVICES)
    logging.warning(f"CHAOS: spiking traffic on {service}")
    for _ in range(50):
        endpoint = random.choice(ENDPOINTS[service])
        url = f"{service}{endpoint}"
        try:
            requests.get(url, timeout=2)
        except Exception:
            pass
    logging.warning(f"CHAOS: spike complete on {service}")

def run():
    logging.info("Chaos injector started")
    while True:
        action = random.choices(
            ['normal', 'spike'],
            weights=[80, 20]
        )[0]

        if action == 'normal':
            normal_traffic()
            time.sleep(random.uniform(0.5, 2.0))
        elif action == 'spike':
            spike_traffic()
            time.sleep(random.uniform(5, 15))

if __name__ == "__main__":
    run()