import requests


api = 'https://api.tiingo.com/tiingo/daily/btcusd/prices?startDate=2006-1-1&endDate=2021-4-12&format=csv'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token e8f19de4f1014da0c82def9df3edf347cc139584'
}

request = requests.get(api, headers=headers)
csv_file = open('eth.csv', 'wb')
csv_file.write(request.content)
csv_file.close()