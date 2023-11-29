import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Create 4 random sets of data
data1, data2, data3, data4 = np.random.randn(4, 100)

# Create the figure and the axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.28, 6.80))
ax1.plot(data1, data2, marker='x', color='darkred')
ax2.plot(data3, data4, marker='o')

# plt.show()


# Styling Artist
fig, ax = plt.subplots(1, 1, figsize=(10.28, 6.80))
x = np.arange(len(data1))       # This method will give us an array starting from 0 to the end of len(data1) - 1
ax.plot(x, np.cumsum(data1), color='blue', linewidth=1, linestyle='dashdot', label='Data-1')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2, label='Data-2')
# Can set the style either in the plt function itself or by calling the methods to the instance
l.set_linestyle('--')
ax.legend()


# Colors
fig, nax = plt.subplots(1, 1, figsize=(10.80, 6.80))
nax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
nax.set_ylabel("Y Label Name")
# nax.set_xlabel("X Label Name")
nax.set_title('Some Scatter Figure', fontsize=20)
nax.text(-2, 1.5, r'$\mu=15, \ \sigma=115$')    # This adds text to the specified position in grid
# nax.axis([55, 175, 0, 0.03]) # This sets the exact axis points you want to display
nax.grid(True)  # This displays a grid in the figure
# All those functions return matplotlib.text.text file where you can customize the text properties using kwargs
t = nax.set_xlabel('X Label Name', fontsize=16, color='blue')
plt.show()




