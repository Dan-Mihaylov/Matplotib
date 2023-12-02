import yfinance as yf
import pandas as pd
import time
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt


def get_ticker_history(ticker: str, period: str, interval: str) -> yf.Ticker.history:
    curr = yf.Ticker(ticker)
    return curr.history(period, interval)


mpl.use('Qt5Agg')
fig, ax1 = plt.subplots(figsize=(9.80, 6.80), layout='constrained')


MSFT = 'MSFT'
msft = get_ticker_history(MSFT, '5d', '15m')
timestamps = msft.index
datetimes = timestamps.to_pydatetime()

cdf = mpl.dates.ConciseDateFormatter(ax1.xaxis.get_major_locator())
ax1.xaxis.set_major_formatter(cdf)

ax1.set_title(MSFT)
ax1.set_ylabel('Price')
ax1.set_xlabel('Date Time')

# get the price data
prices = [price for price in msft.Close]

ax1.plot(datetimes, prices, '-', label='MSFT')
ax1.legend()
ax1.grid(True, which='both', dashes=(2.5, 2.5), fillstyle='bottom')
plt.show()
