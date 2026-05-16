def func(x):
    return 1/(1+x*x)

def trapezoidal_rule(Xo,Xn,n):
    h=(Xn-Xo)/n
    total=func(Xo)+func(Xn)
    Xi=Xo
    for i in range(1, int(n)):
        Xi=Xi+h
        total+=2*func(Xi)
    return (h/2)*total

Xo=float(input("Enter lower limit (Xo): "))
Xn=float(input("Enter upper limit (Xn): "))
n=int(input("Enter number of intervals (n): "))
print("=> By using Trapezoidal rule:")
ans = trapezoidal_rule(Xo, Xn, n)
print(f"Approximate value of the integral is: {ans:.5f}")

