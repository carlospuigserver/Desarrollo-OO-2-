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

class MenuSanValentin(Componente):
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

def mostrar_menu(menu: MenuSanValentin) -> None:
    print("\nMenú:")
    print(menu)

if __name__ == "__main__":
    # Crear el menú San Valentín
    menu_san_valentin = MenuSanValentin("Menú San Valentín")

    # Agregar opciones al menú San Valentín
    bebidas_san_valentin = [
        Componente("Botella de Vino Tinto", 15.0),
        Componente("Botella de Vino Blanco", 15.0),
        Componente("Botea de Vino Rosado", 15.0),
        Componente("Agua con Gas de Litro", 3.0),
        Componente("Refresco de Naranja", 2.5),
        Componente("Agua Mineral de Litro", 2.5),
    ]
    

    primeros_platos_valentin = [
        Componente("Pasta a la Trufa con Gambas", 15.0),
        Componente("Risotto de Champiñones y Espárragos", 14.0),
        Componente("Pasta al Pesto con Langostinos",14.0),
        Componente("Tartar de Atún con Aguacate y Sésamo",15.0)
    ]


    
    segundo_platos_valentin = [ 
        Componente("Filete de Ternera con Salsa de Vino Tinto", 18.0),
        Componente("Pechuga de Pato con Salsa de Frutos Rojos",16.0),
        Componente("Medallones de Solomillo con Reducción de Balsámico",17.0),
        Componente("Salmón al Horno con Hierbas", 16.0)
    ]

    
    
    postres_san_valentin = [
        Componente("Tarta de Chocolate y Frambuesas", 9.0),
        Componente("Helado de Vainilla con Fresas", 6.0),
        Componente("Soufflé de Frambuesa", 7.5),
        Componente("Café Especial de San Valentín", 4.0),
    ]

    # Solicitar al cliente que elija opciones para San Valentín
    aperitivo_cliente_san_valentin = mostrar_opciones(bebidas_san_valentin, "Bebidas")
    principal_cliente_san_valentin = mostrar_opciones(primeros_platos_valentin, "Primer Plato")
    segundo_platos_valentin0 = mostrar_opciones(segundo_platos_valentin, "Segundo Plato")
    postre_cliente_san_valentin = mostrar_opciones(postres_san_valentin, "Postre")

    # Crear el pedido del cliente para San Valentín
    pedido_cliente_san_valentin = MenuSanValentin("Menú San Valentín")
    pedido_cliente_san_valentin.agregar(aperitivo_cliente_san_valentin, principal_cliente_san_valentin, postre_cliente_san_valentin)

    # Mostrar el resumen del pedido del cliente y el precio total para San Valentín
    print("\nResumen del Pedido para San Valentín:")
    mostrar_menu(pedido_cliente_san_valentin)
    print(f"\nPrecio Total: ${pedido_cliente_san_valentin.precio():.2f}")

    # Obtener y mostrar la presentación del menú para San Valentín
    print("\nPresentación del Menú para San Valentín:")
    print(menu_san_valentin.obtener_presentacion())
