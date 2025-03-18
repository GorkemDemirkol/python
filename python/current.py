import freecurrencyapi  
from requests import get  
from pprint import pprint  # pprint fonksiyonunu kullanıyoruz  
API_KEY = "fca_live_1FcUqdQ5shT7vUYHJHJt3EAgcXcRTp0EEnFw4GQR"  # Geçerli API anahtarınızı buraya yerleştirin  
BASE_URL = 'https://api.freecurrencyapi.com/v1/'  

def get_currency():  
    endpoint = f'currencies?apikey={API_KEY}'  
    url = BASE_URL + endpoint  
    data = get(url).json()  
    pprint(data)  # Burada pprint fonksiyonunu kullandık 

    data = list(data['data'].values())
    data.sort(key=lambda x: x['code'])
    return data

def print_currency(currencies):
    for currency in currencies:
        name = currency.get('name', 'N/A')
        _id = currency.get('code', 'N/A')
        symbol = currency.get('symbol', 'N/A')
        print(f"{name} ({_id}) {symbol}")

def exchange_rate(curry1="USD", curry2="TRY,EUR,GBP"):
    endpoint = f'latest?apikey={API_KEY}&base_currencies={curry1}&currencies={curry2}'
    url = BASE_URL + endpoint
    response = get(url)

    if response.status_code == 200:
        data = response.json().get('data', {})
        rates = {currency: data.get(currency, 'N/A') for currency in curry2.split(',')}
        return rates
    else:
        return None
   
  

data = get_currency()
print_currency(data)

rates = exchange_rate('USD', 'TRY,EUR,GBP')
if rates:
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")
        

