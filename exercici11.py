# Demanar a l'usuari que introdueixi un número
numero = int(input("Introdueix un número per mostrar la seva taula de multiplicar: "))

# Mostrar la taula de multiplicar
print(f"Taula de multiplicar de {numero}:")
for i in range(1, 11):  # Iterem del 1 al 10
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")