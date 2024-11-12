#Lea 5 números y devuelva el mayor, el menor, la media y la diferencia
#entre el mayor y el menor

def numeros():
    numero=input("Dame tu numero papito: ")
    mayor=numero
    menor=numero
    suma=0
    for cont in range(1,5):
        numero=input("Dame tu numero papito: ")
        if(numero>mayor):
            mayor=numero
        if(numero<menor):
            menor=numero
        suma=suma+numero
    print("Mayor: "+str(mayor))
    print("Menor: "+str(menor))
    promedio=float(suma)/cont
    print("Promedio: "+str(promedio))
    diferencia=mayor-menor
    print("Diferencia: "+str(diferencia))

numeros()
