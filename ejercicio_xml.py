def nombreanimales(doc):
    lista = doc.xpath('//nombre/text()')
    return lista

def contaranimales(doc,estado):
    count = doc.xpath('count(//animales[estado/text() = "%s"])'%estado)
    return count

def buscarpalabras(doc,busqueda):
    search = doc.xpath("//animales/[datocurioso/text() = '%a'] " %busqueda)
    return search

def numcrias(doc):
    crias = doc.xpath('count(//animales/[numcrias/text() = "%b""])'%cria)
    return crias

from lxml import etree
doc = etree.parse('animales.xml')

#Ejercicio 1. Función que devuelve una lista con los nombres de todos los animales
print("\n 1. Función que devuelve una lista con los nombres de todos los animales")
for prov in nombreanimales(doc):
    print(prov)
    
#Ejercicio 2.Contar los animales que esten en algun estado concreto.(Ej:en peligro).
print("\n 2.Contar los animales que esten en algun estado concreto.")

print('''
Chuleta de estados:
-.en peligro
-.vulnerable
-.criticamente amenazado
-.preocupacion menor''')
estado=str(input("\nDime el estado que quieres contar: "))
print("Hay",contaranimales(doc,estado),"animales en esta situación.")

#Ejercicio 3.Buscar una palabra clave en "Datos Curiosos".
print("\n 3.Buscar una palabra clave en 'Datos Curiosos'.")
busqueda=str(input("Dime que palabra quieres buscar: "))

while True:
    if busqueda == doc.xpath('count(//animales/datocurioso/text())'):
        print(buscarpalabras(doc,busqueda))
    else:
        print("Esa palabra no se encuentra, prueba de nuevo.")
    break
        

#Ejercicio 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias o mas.
print("\n 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias o mas.")

cria=int(input("\n ¿Cuantas crias puede tener el animal que estas buscando?   "))
for listacrias in numcrias(doc):
    print(listacrias)

#Ejercicio 5.Comparar una caracteristica entre dos animales pedidos por teclado.
print("\n 5.Comparar una caracteristica entre dos animales pedidos por teclado.")

animal1=str(input("Dime el nombre del primer aninmal: ")
animal2=str(input("Dime el nombre del segudno aninmal: ")
            
