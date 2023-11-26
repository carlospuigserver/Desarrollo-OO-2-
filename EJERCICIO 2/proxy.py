from abc import ABC, abstractmethod
from datetime import datetime

# Clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase ListaBlanca (LogIn)
class ListaBlanca:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def esta_en_lista_blanca(self, usuario):
        return usuario in self.usuarios

# Clase Subject (ABC)
class Subject(ABC):
    @abstractmethod
    def request(self, usuario) -> None:
        pass

# Clase RealSubject Documento
class RealSubjectDocumento(Subject):
    def __init__(self, nombre):
        self._nombre = nombre
        self._registro = []

    def request(self, usuario) -> None:
        if self._verificar_acceso(usuario):
            self._registro.append(f"Acceso al documento {self._nombre} registrado en {datetime.now()}")
            self.mostrar_info()

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} al documento {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def mostrar_info(self):
        print(f"Información del Documento {self._nombre}:")
        print("Nombre: Documento1")
        print("Tipo: Texto")
        print("Tamaño: 1024")
        print("Contenido: Contenido de ejemplo")
        print("Ruta: /ruta/ejemplo")

# Clase RealSubject Enlace
class RealSubjectEnlace(Subject):
    def __init__(self, nombre, destino, ruta_destino=None):
        self._nombre = nombre
        self._destino = destino
        self._ruta_destino = ruta_destino

    def request(self, usuario) -> None:
        if self._verificar_acceso(usuario):
            self.mostrar_info()

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} al enlace {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def mostrar_info(self):
        print(f"Información del Enlace {self._nombre}:")
        print(f"Nombre: Enlace1")
        print(f"Destino: {self._destino}")
        print(f"Ruta Destino: {self._ruta_destino}")

# Clase RealSubject Carpeta
class RealSubjectCarpeta(Subject):
    def __init__(self, nombre, documentos=None):
        self._nombre = nombre
        self._documentos = documentos or []

    def request(self, usuario) -> None:
        if self._verificar_acceso(usuario):
            self.mostrar_info()

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} a la carpeta {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def add(self, documento) -> None:
        self._documentos.append(documento)

    def mostrar_info(self):
        print(f"Información de la Carpeta {self._nombre}:")
        for documento in self._documentos:
            documento.mostrar_info()

# Clase Proxy
class Proxy(Subject):
    def __init__(self, real_subject: Subject, lista_blanca):
        self._real_subject = real_subject
        self._lista_blanca = lista_blanca

    def request(self, usuario) -> None:
        if self._lista_blanca.esta_en_lista_blanca(usuario):
            self._real_subject.request(usuario)
        else:
            print(f"Acceso denegado a {usuario.nombre}. No está en la lista blanca.")

# Código de prueba
if __name__ == "__main__":
    usuario1 = Usuario("Usuario1")
    usuario2 = Usuario("Usuario2")

    lista_blanca = ListaBlanca()
    lista_blanca.agregar_usuario(usuario1)

    documento = RealSubjectDocumento("Documento1")
    proxy_documento = Proxy(documento, lista_blanca)

    enlace = RealSubjectEnlace("Enlace1", "Documento1", "/ruta/ejemplo")
    proxy_enlace = Proxy(enlace, lista_blanca)

    carpeta = RealSubjectCarpeta("Carpeta1", [documento, enlace])
    proxy_carpeta = Proxy(carpeta, lista_blanca)

    print("Acceso a través del Proxy:")
    print("Documento:")
    proxy_documento.request(usuario1)
    proxy_documento.request(usuario2)  # Intento de acceso por Usuario2

    print("\nEnlace:")
    proxy_enlace.request(usuario1)
    proxy_enlace.request(usuario2)  # Intento de acceso por Usuario2

    print("\nCarpeta:")
    proxy_carpeta.request(usuario1)
    proxy_carpeta.request(usuario2)  # Intento de acceso por Usuario2
