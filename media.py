#Problema con los decimales

#Leo cinco n�meros y me dice la media de los cinco
def media_numeros():
    #definimos una variable ACUMULADORA, es decir una variable que recoge la suma
    #de los n�meros hasta el momento
    suma=0 #inicializar la variable.
    for cont in range(1,6):
        numero=int(input("Dime un n�mero entero mayor que cero: "))
        suma=suma+numero #suma=+suma
       
    media=suma/5.0  
    print("La media vale  "+str(media))

media_numeros()
