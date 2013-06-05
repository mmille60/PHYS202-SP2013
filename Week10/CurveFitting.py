def LinearLeastSquaresFit(x,y):
    from numpy import *
    """takes in array repersenting (x,y) values for a set of linearly varying data and perform a linear least squares refression. Return the resulting slope and intercenpt parameters of the best fir line with their uncertainties"""
    m=(average(x*y)-average(x)*average(y))/(average(x**2)-(average(x))**2)
    b=(average(x*x)*average(y)-average(x)*average(x*y))/(average(x**2)-(average(x))**2)
    u=y-(m*x+b)
    n=len(x)
    um=((1/(n-2.))*average(u**2)/(average(x**2)-(average(x))**2))**.5
    ub=((1/(n-2.))*(average(u**2)*average(x**2))/(average(x**2)-(average(x))**2))**.5
    return m,b,um,ub

