# documentos.py

class Documento:
    def __init__(self, nombre, tipo, tamaño, contenido, ruta=None):
        self._nombre = nombre
        self._tipo = tipo
        self._tamaño = tamaño
        self._contenido = contenido
        self._ruta = ruta

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto.")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if isinstance(nuevo_tipo, str):
            self._tipo = nuevo_tipo
        else:
            raise ValueError("El tipo debe ser una cadena de texto.")

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, nuevo_tamaño):
        if isinstance(nuevo_tamaño, (int, float)):
            self._tamaño = nuevo_tamaño
        else:
            raise ValueError("El tamaño debe ser un número.")

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        if isinstance(nuevo_contenido, str):
            self._contenido = nuevo_contenido
        else:
            raise ValueError("El contenido debe ser una cadena de texto.")

    @property
    def ruta(self):
        return self._ruta

    @ruta.setter
    def ruta(self, nueva_ruta):
        self._ruta = nueva_ruta

    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nTipo: {self.tipo}\nTamaño: {self.tamaño}\nContenido: {self.contenido}\nRuta: {self.ruta}"

class Carpeta:
    def __init__(self, nombre, documentos=None):
        self._nombre = nombre
        self._documentos = documentos or []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre de la carpeta debe ser una cadena de texto.")

    @property
    def documentos(self):
        return self._documentos

    @documentos.setter
    def documentos(self, nuevos_documentos):
        self._documentos = nuevos_documentos

    def agregar_documento(self, documento):
        self._documentos.append(documento)

    def tamaño_total(self):
        return sum(documento.tamaño for documento in self._documentos)

    def mostrar_info(self):
        info = f"Información de la Carpeta:\nNombre: {self.nombre}\nDocumentos:\n"
        for documento in self._documentos:
            info += f" - {documento.mostrar_info()}\n"
        info += f"Tamaño Total: {self.tamaño_total()}\n"
        return info

# Ejemplo de uso
documento_ejemplo = Documento("Documento1", "Texto", 1024, "Contenido de ejemplo", "ruta/ejemplo")
documento_ejemplo2 = Documento("Documento2", "Imagen", 2048, "Contenido de imagen", "ruta/ejemplo2")
carpeta_ejemplo = Carpeta("Carpeta1", [documento_ejemplo, documento_ejemplo2])

# Mostrar información de la carpeta
print(carpeta_ejemplo.mostrar_info())
