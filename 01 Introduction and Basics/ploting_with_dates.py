import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Plotting dates
fig, ax = plt.subplots(figsize=(6.8, 3.2), layout='constrained')
dates = np.arange(np.datetime64('2023-10-01'), np.datetime64('2023-12-25'), np.timedelta64(1, 'D'))
data = np.cumsum(np.random.randn(len(dates)))


# no.datetime64('2023-11-15') gives us the starting point in the arrange function, the timedelta gives us the STEP with
# which we can increase the dates. Use 'h' for hour 'D' for day and so on and so forth

cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
# Attach the CDF (Consise Date Formatter) to the xaxis, as a get_major_locator
# and then set it as a major formatter

ax.xaxis.set_major_formatter(cdf)
ax.plot(dates, data)


# For strings we get categorical plotting
fig2, ax2 = plt.subplots(figsize=(6.8, 3.2), layout='constrained')
categories = ['swimming', 'running', 'walking', 'sleeping']
ax2.bar(categories, np.random.rand(len(categories)), color='red')
plt.show()






