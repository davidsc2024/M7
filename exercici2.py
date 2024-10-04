var = float(input("Introduce la cantidad en euros: "))
var1 = int(input("Aplica un porcentaje de IVA.\n 4%, 10%, 21%"))
res = 0

while var1 == 4 or 10 or 21:
    print("El valor en euros introducido es: " + str(var) + "€")
    res = var + (var * (var1 / 100))
    print("El % de IVA introducido es ")
else:
    print("El valor introducido no es correcto.")