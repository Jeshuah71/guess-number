#!/usr/bin/env python3
import random

def main():
    numero = random.randint(1, 100)
    intentos = 0

    print("🎲 Adivina el número entre 1 y 100")

    while True:
        try:
            guess = int(input("Tu intento: ").strip())
        except ValueError:
            print("❗ Por favor, ingresa un número válido.")
            continue

        intentos += 1
        if guess < numero:
            print("⬆️ Muy bajo.")
        elif guess > numero:
            print("⬇️ Muy alto.")
        else:
            print(f"🎉 ¡Correcto! Era {numero}. Lo lograste en {intentos} intentos.")
            break

if __name__ == "__main__":
    main()
