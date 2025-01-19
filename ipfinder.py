from flask import Flask, request
import pandas as pd
import os
from datetime import datetime
import logging

app = Flask(__name__)

# Configure Logging for Heroku
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route('/')
def track_ip():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log details in Heroku logs
    logging.info(f"IP Address: {ip} | User Agent: {user_agent} | Timestamp: {timestamp}")

    return "Tracking successful! Redirecting...", 302, {"Location": "https://www.google.com/"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
