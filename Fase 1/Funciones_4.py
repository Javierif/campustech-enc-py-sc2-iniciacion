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


# Function that doesn't receive parameters
def imprimir_informacion():
    print("Nombre:", InventarioDeEjercito["nombre"])
    print("Raza:", InventarioDeEjercito["raza"])
    print("Salud:", InventarioDeEjercito["salud"])
    print("Daño:", InventarioDeEjercito["daño"])
    print("Velocidad:", InventarioDeEjercito["velocidad"])

# Function that receives parameters
def hacer_dano(cantidad):
    i = 0
    while i < cantidad:
        print("Zergling ha hecho daño.")
        i += 1

# Function that returns data
def obtener_habilidades():
    return InventarioDeEjercito["habilidades"]

# Call function that doesn't receive parameters
imprimir_informacion()

# Call function that receives parameters
hacer_dano(3)

# Call function that returns data
habilidades = obtener_habilidades()
print("Habilidades de Zergling:")
for habilidad in habilidades:
    print(habilidad)