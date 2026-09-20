import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ID = [242311041, 242311042, 242311043, 242311044, 242311045]

Name = [
    "MST. RUKAIYA ZANNAT",
    "ABID ANZUM",
    "MD. SHIFAT AHMED SOBUJ",
    "TOMA SARKAR",
    "MD. HAMIDULLAH"
]

Gender = ["Female", "Male", "Male", "Female", "Male"]

Home_District = ["Rajshahi", "Rajshahi", "Rajshahi", "Naogaon", "Rajshahi"]

Age = [23, 24, 24, 23, 25]

Parents_Income = [40000, 45000, 35000, 37000, 40000]

CGPA = [2.66, 1.76, 2.61, 3.45, 3.23]



for i in range(5):
    print("Student", i + 1)
    print("ID:", ID[i])
    print("Name:", Name[i])
    print("Gender:", Gender[i])
    print("Home District:", Home_District[i])
    print("Age:", Age[i])
    print("Parents Income:", Parents_Income[i])
    print("CGPA:", CGPA[i])
    print()





df = pd.DataFrame({
    "ID": ID,
    "Name": Name,
    "Gender": Gender,
    "Home District": Home_District,
    "Age": Age,
    "Parents Income": Parents_Income,
    "CGPA": CGPA
})

print(df.to_string(index=False))





def AM(data):
    return np.mean(data)


def GM(data):
    return np.exp(np.mean(np.log(data)))


def HM(data):
    return len(data) / sum(1 / x for x in data)


def Mode(data):
    mode = pd.Series(data).mode().tolist()

    if len(mode) == len(data):
        return "No Mode"

    return mode

print("Age AM =", AM(Age))
print("Age GM =", GM(Age))
print("Age HM =", HM(Age))
print("Age Median =", np.median(Age))
print("Age Mode =", Mode(Age))

print("Income AM =", AM(Parents_Income))
print("Income GM =", GM(Parents_Income))
print("Income HM =", HM(Parents_Income))
print("Income Median =", np.median(Parents_Income))
print("Income Mode =", Mode(Parents_Income))

print("CGPA AM =", AM(CGPA))
print("CGPA GM =", GM(CGPA))
print("CGPA HM =", HM(CGPA))
print("CGPA Median =", np.median(CGPA))
print("CGPA Mode =", Mode(CGPA))



# plt.plot(Age, marker="o")
# plt.title("Line Plot of Students Age")
# plt.xlabel("Student")
# plt.ylabel("Age")
# plt.show()

# plt.hist(Age)
# plt.title("Histogram of Students Age")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# plt.hist(Age)
# plt.title("Histogram of Students Age")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# plt.bar(Name, Age)
# plt.title("Bar Plot of Students Age")
# plt.xlabel("Student")
# plt.ylabel("Age")
# plt.show()




# plt.plot(Parents_Income, marker="o")
# plt.title("Line Plot of Parents Income")
# plt.xlabel("Student")
# plt.ylabel("Income")
# plt.show()

# plt.hist(Parents_Income)
# plt.title("Histogram of Parents Income")
# plt.xlabel("Income")
# plt.ylabel("Frequency")
# plt.show()

# plt.bar(Name, Parents_Income)
# plt.title("Bar Plot of Parents Income")
# plt.xlabel("Student")
# plt.ylabel("Income")
# plt.show()

# plt.pie(Parents_Income, labels=Name, autopct="%1.1f%%")
# plt.title("Pie Chart of Parents Income")
# plt.show()


# plt.plot(CGPA, marker="o")
# plt.title("Line Plot of CGPA")
# plt.xlabel("Student")
# plt.ylabel("CGPA")
# plt.show()


# plt.hist(CGPA)
# plt.title("Histogram of CGPA")
# plt.xlabel("CGPA")
# plt.ylabel("Frequency")
# plt.show()

# plt.bar(Name, CGPA)
# plt.title("Bar Plot of CGPA")
# plt.xlabel("Student")
# plt.ylabel("CGPA")
# plt.show()

# plt.pie(CGPA, labels=Name, autopct="%1.1f%%")
# plt.title("Pie Chart of CGPA")
# plt.show()


plt.bar(Gender, CGPA)

plt.title("Gender vs CGPA")
plt.xlabel("Gender")
plt.ylabel("CGPA")

plt.show()