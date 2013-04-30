def foutPtFiniteDiff(x,y):
    """takes an array x and a function y as inputs and returns the derivative of the function y"""
    import numpy as np
    h= x[2]-x[1]
    dydx =np.zeros(y.shape,float)
    for i in range(2,len(y)-2):
        dydx[i]=(y[i-2]-8*y[i-1]+8*y[i+1]-y[i+2])/(12*h)
    return dydx
#creating a function to take a derivative
def finiteDifference(x,y):
    """returns the derivative of y with respect to x forward differentiation"""
    import numpy as np
    dy =np. diff(y) #y(n+1)-y(n)
    dx =np. diff(x)
    dydx1 =np.zeros(y.shape,float)
    dydx1[:-1] = dy/dx
    dydx1[-1] = (y[-1] -y[-2])/(x[-1] - x[-2])#diferintionation method
    return dydx1

