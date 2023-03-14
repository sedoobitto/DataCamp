# Specify s for size,c for color and alpha for transparency inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

# Add text to these coordinates
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call. This adds gridlines to the plot
plt.grid(True)


# Show the plot
plt.show()

