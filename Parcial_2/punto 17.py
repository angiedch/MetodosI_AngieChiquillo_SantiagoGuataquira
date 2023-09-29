# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:59:32 2023

@author: santi
"""

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
def GetLaguerre(n, x):
     y = sym.exp(-x)*x**n
    
     poly = sym.exp(x)*sym.diff(y,x,n)/( np.math.factorial(n) )
     
     return sym.expand(poly,x)
    


def GetDLaguerre (n, x):
    Pn= GetLaguerre(n,x)
    return sym.diff(Pn,x,1)
    
def NewtonRaphson(f,df,xn,itmax=100,precision=1e-6):
    error=1
    it=0
    while error >= precision and it < itmax:
        try:
            xn1=xn- f(xn)/df(xn)    
            error=np.abs(f(xn)/df(xn))
        except ZeroDivisionError:
            print("división por cero")
        xn= xn1 
        it+=1
    if it==itmax:
        return False
    else:
        return xn
    
def GetRootsGLag(funcion, derivada, x,tolerancia=10):
    raices=np.array([])
    
    for i in x:
        
        raiz=NewtonRaphson(funcion,derivada,i)
        
        if type(raiz) != bool:
            croot = np.round( raiz, tolerancia )
            if croot not in raices:
                raices=np.append(raices,croot)
    

    raices.sort()
    return raices
def GetAllRootsLag(n):
    
    xn = np.linspace(0,n+((n-1)*np.sqrt(n)),100)
    
    Laguerre = []
    DLaguerre = []
    
    
    for i in range(n+1):
        Laguerre.append(GetLaguerre(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRootsGLag(poly,Dpoly,xn)
    
    return Roots


def GetWeightsGLag(n):
    raices = GetAllRootsLag(n)
    weights = []

    for i in range(n):
        Laguerre_i = GetLaguerre(i, x)
        poly = sym.lambdify([x], Laguerre_i, 'numpy')
        weight_i = raices[i] /(((n+1)**2)* (poly(raices[i])**2))
        weights.append(weight_i)

    return weights



r=np.linspace(1,10,10)

def integral (f,n):
    pesos=GetWeightsGLag(n)
    raices=GetAllRootsLag(n)
    I=0
    for i in range(n):
        I+=pesos[i]*f(raices[i])
    return I

f= lambda x: ((x**3)*((np.exp(x)-1))/((np.exp(x))-2+(1/np.exp(x))))

print(GetAllRootsLag(3))
print(GetWeightsGLag(3))
print(integral(f, 3))


def graf(n,f):
    lista=[]
    

    for i in n:
        lista.append(integral(f,int(i))/((np.pi**4)/15))
    plt.scatter(n,lista)
    plt.show()
    
print (graf(r,f))