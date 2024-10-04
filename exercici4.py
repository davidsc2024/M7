var = int(input("Introduce el primer valor: "))
var1 = int(input("Introduce el segundo valor: "))

suma = var + var1
multi = var * var1
div = var / var1
resta = var - var1

print("La suma de estos numeros es: " + str(suma) +
      "\nMultiplicación es: " + str(multi) +
      "\nDivisión: " + str(div) +
      "\nResta: " + str(resta))

print(f"La suma es {suma}")