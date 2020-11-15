import platform
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from sympy import *
from sympy.abc import x, y
from sympy import Function, dsolve, pprint, exp, cos, csc, tan, sec, sin, sqrt
from sympy.parsing.sympy_parser import *


def imprimir():
    cleanScreen()
    print("___________________________________________________")
    print(" Bienvenido a la calculadora de Métodos númericos ")
    print("___________________________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Calcular polinomio de Tylor")
    print("2. Encontrar polinomio de interpolacion lagrange")
    print("3. Ec. de la recta Minimos Cuadrados")
    print("4. Newton Raphson")
    print("5. Punto fijo")
    print("6. Método de Simpson")
    print("7. Runge Kutta")
    print("0. Salir")
    print("\n** NOTA **\nHasta que cierre la ventana de las graficas el programa continuará")
    print()


def menu():
    while True:
        imprimir()
        try:
            opSelected = int(input("Seleccione una opcion: "))

            if opSelected in range(8):

                if opSelected == 0:
                    print("Adios! :)")
                    break
                print()
                chooseMetodo(opSelected)
            else:
                print('Error, solo de aceptan numeros del 0 al 7')

        except ValueError:
            print("Error, ingrese solamente numeros.")


def chooseMetodo(opcion):
    print("Usted eligió la opcion %i ! ...\n" % (opcion))
    switch = {
        1: tylor,
        2: lagrange,
        3: minCua,
        4: newRap,
        5: puntof,
        6: simpson,
        7: kutta
    }
    func = switch.get(opcion, "inválido")

    func()

############################ Taylor #########################################
def tylor():
    cleanScreen()
    print("_____________________________________________________")
    print(" I.- Polinomios de Taylor  ")
    print("_____________________________________________________")
    print("Sigue los siguiente pasos:")
    print("1.- Ingrese la ecuacion: ")
    ecu = input()
    ec = parse_expr(ecu,evaluate=False)
    #ec = ln(1+x)
    #ec = 2*(x**3)-4*ln(x) #funcion sin derivar
    x0 = int(input("2.- Ingrese el valor inicial: "))
    N = int(input("3.- Ingrese el numero de orden N: "))
    A = [] # Lista de sustituciones en funciones y derivadas
    F = [] # Lista de funcion y derivadas
    N += 1
    
    for k in range(N):
        F.append(ec)
        sust = ec.subs(x,x0)
        A.append(sust)
        dec = diff(ec,x) # N derivada
        ec = dec
        

    #print(A)
    #print(F)
    T = []
    T.append(A[0])
    N-= 1
    for k in range(N):
        #print(k)
        #print((x-x0)**(k+1))
        f1 = (A[k+1]/factorial(k+1))*((x-x0)**(k+1))
        T.append(f1)
    
    poli = sum(T)
    print("Polinomio de taylor : ", poli)

    input("Presione enter para continuar... ")

############################ LAGRANEGE #########################################
def lagrange():
    cleanScreen()
    print("_____________________________________________________")
    print(" II.- Encontrar polinomio de interpolacion lagrange  ")
    print("_____________________________________________________")
    print("Sigue los siguiente pasos:")
    print("1.- Ingrese 4 puntos (x,y)")
    Xs = []
    Ys = []
    xi = 0
    yi = 0
    j = 0
    for j in range(4):
        xi = int(input("Ingresa X%i " % (j)))
        yi = int(input("Ingresa Y%i " % (j)))
        Xs.append(int(xi))
        Ys.append(int(yi))

    # X=[4,6,8,10]
    # Y=[1,3,8,20]

    x = np.linspace(0, 20)  # de donde a donde en eje X grafica
    y = (((x-6)*(x-8)*(x-10))*1/(1-3)*(1-8)*(1-20))+(((x-4)*(x-8)*(x-10))*3/(3-1)*(3-8)*(3-20)) + \
        (((x-6)*(x-1)*(x-10))*8/(8-3)*(8-1)*(8-20)) + \
        (((x-6)*(x-8)*(x-4))*20/(20-3)*(20-8)*(20-1))

    plt.plot(x, y, label="Polinomio aproximado")
    plt.plot(Xs, Ys, 'o', color='r')
    plt.title("Interpolación de Lagrange - Por Jair GV")
    plt.grid(True)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()

############################ Minimos cuadrados #########################################
def minCua():
    cleanScreen()
    print("_____________________________________________________")
    print(" III.- Encontrar la ecuación de la recta \n con método de minimos cuadrados  ")
    print("_____________________________________________________")
    print("Sigue los siguiente pasos:")
    n = int(input("1.- Ingrese la cantidad de puntos deseados: "))

    Xs = []
    justXs = []
    Ys = []
    xi = 0
    yi = 0
    j = 0
    print("2.- Ingrese los puntos")
    for j in range(n):
        xi = int(input("Ingresa X%i " % (j)))
        yi = int(input("Ingresa Y%i " % (j)))
        #Xs.append([int(1),int(xi),int(xi**2)])
        Xs.append([int(1),int(xi),int(xi**2)])
        justXs.append(int(xi))
        Ys.append(int(yi))

    AA = np.transpose(Xs)  # transpuesta
    u = np.dot(AA, Xs)  # multiplica
    u1 = np.linalg.inv(u)
    u2 = np.dot(u1, AA)
    u3 = np.dot(u2, Ys)  # u3[0]=b u3[1]=a donde y = ax+b

    # los simbolos %s sirven para mezclar textos con variables
    print(" La recta es y= %s*x^2+%s*x+ %s" % (u3[2],u3[1], u3[0]))
    print("3.- Ingrese el rango en el eje X para graficar ")
    xo = int(input("X inicial: "))
    xf = int(input("X final: "))
    x = np.linspace(xo, xf)
    y1 = (u3[2]*(x**2))+u3[1]*x+u3[0]  # Ecuación de la recta
    plt.plot(x, y1)  # Grafica la recta
    plt.plot(justXs, Ys, 'o', color='r')  # grafica puntos
    plt.title("Regresion cuadrática_ y= %s*x+ %s" % (u3[1], u3[0]))
    plt.grid(True)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()
    
############################ Newton Raphson #########################################
def newRap():
    cleanScreen()
    print("_____________________________________________________")
    print(" IV.- Resolver mediante Newton Raphson  ")
    print("_____________________________________________________")
    print("Sigue los siguiente pasos:")
    x0 = int(input("1.- Ingrese el valor inicial: "))
    #x0 = int(input("2.- Ingrese la ecuacion a resolver "))
    N = int(input("3.- Ingrese el numero de iteracioes deseada: "))
    #ec = (2*(x**3))-(11.7*(x**2))+(17.7*x)-5 #ecuacion / (exp(-x))-x
    ec = (exp(-x))-x
    dec = diff(ec,x)
    A=[]
    for k in range(N):
        x1 = x0 - float(ec.subs(x,x0))/float((dec.subs(x,x0)))
        A.append(x1)
        #print("Xn",k,float(x1))
        print("X_%i: %.16f" % (k,float(x1)),"| Error: ",float(ec.subs(x,x1)))
        x0 = x1
    input("\nPresione enter para continuar... ")

############################ Punto fijo #########################################
def puntof():
    cleanScreen()
    print("_____________________________________________________")
    print(" V.- Resolver mediante Punto Fijo  ")
    print("_____________________________________________________")
    print("Sigue los siguiente pasos:")
        
    print("1.- Introduce la ecuación a resolver")
    ecu = input()
    gx = parse_expr(ecu,evaluate=False)

    print("Introduce el valor inicial x0 ")
    x0 = float(input('x0: '))
    print("Introduce el numero de iteraciones ")
    n = int(input('n: '))

    #ec = 2-sin(sqrt(x))-x # ECUACION A RESOLVER
    #gx = 2-sin(sqrt(x))
    
    #gdx = -cos(sqrt(x))/(2*sqrt(x)) 
    gdx = diff(gx,x)


    print("       g'(x)      |     x")
    print("__________________|________________")

    for k in range(n):
    
        gddx = gdx.subs(x,x0)
        if gddx < 1 and gddx > -1 :
            x0 = gx.subs(x,x0)
            
            print(gddx,x0)

        else:
            print("el valor x0 diverge en: ",x0)
            gx = gx.subs(x,x0)
            x0 = gx
            print(x0)


    xx = np.linspace(0,2)  
    #plt.plot(x,-cos(sqrt(x))/(2*sqrt(x)))  # DERIVADA DE LA ECUACION INICIAL - g'(x)
    plt.plot(xx,2-np.sin(np.sqrt(xx)))        # DESPEJE DE LA ECUACION - g(x)
    #plt.plot(x,2-np.sin(np.sqrt(x))-x)     # ECUACION INICIAL - f(x)
    plt.grid()
    plt.title("Jair Gómez Vásquez")
    plt.show()

    input("\nPresione enter para continuar... ")

############################ Simpson #########################################
def simpson():
    cleanScreen()
    print("____________________________________________")
    print(" VI.- Resolver integral con método de Simpson  ")
    print("____________________________________________")
    print("Sigue los siguiente pasos:")
    print("1.- Ingrese la función a integrar")
    ecu = input()
    ec = parse_expr(ecu,evaluate=False)
    a = int(input("2.- Ingrese el limite inferior de la integral (a): "))
    b = int(input("3.- Ingrese el limite superior de la integral (b): "))
    n = int(input("4.- Ingrese el numero de iteraciones: "))
    delx = (b - a)/n # lim sup - lim inf ente iteraciones
    A = [] # Lista que guarda las funciones ya evaluadas
    fx0 = ec.subs(x,a) # El coeficiente 1 inicial
    A.append(fx0)
    k = float(a)
    band = True # Significa que inicia con el 4
    while(k<=(b-delx)):
        k += delx
        fxn = ec.subs(x,k)
        if band:
            fxn = fxn*4
            band = False
        else:
            fxn = fxn*2
            band = True
        A.append(fxn)
    
     
    kf = k + delx
    fxnf = ec.subs(x,kf) # El coeficiente 1 final
    A.append(fxnf)
    #Asum = sum(A)
    Atotal = sum(A) * (delx/3)
    print("El resultado de la integral ", ec, " es: ", Atotal)
    
    input("Presione enter para continuar... ")
    
    
############################ Runge Kutta #########################################
def kutta():
    cleanScreen()
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
        print("   %.12f       %.2f    " % (y0,x0))
        
    print("K1 = %.12f" % (k1))
    print("K2 = %.12f" % (k2))
    print("K3 = %.12f" % (k3))
    print("K4 = %.12f" % (k4))


    input("Presione enter para continuar... ")


def cleanScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    menu()
