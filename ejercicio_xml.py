from lxml import etree
doc = etree.parse('animales.xml')

#Ejercicio 1. Función que devuelve una lista con los nombres de todos los animales
print("\n 1. Función que devuelve una lista con los nombres de todos los animales")

def nombreanimales(doc):
    lista = doc.xpath('//nombre/text()')
    return lista

for prov in nombreanimales(doc):
    print(prov)
    
#Ejercicio 2.Contar los animales que esten en algun estado concreto.(Ej:en peligro).
print("\n 2.Contar los animales que esten en algun estado concreto.")

def contaranimales(doc,estado):
    count = doc.xpath('count(//animales[estado/text() = "%s"])'%estado)
    return count

print('''
Chuleta de estados:
-.en peligro
-.vulnerable
-.criticamente amenazado
-.preocupacion menor''')
estado=str(input("\nDime el estado que quieres contar: "))
print("Hay",contaranimales(doc,estado),"animales en esta situación.")

#Ejercicio 3.Buscar 'Datos Curiosos' de un animal indicado.
print("\n 3.Buscar 'Datos Curiosos' de un animal indicado.")

def buscarcurioso(doc,animal):
    curiosidad = doc.xpath('//animales[nombre/text() = "%s"]/datocurioso/text()'%animal)[0]
    return curiosidad

animal=str(input("\n Dime el nombre del animal que quieres conocer sus datos curiosos: "))
animal=animal.upper()
print("\n",buscarcurioso(doc,animal))
    

#Ejercicio 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias o mas.
print("\n 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias o mas.")

def numcrias(doc,cria):
    crias = doc.xpath('//animales[caracteristicas/reproduccion/numcrias/text() = "%i"]/nombre/text()'%cria)
    return crias

cria=int(input("\n ¿Cuantas crias puede tener el animal que estas buscando?   "))
print(numcrias(doc,cria))

#Ejercicio 5.Mostrar lista de caracteristicas, pide animal y una caracteristica y muestre el animal y su caracteristica.
print("\n 5.Comparar una caracteristica entre dos animales pedidos por teclado.")

def compara(doc):
    companimal = doc.xpath('//animales/[peso/text() = "%c"]'%peso)
    return companimal

animal1 =str(input("Dime el nombre del primer aninmal: "))
animal2 =str(input("Dime el nombre del segudno aninmal: "))
            
