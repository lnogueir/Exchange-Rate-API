from datetime import datetime as dt
import time
import requests
from emailer import Emailer

'''
The program below sends an email everyday  at 10am
With the currency rate between US Dollars and Euros
'''

e = Emailer()
while True:
    your_hour = dt.now().hour
    if your_hour == 10:
        url = 'http://127.0.0.1:5000/rate'
        conversion_info = {"FROM": "USD", "TO": "EUR"}
        try:
            r = requests.post(url, json = conversion_info)
            rate = r.json()[u'rate']
            e.connect()
            e.make_email(rate)
            e.send_email()
            e.disconnect()
        except:
            print('ERROR')
    time.sleep(3600)
