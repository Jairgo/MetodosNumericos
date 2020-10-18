import matplotlib.pyplot as plt
from pylab import *
from sympy import *
from sympy.abc import x, y 
from sympy import Function, dsolve, pprint, exp, cos, csc, tan, sec, sin, sqrt

print("La ecuacion ya esta definida en el código")
print("Introduce el valor inicial x0 ")
x0 = float(input('x0: '))
print("Introduce el numero de iteraciones ")
n = int(input('n: '))

ec = 2-sin(sqrt(x))-x # ECUACION A RESOLVER
gx = 2-sin(sqrt(x))
gdx = -cos(sqrt(x))/(2*sqrt(x))



print("       g'(x)      |     x")
print("__________________|________________")

for k in range(n):
    
    gddx = gdx.subs(x,x0)
    if gddx < 1 and gddx > -1 :
        x0=gx.subs(x,x0)
        
        print(gddx,x0)

else:
    print("el valor x0 diverge en: ",x0)
    gx=gx.subs(x,x0)
    x0=gx
    print(x0)


x = np.linspace(0,2)  
#plt.plot(x,-cos(sqrt(x))/(2*sqrt(x)))  # DERIVADA DE LA ECUACION INICIAL - g'(x)
plt.plot(x,2-np.sin(np.sqrt(x)))        # DESPEJE DE LA ECUACION - g(x)
#plt.plot(x,2-np.sin(np.sqrt(x))-x)     # ECUACION INICIAL - f(x)
plt.grid()
plt.title("Jair Gómez Vásquez")
plt.show()
