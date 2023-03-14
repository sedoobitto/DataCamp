# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label = "Deshaun")

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked, label = "Aditya")

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label = "Mengfei")

# Add a title
plt.title("Hours worked per day, by officer, on the Missing Puppy Report for Bayes")

# Add y-axis label
plt.ylabel("Hours worked per Day")

# Add a command to make the legend display
plt.legend()

# Display all three line plots
plt.show()
