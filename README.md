# EJERCICIO 1

## Contexto: 
Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca.

## Objetivos: 
### Desarrollo de Menús Personalizados:
Introducir la noción de un "menú", que puede contener varios elementos: entradas, bebidas, pizzas (que ya han sido definidas previamente con su sistema de creación de pizzas) y postres.
Un "menú" puede ser simple (contener elementos básicos) o compuesto (incluir otros menús más pequeños, como un "Combo Pareja" que incluye dos menús individuales).
Cada "menú" tendrá un código único y un precio, que se determina como la suma de los precios de sus elementos, con un descuento según la promoción aplicada.
### Patrones de Diseño:
Implementar el patrón Composite para modelar la relación entre los elementos y menús, facilitando la creación, modificación y cálculo de precios de menús compuestos.
Continuar utilizando el patrón Builder para la creación detallada de las pizzas.
### Interacción con CSV:
Ampliar el sistema de almacenamiento en CSV para incluir los menús personalizados, de forma que se pueda registrar y recuperar la información de menús individuales y compuestos.
Permitir que, a partir de un menú almacenado, se pueda reconstruir toda la estructura del menú con sus elementos individuales y precios.
### Restricciones:
Las librerías estándar de Python para la interacción con archivos CSV están permitidas.
Se espera un diseño modular y orientado a objetos, con una clara separación de responsabilidades.
La implementación del cálculo del precio de un "menú" debe hacerse en tiempo de ejecución y ser eficiente.


## 1-Desarrollo de Menús Personalizados:


En el desarrollo del programa, he implementado una estructura de clases que refleja de manera efectiva la diversidad de menús disponibles. He adoptado el patrón composite para crear cinco tipos distintos de menús, cada uno con sus propias características únicas.
Cada tipo de menú tiene su propia implementación, pero comparten una estructura común. En la selección de opciones por parte del usuario, se utilizan métodos específicos para cada tipo de menú, garantizando así una experiencia intuitiva y coherente. Además, la implementación del patrón composite permite que los menús sean fáciles de organizar y ejecutar, proporcionando una flexibilidad significativa en la creación y gestión.
Personalmente, veo mejor la opción de  que cada componente de cada menú tuviese un precio distinto, de esta manera, el usuario se sumerge y se implica más en cada elección, mucho más que si los precios del menú fuesen fijos. Para ello he integrado la capacidad de calcular el precio total de los menús, teniendo en cuenta los precios individuales de los elementos seleccionados por el usuario.
El uso del programa es muy sencillo, el usuario elige entre las opciones de bebida, primer plato, segundo plato y postre para cada tipo de menú. Al finalizar la selección, se muestra el precio total.
Este diseño proporciona una estructura robusta y flexible para gestionar la diversidad de menús, asegurando una experiencia coherente y la capacidad de adaptarse a futuras expansiones de opciones de menú.


### El Menú Simple es el siguiente: 

```
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
```


### El Menú Niños es el siguiente: 

```
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
```


### El Menú Combo Pareja es el siguiente: 

```
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
```

### El Menú Halloween es el siguiente: 
```
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
```

### El Menú San Valentín es el siguiente: 
```
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
```


