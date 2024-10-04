# Pedir al usuario que introduzca entre 1 y 3 palabras
entrada = input("Introdueix entre 1 i 3 paraules separades per espais: ")

# Utilizar split() para dividir la cadena de texto en palabras
paraules = entrada.split()

# Validar que el número de palabras sea entre 1 y 3
if 1 <= len(paraules) <= 3:
    # Recorrer cada palabra y mostrar información
    for paraula in paraules:
        print(f"\nParaula: {paraula}")
        print(f"Nombre de caràcters: {len(paraula)}")
        print(f"Primer caràcter: {paraula[0]}")
        print(f"Últim caràcter: {paraula[-1]}")
else:
    print("Si us plau, introdueix entre 1 i 3 paraules.")