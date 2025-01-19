from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def track_ip():
    ip = request.remote_addr  
    user_agent = request.headers.get('User-Agent') 

    with open("log.txt", "a") as f:
        f.write(f"IP: {ip} | Device: {user_agent}\n")

    return "Tracking successful! Redirecting...", 302, {"Location": "https://www.google.com"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)