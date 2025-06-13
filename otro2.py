def validar_lista():
    while(True):
        lista=input("ingrese numeros separados por espacios: ")
        datos=lista.split()
        try:
            numeros=[]
            for elemento in datos:
                numeros.append(int(elemento))
            return numeros
        except ValueError:
            print("error debe ingresar numeros enteros")

def clasificar_pares_impares(numeros):
    pares=[]
    impares=[]
    for num in numeros:
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    return pares,impares
    