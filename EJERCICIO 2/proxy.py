import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime
import random

# Clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase ListaBlanca (LogIn) con SQLite
class ListaBlancaSQLite:
    def __init__(self, db_path="lista_blanca.sql"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT UNIQUE,
                estado TEXT
            )
        ''')
        connection.commit()
        connection.close()

    def agregar_usuarios_aleatorios(self, cantidad):
        for _ in range(cantidad):
            nombre = f"Usuario{random.randint(1, 100)}"
            estado = random.choice(["Aprobado", "Denegado"])
            self._agregar_usuario(nombre, estado)

    def _agregar_usuario(self, nombre, estado):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('INSERT OR IGNORE INTO usuarios (nombre, estado) VALUES (?, ?)', (nombre, estado))
        connection.commit()
        connection.close()

    def esta_en_lista_blanca(self, usuario):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT estado FROM usuarios WHERE nombre = ?', (usuario.nombre,))
        result = cursor.fetchone()
        connection.close()
        return result == ("Aprobado",)

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


if __name__ == "__main__":
    lista_blanca_sqlite = ListaBlancaSQLite()

    # Agregar usuarios aleatorios a la lista blanca o denegados
    lista_blanca_sqlite.agregar_usuarios_aleatorios(5)

    documento = RealSubjectDocumento("Documento1")
    proxy_documento = Proxy(documento, lista_blanca_sqlite)

    enlace = RealSubjectEnlace("Enlace1", "Documento1", "/ruta/ejemplo")
    proxy_enlace = Proxy(enlace, lista_blanca_sqlite)

    carpeta = RealSubjectCarpeta("Carpeta1", [documento, enlace])
    proxy_carpeta = Proxy(carpeta, lista_blanca_sqlite)

    print("Acceso a través del Proxy con SQLite:")
    
    # Obtener usuarios de la base de datos y verificar acceso
    connection = sqlite3.connect(lista_blanca_sqlite.db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nombre, estado FROM usuarios')
    usuarios_bd = cursor.fetchall()
    connection.close()

    for usuario_nombre, usuario_estado in usuarios_bd:
        usuario = Usuario(usuario_nombre)
        
        print(f"\nDocumento para {usuario.nombre}:")
        proxy_documento.request(usuario)

        print(f"\nEnlace para {usuario.nombre}:")
        proxy_enlace.request(usuario)

        print(f"\nCarpeta para {usuario.nombre}:")
        proxy_carpeta.request(usuario)
