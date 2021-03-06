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
- En peligro
- Vulnerable
- Criticamente amenazado
- Preocupacion menor''')
estado=str(input("\nDime el estado que quieres contar: "))
estado=estado.lower()
print("Hay",contaranimales(doc,estado),"animales en esta situación.")

#Ejercicio 3.Buscar 'Datos Curiosos' de un animal indicado.
print("\n 3.Buscar 'Datos Curiosos' de un animal indicado.")

def buscarcurioso(doc,animal):
    curiosidad = doc.xpath('//animales[nombre/text() = "%s"]/datocurioso/text()'%animal)[0]
    return curiosidad

animal=str(input("\n Dime el nombre del animal que quieres conocer sus datos curiosos: "))
animal=animal.upper()
print("\n",buscarcurioso(doc,animal))
    

#Ejercicio 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias.
print("\n 4.Pedir el numero de crias maximo que puede tener una especie por camada y imprima todas las especies que hay con ese numero de crias.")

def numcrias(doc,cria):
    crias = doc.xpath('//animales[caracteristicas/reproduccion/numcrias/text() = "%i"]/nombre/text()'%cria)
    return crias

cria=int(input("\n ¿Cuantas crias como maximo puede tener el animal que estas buscando?   "))
print(numcrias(doc,cria))

#Ejercicio 5.Mostrar lista de caracteristicas, pide animal y una caracteristica y muestre el animal y su caracteristica.
print("\n 5.Mostrar lista de caracteristicas, pide animal y una caracteristica y muestre el animal y su caracteristica.")

def compara(doc,opcion):
    
    if opcion == "1":
        lista = doc.xpath('//nombre/text()')
        return lista

    if opcion == "2":
        animal=str(input("Dime el nombre de un aninmal: "))
        animal=animal.upper()
        tamaño = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/talla/longitud/text()'%animal)
        tamaño2 = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/talla/alza/text()'%animal)
        return str(tamaño)+" "+str(tamaño2)
    
    
    if opcion == "3":
        animal=str(input("Dime el nombre de un aninmal: "))
        animal=animal.upper()
        peso = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/peso/text()'%animal)
        return peso
    
    if opcion == "4":
        animal=str(input("Dime el nombre de un aninmal: "))
        animal=animal.upper()
        repro1 = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/reproduccion/MadurezSexual/text()'%animal)
        repro2 = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/reproduccion/celo/text()'%animal)
        repro3 = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/reproduccion/gestacion/text()'%animal)
        repro4 = doc.xpath('//animales[nombre/text() = "%s"]/caracteristicas/reproduccion/numcrias/text()'%animal)
        return "\n Madurez sexual: "+str(repro1)+"\n Celo: "+str(repro2)+"\n Gestacion: "+str(repro3)+"\n Número maximo de crías: "+str(repro4)
    
    
print('''
    1. Lista de animales
    2. Tamaño
    3. Peso
    4. Reproduccion
    ''')
opcion=str(input("Elige una opcion: "))
print(compara(doc,opcion))
            
