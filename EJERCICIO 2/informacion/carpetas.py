class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        self.accesos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def acceder(self, usuario):
        self.accesos.append((usuario, "Acceso"))
