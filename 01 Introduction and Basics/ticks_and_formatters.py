import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Ticks and Formatters
# You can choose to add the ticks and the spacing between them manually


data1 = np.random.randint(20, 50, 100)
data2 = np.random.randint(30, 50, 100)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10.08, 6.80))

ax1.set_title("Automatic Ticks", fontsize=20)
ax1.plot(np.arange(100), data1)

ax2.set_title("Manual Ticks", fontsize=20)
ax2.plot(np.arange(100), data1)
# Use the set_xticks() specify the ticks ratio, and add labels for each tick.
ax2.set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'], fontsize=14)

plt.show()
