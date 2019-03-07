def nombreanimales(doc):
    lista = doc.xpath('///nombre/text()')
    return lista

def contaranimales(doc,estado):
    count = doc.xpath('count(/mamíferos[//estado/text() = "%s"])'%estado)
    return count

from lxml import etree
doc = etree.parse('animales.xml')

#Ejercicio 1. Función que devuelve una lista con los nombres de todos los animales

for prov in nombreanimales(doc):
    print(prov)
    
#Ejercicio 2.Contar los animales que esten en algun estado concreto.(Ej:en peligro).

for prov2 in contaranimales(dos,estado):
    print(prov2)

#Ejercicio 3.Buscar una palabra clave en "Datos Curiosos".



#Ejercicio 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias o mas.



#Ejercicio 5.Comparar una caracteristica entre dos animales pedidos por teclado.


