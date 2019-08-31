from flask import Flask, jsonify, request
from exchange_rate import Exchange_Rate
app = Flask(__name__)

@app.route('/rate', methods = ['POST'])
def get_exchange_rate():
    conversion = request.get_json()
    original_currency = conversion['FROM']
    converted_currency = conversion['TO']
    er_obj = Exchange_Rate(original_currency, converted_currency)
    rate = er_obj.get_exchange_rate()
    return jsonify({'from': original_currency, 'to': converted_currency,'rate': rate})

app.run()
