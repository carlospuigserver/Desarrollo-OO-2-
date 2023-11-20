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

class MenuNiños(Componente):
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

def mostrar_menu(menu: MenuNiños) -> None:
    print("\nMenú:")
    print(menu)

if __name__ == "__main__":
    # Crear el menú de niños
    menu_ninos = MenuNiños("Menú Niños")

    # Agregar opciones al menú de niños
    bebidas_ninos = [
        Componente("Zumo de Fresa", 2.0),
        Componente("Zumo de Manzana", 2.0),
        Componente("Zumo de Naranja", 2.0),
        Componente("Agua con Gas", 1.5),
        Componente("Leche con Chocolate", 2.5)
    ]

    primeros_platos_ninos = [
        Componente("Nuggets de Pollo", 5.0),
        Componente("Mini Pizzas con Queso", 4.0),
        Componente("Macarrones con Queso", 4.5),
        Componente("Mini Hamburguesas", 5.5)
    ]

    segundos_platos_ninos = [
        Componente("Mini Pizza Delizioso (Pizza personalizada con el Builder)", 8.0),
        Componente("Mini Pizza Margherita", 7.0),
        Componente("Mini Pizza Hawaiana", 7.5),
        Componente("Mini Pizza Vegetariana", 8.0)
    ]

    postres_ninos = [
        Componente("Helado de Vainilla con Toppings", 4.0),
        Componente("Galletas Decoradas", 3.5),
        Componente("Gelatina de Frutas", 3.0),
        Componente("Frutas Frescas", 3.5)
    ]

    # Solicitar al cliente que elija opciones para niños
    bebida_cliente_ninos = mostrar_opciones(bebidas_ninos, "Bebida")
    primer_plato_cliente_ninos = mostrar_opciones(primeros_platos_ninos, "Primer Plato")
    segundo_plato_cliente_ninos = mostrar_opciones(segundos_platos_ninos, "Segundo Plato")
    postre_cliente_ninos = mostrar_opciones(postres_ninos, "Postre")

    # Crear el pedido del cliente para niños
    pedido_cliente_ninos = MenuNiños("Menú Cliente Niños")
    pedido_cliente_ninos.agregar(bebida_cliente_ninos, primer_plato_cliente_ninos, segundo_plato_cliente_ninos, postre_cliente_ninos)

    # Mostrar el resumen del pedido del cliente y el precio total para niños
    print("\nResumen del Pedido para Niños:")
    mostrar_menu(pedido_cliente_ninos)
    print(f"\nPrecio Total: ${pedido_cliente_ninos.precio():.2f}")

    # Obtener y mostrar la presentación del menú para niños
    print("\nPresentación del Menú para Niños:")
    print(menu_ninos.obtener_presentacion())
