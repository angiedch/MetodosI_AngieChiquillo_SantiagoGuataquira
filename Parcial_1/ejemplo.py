# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:11:52 2023

@author: santi
"""
import numpy as np
import matplotlib.pyplot as mp 
import pandas as pd 
import sympy as sp
datos=pd.read_csv("Parabolico.csv",sep=",")
X=np.array(datos.X)
Y=np.array(datos.Y)

def Lagrange(x,X,i):
    
    L = 1
    
    for j in range(X.shape[0]):
        if i != j:
            L *= (x - X[j])/(X[i]-X[j])
            
    return L
def polinomio(x,X,Y):
    
    Pol = 0
    
    for i in range(X.shape[0]):
        Pol += Lagrange(x,X,i)*Y[i]
        
    return Pol



x=np.linspace(1,7,50)
y1= polinomio(x, X, Y)
mp.plot(x,y1)
mp.scatter(X, Y, color='g')

_x=sp.Symbol('x',real=True)
f =polinomio(_x, X, Y)
f= sp.simplify(f)
print (f)


