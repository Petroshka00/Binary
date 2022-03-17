import random
import math

def binary(lista, obj):
    #print(format("{} \n").format(lista))
    if len(lista) > 1:
        pivot = lista[math.floor(len(lista)/2)]                 #Crear pivot (numero a partir del cual se acorta la lista)
        if pivot > obj:
            nuevalista = lista[0: math.floor(len(lista)/2)]     #Eliminar objetos a la derecha 
            return binary(nuevalista, obj)
        else:
            nuevalista = lista[math.floor(len(lista)/2)::]      #Eliminar objetos a la izquierda
            return binary(nuevalista, obj)
    else:
        if obj in lista:
            return True                                         #El objeto esta en la lista
        else:
            return False                                        #El objeto no esta en la lista
        
while True:
    numeros = []
    min = 1
    max = 4
    test = False
    print("Intenta adivinar un numero de la lista \n")
    cantidad = int(input("Determinar largo de la lista: "))
    while len(numeros) < cantidad:
        x = random.randint(min, max)
        numeros.append(x)               #Esto crea una lista de numeros que saltan aleatoreamente
        min += 4                        #Entre 1 y 8 entre un numero y el siguiente
        max += 4
    while test == False:
        objetivo = int(input("Intenta adivinar un numero de la lista: "))
        if (binary(numeros, objetivo)):
            print("¡Felicidades! \nTu numero estaba en la lista")
            test = True
        else:
            print("Tu numero no estaba en la lista")
