# Demanar a l'usuari que introdueixi dues paraules
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

# Assegurar-nos que les dues paraules tenen almenys 2 caràcters
if len(paraula1) >= 2 and len(paraula2) >= 2:
    # Intercanviem els dos primers caràcters de cada paraula
    nova_paraula1 = paraula2[:2] + paraula1[2:]
    nova_paraula2 = paraula1[:2] + paraula2[2:]
    
    # Mostrem el resultat per pantalla
    print(f"Les noves paraules són: {nova_paraula1} {nova_paraula2}")
else:
    print("Les dues paraules han de tenir almenys 2 caràcters.")