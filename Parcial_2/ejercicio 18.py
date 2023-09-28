# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:06:20 2023

@author: santi
"""

import sympy as sym 
import numpy as np 
x = sym.Symbol('x',real=True)

def GetHermite(n,x):

      
    y = sym.exp(-x**2)
    
    poly = ((-1)**n)*sym.exp(x**2)*sym.diff(y,x,n)
    
    return sym.expand(poly,x)   

def GetDHermite (n, x):
    Pn= GetHermite(n,x)
    return sym.diff(Pn,x,1)

def NewtonRaphson(f,df,xn,itmax=100,precision=1e-8):
    error=1
    it=0
    while error > precision and it < itmax:
        try:
            xn1=xn-(f(xn)/df(xn))
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

def GetAllRootsGHer(n):
    inter=int(np.sqrt(4*n+1))
    xn= np.linspace(-inter,inter,100)
    Hermite= []
    DHermite=[]
    for i in range(n+1):
        Hermite.append(GetHermite(i,x))
        DHermite.append(GetDHermite(i,x))
        
    poli=sym.lambdify([x],Hermite[n],'numpy')
    Dpoli=sym.lambdify([x],DHermite[n],'numpy')
    Raices= GetRootsGLag(poli,Dpoli,xn)
    return Raices
def GetWeightsGHer(n):
    raices=GetAllRootsGHer(n)
    Hermite=[]
    for i in range(1,(n+1)):
        Hermite.append(GetHermite(i-1, x))
    poli=sym.lambdify([x],Hermite[n-1],'numpy')
    pesos= (2**(n-1)*np.math.factorial(n)*np.sqrt(np.pi))/((n**2)*(poli(raices))**2)
    return pesos



print(GetAllRootsGHer(20))

# b 
pesos=GetWeightsGHer(5)
raices=GetAllRootsGHer(5)
f=lambda x: (x**2/(2*np.sqrt(np.pi)))*(4*x**2)
I=0                   
for i in range(5):
    I += pesos[i]*f(raices[i])
    
print (I)

