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


### El Menú Simple es el siguiente (Menus/menu_simple.py): 

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


### El Menú Niños es el siguiente (Menus/menu_ninos.py) : 

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


### El Menú Combo Pareja es el siguiente (Menus/menu_combo_pareja.py) : 

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

### El Menú Halloween es el siguiente (Menus/menu_halloween.py) : 
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

### El Menú San Valentín es el siguiente (Menus/menu_sanvalentin.py) : 
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



## Gestionador de los Menús (menu_selector.py): 

Este código, es básicamente la implementación de un sistema de gestión de menús y pedidos que utiliza el patrón de diseño Composite para estructurar los menús de manera jerárquica. También incluye funcionalidades de registro y autenticación de usuarios. Aquí hay una explicación más detallada:

En primer lugar, el código aborda la gestión de usuarios. La función registrar_nuevo_usuario() permite a los usuarios crear una cuenta proporcionando un nombre de usuario y una contraseña. La información del usuario se almacena en un archivo CSV llamado usuario.csv en la carpeta Usuario. La función autenticar_usuario(nombre_usuario, contraseña) verifica si el nombre de usuario y la contraseña coinciden con los registros existentes, y obtener_usuarios() lee los usuarios registrados desde el archivo CSV.

Luego, se implementa el patrón Composite para representar los menús y sus elementos. La clase abstracta ComponenteMenu define una interfaz común para los elementos individuales y los menús compuestos. Luego, hay clases concretas como MenuSimple, MenuNiños, MenuComboPareja, MenuHalloween, y MenuSanValentin, cada una representando un tipo de menú y permitiendo la agregación de opciones, el cálculo de precios y la obtención de presentaciones.

Para facilitar la creación de menús, se proporcionan funciones como opciones_menu_normal(), opciones_menu_ninos(), opciones_menu_halloween(), opciones_menu_san_valentin(), y opciones_menu_combo_pareja(). Estas funciones permiten al usuario seleccionar opciones para cada tipo de menú y devuelven las opciones elegidas.

La función escribir_menu_a_csv(menu_seleccionado, nombre_usuario) se encarga de guardar los detalles del menú seleccionado en un archivo CSV llamado menus.csv en la carpeta storage. Este archivo incluye información sobre el usuario, el tipo de menú y las opciones seleccionadas, así como el precio total del menú.

La ejecución del pedido se realiza mediante la función ejecutar_pedido(). El usuario puede seleccionar un tipo de menú, elegir opciones y los detalles del pedido se guardan en el archivo CSV mencionado anteriormente.

En resumen, este código proporciona una estructura modular para la gestión de usuarios, menús y pedidos, aprovechando el patrón Composite para organizar los menús de manera flexible y permitir una variedad de opciones y combinaciones en la creación de pedidos.


### El código es el siguiente: 
```
from Menus.menu_simple import*
from Menus.menu_ninos import*
from Menus.menu_combo_pareja import*
from Menus.menu_halloween import*
from Menus.menu_sanvalentin import*
import csv
import os



# Funciones de gestión de usuarios
def registrar_nuevo_usuario():
    usuarios = obtener_usuarios()
    nombre_usuario = input("Ingrese un nombre de usuario: ")

    # Verificar si el nombre de usuario ya existe
    while nombre_usuario in usuarios:
        print("Este nombre de usuario ya está en uso. Por favor, elija otro.")
        nombre_usuario = input("Ingrese un nombre de usuario: ")

    # Solicitar y guardar la contraseña
    contraseña = input("Ingrese una contraseña: ")

    # Guardar el nuevo usuario en el archivo CSV
    with open('EJERCICIO 1/Usuario/usuario.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre_usuario, contraseña])

    print("Usuario registrado con éxito.")

def autenticar_usuario(nombre_usuario, contraseña):
    usuarios = obtener_usuarios()

    # Verificar si el nombre de usuario y la contraseña coinciden
    return (nombre_usuario, contraseña) in usuarios

def obtener_usuarios():
    usuarios = set()

    # Leer usuarios desde el archivo CSV
    with open('EJERCICIO 1/Usuario/usuario.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                usuarios.add((row[0], row[1]))

    return usuarios



from abc import ABC, abstractmethod

class ComponenteMenu(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

    @abstractmethod
    def obtener_presentacion(self):
        pass

class MenuSimple(ComponenteMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.opciones = []

    def agregar_opcion(self, *opciones):
        self.opciones.extend(opciones)

    def obtener_precio(self):
        return sum(opcion.obtener_precio() for opcion in self.opciones)

    def obtener_presentacion(self):
        presentacion = f"{self.nombre}:\n"
        presentacion += "\n".join([f"  - {opcion.obtener_presentacion()}" for opcion in self.opciones])
        return presentacion

class Componente(ComponenteMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

    def obtener_presentacion(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class MenuComboPareja(ComponenteMenu):
    def __init__(self, nombre, *menus):
        self.nombre = nombre
        self.menus = list(menus)

    def agregar(self, *menus):
        self.menus.extend(menus)  # Cambiado de self.opciones a self.menus

    def obtener_precio(self):
        return sum(menu.obtener_precio() for menu in self.menus)

    def obtener_presentacion(self):
        presentacion = f"{self.nombre}:\n"
        presentacion += "\n".join([f"  - {menu.obtener_presentacion()}" for menu in self.menus])
        return presentacion

class MenuNiños(ComponenteMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.opciones_ninos = []

    def agregar(self, *opciones_ninos):
        self.opciones_ninos.extend(opciones_ninos)

    def obtener_precio(self):
        return sum(opcion.obtener_precio() for opcion in self.opciones_ninos)

    def obtener_presentacion(self):
        presentacion = f"{self.nombre} Niños:\n"
        presentacion += "\n".join([f"  - {opcion.obtener_presentacion()}" for opcion in self.opciones_ninos])
        return presentacion

class MenuHalloween(ComponenteMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.opciones_halloween = []

    def agregar(self, *opciones_halloween):
        self.opciones_halloween.extend(opciones_halloween)

    def obtener_precio(self):
        return sum(opcion.obtener_precio() for opcion in self.opciones_halloween)

    def obtener_presentacion(self):
        presentacion = f"{self.nombre} Halloween:\n"
        presentacion += "\n".join([f"  - {opcion.obtener_presentacion()}" for opcion in self.opciones_halloween])
        return presentacion

class MenuSanValentin(ComponenteMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.opciones_san_valentin = []

    def agregar(self, *opciones_san_valentin):
        self.opciones_san_valentin.extend(opciones_san_valentin)

    def obtener_precio(self):
        return sum(opcion.obtener_precio() for opcion in self.opciones_san_valentin)

    def obtener_presentacion(self):
        presentacion = f"{self.nombre} San Valentín:\n"
        presentacion += "\n".join([f"  - {opcion.obtener_presentacion()}" for opcion in self.opciones_san_valentin])
        return presentacion


def mostrar_opciones(opciones, tipo):
    print(f"Seleccione {tipo} (Ingrese el número):")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion.obtener_presentacion()}")

    seleccion = int(input("Ingrese el número de su elección: "))
    return opciones[seleccion - 1]



def opciones_menu_normal():
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
        Componente("Pizza Delizioso ", 12.0),
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

    return bebida_cliente, primer_plato_cliente, segundo_plato_cliente, postre_cliente


def opciones_menu_ninos():
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
        Componente("Mini Pizza Delizioso ", 8.0),
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

    return bebida_cliente_ninos, primer_plato_cliente_ninos, segundo_plato_cliente_ninos, postre_cliente_ninos

def opciones_menu_halloween():
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

    return bebida_cliente_halloween, entrante_cliente_halloween, principal_cliente_halloween, postre_cliente_halloween


def opciones_menu_san_valentin():
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

    return aperitivo_cliente_san_valentin, principal_cliente_san_valentin, segundo_platos_valentin0, postre_cliente_san_valentin


def opciones_menu_combo_pareja():
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
        Componente("Pizza Combo Pareja ", 24.0),
        Componente("Pizza Quattro Stagioni para compartir", 20.0),
        Componente("Pasta Carbonara para compartir", 20.0),
        Componente("Risotto de Champiñones para compartir", 18.0),
    ]

    postres_pareja = [
        Componente("Dos Tiramisú de chocolate y Café", 8.0),
        Componente("Dos Fondue de Chocolate", 10.0),
        Componente("Dos Helados de Vainilla con Frutas", 6.0),
        Componente("Dos Pasteles de Chocolate y Frambuesa", 9.0),
    ]

    # Solicitar al cliente que elija opciones para Combo Pareja
    
    bebida_cliente_pareja = mostrar_opciones(bebidas_pareja, "Bebida")
    primerplato_cliente_pareja = mostrar_opciones(primeros_platos_pareja, "Primer Plato")
    segundoplato_cliente_pareja = mostrar_opciones(segundos_platos_pareja, "Segundo Plato")
    postre_cliente_pareja = mostrar_opciones(postres_pareja, "Postre")

    return bebida_cliente_pareja, primerplato_cliente_pareja, segundoplato_cliente_pareja, postre_cliente_pareja



def escribir_menu_a_csv(menu_seleccionado, nombre_usuario):
    nombre_archivo = "EJERCICIO 1/storage/menus.csv"

    with open(nombre_archivo, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Si el archivo está vacío, escribe la fila de encabezado
        if csv_file.tell() == 0:
            writer.writerow(["Nombre Usuario", "Tipo", "Bebida", "Primer Plato", "Segundo Plato", "Postre", "Precio Total"])

    

        if isinstance(menu_seleccionado, MenuSimple):
                bebidas_n, primeros_platos_n, segundos_platos_n, postres_n = menu_seleccionado.opciones
                precio_total = menu_seleccionado.obtener_precio()
                writer.writerow([nombre_usuario,menu_seleccionado.nombre, bebidas_n.nombre, primeros_platos_n.nombre, segundos_platos_n.nombre, postres_n.nombre, precio_total])

        elif isinstance(menu_seleccionado, MenuNiños):
                bebidas_ninos, primeros_platos_ninos, segundos_platos_ninos, postres_ninos = menu_seleccionado.opciones_ninos
                precio_total_nino = menu_seleccionado.obtener_precio()
                writer.writerow([nombre_usuario,menu_seleccionado.nombre, bebidas_ninos.nombre, primeros_platos_ninos.nombre, segundos_platos_ninos.nombre, postres_ninos.nombre, precio_total_nino])

        elif isinstance(menu_seleccionado, MenuHalloween):
                bebidas_halloween, primeros_platos_halloween, segundos_platos_halloween, postres_halloween = menu_seleccionado.opciones_halloween
                precio_total_halloween = menu_seleccionado.obtener_precio()
                writer.writerow([nombre_usuario,menu_seleccionado.nombre, bebidas_halloween.nombre, primeros_platos_halloween.nombre, segundos_platos_halloween.nombre, postres_halloween.nombre, precio_total_halloween])

        elif isinstance(menu_seleccionado, MenuSanValentin):
                bebidas_san_valentin, primeros_platos_valentin_valentin, segundo_platos_valentin, postres_san_valentin = menu_seleccionado.opciones_san_valentin
                precio_total_valentin = menu_seleccionado.obtener_precio()
                writer.writerow([nombre_usuario,menu_seleccionado.nombre, bebidas_san_valentin.nombre, primeros_platos_valentin_valentin.nombre, segundo_platos_valentin.nombre, postres_san_valentin.nombre, precio_total_valentin])

        elif isinstance(menu_seleccionado, MenuComboPareja):
                bebidas_pareja, primeros_platos_pareja, segundos_platos_pareja, postres_pareja = menu_seleccionado.opciones_pareja
                precio_total_pareja = menu_seleccionado.obtener_precio()
                writer.writerow([nombre_usuario,menu_seleccionado.nombre, bebidas_pareja.nombre, primeros_platos_pareja.nombre, segundos_platos_pareja.nombre, postres_pareja.nombre, precio_total_pareja])

        print(f"Detalles del menú guardados en {nombre_archivo}")




def ejecutar_pedido():
    menus = [
        MenuSimple("Menú Simple"),
        MenuNiños("Menú Niños"),
        MenuHalloween("Menú Halloween"),
        MenuSanValentin("Menú San Valentín"),
        MenuComboPareja("Menú Combo Pareja")
    ]

    
    
    print("¿Qué menú desea ver?")
    for i, menu in enumerate(menus, 1):
        if hasattr(menu, 'nombre'):
            print(f"{i}. {menu.nombre}")
        else:
            print(f"{i}. Menú Desconocido")

    opcion = int(input("Ingrese el número del menú que desea tomar: "))
    menu_seleccionado = menus[opcion - 1]

    print(f"\nHa seleccionado: {menu_seleccionado.nombre if hasattr(menu_seleccionado, 'nombre') else 'Menú Desconocido'}")

    

    # Agregar opciones al menú seleccionado
    if isinstance(menu_seleccionado, MenuSimple):
        bebidas_n, primeros_platos_n, segundos_platos_n,postres_n = opciones_menu_normal()
        menu_seleccionado.agregar_opcion(bebidas_n, primeros_platos_n, segundos_platos_n, postres_n)
    
    elif isinstance(menu_seleccionado, MenuNiños):
        bebidas_ninos, primeros_platos_ninos, segundos_platos_ninos, postres_ninos = opciones_menu_ninos()
        menu_seleccionado.agregar(bebidas_ninos, primeros_platos_ninos, segundos_platos_ninos, postres_ninos)
    
    elif isinstance(menu_seleccionado, MenuHalloween):
        bebidas_halloween, primeros_platos_halloween, segundos_platos_halloween, postres_halloween = opciones_menu_halloween()
        menu_seleccionado.agregar(bebidas_halloween, primeros_platos_halloween, segundos_platos_halloween, postres_halloween)

    elif isinstance(menu_seleccionado, MenuSanValentin):
        bebidas_san_valentin, primeros_platos_valentin, segundos_platos_valentin, postres_san_valentin = opciones_menu_san_valentin()
        menu_seleccionado.agregar(bebidas_san_valentin, primeros_platos_valentin, segundos_platos_valentin, postres_san_valentin)

    elif isinstance(menu_seleccionado, MenuComboPareja):
        bebidas_pareja, primeros_platos_pareja, segundos_platos_pareja, postres_pareja = opciones_menu_combo_pareja()
        menu_seleccionado.agregar(bebidas_pareja, primeros_platos_pareja, segundos_platos_pareja, postres_pareja)
    

    
    
    print("\nResumen del Pedido:")
    mostrar_menu(menu_seleccionado)
    print(f"\nPrecio Total: ${menu_seleccionado.obtener_precio():.2f}")
    escribir_menu_a_csv(menu_seleccionado, nombre_usuario)

    # Obtener y mostrar la presentación del menú
    print("\nPresentación del Menú:")
    print(menu_seleccionado.obtener_presentacion())
    escribir_menu_a_csv(nombre_usuario, menu_seleccionado)


if __name__ == "__main__":
    registrar_nuevo_usuario()  # Registra un nuevo usuario
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if autenticar_usuario(nombre_usuario, contraseña):
        ejecutar_pedido()

```

### El link del diagrama UML junto a una fotografía del mismo son los siguientes: 
//www.plantuml.com/plantuml/png/dPD1JiGW58Rtd89bEyvSO1PcT3PkD2OcRicR-Xmny6Y0wa8zb6VmOjBYX48aJMPP-Fx_vwUydVDW_Q0LwnGun_T6zuQGFDuY3Vo3SNx1pS4ZeHMznKwQfjtoPsN0btiko200D1BEM_R5_bn7hmUfUuMJuuQJqGUBaHg_JJ_gq6svaYuQ2o59UY6Q6TjEEt2qU0GhegXPdSHj2amrAe6nIYnIprldN9itsWVGt8F5LwYaw40jTLhprOHbtPguLWJUoPzlunQkK90ainHQXENQ8lK6b3BlYBGK_782pmjF-hPuEK2Fe92yN3o20n9laJth58N5x21Nr_lgDC0X-45N7uWC2fQpUTXiFY-BgMFbuwenyJrKjzEFgn7fPlzdMFuTcN0Ji_MqjaDw6hJw1G00



![uml](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/fa97626f-b683-497d-88a9-e8f6b8034ed3)
