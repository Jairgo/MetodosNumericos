import platform
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from sympy import *
from sympy.abc import x, y, z
from sympy import Function, dsolve, pprint, exp, cos, csc, tan, sec, sin, sqrt
from sympy.parsing.sympy_parser import *


print("Bienvenido, calculará la integral mediante el método de RungeKutta 4")
print("1.- Ingrese la ecuacion: ")

ecu = input()
ec = parse_expr(ecu,evaluate=False)

x0 = int(input("Ingrese el valor x0: "))
y0 = int(input("Ingrese el valor y(x0): "))
n = int(input("Ingrese el numero de iteraciones n: "))
h = float(input("Ingrese el valor de h: "))

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
    print("   %.6f       %.1f    " % (y0,x0))
