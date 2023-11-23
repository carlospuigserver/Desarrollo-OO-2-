from __future__ import annotations
from typing import List

class Componente:
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    def __str__(self) -> str:
        return f"{self._nombre} - ${self._precio:.2f}"

    def precio(self) -> float:
        return self._precio

class MenuComboPareja(Componente):
    def __init__(self, nombre: str):
        super().__init__(nombre, 0)
        self._ninos: List[Componente] = []

    def agregar(self, *componentes: Componente) -> None:
        self._ninos.extend(componentes)

    def quitar(self, componente: Componente) -> None:
        self._ninos.remove(componente)

    def __str__(self) -> str:
        resultados = [str(nino) for nino in self._ninos]
        return f"{self._nombre} - {' + '.join(resultados)}"

    def precio(self) -> float:
        opciones_validas = [nino for nino in self._ninos if nino is not None]
        return sum(nino.precio() for nino in opciones_validas)

    def obtener_presentacion(self) -> str:
        return f"{self._nombre}: {', '.join([str(opcion) for opcion in self._ninos])}"

def mostrar_opciones(categoria: List[Componente], nombre_categoria: str) -> Componente:
    print(f"\nOpciones de {nombre_categoria}:")
    for opcion in categoria:
        print(f"- {opcion}")
    seleccion = input(f"Seleccione un(a) {nombre_categoria.lower()}: ")
    seleccion = next((x for x in categoria if x._nombre.lower() == seleccion.lower()), None)
    return seleccion

def mostrar_menu(menu: MenuComboPareja) -> None:
    print("\nMenú:")
    print(menu)

if __name__ == "__main__":
    # Crear el menú Combo Pareja
    combo_pareja = MenuComboPareja("Combo Pareja")

    # Agregar opciones al menú Combo Pareja
    bebidas_pareja = [
        Componente("Botella de Vino Tinto", 15.0),
        Componente("Botella de Vino Blanco", 15.0),
        Componente("Botea de Vino Rosado", 15.0),
        Componente("Agua con Gas de Litro", 3.0),
        Componente("Refresco de Naranja", 2.5),
        Componente("Agua Mineral de Litro", 2.5),
    ]

    primeros_platos_pareja = [
        Componente("Ensalada Mixta para compartir ", 15.0),
        Componente("Carpaccio de Salmón para compartir ", 12.0),
        Componente("Tartaleta de Queso de Cabra", 12.0),
        Componente("Croquetas de Jamón", 12.0),
    ]

    segundos_platos_pareja = [
        Componente("Pizza Combo Pareja (Pizza personalizada con el Builder)", 24.0),
        Componente("Pizza Quattro Stagioni para compartir", 20.0),
        Componente("Pasta Carbonara para compartir", 20.0),
        Componente("Risotto de Champiñones para compartir", 18.0),
    ]

    postres_pareja = [
        Componente(" Dos Tiramisú de chocolate y Café", 8.0),
        Componente(" Dos Fondue de Chocolate", 10.0),
        Componente("Dos Helados de Vainilla con Frutas", 6.0),
        Componente("Dos Pasteles de Chocolate y Frambuesa", 9.0),
    ]

    # Solicitar al cliente que elija opciones para Combo Pareja
    bebida_cliente_pareja = mostrar_opciones(bebidas_pareja, "Bebida")
    entrante_cliente_pareja = mostrar_opciones(primeros_platos_pareja, "Entrante")
    pizza_cliente_pareja = mostrar_opciones(segundos_platos_pareja, "Pizza")
    postre_cliente_pareja = mostrar_opciones(postres_pareja, "Postre")

    # Crear el pedido del cliente para Combo Pareja
    pedido_cliente_pareja = MenuComboPareja("Menú Combo Pareja")
    pedido_cliente_pareja.agregar(bebida_cliente_pareja, entrante_cliente_pareja, pizza_cliente_pareja, postre_cliente_pareja)

    # Mostrar el resumen del pedido del cliente y el precio total para Combo Pareja
    print("\nResumen del Pedido para Combo Pareja:")
    mostrar_menu(pedido_cliente_pareja)
    print(f"\nPrecio Total: ${pedido_cliente_pareja.precio():.2f}")

    # Obtener y mostrar la presentación del menú para Combo Pareja
    print("\nPresentación del Menú para Combo Pareja:")
    print(combo_pareja.obtener_presentacion())
