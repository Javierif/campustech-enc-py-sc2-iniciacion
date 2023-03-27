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


print("Nombre:" + InventarioDeEjercito["nombre"])

#print habilidad 0
print("Habilidad 0:" + InventarioDeEjercito["habilidades"][0])

print("nombre científico:" + InventarioDeEjercito["información adicional"]["nombre científico"])


InventarioDeEjercito["nombre"] = "Zergling 2.0"

print("Nombre actual:" +InventarioDeEjercito["nombre"])

#Añadir un nuevo atributo

InventarioDeEjercito["costo"] = 50

print("Costo:" + str(InventarioDeEjercito["costo"]))

#Eliminar un atributo
InventarioDeEjercito.pop("costo")

print(InventarioDeEjercito)