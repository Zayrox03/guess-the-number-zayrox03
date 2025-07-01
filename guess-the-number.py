import random
import sys

while True:
    secreto = random.randint(1, 100)
    intento = 0

    while True:
        try:
            print("--¡Adivina el numero!--")
            adivina = int(input("Adivina un numero del 1 al 100: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if not (1 <= adivina <= 100):
            print("Numero fuera de rango.")
            continue

        intento += 1

        if secreto > adivina:
            print("Es mayor, intenta un numero mas bajo")
        elif secreto < adivina:
            print("Es menor, intenta un numero mas alto")
        else:
            print(f"FELICIDADES! Adivinaste el número {secreto} en {intento} intentos.")
            break  

    opcion = input("¿Quieres jugar otra vez? (s/n): ")
    if opcion.lower() != "s":
        print("Gracias por jugar!")
        sys.exit()
        
#CODE MADE BY Zayrox03!