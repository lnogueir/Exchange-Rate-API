import requests

url = 'http://127.0.0.1:5000/rate'
conversion_info = {"FROM": "USD", "TO": "EUR"}
try:
    r = requests.post(url, json = conversion_info)
    rate = r.json()[u'rate']
    print(rate)
except:
    print('ERROR - Make sure you have the server running and all libraries installed.')

