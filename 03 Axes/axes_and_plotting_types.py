import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


"""
Plotting types for axes.

Pairwise Data:  plot, scatter, bar, step
Array objects:  pcolormesh, contour, quiver, steamplot, ishow
Statistical distributions:  hist, errorbar, hist2d, pie, boxplot, violinplot
Irregularly gridded data:  tricontour, tripcolor
"""

# Pie creation
# x = [3, 2, 10, 4, 5]
# colors_range = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
# fig, ax = plt.subplots(figsize=(6.8, 4.2), facecolor='#e6e6ff')
# ax.pie(x, colors=colors_range, labels=['study', 'play', 'work', 'sleep', 'eat'], radius=1.4, startangle=90,)


# Axes labelling and annotation

# to set the minorticks appearance you can use ax.minorticks_on() and off() functions
# to manualy set on which ticks to be zoomed in you can use ax.set_xticks(), ax.set_yticks()

# can style the locations of the ticks and the colors of the ticks and the labels as well with
# ax.tick_params(top=True, labeltop=True, color='red', labelcolor='green')
# This sets the ticks to be visible at the top of the chart, the color is for the ticks
# the label color is for the text on each tick

fig, ax = plt.subplots(figsize=(6.8, 4.2), layout='constrained')
np.random.seed(19680803)
t = np.arange(200)
x = np.cumsum(np.random.randn(200))
y = np.cumsum(np.random.randn(200))
linesx = ax.plot(t, x, label='Random walk x')
linesy = ax.plot(t, y, label='Random walk y')

ax.set_xlabel('Time [s]')
ax.set_ylabel('Distance [km]')
ax.set_title('Random walk example')
ax.minorticks_on()
ax.tick_params(top=True, labeltop=True, color='blue', labelcolor='green', axis='x')
ax.legend()
plt.show()


