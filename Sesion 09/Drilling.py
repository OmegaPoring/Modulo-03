def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def suremudi(a,b):
    return (suma(a,b), resta(a,b), multiplicacion(a,b), division(a,b))

selectorOp=input("Indique la operacion que desea realizar:\n1.-Suma\n2.-Resta\n3.-Multiplicaion\n4.-Division\n5.-Todas las anteriores\n")

if selectorOp == "1":
    a = int(input("Indique su primer valor:\n"))
    b = int(input("Indique su segundo valor:\n"))
    resultado = {"Suma": suma(a,b)}
    print(resultado)
elif selectorOp == "2":
    a = int(input("Indique su primer valor:\n"))
    b = int(input("Indique su segundo valor:\n"))
    resultado = {"Resta": resta(a,b)}
    print(resultado)
elif selectorOp == "3":
    a = int(input("Indique su primer valor:\n"))
    b = int(input("Indique su segundo valor:\n"))
    resultado = {"Multiplicacion": multiplicacion(a,b)}
    print(resultado)
elif selectorOp == "4":
    a = int(input("Indique su primer valor:\n"))
    b = int(input("Indique su segundo valor:\n"))
    resultado = {"Division": division(a,b)}
    print(resultado)
elif selectorOp == "5":
    a = int(input("Indique su primer valor:\n"))
    b = int(input("Indique su segundo valor:\n"))
    resultado = {"Suma": suremudi(a,b)[0], "Resta": suremudi(a,b)[1], "Multiplicacion": suremudi(a,b)[2], "Division": suremudi(a,b)[3]}
    print(resultado)