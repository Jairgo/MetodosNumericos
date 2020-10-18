import platform
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy.abc import x, y
from pylab import *
from sympy import Function, dsolve, pprint, exp, cos, csc, tan, sec, sin, sqrt


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
    print("4. Newton Raphson y Punto fijo")
    print("5. Método de Simpson")
    print("6. Runge Kutta")
    print("0. Salir")
    print("** NOTA ** -> Hasta que cierre la ventana de las graficas el programa continuará")
    print()


def menu():
    while True:
        imprimir()
        try:
            opSelected = int(input("Seleccione una opcion: "))

            if opSelected in range(7):

                if opSelected == 0:
                    print("Adios! :)")
                    break
                print()
                chooseMetodo(opSelected)
            else:
                print('Error, solo se aceptan numeros del 0 al 6')
                time.sleep(2)

        except ValueError:
            print("Error, ingrese solamente numeros.")
            time.sleep(2)


def chooseMetodo(opcion):
    print("Usted eligió la opcion %i ! ...\n" % (opcion))
    switch = {
        1: tylor,
        2: lagrange,
        3: minCua,
        4: newRap,
        5: simpson,
        6: kutta
    }
    func = switch.get(opcion, "inválido")

    func()

############################ Tylor #############################################
def tylor():
    print("January")

############################ LAGRANGE ##########################################
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

    input("Presione enter para continuar...")

############################ Minimos cuadrados #################################
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
        Xs.append([int(1),int(xi),int(xi**2)])
        justXs.append(int(xi))
        Ys.append(int(yi))

    AA = np.transpose(Xs)  # transpuesta
    u = np.dot(AA, Xs)  # multiplica
    u1 = np.linalg.inv(u)
    u2 = np.dot(u1, AA)
    u3 = np.dot(u2, Ys)  # u3[0]=b u3[1]=a donde y = ax+b

    print(" La recta es y= %s*x^2+%s*x+ %s" % (u3[2],u3[1], u3[0]))
    print("3.- Ingrese el rango en el eje X para graficar ")

    xo = int(input("X inicial: "))
    xf = int(input("X final: "))
    x = np.linspace(xo, xf)
    y1 = (u3[2]*(x**2))+u3[1]*x+u3[0]  # Ecuación de la recta

    plt.plot(x, y1)  # Grafica la recta
    plt.plot(justXs, Ys, 'o', color='r')  # Grafica los puntos
    plt.title("Regresion cuadrática_ y= %s*x+ %s" % (u3[1], u3[0]))
    plt.grid(True)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()

    input("Presione enter para continuar...")
    
############################ Newton Raphson ####################################
def newRap():
    cleanScreen()
    print("________________________________________")
    print(" IV.- Solución mediante Newton-Raphson  ")
    print("________________________________________")
    print("Sigue los siguiente pasos:")
    x0 = int(input("1.- Ingrese el valor inicial: ")) # Valor inicial
    print("2.- Ingrese la ecuacion deseada: ") 
    ec = (2*(x**3))-(11.7*(x**2))+(17.7*x)-5 # Ecuación
    dec = diff(ec,x)
    A =[]
    N = int(input("3.- Ingrese el numero de iteraciones deseada: ")) # numero de iteraciones
    for k in range(N):
        x1 = x0 - float(ec.subs(x,x0))/float((dec.subs(x,x0)))
        A.append(x1)
        print("X_%i:  %s" % (int(k),float(x1)),"| Error: ",float(ec.subs(x,x1)))
        x0 = x1
    
    input("Presione enter para continuar...")
    cleanScreen()
    import punto_fijo
    exec(open('punto_fijo.py').read())
    input("Presione enter para continuar...")


def simpson():
    return "May"


def kutta():
    return "June"


def cleanScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    menu()
