from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from documentos import Documento
from enlaces import Enlace
from carpetas import Carpeta

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


class DocumentoComponente(Componente):
    def __init__(self, documento: Documento):
        self.documento = documento

    def operation(self) -> str:
        return f"Documento {self.documento.tipo} {self.documento.nombre}"

    # Puedes agregar lógica específica del documento aquí si es necesario


class EnlaceComponente(Componente):
    def __init__(self, enlace: Enlace):
        self.enlace = enlace

    def operation(self) -> str:
        return f"Enlace {self.enlace.nombre}"

    # Puedes agregar lógica específica del enlace aquí si es necesario


class CarpetaComponente(Componente):
    def __init__(self, carpeta: Carpeta):
        self.carpeta = carpeta

    def add(self, componente: Componente) -> None:
        self.carpeta.agregar_elemento(componente)

    def remove(self, componente: Componente) -> None:
        self.carpeta.eliminar_elemento(componente)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        resultados = [elemento.operation() for elemento in self.carpeta.elementos]
        return f"Carpeta {self.carpeta.nombre} ({', '.join(resultados)})"


def client_code(componente: Componente) -> None:
    print(f"Resultado: {componente.operation()}", end="")


if __name__ == "__main__":
    # Crear instancias de Documento, Enlace y Carpeta aquí

    # Crear instancias de DocumentoComponente, EnlaceComponente y CarpetaComponente aquí

    # Llamar a client_code con la estructura compuesta
