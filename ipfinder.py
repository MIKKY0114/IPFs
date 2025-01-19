from flask import Flask, request
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "log.xlsx"

@app.route('/')
def track_ip():
    ip = request.remote_addr
    user_agent= request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[ip, user_agent, timestamp]], columns= ["IP Address", "User Agent", "Login time"])


    if os.path.exists(LOG_FILE):
        existing_data = pd.read_excel(LOG_FILE)
        update_data = pd.concat([existing_data, new_data], ignore_index=True)
        update_data.to_excel(LOG_FILE, index=False)
    else:
        new_data.to_excel(LOG_FILE, index=False)

    return "Tracking successful! Redirecting...", 302, {"Location":"https://www.google.com/"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))