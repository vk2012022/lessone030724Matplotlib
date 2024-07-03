import matplotlib.pyplot as plt

data = [5, 6, 7, 4, 6, 5, 7, 8, 5, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]

plt.hist(data, bins=3)

plt.xlabel("часы сна")
plt.ylabel("количество людей")
plt.title("гистограма по часам сна")

plt.show()