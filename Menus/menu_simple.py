from typing import List

class Componente:
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    def __str__(self) -> str:
        return f"{self._nombre} - ${self._precio:.2f}"

    def precio(self) -> float:
        return self._precio

class MenuSimple(Componente):
    def __init__(self, nombre: str):
        super().__init__(nombre, 0)
        self._opciones: List[Componente] = []

    def agregar_opcion(self, *opciones: Componente) -> None:
        self._opciones.extend(opciones)

    def quitar_opcion(self, opcion: Componente) -> None:
        self._opciones.remove(opcion)

    def __str__(self) -> str:
        resultados = [str(opcion) for opcion in self._opciones]
        return f"{self._nombre} - {' + '.join(resultados)}"

    def precio(self) -> float:
        return sum(opcion.precio() for opcion in self._opciones)

    def obtener_presentacion(self) -> str:
        return f"{self._nombre}: {', '.join([str(opcion) for opcion in self._opciones])}"

def mostrar_opciones(categoria: List[Componente], nombre_categoria: str) -> Componente:
    print(f"\nOpciones de {nombre_categoria}:")
    for opcion in categoria:
        print(f"- {opcion}")
    seleccion = input(f"Seleccione un(a) {nombre_categoria.lower()}: ")
    seleccion = next((x for x in categoria if x._nombre.lower() == seleccion.lower()), None)
    return seleccion

def mostrar_menu(menu: MenuSimple) -> None:
    print("\nMenú:")
    print(menu)

if __name__ == "__main__":
    # Crear el menú normal
    menu_normal = MenuSimple("Menú Simple")

    # Agregar opciones al menú normal
    bebidas_n = [
        Componente("Nestea", 2.0),
        Componente("Fanta (Naranja)", 2.5),
        Componente("Fanta (Limón)", 2.5),
        Componente("Aquarius (Naranja)", 3.0),
        Componente("Aquarius (Limón)", 3.0),
        Componente("Coca Cola (Normal)", 2.5),
        Componente("Coca Cola (Zero)", 2.5),
        Componente("Sprite", 2.5),
        Componente("Agua Mineral", 1.5)
    ]

    primeros_platos_n = [
        Componente("Bruschetta", 4.5),
        Componente("Ensalada Caprese", 5.0),
        Componente("Carpaccio de Res", 8.0),
        Componente("Calamares a la Romana", 7.0)
    ]

    segundos_platos_n = [
        Componente("Pizza Delizioso (Pizza personalizada con el Builder)", 12.0),
        Componente("Pizza Margherita", 10.0),
        Componente("Pizza Pepperoni", 11.0),
        Componente("Pizza Vegetariana", 11.5)
    ]

    postres_n = [
        Componente("Tiramisú", 6.0),
        Componente("Panna Cotta", 5.0),
        Componente("Cannoli", 4.5),
        Componente("Brownie con Helado", 7.0),
        Componente("Sorbete de Frutas", 4.0)
    ]

    # Solicitar al cliente que elija opciones
    bebida_cliente = mostrar_opciones(bebidas_n, "Bebida")
    primer_plato_cliente = mostrar_opciones(primeros_platos_n, "Primer Plato")
    segundo_plato_cliente = mostrar_opciones(segundos_platos_n, "Segundo Plato")
    postre_cliente = mostrar_opciones(postres_n, "Postre")

    # Crear el pedido del cliente
    pedido_cliente = MenuSimple("Menú Cliente")
    pedido_cliente.agregar_opcion(bebida_cliente, primer_plato_cliente, segundo_plato_cliente, postre_cliente)

    # Mostrar el resumen del pedido del cliente y el precio total
    print("\nResumen del Pedido:")
    mostrar_menu(pedido_cliente)
    print(f"\nPrecio Total: ${pedido_cliente.precio():.2f}")

    # Obtener y mostrar la presentación del menú
    print("\nPresentación del Menú:")
    print(menu_normal.obtener_presentacion())
