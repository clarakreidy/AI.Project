import requests
import io
import pandas as pd
import numpy as np
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)

api = 'https://api.tiingo.com/tiingo/daily/btcusd/prices?startDate=2005-1-1&endDate=' + yesterday.strftime('%Y-%m-%d') + '&format=csv'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token e8f19de4f1014da0c82def9df3edf347cc139584'
}

request = requests.get(api, headers=headers).content
btc = pd.read_csv(io.StringIO(request.decode('utf-8')))

# Bollinger Bands
btc['movingAverage'] = btc.adjClose.rolling(20).mean()
btc['standardDeviation'] = btc.adjClose.rolling(20).std()
btc['BollingerBandsUpper'] = btc['movingAverage'] + (btc['standardDeviation'] * 2)
btc['BollingerBandsLower'] = btc['movingAverage'] - (btc['standardDeviation'] * 2)


# RSI
N = 14


def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]


btc['change'] = btc['adjClose'].diff(1)
btc['gain'] = btc.change.mask(btc.change < 0, 0.0)
btc['loss'] = -btc.change.mask(btc.change > 0, -0.0)
btc['AvgU'] = rma(btc.gain[N+1:].to_numpy(), N, np.nansum(btc.gain.to_numpy()[:N+1])/N)
btc['AvgD'] = rma(btc.loss[N+1:].to_numpy(), N, np.nansum(btc.loss.to_numpy()[:N+1])/N)
btc['rs'] = abs(btc['AvgU']/btc['AvgD'])
btc['rsi'] = 100 - 100 / (1 + btc['rs'])

btc.to_csv('bitcoin.csv', index=False)
