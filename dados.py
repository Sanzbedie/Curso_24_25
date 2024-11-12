def jugar():
    # La persona tira el dado (3 veces)
    persona = sum(tirar_dado() for _ in range(3))
    print(f"Tú tiraste los dados y tus resultados fueron: {persona}")

    # La máquina tira el dado (3 veces)
    maquina = sum(tirar_dado() for _ in range(3))
    print(f"La máquina tiró los dados y sus resultados fueron: {maquina}")

    # Comparar los resultados
    if persona > maquina:
        print(f"¡Ganaste! Tu puntuación ({persona}) es mayor que la de la máquina ({maquina}).")
    elif persona < maquina:
        print(f"La máquina ganó. Su puntuación ({maquina}) es mayor que la tuya ({persona}).")
    else:
        print(f"¡Empate! Ambos tienen la misma puntuación: {persona}.")

if __name__ == "__main__":
    jugar()
