# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:44:19 2023

@author: santi
"""

import sympy as sym 


x = sym.Symbol('x',real=True)



def error (f,a,b): 
    h=(b-a)/3
    f1= x*(x-h)*(x-2*h)*(x-3*h)
   
    e=sym.diff(f, x, 4) / sym.factorial(4) * sym.integrate(f1, (x, 0, 3 * h))
    return e

f= x**4

# en el caso del ejemplo vamos a usar la funcion f=x**4 y (a,b)=(2,5)
error_real=-(3/80)*1*24

print(error(f,2,5))
print(error_real)