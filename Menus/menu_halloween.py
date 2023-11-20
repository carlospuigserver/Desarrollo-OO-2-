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

class MenuHalloween(Componente):
    def __init__(self, nombre: str):
        super().__init__(nombre, 0)
        self._opciones: List[Componente] = []

    def agregar(self, *componentes: Componente) -> None:
        self._opciones.extend(componentes)

    def quitar(self, componente: Componente) -> None:
        self._opciones.remove(componente)

    def __str__(self) -> str:
        resultados = [str(opcion) for opcion in self._opciones]
        return f"{self._nombre} - {' + '.join(resultados)}"

    def precio(self) -> float:
        opciones_validas = [opcion for opcion in self._opciones if opcion is not None]
        return sum(opcion.precio() for opcion in opciones_validas)

    def obtener_presentacion(self) -> str:
        return f"{self._nombre}: {', '.join([str(opcion) for opcion in self._opciones])}"

def mostrar_opciones(categoria: List[Componente], nombre_categoria: str) -> Componente:
    print(f"\nOpciones de {nombre_categoria}:")
    for idx, opcion in enumerate(categoria, start=1):
        print(f"{idx}. {opcion}")
    seleccion_idx = input(f"Seleccione un(a) {nombre_categoria.lower()} (número o nombre): ")

    try:
        # Intentar convertir la selección a entero
        seleccion_idx = int(seleccion_idx)
        return categoria[seleccion_idx - 1] if 1 <= seleccion_idx <= len(categoria) else None
    except ValueError:
        # Si no se puede convertir a entero, buscar por nombre
        return next((x for x in categoria if x._nombre.lower() == seleccion_idx.lower()), None)

def mostrar_menu(menu: MenuHalloween) -> None:
    print("\nMenú:")
    print(menu)

if __name__ == "__main__":
    # Crear el menú Halloween
    menu_halloween = MenuHalloween("Menú Halloween")

    # Agregar opciones al menú Halloween
    bebidas_halloween = [
        Componente("Poción de Bruja (Bebida de Frutas)", 3.0),
        Componente("Sangre de Vampiro (Zumo de Tomate)", 2.5),
        Componente("Limo Verde (Refresco de Lima)", 2.5),
        Componente("Agua Embrujada (Agua Mineral)", 1.5),
    ]

    primeros_platos_halloween = [
        Componente("Dedos de Zombie (Palitos de Queso)", 5.0),
        Componente("Ojos de Murciélago (Aceitunas rellenas)", 4.0),
        Componente("Calabaza Rellena de Quinoa", 7.0),
        Componente("Cerebros a la Parrilla (Empanadas de Carne)", 6.5),
    ]

    segundos_platos_halloween = [
        Componente("Pizza Espectral (Pizza de Queso)", 10.0),
        Componente("Pasta de la Noche (Pasta con Salsa de Calabaza)", 9.0),
        Componente("Estofado de Calabaza y Setas", 11.0),
        Componente("Hamburguesa Monstruosa (Hamburguesa de Ternera)", 12.0),
    ]

    postres_halloween = [
        Componente("Ojos Saltarines (Gelatina de Uva)", 4.0),
        Componente("Fantasmas de Chocolate (Brownies)", 5.0),
        Componente("Cupcakes de Araña", 4.5),
        Componente("Cementerio de Helado (Helado de Vainilla con Galletas)", 7.0),
    ]

    # Solicitar al cliente que elija opciones para Halloween
    bebida_cliente_halloween = mostrar_opciones(bebidas_halloween, "Bebida")
    entrante_cliente_halloween = mostrar_opciones(primeros_platos_halloween, "Primer Plato")
    principal_cliente_halloween = mostrar_opciones(segundos_platos_halloween, "Segundo Plato")
    postre_cliente_halloween = mostrar_opciones(postres_halloween, "Postre")

    # Crear el pedido del cliente para Halloween
    pedido_cliente_halloween = MenuHalloween("Menú Halloween")
    pedido_cliente_halloween.agregar(bebida_cliente_halloween, entrante_cliente_halloween, principal_cliente_halloween, postre_cliente_halloween)

    # Mostrar el resumen del pedido del cliente y el precio total para Halloween
    print("\nResumen del Pedido para Halloween:")
    mostrar_menu(pedido_cliente_halloween)
    print(f"\nPrecio Total: ${pedido_cliente_halloween.precio():.2f}")

    # Obtener y mostrar la presentación del menú para Halloween
    print("\nPresentación del Menú para Halloween:")
    print(menu_halloween.obtener_presentacion())
