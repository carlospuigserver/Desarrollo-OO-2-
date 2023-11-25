class Documento:
    def __init__(self, nombre, tipo, tamaño, contenido):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.contenido = contenido
        self.accesos = []

    def acceder(self, usuario):
        self.accesos.append((usuario, "Acceso"))

    def modificar(self, usuario, nuevo_contenido):
        self.contenido = nuevo_contenido
        self.accesos.append((usuario, "Modificación"))
