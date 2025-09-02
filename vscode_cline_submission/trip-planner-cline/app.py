
#!/usr/bin/env python3
# trip-planner-cline/app.py - minimal Flask app integrating 12306 MCP and China weather MCP.
from flask import Flask, request, jsonify
import requests, os, json, sys

app = Flask(__name__)

cfg_path = os.path.join(os.path.dirname(__file__), 'config.json')
if os.path.exists(cfg_path):
    cfg = json.load(open(cfg_path, 'r', encoding='utf-8'))
else:
    cfg = json.load(open(os.path.join(os.path.dirname(__file__), 'config.example.json'), 'r', encoding='utf-8'))

MCP_12306 = cfg.get('MCP_12306_URL', 'http://localhost:8080')
MCP_CN_WEATHER = cfg.get('MCP_CHINA_WEATHER_URL', 'http://localhost:8091')

def query_12306(origin, destination, date_str):
    try:
        params = {'from': origin, 'to': destination, 'date': date_str}
        r = requests.get(f"{MCP_12306}/get-tickets", params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {'error': str(e)}

def query_cn_weather(city, date=None):
    try:
        params = {'city': city}
        if date: params['date'] = date
        r = requests.get(f"{MCP_CN_WEATHER}/weather", params=params, timeout=8)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {'error': str(e)}

@app.route('/plan', methods=['POST'])
def plan():
    body = request.get_json(force=True)
    origin = body.get('origin')
    destination = body.get('destination')
    date = body.get('date')
    prefs = body.get('preferences', '')

    if not origin or not destination or not date:
        return jsonify({'error': 'origin, destination and date are required'}), 400

    tickets = query_12306(origin, destination, date)
    # For weather, get origin and destination weather
    weather_origin = query_cn_weather(origin, date)
    weather_dest = query_cn_weather(destination, date)

    # Compose simple plan summary (no ML model required)
    summary = {
        'origin': origin,
        'destination': destination,
        'date': date,
        'preferences': prefs,
        'tickets_sample': tickets if isinstance(tickets, dict) else tickets[:6],
        'weather_origin': weather_origin,
        'weather_dest': weather_dest
    }
    return jsonify(summary)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'ok': True, 'mcp_12306': MCP_12306, 'mcp_cn_weather': MCP_CN_WEATHER})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
