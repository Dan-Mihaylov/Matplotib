from date_converter import convert_date

import yfinance as yf
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.use('Qt5Agg')
aapl = yf.Ticker('AAPL')
# Next it will give us a panda df object with an index of panda timestamp and values [Open, High, Low, Close, Volume]
# and more. You access the data from each object using the . notation.
# ex. To access all the Open times, you can use aapl_history.Open, it will give you a dict like
# object in which you can call a method .items() to get the date and the values.
aapl_history = aapl.history("2Y", '1d')


# We are going to do a simple graph to show the close times from a ticker.
fig, ax = plt.subplots(figsize=(6.8, 4.2), layout='constrained')


ax.set_title("AAPL\nStock Price")
ax.set_ylabel('Price')
ax.set_xlabel('Date')

cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
# Attach the CDF (Consise Date Formatter) to the xaxis, as a get_major_locator
# and then set it as a major formatter

ax.xaxis.set_major_formatter(cdf)


close_prices = []
# timestamps = []

for timestamp, price in aapl_history.Close.items():
    # timestamps.append(timestamp)
    # dates.append(convert_date(timestamp))
    close_prices.append(price)

close_prices = np.array(close_prices)
dates = aapl_history.index.to_pydatetime()

ax.plot(dates, close_prices, '-', label='AAPL price', lw=1)
# Now we will get all the tick labels and rotate them to fit more of them on the xaxis
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)  # rotate them to 45 degrees


ax.fill_between(dates, close_prices[0], close_prices, alpha=0.3, color='green', where=(close_prices > close_prices[0]))
ax.fill_between(dates, close_prices[0], close_prices, alpha=0.3, color='red', where=(close_prices < close_prices[0]))

ax.legend()
ax.grid(True)
plt.show()

