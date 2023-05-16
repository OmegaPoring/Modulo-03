lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for element in lista:
    if element[0] != 0:
        i=0
        while i < len(element):
            if element[i] != 0:
                print(element[i])
            i=i+1