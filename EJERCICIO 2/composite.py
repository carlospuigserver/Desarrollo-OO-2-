from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    @property
    def parent(self) -> Componente:
        return self._parent

    @parent.setter
    def parent(self, parent: Componente):
        self._parent = parent

    def add(self, componente: Componente) -> None:
        pass

    def remove(self, componente: Componente) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


def client_code(componente: Componente) -> None:
    print(f"Resultado: {componente.operation()}", end="")


class Documento(Componente):
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

    def operation(self) -> str:
        return f"Documento {self.tipo} {self.nombre}"


class DocumentoAudio(Documento):
    def __init__(self, nombre, tamaño, contenido, duracion):
        super().__init__(nombre, "Audio", tamaño, contenido)
        self.duracion = duracion

    def operation(self) -> str:
        return f"Documento Audio {self.nombre} ({self.duracion} segundos)"


class Enlace(Componente):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
        self.accesos = []

    def acceder(self, usuario):
        self.accesos.append((usuario, "Acceso"))

    def operation(self) -> str:
        return f"Enlace {self.nombre}"


class Carpeta(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos: List[Componente] = []
        self.accesos = []

    def add(self, componente: Componente) -> None:
        self.elementos.append(componente)
        componente.parent = self

    def remove(self, componente: Componente) -> None:
        self.elementos.remove(componente)
        componente.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [elemento.operation() for elemento in self.elementos]
        return f"Carpeta {self.nombre} ({', '.join(results)})"


if __name__ == "__main__":
    documento_texto = Documento("Texto1", "Texto", 1024, "Contenido de texto")
    documento_imagen = Documento("Imagen1", "Imagen", 2048, "Contenido de imagen")
    documento_video = Documento("Video1", "Video", 4096, "Contenido de video")
    documento_audio = DocumentoAudio("Audio1", 512, "Contenido de audio", 120)

    enlace_1 = Enlace("Enlace1", "Destino1")
    enlace_2 = Enlace("Enlace2", "Destino2")

    carpeta_1 = Carpeta("Carpeta1")
    carpeta_1.add(documento_texto)
    carpeta_1.add(documento_imagen)

    carpeta_2 = Carpeta("Carpeta2")
    carpeta_2.add(documento_video)
    carpeta_2.add(enlace_1)
    carpeta_2.add(enlace_2)

    carpeta_3 = Carpeta("Carpeta3")
    carpeta_3.add(documento_audio)

    print("Cliente: Ahora tengo una estructura compuesta.")
    while True:
        try:
            opcion = int(input("Seleccione la carpeta (1, 2 o 3): "))
            if opcion == 1:
                client_code(carpeta_1)
                break
            elif opcion == 2:
                client_code(carpeta_2)
                break
            elif opcion == 3:
                client_code(carpeta_3)
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
