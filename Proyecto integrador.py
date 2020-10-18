import platform
import os
import time
import matplotlib.pyplot as plt
import numpy as np



def imprimir():
    #cleanScreen()
    print("___________________________________________________")
    print(" Bienvenido a la calculadora de Métodos númericos ")
    print("___________________________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Calcular polinomio de Tylor")
    print("2. Encontrar polinomio de interpolacion lagrange")
    print("3. Ec. de la recta Minimos Cuadrados")
    print("4. Newton Raphson")
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
                print('Error, solo de aceptan numeros del 0 al 6')

        except ValueError:
            print("Error, ingrese solamente numeros.")


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


def tylor():
    print("January")


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

###########################################################################


def minCua():
    cleanScreen()
    print("_____________________________________________________")
    print(" II.- Encontrar la ecuación de la recta \n con método de minimos cuadrados  ")
    print("_____________________________________________________")
    print("Sigue los siguiente pasos:")
    n = int(input("1.- Ingrese la cantidad de punto deseados: "))

    Xs = []
    Ys = []
    xi = 0
    yi = 0
    j = 0
    for j in range(n):
        xi = int(input("Ingresa X%i " % (j)))
        yi = int(input("Ingresa Y%i " % (j)))
        #Xs.append([int(1),int(xi),int(xi**2)])
        Xs.append([int(1),int(xi)])
        Ys.append(int(yi))

    AA = np.transpose(Xs)  # transpuesta
    u = np.dot(AA, Xs)  # multiplica
    u1 = np.linalg.inv(u)
    u2 = np.dot(u1, AA)
    u3 = np.dot(u2, Ys)  # u3[0]=b u3[1]=a donde y = ax+b

    # los simbolos %s sirven para mezclar textos con variables
    print(" La recta es y= %s*x+ %s" % (u3[1], u3[0]))
    time.sleep(2)
    x = np.linspace(-5, 7)
    y1 = u3[1]*x+u3[0]  # Ecuación de la recta
    plt.plot(x, y1)  # Grafica la recta
    X = [4, 5, -1, 1]
    plt.plot(X, Ys, 'o', color='r')  # grafica puntos
    plt.title("Regresion cuadrática_ y= %s*x+ %s" % (u3[1], u3[0]))
    plt.grid(True)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()
    


def newRap():
    return "April"


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
