import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.use('Qt5Agg')
# mpl.use('WebAgg')
# This function will tell the backend which backend to use to display the figure,
# in our case we are going to use an external library Qt5 to generate a new window to display the result.

fig, ax = plt.subplots(facecolor='lightblue', figsize=(6.80, 4.20))


# Sometimes we want to have a nested layout in a Figure, with two or more sets of axes. In this case we use the subplots
# Layout options provided by matplotlib are ['constrained', 'compressed', 'tight'] to prevent overlap of tickables
fig = plt.figure(layout='constrained', facecolor='lightblue')
fig.suptitle("Figure")      # That is a suptitle for the whole Figure
fig_left, fig_right = fig.subfigures(1, 2)
fig_left.set_facecolor('purple')
ax_left = fig_left.subplots(2, 1, sharex=True)      # Both axes will have the same x values
ax_left[1].set_xlabel('x[m]')
fig_left.suptitle("Left SubFigure")
fig_right.set_facecolor('paleturquoise')
ax_right = fig_right.subplots(1, 2, sharey=True)
ax_right[0].set_title('Axes 1')
fig_right.suptitle('Right SubFigure')

data1 = np.linspace(1, 100, 100)

ax_left[0].plot(np.arange(len(data1)), data1, label='Linear Data')
ax_left[0].legend()
ax_left[1].plot(np.arange(len(data1)), np.cumsum(data1), label='CumSum')
ax_left[1].legend()
plt.show()



