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
X = np.linspace(0,10,101)

def polinomio (x, X, a_0, a_1, a_2):
    return a_0 + a_1*(X-x[0]) + a_2*(X-x[0])*(X-x[1])

p = polinomio(x, X, a_0, a_1, a_2)
print(p)

#Derivada Exacta
def DerExacta(x):
    return ((1/np.cos(x))**2)/(2*(np.tan(x))**(1/2))

#Derivada progresiva
def DerProgresiva(f, x, h): 
    return (f(x+h) - f(x))/h
    

def DerCentral(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)


RDerivative = DerProgresiva(function,x,h)
CDerivative = DerCentral(function,x,h)
EDerivative = DerExacta(x)

plt.scatter(x,RDerivative,label='Derivada Derecha')
plt.scatter(x,CDerivative,label='Derivada Central')
plt.scatter(x,EDerivative,label='Derivada Exacta')
plt.legend()
plt.show()

#ERROR NODAL
EProgresiva = np.abs(EDerivative-RDerivative)
ECentral = np.abs(EDerivative-CDerivative)
plt.scatter(X, EProgresiva, label='Error Progresiva')
plt.scatter(X, ECentral, label='Error Central')
plt.legend()
plt.show()


<<<<<<< HEAD

=======
>>>>>>> eea3575b61773d3dfa285209b2973ccf8489de6b
