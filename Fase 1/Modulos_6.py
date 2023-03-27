from Clases_5 import Tropa, zerlingJson


# Create object of class Zergling
zergling = Tropa(zerlingJson)

# Call methods of class Zergling
zergling.imprimir_informacion()
zergling.hacer_dano(3)
habilidades = zergling.obtener_habilidades()
print("Habilidades de Zergling:")
for habilidad in habilidades:
    print(habilidad)