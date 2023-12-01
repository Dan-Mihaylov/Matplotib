import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
# np.random.seed(19680801)
#
# fig, axs = plt.subplots(2, 2)
# cmaps = ['RdBu_r', 'viridis']
# for col in range(2):
#     for row in range(2):
#         ax = axs[row, col]
#         pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
#                             cmap=cmaps[col])
#         fig.colorbar(pcm, ax=ax)
#
#


# Two columns have the same color so might be better to add one color bar per two columns
fig, axs = plt.subplots(2, 2)
cmaps = ['RdBu_r', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
                            cmap=cmaps[col])
    fig.colorbar(pcm, ax=axs[:, col], shrink=0.6)

plt.show()



# To get the full list of properties you can use the mpl.getp('Artist you want to see the props for')

