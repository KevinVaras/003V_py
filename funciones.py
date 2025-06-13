def mostrarlistas(lista):
    par=[]
    impar=[]
    for i in lista:
        if(i%2==0):
            par.append(i)
        else:
            impar.append(i)
    print("numeros pares: ",par)
    print("numeros impares: ", impar)



def validarLista(lista):
    try:
        for num in lista:
            posicion=lista.index(num)
            lista[posicion]=int(num)
        mostrarlistas(lista)
        return True
    except ValueError:
        print("ERROR la lista debe ser de numeros enteros")
        print("porfavor vuelva a ingresar la lista")
        return False



