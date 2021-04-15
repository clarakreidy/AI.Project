import requests
import io
import pandas as pd
import numpy as np


api = 'https://api.tiingo.com/tiingo/daily/adausd/prices?startDate=2015-1-1&endDate=2021-5-1&format=csv'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token e8f19de4f1014da0c82def9df3edf347cc139584'
}

request = requests.get(api, headers=headers).content
eth = pd.read_csv(io.StringIO(request.decode('utf-8')))

# Bollinger Bands
eth['movingAverage'] = eth.adjClose.rolling(20).mean()
eth['standardDeviation'] = eth.adjClose.rolling(20).std()
eth['BollingerBandsUpper'] = eth['movingAverage'] + (eth['standardDeviation'] * 2)
eth['BollingerBandsLower'] = eth['movingAverage'] - (eth['standardDeviation'] * 2)


# RSI
N = 14


def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]


eth['change'] = eth['adjClose'].diff(1)
eth['gain'] = eth.change.mask(eth.change < 0, 0.0)
eth['loss'] = -eth.change.mask(eth.change > 0, -0.0)
eth['AvgU'] = rma(eth.gain[N+1:].to_numpy(), N, np.nansum(eth.gain.to_numpy()[:N+1])/N)
eth['AvgD'] = rma(eth.loss[N+1:].to_numpy(), N, np.nansum(eth.loss.to_numpy()[:N+1])/N)
eth['rs'] = abs(eth['AvgU']/eth['AvgD'])
eth['rsi'] = 100 - 100 / (1 + eth['rs'])

eth.to_csv('ethereum.csv', index=False)