def categorizacion(imp):
    categorizado=[]
    for element in imp:
        if element == "Harry Houdini" or element == "David Blaine" or element == "Teller":
            categorizado.append({"Nombre": element, "Categoria": "Mago"})
        elif element == "Newton" or element == "Hawking" or element == "Einstein":
            categorizado.append({"Nombre": element, "Categoria": "Cientifico"})
        else:
            categorizado.append({"Nombre": element, "Categoria": "Otro"})
    return categorizado

def hacer_grandioso(imp):
    modImp=imp
    for element in modImp:
        if element["Categoria"] == "Mago":
            element["Nombre"] = "El gran "+element["Nombre"]
    return modImp

def imprimir_nombres(lista):
    i=0
    while i < len(lista):
        print(lista[i]["Nombre"])
        i=i+1

def imprimir_magos(lista):
    for element in lista:
        if element["Categoria"] == "Mago":
            print(element["Nombre"])

def imprimir_cientificos(lista):
    for element in lista:
        if element["Categoria"] == "Cientifico":
            print(element["Nombre"])

def imprimir_otros(lista):
    for element in lista:
        if element["Categoria"] == "Otro":
            print(element["Nombre"])

lista=["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

categ = categorizacion(lista)

imprimir_nombres(categ)
print("----------")
imprimir_nombres(hacer_grandioso(categ))
print("----------")
imprimir_magos(hacer_grandioso(categ))
print("----------")
imprimir_cientificos(categ)
print("----------")
imprimir_otros(categ)