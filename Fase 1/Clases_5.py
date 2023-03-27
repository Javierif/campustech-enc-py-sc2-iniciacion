# Class definition
class Tropa:
    def __init__(self, datos):
        self.nombre = datos["nombre"]
        self.raza = datos["raza"]
        self.salud = datos["salud"]
        self.daño = datos["daño"]
        self.velocidad = datos["velocidad"]
        self.habilidades = datos["habilidades"]

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Raza:", self.raza)
        print("Salud:", self.salud)
        print("Daño:", self.daño)
        print("Velocidad:", self.velocidad)

    def hacer_dano(self, cantidad):
        i = 0
        while i < cantidad:
            print(self.nombre," ha hecho daño.")
            i += 1

    def obtener_habilidades(self):
        return self.habilidades


zerlingJson = {
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


# Create object of class Zergling
zergling = Tropa(zerlingJson)

# Call methods of class Zergling
zergling.imprimir_informacion()
zergling.hacer_dano(3)
habilidades = zergling.obtener_habilidades()
print("Habilidades de Zergling:")
for habilidad in habilidades:
    print(habilidad)