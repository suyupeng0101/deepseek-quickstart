
#!/usr/bin/env python3
"""US Weather Assistant - Flask app that queries a configurable US weather MCP-like HTTP endpoint.
Includes a small CLI for local testing and a simple front endpoint /weather for integration with CLINE/VSCode.
Configuration: copy config.example.json -> config.json and set US_WEATHER_MCP_URL

This project includes a mock MCP server (mock_us_mcp.py) you can run locally for development/testing.
"""
from flask import Flask, request, jsonify
import requests, os, json, sys

app = Flask(__name__)

cfg_path = os.path.join(os.path.dirname(__file__), 'config.json')
if os.path.exists(cfg_path):
    cfg = json.load(open(cfg_path, 'r', encoding='utf-8'))
else:
    cfg = json.load(open(os.path.join(os.path.dirname(__file__), 'config.example.json'), 'r', encoding='utf-8'))

US_WEATHER_MCP = cfg.get('US_WEATHER_MCP_URL', 'http://localhost:8090')

def query_us_mcp(city, date=None):
    """Query the configured US weather MCP Server. Expected endpoint:
       GET /weather?country=US&city=CityName&date=YYYY-MM-DD (date optional)
       The actual MCP may differ; adjust this function accordingly.
    """
    try:
        params = {'country': 'US', 'city': city}
        if date:
            params['date'] = date
        r = requests.get(f"{US_WEATHER_MCP}/weather", params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {'error': str(e)}

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    date = request.args.get('date')  # optional
    if not city:
        return jsonify({'error': 'city parameter required'}), 400
    data = query_us_mcp(city, date)
    # simple normalization for front-end
    return jsonify({'source': US_WEATHER_MCP, 'data': data})

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'mock':
        # run mock MCP for easy testing
        import mock_us_mcp
        mock_us_mcp.run_mock()
    else:
        app.run(host='0.0.0.0', port=5001)
