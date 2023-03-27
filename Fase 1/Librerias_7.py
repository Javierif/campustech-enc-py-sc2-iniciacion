from Clases_5 import Tropa, zerlingJson
import math


# Create object of class Zergling
zergling = Tropa(zerlingJson)

# Modify class definition
zergling.velocidad = math.ceil(zergling.velocidad * 1.5)

# Call methods of class Zergling
zergling.imprimir_informacion()
zergling.hacer_dano(3)
habilidades = zergling.obtener_habilidades()
print("Habilidades de Zergling:")
for habilidad in habilidades:
    print(habilidad)