import random

# Lanzar dado
def tirar_dado():
    return random.randint(1, 6)

# Marcadores
def jugar():
    puntaje_jugador = 0
    puntaje_maquina = 0

    nombre_jugador = raw_input("Ingresa tu nombre: ")

    #Tres rondas de lanzamientos
    for ronda in range(1, 4):
        print "\n Ronda", ronda

        # Turno J
        lanzamiento_jugador = tirar_dado()
        puntaje_jugador += lanzamiento_jugador
        print nombre_jugador, "lanzó:", lanzamiento_jugador

        # Turno M
        lanzamiento_maquina = tirar_dado()
        puntaje_maquina += lanzamiento_maquina
        print "Máquina lanzó:", lanzamiento_maquina

    # Puntuacion final
    print "\n JuaResultados finales"
    print "Puntaje total de", nombre_jugador + ":", puntaje_jugador
    print "Puntaje total de Máquina:", puntaje_maquina

    # Ganador
    if puntaje_jugador > puntaje_maquina:
        print "Ganador", nombre_jugador

    elif puntaje_maquina > puntaje_jugador:
        print "Gana la maquina."

    else:
        print "Empate."

# Iniciar el juego
jugar()
