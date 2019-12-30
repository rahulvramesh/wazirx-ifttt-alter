import requests
from requests.exceptions import HTTPError
import json

def check_price(btc_usdt):
    #print(btc_usdt)
    if float(btc_usdt["sell"]) > 7500.00 :
        print("Sell")
        btc_usdt["note"] = "Sell"
        post_ifttt(btc_usdt)
    if float(btc_usdt["buy"]) < 6000.00 :
        print("Buy")
        btc_usdt["note"] = "Buy"
        post_ifttt(btc_usdt)

def post_ifttt(btc_usdt):

    #webhook
    url = "https://maker.ifttt.com/trigger/warixz_price_alert/with/key/{key}"
    

    payload = {
        'value1': btc_usdt['buy'],
        'value2': btc_usdt['sell'],
        'value3': btc_usdt['note']
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


#basic api url
url = "https://api.wazirx.com/api/v2/tickers"


payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

if response:
    print('Success!')
    json_response = response.json()
    btc_usdt = json_response["btcusdt"]
    check_price(btc_usdt)
else:
    print('An error has occurred.')



