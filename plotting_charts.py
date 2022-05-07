import matplotlib.pyplot as plt

x_data = [1, 3, 4, 5, 6, 9]
y_data = [0.5, 1.3, 2.7, 6.8, 12.9, 20]

y_data2 = [1, 3, 6, 10, 15, 21]

plt.plot(x_data, y_data, linewidth=5)  # line chart

plt.scatter(x_data, y_data2, c=y_data2, cmap=plt.cm.Blues, s=200)  # plot using dots

plt.title("Height of Plant Per Day", fontsize=24)
plt.xlabel("Days", fontsize=15)
plt.ylabel("Centimeters", fontsize=15)

plt.show()   # display the plot