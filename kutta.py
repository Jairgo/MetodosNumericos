import platform
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy import  *
from pylab import *
from sympy import *
from sympy.abc import x, y
from sympy import Function, dsolve, pprint, exp, cos, csc, tan, sec, sin, sqrt
from sympy.parsing.sympy_parser import *    

print("________________________________________________________________")
print(" VII.- Resolver Ecuación diferencial con método de Runge Kutta 4")
print("________________________________________________________________")
print("Sigue los siguiente pasos:")
print("1.- Ingrese la ecuacion: ")

ecu = input()
ec = parse_expr(ecu,evaluate=False)
print(ec)
x0 = int(input("Ingrese el valor x0: [int] "))
y0 = float(input("Ingrese el valor y(x0): [float] "))
n = int(input("Ingrese el numero de iteraciones n: [int] "))
h = float(input("Ingrese el valor de h: [float] "))
justXs = np.array([])
Ys = np.array([])
print("     yn        |   xn       |")
print("_______________|____________|")
print("        "+str(y0)+"          "+str(x0))
for i in range(n):
    k1 = ec.subs([(x,x0),(y,y0)])
    k2 = ec.subs([(x,x0+(0.5*h)),(y,y0+(0.5*h*k1))])
    k3 = ec.subs([(x,x0+(0.5*h)),(y,y0+(0.5*h*k2))])
    k4 = ec.subs([(x,x0+h),(y,y0+(h*k3))])
    yn = y0 +((h/6)*(k1+2*k2+2*k3+k4))
    y0 = yn
    x0 += h
    np.append(justXs,int(x0))
    np.append(Ys,int(y0))
    #print("   %.12f       %.2f    " % (y0,x0))

print(justXs)
print(Ys)
#xx = np.linspace(0,10)  
#plt.plot(x,-cos(sqrt(x))/(2*sqrt(x)))  # DERIVADA DE LA ECUACION INICIAL - g'(x)
#yzz=2*x*y
#plt.plot(xx,yzz)        # DESPEJE DE LA ECUACION - g(x)
#plt.plot(justXs, Ys, 'o', color='r')

#plt.plot(x,2-np.sin(np.sqrt(x))-x)     # ECUACION INICIAL - f(x)
#plt.grid()
#plt.title("Jair Gómez Vásquez")
#plt.xlabel('Eje X')
#plt.ylabel('Eje Y')
#plt.show()