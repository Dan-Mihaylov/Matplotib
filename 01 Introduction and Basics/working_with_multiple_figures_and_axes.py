import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# You can use subplot_mosaic to add a more complex layout to your figures axes.

# In this example we add, an up left plot, a down left plot and a right plot to take up and down spaces.
fig, axd = plt.subplot_mosaic(
    [
        ['upleft', 'right'],
        ['downleft', 'right']
    ],
    layout='constrained'
)
axd['upleft'].set_title('Up Left')
axd['downleft'].set_title('Down Left')
axd['right'].set_title('Right Side')

plt.show()





