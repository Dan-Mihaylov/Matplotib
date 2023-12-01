import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time


mpl.use('Qt5Agg')
plt.style.use('../styles/presentation.mplstyle')    # You can use predefined styles for the figures from matplotlib
fig, ax = plt.subplots(figsize=(10.08, 6.8))
print(ax.__dict__.keys())
fig.suptitle('Fig Title')
x = np.arange(0, 13, 0.2)
y = np.sin(x)
lines = ax.plot(x, y, '-', label='Normal X')
ax.plot(x, np.cos(x), label='Cos X')
ax.legend()

# lines[0].set_data([x, np.cos(x)])

# print(plt.style.available)  # Here you can see what are the styles available to use.
plt.show()