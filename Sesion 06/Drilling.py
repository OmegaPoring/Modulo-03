val1=input("Ingrese el primer número:\n")
val2=input("Ingrese el segundo número:\n")
val3=input("Ingrese el tercer número:\n")

listaDesordenada=[val1, val2, val3]
# listaDesordenada.sort(reverse=True) <--- podria hacerlo asi pero
#                                         me imagino que no se vale

listaOrdenada = []

for val in listaDesordenada:
    if val1 > val2 and val1 > val3 and val2 > val3:
        listaOrdenada = [val1, val2, val3]
    elif val1 > val2 and val1 > val3 and val3 > val2:
        listaOrdenada = [val1, val3, val2]
    elif val2 > val1 and val2 > val3 and val1 > val3:
        listaOrdenada = [val2, val1, val3]
    elif val2 > val1 and val2 > val3 and val3 > val1:
        listaOrdenada = [val2, val3, val1]
    elif val3 > val1 and val3 > val2 and val1 > val2:
        listaOrdenada = [val3, val1, val2]
    elif val3 > val1 and val3 > val2 and val2 > val1:
        listaOrdenada = [val3, val2, val1]
    elif val1 == val2 and val1 > val3:
        listaOrdenada = [val1, val2, val3]
    elif val1 == val2 and val1 < val3:
        listaOrdenada = [val3, val1, val2]
    elif val2 == val3 and val1 > val2:
        listaOrdenada = [val1, val2, val3]
    elif val2 == val3 and val1 < val2:
        listaOrdenada = [val2, val3, val1]
    elif val3 == val1 and val3 > val2:
        listaOrdenada = [val3, val1, val2]
    elif val3 == val1 and val3 < val2:
        listaOrdenada = [val2, val3, val1]
    elif val1 == val2 == val3:
        listaOrdenada = [val1, val2, val3]
        
                
print(listaOrdenada)