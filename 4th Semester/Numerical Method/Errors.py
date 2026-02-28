true_value=float(input("Enter true value: "))
measured_value=float(input("Enter measured value: "))

abs_error=abs(measured_value-true_value)
relative_error=abs_error/true_value
percentage_error=relative_error*100

print("Absolute Error:", abs_error)
print("Relative Error:", relative_error)
print("Percentage Relative Error:", percentage_error, "%")