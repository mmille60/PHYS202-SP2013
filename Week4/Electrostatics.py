import numpy as np

k=8.8987*(10**9)
def pointPotential(x,y,q,posy,posx):
    """Vxy is the eletra potential it takes x,y,q,posx,posy and returns the potential"""
    Vxy=((k*q)/((x-posx)**2+(y-posy)**2)**.5)
    return Vxy
def dipolePotential(x,y,q,d):
    """dipole pontial of 2 particles seperated by a distance d algo x axis"""
    Vxy=pointPotential(x,y,q,(d/2.),0)+pointPotential(x,y,-q,(-d/2.),0)
    return Vxy
def dipolePotentialy(x,y,q,d):
    """dipole pontial of 2 particles seperated by a distance y algo x axis"""
    Vy=pointPotential(x,y,q,(0),(d/2.))+pointPotential(x,y,-q,(0),(-d/2.))
    return Vy
def dipolePotentialangle(x,y,q,d,Theta):
    """returns dispole pontial betweentwo particles seperated by distance d and angle theta with axis"""
    Vxy= pointPotential(x,y,q,(d/2.*cos(Theta)),(d/2.*sin(Theta)))+pointPotential(x,y,-q,-(d/2.*cos(Theta)),(-d/2.*sin(Theta)))
    return Vxy
k=8.987*10**9
def pointFeild(x,y,q,Xq,Yq):
        """put in x,y,q,Xq,Yq returns a tuple of the electric field componets Ex , Ey"""
        Ex=(k*q)*(x-Xq)/((x-Xq)**2+(y-Yq)**2)**.5
        Ey=(k*q)*(y-Yq)/((x-Xq)**2+(y-Yq)**2)**.5
        return (Ex,Ey)
