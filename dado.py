#Vamos a hacer un ejercio que genere al azar un n�mero entre 1 y 6.
import random

def dado():
    respuesta=raw_input("�Quieres que tire un dado (S/N)? ")
    while(respuesta=="S"):
        tirada=random.random()
        print("Ha salido un "+str(tirada))
        respuesta=raw_input("�Quieres volver a tirar el dado (S/N)? ")
    print("Se acab� el juego")

dado()
