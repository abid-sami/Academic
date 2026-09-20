import matplotlib.pyplot as plt

# shoes = ["Nike", "Adidas", "Reebok", "Asics", "Other"]

# runners = [92, 49, 37, 13, 9]

# plt.pie(
#     runners,
#     labels=shoes,
#     autopct="%1.1f%%"
# )

# plt.title("Favorite Running Shoes of 200 Runners")

# plt.show()


# 



import matplotlib.pyplot as plt

midpoints = [5, 15, 25, 35, 45, 55]

frequency = [5, 8, 12, 10, 7, 3]

data = []

for i in range(len(midpoints)):
    data.extend([midpoints[i]] * frequency[i])

plt.hist(
    data,
    bins=[0, 10, 20, 30, 40, 50, 60]
)

plt.title("Histogram of Frequency Distribution")
plt.xlabel("Class")
plt.ylabel("Frequency")

plt.show()