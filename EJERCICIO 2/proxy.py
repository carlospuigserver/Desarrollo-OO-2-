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
        cursor.execute('INSERT OR IGNORE INTO usuarios (nombre, contrasena, estado, accion) VALUES (?, ?, ?, ?)',
                       (nombre, contrasena, estado, ''))
        connection.commit()
        connection.close()

    def esta_en_lista_blanca(self, usuario):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT contrasena, estado FROM usuarios WHERE nombre = ?', (usuario.nombre,))
        result = cursor.fetchone()
        connection.close()
        return result and result[1] == "Aprobado" and result[0] == usuario.contrasena

    def registrar_accion(self, usuario, accion):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('UPDATE usuarios SET accion = ? WHERE nombre = ?', (accion, usuario.nombre))
        connection.commit()
        connection.close()

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
            acciones_posibles = ['acceder', 'modificar', 'eliminar', 'agregar']
            accion_elegida = random.choice(acciones_posibles)
            lista_blanca_sqlite.registrar_accion(usuario, f'Ha {accion_elegida} el documento {self._nombre}.')

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} al documento {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def mostrar_info(self):
        print(f"Información del Documento {self._nombre}:")
        print("Nombre:", self._nombre)
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
            acciones_posibles = ['acceder', 'modificar', 'eliminar', 'agregar']
            accion_elegida = random.choice(acciones_posibles)
            lista_blanca_sqlite.registrar_accion(usuario, f'Ha {accion_elegida} el enlace {self._nombre}.')

    def _verificar_acceso(self, usuario) -> bool:
        print(f"Proxy: Verificando acceso de {usuario.nombre} al enlace {self._nombre}.")
        return True  # Implementa tu lógica de verificación de lista blanca aquí

    def mostrar_info(self):
        print(f"Información del Enlace {self._nombre}:")
        print(f"Nombre: {self._nombre}")
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
            acciones_posibles = ['acceder', 'modificar', 'eliminar', 'agregar']
            accion_elegida = random.choice(acciones_posibles)
            lista_blanca_sqlite.registrar_accion(usuario, f'Ha {accion_elegida} la carpeta {self._nombre}.')

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

    # Crear objetos Usuario con contraseñas
    connection = sqlite3.connect(lista_blanca_sqlite.db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nombre, contrasena, estado FROM usuarios')
    usuarios_bd = cursor.fetchall()
    connection.close()

    usuarios = [Usuario(nombre, contrasena) for nombre, contrasena, estado in usuarios_bd if estado == 'Aprobado']

    # Crear objetos aleatorios (documentos, enlaces y carpetas)
    objetos = []
    for _ in range(5):  # Puedes ajustar el número de objetos a crear
        tipo_objeto = random.choice(['Documento', 'Enlace', 'Carpeta'])
        nombre_objeto = f"{tipo_objeto}{random.randint(1, 100)}"
        if tipo_objeto == 'Documento':
            objetos.append(RealSubjectDocumento(nombre_objeto))
        elif tipo_objeto == 'Enlace':
            destino_objeto = f"Documento{random.randint(1, 100)}"
            ruta_destino_objeto = f"/ruta/ejemplo{random.randint(1, 100)}"
            objetos.append(RealSubjectEnlace(nombre_objeto, destino_objeto, ruta_destino_objeto))
        elif tipo_objeto == 'Carpeta':
            documentos_objeto = [RealSubjectDocumento(f"Documento{random.randint(1, 100)}") for _ in range(3)]  # Puedes ajustar el número de documentos
            objetos.append(RealSubjectCarpeta(nombre_objeto, documentos_objeto))

    # Crear proxies para los objetos
    proxies = [Proxy(objeto, lista_blanca_sqlite) for objeto in objetos]

    print("Acceso a través del Proxy con SQLite:")

    for usuario in usuarios:
        print(f"\nAcciones para {usuario.nombre}:")
        for _ in range(3):  # Puedes ajustar el número de acciones
            proxy = random.choice(proxies)
            proxy.request(usuario)
