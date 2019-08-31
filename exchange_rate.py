from bs4 import BeautifulSoup
import requests

class Exchange_Rate:
    def __init__(self, FROM, TO, amount = 1): 
        self.conversion = FROM + TO
        self.amount = amount
    
    def get_exchange_rate(self):
        try:
            r = requests.get('https://br.financas.yahoo.com/quote/'+self.conversion+'=X/')
        except:
            print('ERROR LOADING PAGE')
        print('PAGE LOADED')
        soup = BeautifulSoup(r.text, 'xml')
        exchange_div = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0]
        exchange_rate = exchange_div.find('span').text
        exchange_rate = float(exchange_rate.replace(',','.'))
        return exchange_rate

    def convert_amount(self):
        return self.rate*self.amount
