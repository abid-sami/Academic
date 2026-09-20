import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = [
    11, 17, 15, 22, 11, 16, 19, 24, 29, 25,
    18, 18, 25, 26, 32, 14, 17, 20, 23, 27,
    30, 12, 24, 36, 18, 15, 20, 28, 33, 38,
    34, 13, 12, 16, 20, 22, 29, 19, 23, 31
]

print(X)

X = np.array(X)

AM_X = np.mean(X)

GM_X = np.exp(np.mean(np.log(X)))

HM_X = len(X) / np.sum(1 / X)

Median_X = np.median(X)

Mode_X = pd.Series(X).mode().tolist()

print("AM =", AM_X)
print("GM =", GM_X)
print("HM =", HM_X)
print("Median =", Median_X)
print("Mode =", Mode_X)

classes = ["10-14", "15-19", "20-24",
           "25-29", "30-34", "35-39"]

frequency = [6, 11, 9, 7, 5, 2]

freq_table = pd.DataFrame({
    "Class Interval": classes,
    "Frequency": frequency
})

print(freq_table)





plt.plot(X, marker="o")
plt.title("Line Plot of X")
plt.xlabel("Observation")
plt.ylabel("Value")
plt.show()

plt.hist(X, bins=[10, 15, 20, 25, 30, 35, 40])
plt.title("Histogram of X")
plt.xlabel("Class Interval")
plt.ylabel("Frequency")
plt.show()

plt.bar(classes, frequency)
plt.title("Bar Plot of X")
plt.xlabel("Class Interval")
plt.ylabel("Frequency")
plt.show()

plt.pie(
    frequency,
    labels=classes,
    autopct="%1.1f%%"
)
plt.title("Pie Chart of X")
plt.show()