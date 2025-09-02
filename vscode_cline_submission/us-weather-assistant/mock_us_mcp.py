
#!/usr/bin/env python3
"""mock_us_mcp.py - a tiny mock MCP-style HTTP server that returns sample US weather data.
Run: python mock_us_mcp.py
"""
from flask import Flask, request, jsonify
app = Flask('mock_us_mcp')

@app.route('/weather', methods=['GET'])
def weather():
    country = request.args.get('country')
    city = request.args.get('city', 'Unknown')
    date = request.args.get('date', '2025-09-10')
    sample = {
        'city': city,
        'country': country or 'US',
        'date': date,
        'forecast': [
            {'time': '08:00', 'temp_c': 18, 'cond': 'Sunny'},
            {'time': '14:00', 'temp_c': 25, 'cond': 'Partly Cloudy'},
            {'time': '20:00', 'temp_c': 20, 'cond': 'Clear'}
        ],
        'notes': 'Mock data for development'
    }
    return jsonify(sample)

def run_mock():
    app.run(host='0.0.0.0', port=8090)

if __name__ == '__main__':
    run_mock()
