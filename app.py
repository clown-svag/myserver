from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def log_data():
    ip = request.args.get('ip', '?')
    city = request.args.get('city', '?')
    lat = request.args.get('lat', '?')
    lon = request.args.get('lon', '?')
    
    log_msg = f"Дата: {datetime.datetime.now()} | IP: {ip} | Город: {city} | Широта: {lat} | Долгота: {lon}"
    print(log_msg, flush=True) # Это запишет лог в консоль сервера
    
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
