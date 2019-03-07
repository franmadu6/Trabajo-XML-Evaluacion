def nombreanimales(doc):
    lista = doc.xpath('///nombre/text()')
    return lista

from lxml import etree
doc = etree.parse('animales.xml')

#Ejercicio 1. Función que devuelve una lista con los nombres de todos los animales

for prov in nombreanimales(doc):
    print(prov)
