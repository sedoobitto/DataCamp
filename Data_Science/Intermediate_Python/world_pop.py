# Assess the correlation between the gdp per capita and the life expectancy rate

# Import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(gdp_cap , life_exp)

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale.
# A correlation will become clear when you display the GDP per capita
# on a logarithmic scale. Add the line plt.xscale('log').
plt.xscale('log')

# Show plot
plt.show()

# Display the plot with plt.show()
plt.show()
