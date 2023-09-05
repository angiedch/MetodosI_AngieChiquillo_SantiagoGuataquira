# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:11:53 2023

@author: santi
"""
import numpy as np
import matplotlib.pyplot as plt

#Polinomio de interpolación
#p(x) = a0 + a1(x-x0) + a2 (x-x0)(x-x1)


h= 0.01
x= np.linspace(0.1,1.1,101)


#función evaluada en x
def function(x):
    return (np.tan(x))**0.5

f = function(x)
#print(y)

#Hacer el polinomio evaluado en x
a_0 = f[0]
a_1 = (f[1]-f[0])/h
a_2= (f[2]-f[1])/(2*(h**2))

X = np.linspace(0,1,50)
p = a_0 + a_1*(X-x[0]) + a_2*(X-x[0])*(X-x[1])

#plt.scatter(x,f,color='b')
#plt.plot(X,p, color='g')
#plt.show()

#Derivada progresiva
def DefProgresiva(f, x, h): 
    return (f(x+h) - f(x))/h
    

def DefCentral(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)


RDerivative = DefProgresiva(function,x,h)
CDerivative = DefCentral(function,x,h)

plt.scatter(x,RDerivative,label='Derivada Derecha')
plt.scatter(x,CDerivative,label='Derivada Central')
plt.legend()
plt.show()

def ErrorNodal(x, y):
    return y - x

ENodal= ErrorNodal(p, function)
plt.scatter(x, ENodal, label= 'Error Nodal')
plt.legend()
plt.show()

