# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:03:49 2023

@author: santi
"""

import numpy as np 
import sympy as sym 

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLegendreRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = x
    else:
        poly = ((2*n-1)*x*GetLegendreRecursive(n-1,x)-(n-1)*GetLegendreRecursive(n-2,x))/n
   
    return sym.expand(poly,x)

def GetDLegendre(n,x):
    Pn = GetLegendreRecursive(n,x)
    return sym.diff(Pn,x,1)
def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots
def GetAllRootsGLeg(n):

    xn = np.linspace(-1,1,100)
    
    Legendre = []
    DLegendre = []
    
    for i in range(n+1):
        Legendre.append(GetLegendreRecursive(i,x))
        DLegendre.append(GetDLegendre(i,x))
    
    poly = sym.lambdify([x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLeg(n):

    Roots = GetAllRootsGLeg(n)

    

    DLegendre = []
    
    for i in range(n+1):
        DLegendre.append(GetDLegendre(i,x))
    
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights

def func(T,dpT,x):
    return np.tanh(np.sqrt(x**2+((dpT**2)*300/2*T)))/np.sqrt(x**2+dpT**2)
def integral(f,a,b,n,T,dT):
    Ip=0
    for i in range(n):
        t=0.5*((GetAllRootsGLeg(n)[i]*(b-a))+(b+a))
        Ip+=GetWeightsGLeg(n)[i]*f(T,dT,t)
    return Ip*(b-a)*0.5

dt=1e-4
def superconductividad(dt,a,b):
    n=50
    T=0
    for i in range(1,20):
        T+=dt*i
        I=integral(func,a,b,n,T,dt)
        if ((I-1)/0.3)<dt:
            return T
        else:
            return "error"
        
        

print(superconductividad(dt,-1,1))