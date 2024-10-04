import random

# Escollim un número aleatori entre 1 i 100
numero_secret = random.randint(1, 100)
intents = 0  # Inicialitzem el comptador d'intents

print("Endevina el número entre 1 i 100!")

while True:
    # Demanar a l'usuari que introdueixi un número
    intent = int(input("Introdueix un número: "))
    intents += 1  # Incrementem el nombre d'intents

    # Comprovem si l'intent és més gran, més petit o igual que el número secret
    if intent < numero_secret:
        print("El número és més gran.")
    elif intent > numero_secret:
        print("El número és més petit.")
    else:
        print(f"Felicitats! Has encertat el número {numero_secret} en {intents} intents.")
        break  # Acabem el joc quan l'usuari encerta