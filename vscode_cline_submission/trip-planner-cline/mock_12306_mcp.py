
#!/usr/bin/env python3
"""mock_12306_mcp.py - mock server returning sample train options.
Run: python mock_12306_mcp.py
"""
from flask import Flask, request, jsonify
app = Flask('mock_12306')

@app.route('/get-tickets', methods=['GET'])
def get_tickets():
    frm = request.args.get('from', 'Beijing')
    to = request.args.get('to', 'Shanghai')
    date = request.args.get('date', '2025-09-10')
    sample = [
        {'train_no': 'G101', 'depart_time': '07:00', 'arrive_time': '11:20', 'duration': '4h20m', 'price': '¥550'},
        {'train_no': 'G303', 'depart_time': '08:30', 'arrive_time': '12:50', 'duration': '4h20m', 'price': '¥520'},
        {'train_no': 'D201', 'depart_time': '09:15', 'arrive_time': '14:00', 'duration': '4h45m', 'price': '¥480'}
    ]
    return jsonify({'data': sample, 'from': frm, 'to': to, 'date': date})

def run_mock():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    run_mock()
