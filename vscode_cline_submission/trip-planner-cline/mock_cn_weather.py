
#!/usr/bin/env python3
"""mock_cn_weather.py - a tiny mock MCP-style HTTP server that returns sample China weather data.
Run: python mock_cn_weather.py
"""
from flask import Flask, request, jsonify
app = Flask('mock_cn_weather')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', '未知')
    date = request.args.get('date', '2025-09-10')
    sample = {
        'city': city,
        'date': date,
        'forecast': [
            {'time': '08:00', 'temp_c': 22, 'cond': '小雨'},
            {'time': '14:00', 'temp_c': 28, 'cond': '多云'},
            {'time': '20:00', 'temp_c': 24, 'cond': '晴'}
        ],
        'notes': '中国天气 MCP Mock 数据'
    }
    return jsonify(sample)

def run_mock():
    app.run(host='0.0.0.0', port=8091)

if __name__ == '__main__':
    run_mock()
