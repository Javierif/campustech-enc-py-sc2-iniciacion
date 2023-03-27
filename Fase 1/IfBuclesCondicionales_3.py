InventarioDeEjercito = {
    "nombre": "Zergling",
    "raza": "Zerg",
    "salud": 35,
    "daño": 5,
    "velocidad": 2.95,
    "habilidades": ["Ataque rápido", "Correr"],
    "información adicional": {
        "nombre científico": "Zerglingus velocitas",
        "hábitat": "Planetas Zerg"
    }
}



# If statement
if InventarioDeEjercito["salud"] > 50:
    print("La salud de Zergling es mayor que 50.")
else:
    print("La salud de Zergling es menor o igual que 50.")

# For loop
for habilidad in InventarioDeEjercito["habilidades"]:
    print("Zergling puede:", habilidad)

# While loop
i = 0
while i < InventarioDeEjercito["daño"]:
    print("Zergling ha hecho daño.")
    i += 1

# Conditional statement
if InventarioDeEjercito["raza"] == "Zerg":
    print("Zergling es una unidad Zerg.")
else:
    print("Zergling no es una unidad Zerg.")