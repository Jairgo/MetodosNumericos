from sympy import *
from sympy.abc import x,y
from sympy import Function, dsolve, pprint, exp, cos, csc, tan, sec, sin, sqrt,integrate, init_printing
from sympy.parsing.sympy_parser import *


print("Bienvenido, calculará la integral mediante el método del trapecio")
print("1.- Ingrese la ecuacion: ")
ecu = input()
ec = parse_expr(ecu,evaluate=False)
a = int(input("Ingrese el límite inferior a: "))
b = int(input("Ingrese el límite inferior b: "))

fa = ec.subs(x,a)
fb = ec.subs(x,b)
ba = b - a
res = float(ba*((fa+fb)/2))
ve = integrate(ec, (x,a,b))

print("El valor aproximado de la integral es: ", res)
print("El valor exacto de la integral es: ", ve)
print("El error absoluto es: ", abs(res-ve))