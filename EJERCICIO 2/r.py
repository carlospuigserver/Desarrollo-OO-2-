import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime
import random

# Clase Usuario
class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

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
                contrasena TEXT,
                estado TEXT,
                accion TEXT
            )
        ''')
        connection.commit()
        connection.close()

    def agregar_usuarios_aleatorios(self, cantidad):
        for _ in range(cantidad):
            nombre = f"Usuario{random.randint(1, 100)}"
            contrasena = f"Contraseña{random.randint(1, 100)}"
            estado = random.choice(["Aprobado", "Denegado"])
            self._agregar_usuario(nombre, contrasena, estado)

    def _agregar_usuario(self, nombre, contrasena, estado):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('INSERT OR IGNORE INTO usuarios (nombre, contrasena, estado) VALUES (?, ?, ?)', (nombre, contrasena, estado))
        connection.commit()
        connection.close()

    def esta_en_lista_blanca(self, usuario):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT contrasena, estado FROM usuarios WHERE nombre = ?', (usuario.nombre,))
        result = cursor.fetchone()
        connection.close()
        return result and result[1] == "Aprobado" and result[0] == usuario.contrasena

# Clase Subject (ABC)
class Subject(ABC):
    @abstractmethod
    def request(self, usuario, accion) -> None:
        pass

# Clase RealSubject Documento
class RealSubjectDocumento(Subject):
    def __init__(self, nombre):
        self._nombre = nombre
        self._registro = []

    def request(self, usuario, accion) -> None:
        if self._verificar_acceso(usuario):
            self._realizar_accion(accion)
            self.mostrar_info()

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} al documento {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def _realizar_accion(self, accion) -> None:
        self._registro.append(f"{usuario.nombre} ha {accion} el documento {self._nombre} en {datetime.now()}")

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

    def request(self, usuario, accion) -> None:
        if self._verificar_acceso(usuario):
            self._realizar_accion(accion)
            self.mostrar_info()

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} al enlace {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def _realizar_accion(self, accion) -> None:
        print(f"{usuario.nombre} ha {accion} el enlace {self._nombre} en {datetime.now()}")

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
        self._registro = []

    def request(self, usuario, accion) -> None:
        if self._verificar_acceso(usuario):
            self._realizar_accion(accion)
            self.mostrar_info()

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} a la carpeta {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def _realizar_accion(self, accion) -> None:
        self._registro.append(f"{usuario.nombre} ha {accion} la carpeta {self._nombre} en {datetime.now()}")

    def add(self, documento) -> None:
        self._documentos.append(documento)

    def mostrar_info(self):
        print(f"Información de la Carpeta {self._nombre}:")
        for documento in self._documentos:
            documento.mostrar_info()
        print(f"Registro de Acciones en la Carpeta {self._nombre}:")
        for registro in self._registro:
            print(registro)

# Clase Proxy
class Proxy(Subject):
    def __init__(self, real_subject: Subject, lista_blanca):
        self._real_subject = real_subject
        self._lista_blanca = lista_blanca

    def request(self, usuario) -> None:
        if self._lista_blanca.esta_en_lista_blanca(usuario):
            acciones = ["accedido", "modificado", "eliminado", "creado"]
            accion = random.choice(acciones)

            # Mover la acción denegada aquí para evitar errores
            connection = sqlite3.connect(self._lista_blanca.db_path)
            cursor = connection.cursor()
            cursor.execute('UPDATE usuarios SET accion = ? WHERE nombre = ?', (accion, usuario.nombre))
            connection.commit()
            connection.close()

            self._real_subject.request(usuario, accion)
        else:
            print(f"Acceso denegado a {usuario.nombre}. No está en la lista blanca.")
            # Añadir acción denegada en la base de datos
            connection = sqlite3.connect(self._lista_blanca.db_path)
            cursor = connection.cursor()
            cursor.execute('UPDATE usuarios SET accion = ? WHERE nombre = ?', ("Acceso denegado", usuario.nombre))
            connection.commit()
            connection.close()


if __name__ == "__main__":
    lista_blanca_sqlite = ListaBlancaSQLite()

    # Agregar usuarios aleatorios a la lista blanca o denegados
    lista_blanca_sqlite.agregar_usuarios_aleatorios(5)

    # Crear objetos Usuario con contraseñas
    connection = sqlite3.connect(lista_blanca_sqlite.db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nombre, contrasena, estado FROM usuarios')
    usuarios_bd = cursor.fetchall()
    connection.close()

    usuarios = [Usuario(nombre, contrasena) for nombre, contrasena, _ in usuarios_bd]

    documento1 = RealSubjectDocumento("Documento1")
    documento2 = RealSubjectDocumento("Documento2")
    documento3 = RealSubjectDocumento("Documento3")

    enlace1 = RealSubjectEnlace("Enlace1", "Documento1", "/ruta/ejemplo1")
    enlace2 = RealSubjectEnlace("Enlace2", "Documento2", "/ruta/ejemplo2")
    enlace3 = RealSubjectEnlace("Enlace3", "Documento3", "/ruta/ejemplo3")

    carpeta1 = RealSubjectCarpeta("Carpeta1", [documento1, enlace1])
    carpeta2 = RealSubjectCarpeta("Carpeta2", [documento2, enlace2])
    carpeta3 = RealSubjectCarpeta("Carpeta3", [documento3, enlace3])

    proxy_documento1 = Proxy(documento1, lista_blanca_sqlite)
    proxy_documento2 = Proxy(documento2, lista_blanca_sqlite)
    proxy_documento3 = Proxy(documento3, lista_blanca_sqlite)

    proxy_enlace1 = Proxy(enlace1, lista_blanca_sqlite)
    proxy_enlace2 = Proxy(enlace2, lista_blanca_sqlite)
    proxy_enlace3 = Proxy(enlace3, lista_blanca_sqlite)

    proxy_carpeta1 = Proxy(carpeta1, lista_blanca_sqlite)
    proxy_carpeta2 = Proxy(carpeta2, lista_blanca_sqlite)
    proxy_carpeta3 = Proxy(carpeta3, lista_blanca_sqlite)

    print("Acceso a través del Proxy con SQLite:")

    for usuario in usuarios:
        print(f"\nDocumento para {usuario.nombre}:")
        proxy_documento1.request(usuario)

        print(f"\nEnlace para {usuario.nombre}:")
        proxy_enlace1.request(usuario)

        print(f"\nCarpeta para {usuario.nombre}:")
        proxy_carpeta1.request(usuario)

        # Simular otras acciones con otros documentos, enlaces y carpetas
        # basándonos en la longitud del nombre del usuario para mayor variabilidad
        if len(usuario.nombre) % 2 == 0:
            proxy_documento2.request(usuario)
            proxy_enlace2.request(usuario)
            proxy_carpeta2.request(usuario)
        else:
            proxy_documento3.request(usuario)
            proxy_enlace3.request(usuario)
            proxy_carpeta3.request(usuario)
