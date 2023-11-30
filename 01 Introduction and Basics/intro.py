import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# You always initialize a figure with an axes to populate your results, ('x', 'y' in our beginners case)
fig, ax_one = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [150, 140, 200, 219, 230]
z = [155, 145, 205, 224, 235]

# set a title to the figure
ax_one.set_title("First Plot")

# determine the distance of the minor points in the y axis
# ax_one.yaxis.set_minor_locator()
# ax_one.yaxis.set_major_formatter()
# ax_one.scatter(x, y, z)

# Add a label to each axis
ax_one.set_ylabel("Meters")

# The border around the figure
# ax_one.spines()

# add the data to the plot
ax_one.plot(x, y, z)

# # display the plot data
# plt.show()

# save the plot data to a png, or pdf file
# plt.savefig("result.png")


"""
This is the OO-style of initializing figures and plots.
"""

# Create a list with incrementing values
linear_x = np.linspace(0, 10, 100)

# Create the figure and the axes
new_fig, ax_two = plt.subplots(figsize=(5, 3), layout='constrained')
# Add data to the first plot / label='some_name' --> give name inside the legend
ax_two.plot(linear_x, linear_x, label='Linear')
# Add data to the second plot
ax_two.plot(linear_x, linear_x**2, label='Squared')
# Add data to the third plot
ax_two.plot(linear_x, linear_x**3, label='Cubed')
# Set x/y labels, for outside the plot
ax_two.set_xlabel('x label')
ax_two.set_ylabel('y label')
# Set title for the plot
ax_two.set_title('Simple Plot')
# Display the legend
ax_two.legend()
# Display the plot
# plt.show()


"""
This is the pyplot-style of initializing figures and plots
"""

plt.figure(figsize=(10, 7), layout='constrained')
plt.plot(linear_x, linear_x, label='Linear', color='red')
plt.plot(linear_x, linear_x ** 2, label='Squared', color='cyan')
plt.plot(linear_x, linear_x ** 3, label='Cubed', color='orange')
plt.xlabel('Label X')
plt.ylabel('Label Y')
plt.title('Simple Plot \npyplot-style')
plt.legend()
plt.show()








