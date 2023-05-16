lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

def excepciones(lista):
    nueva_lista = []
    for element in lista:
        if element[0] != 0:
            i=0
            while i < len(element):
                if element[i] == 0:
                    del element[i]
                i=i+1
            nueva_lista.append(element)
    return nueva_lista

def diccionarios(lista):
    nueva_lista = []
    indices = ["A", "B", "C", "D"]
    i=0
    while i < len(lista):
        nueva_lista.append({indices[i]: lista[i]})
        i=i+1
    return nueva_lista
        

print(excepciones(lista))
print(diccionarios(excepciones(lista)))