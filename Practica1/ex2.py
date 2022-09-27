#Escribir un programa de Python que despliegue los enteros negativos hasta n, en funciones
#Después verifica cuáles de esos son primos

import sys #Primero se importa la librería de sys para el uso con la terminal

def lista (n):                 #En esta función de lista se llama con un valor que es el número hasta el cual se hace la lista
    lista=[]                   #Se crea la lista 
    for i in range (n+1):      #Desde cero hasta el número más alto de la lista se hace lo siguiente:
        lista.append(i)        #Se junta el número actual a la lista
    return (lista)             #Devuelve la lista completa

def primos (lista):            #Se crea la función primos con la entrada lista generada en la función anterior
    primo=[]                   #Se crea la lista de primos
    for i in lista:            #Desde cero hasta el número más alto de la lista se:
        q=0                    #Se define un contador q que empieza en ceros
        for j in range (1,i):  #Desde uno hasta i se revisa que:
            if i%j==0:         #Si se puede dividir sin residuos 
                q+=1           #Si se así el contador sube
        if q==1:               #Si el contador solo tiene como valor 1, 
            primo.append(i)    #Se agrega a la lista de primos 
    return primo               #Devuelve la lista de primos


x=(lista(int(sys.argv[1])))    #Se llama la función con el sys, diciendo que es entero y se llama la función lista
print (primos(x))              #Una vez ya se tiene la lista, se llama a imprimir el resultado de la función primos
