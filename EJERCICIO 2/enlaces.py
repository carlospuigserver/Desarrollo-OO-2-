class Enlace:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
        self.accesos = []

    def acceder(self, usuario):
        self.accesos.append((usuario, "Acceso"))
