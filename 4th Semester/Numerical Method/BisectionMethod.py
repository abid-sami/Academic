from math import fabs

def f(x):
    return x**3-2*x-5

def Bisection(xl, xu, max_itr=500, eps=0.05):
    if f(xl)*f(xu)>0:
        print("Wrong!")
        return None
    if f(xl)*f(xu)==0:
        if f(xl)==0:
            return xl
        else:
            return xu
    itr=1
    xr_old=(xl + xu)/2
    while True:
        if f(xl)*f(xr_old)>0:
            xl=xr_old
        elif f(xl)*f(xr_old)<0:
            xu=xr_old
        else:
            return xr_old
        xr_new=(xl + xu)/2
        ae=fabs(xr_new - xr_old)
        xr_old=xr_new
        itr=itr+1 
        if ae<=eps or itr>max_itr:
            break
    return xr_old

xl=float(input("Enter Lower limit: "))
xu=float(input("Enter Upper limit: "))
xr=Bisection(xl, xu)

if xr is not None:
    print(f"Root is at : {xr:.3f}")
    print(f"Value of f(xr): {f(xr): .3f}")


