def jugar():
    # La persona tira el dado (3 veces)
    persona = sum(tirar_dado() for _ in range(3))
    print(f"T� tiraste los dados y tus resultados fueron: {persona}")

    # La m�quina tira el dado (3 veces)
    maquina = sum(tirar_dado() for _ in range(3))
    print(f"La m�quina tir� los dados y sus resultados fueron: {maquina}")

    # Comparar los resultados
    if persona > maquina:
        print(f"�Ganaste! Tu puntuaci�n ({persona}) es mayor que la de la m�quina ({maquina}).")
    elif persona < maquina:
        print(f"La m�quina gan�. Su puntuaci�n ({maquina}) es mayor que la tuya ({persona}).")
    else:
        print(f"�Empate! Ambos tienen la misma puntuaci�n: {persona}.")

if __name__ == "__main__":
    jugar()
