
#Leo cinco n�meros y me devuelve el mayor, el menor, la suma de todos, la media
#y la resta entre el mayor y el menor
def media_numeros():
    #definimos una variable ACUMULADORA, es decir una variable que recoge la suma
    #de los n�meros hasta el momento
    suma=0 #inicializar la variable.
    for cont in range(1,6):
        numero=int(input("Dime un n�mero entero mayor que cero: "))
        suma=suma+numero #suma=+suma
       
    media=float(suma)/cont #conversi�n forzada de tipos
    print("La media vale  "+str(media))

propiedades_numeros()
