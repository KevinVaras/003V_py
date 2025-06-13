import funciones as fn


while(True):
    num=input("ingrese la lista de numeros separados por un espacio: ")
    listanumeros=num.split()
    valido=fn.validarLista(listanumeros)
    if(valido):
        break
# ______________para guardar en la lista sin .split()________________________________________________________________________________
'''
listaN=[]
num =input("ingrese lista de numeros separados por espacios: ")
nuevo=""
for i in range (len(num)):
    if(num[i] !=" "):
        nuevo=nuevo + num[i]
    else:
        listaN.append(nuevo)
        nuevo=""
if(nuevo!=""):
    listaN.append(nuevo)
print(listaN)
'''