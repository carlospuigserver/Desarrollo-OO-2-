from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Documento(Component):
    def __init__(self, nombre, tipo, tamaño, contenido, ruta=None):
        self._nombre = nombre
        self._tipo = tipo
        self._tamaño = tamaño
        self._contenido = contenido
        self._ruta = ruta

    def operation(self) -> str:
        return f"Documento({self._nombre}, Tipo: {self._tipo}, Tamaño: {self._tamaño}, Contenido: {self._contenido}, Ruta: {self._ruta})"

    def mostrar_info(self):
        return f"Información del Documento:\n{self.operation()}"


class Enlace(Component):
    def __init__(self, nombre, destino, ruta_destino=None):
        self._nombre = nombre
        self._destino = destino
        self._ruta_destino = ruta_destino

    def add(self, component: Component) -> None:
        print("No se pueden agregar componentes a un enlace.")

    def remove(self, component: Component) -> None:
        print("No se pueden quitar componentes de un enlace.")

    def operation(self) -> str:
        return f"Enlace({self._nombre}, Destino: {self._destino})"

    def mostrar_info(self):
        return f"Información del Enlace:\n{self.operation()}"


class Carpeta(Component):
    def __init__(self, nombre, documentos=None):
        self._nombre = nombre
        self._documentos = documentos or []

    def add(self, component: Component) -> None:
        self._documentos.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._documentos.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [child.operation() for child in self._documentos]
        return f"Carpeta({self._nombre}, {', '.join(results)})"

    def mostrar_info(self):
        return f"Información de la Carpeta:\n{self.operation()}"


def client_code(component: Component) -> None:
    print(component.mostrar_info())


if __name__ == "__main__":
    documento1 = Documento("Documento1", "Texto", 1024, "Contenido de ejemplo", "/ruta/ejemplo")
    enlace1 = Enlace("Enlace1", "Documento1")
    carpeta1 = Carpeta("Carpeta1", [documento1, enlace1])

    while True:
        print("\nSeleccione una opción:")
        print("1. Ver información de un documento")
        print("2. Ver información de un enlace")
        print("3. Ver información de una carpeta")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            client_code(documento1)
        elif opcion == "2":
            client_code(enlace1)
        elif opcion == "3":
            client_code(carpeta1)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
