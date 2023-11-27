# EJERCICIO 1

## Contexto: 
Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca. 

(Obviamente para esta entrega, se han reutilizado carpetas y archivos del Ejercicio 2 de la entrega anterior, los cuales son la Carpeta Builder con todos los builders de la pizza: masa, salsa etc  La Carpeta Usuario, con su archivo csv donde se guardan los usuarios registrados, la Carpeta Storage, donde se guardan las pizzas en un archivo csv despues de haber sido pedidas, y finalmente el Archivo cliente.py, el cual era el gestor del registro y autentificacion de usuarios, donde se realizaba la eleccion de todos los builders, y la pizza finañl se guardaba en el csv.)

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


![codesim](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/3b8f0020-c8ce-47cb-8077-20479a4374bd)


### El Menú Niños es el siguiente (Menus/menu_ninos.py) : 


![codesn](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/36d799a1-b86f-48d3-ac45-36dcc038a264)


### El Menú Combo Pareja es el siguiente (Menus/menu_combo_pareja.py) : 

![codems](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/7739bd8a-c0ca-4095-80fd-ffa3beda3c64)


### El Menú Halloween es el siguiente (Menus/menu_halloween.py) : 
![codeh](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/39ae0f4b-f6e8-47b0-a398-921a9b66c7ed)


### El Menú San Valentín es el siguiente (Menus/menu_sanvalentin.py) : 

![codesv](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/29698686-d152-426a-aaa9-e860b442cd63)



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







## Restaurante: 

Finalmente encontramos el archivo restaurante.py, el cual es el gestor de este ejercicio, y el programa que se debe ejecutar. Este funciona como ampliación de la Pizzeria y la convierte en Restaurante, ofreciendo así la opción de elegir o una Pizza personalizada, o uno de los Menús. En el caso de escoger la Pizza, este la crea usando los Builders ya creados, y en este caso ejerciendo un precio fijo por la creación de la pizza de 25 euros, con una ligera ampliación, el postre. Si el cliente no desea postre, los detalles de la pizza junto a su precio fijo , son guardados storage/pizzas.csv, pero en el caso de elegir uno de entre los 14 postres disponibles ( cada uno con un precio distinto), los detalles de la pizza, junto al postre, y junto al precio total, siendo este la suma del precio de la Pizza personalizada junto al precio de el postre en particular, son guardados en storage/pizzas-postre.csv.
Por otro lado, si el comensal, elige la opción Menús, este ofrece el mismo servicio que "menu-selector.py", llevando a cabo la elección del Menú seleccionado, en el cual se elige una opción de entre tantas en bebidas, primeros y segundos platos y postres, detallando al final las opciones elegidas del menú junto a su precio, todo esto guardado en un csv, en storage/menus.csv.

Después de esta visión general de la base del Ejercicio, aquí va una explicación más detallada y técnica: 



### 1. Estructura de Clases Abstractas:
En el código, se define una clase abstracta llamada ComponenteMenu que sirve como base para los diferentes elementos del menú. Contiene métodos abstractos para obtener el precio y la presentación de un componente del menú. Además, se presenta una clase ItemMenu que representa un elemento individual del menú, y la clase MenuComposite que actúa como un contenedor para elementos del menú, permitiendo la creación de menús compuestos.

### 2. Elección del Tipo de Menú:
El programa comienza solicitando al usuario que elija entre dos opciones de menú: pizza personalizada o menú predefinido. Dependiendo de la elección, el flujo del programa se bifurca para manejar la creación de una pizza personalizada o la selección de un menú predefinido.

### 3. Creación de Pizza Personalizada:
Si se elige la opción de pizza personalizada, se procede a solicitar al usuario que elija diferentes componentes de la pizza, como masa, salsa, ingredientes, bebida, etc. Cada elección se agrega al menú compuesto de la pizza personalizada. Se proporcionan opciones para elegir si se desea agregar un postre y se calcula el precio total.

### 4. Menús Predefinidos:
Si se elige la opción de menú predefinido, se importan diferentes menús predefinidos, como menú simple, menú para niños, menú de Halloween, menú de San Valentín y menú combo pareja. Estos menús están implementados como clases que heredan de la clase abstracta ComponenteMenu. Cada menú tiene sus propias opciones y precios.

### 5. Gestión de Usuarios:
El programa incluye funciones para registrar nuevos usuarios, autenticar usuarios existentes y almacenar esta información en archivos CSV. La autenticación se realiza mediante el nombre de usuario y la contraseña.

### 6. Escritura en Archivos CSV:
Después de que se completa la elección del menú, los detalles del menú, junto con el nombre de usuario y el precio total, se escriben en un archivo CSV correspondiente (pizzas.csv, pizzas-postre.csv o menus.csv).

### 7. Ejecución del Pedido:
La función principal ejecutar_pedido permite a los usuarios seleccionar un tipo de menú, realizar sus elecciones y mostrar un resumen del pedido, incluido el precio total. Luego, la información se almacena en el archivo correspondiente.

### 8. Presentación y Detalles del Menú:
Al final del programa, se muestra la presentación del menú elegido, resaltando las opciones seleccionadas y el precio total. Además, se informa al usuario que los detalles del menú se han guardado en un archivo CSV.

La estructura modular y extensible del programa, facilita la adición de nuevos menús predefinidos o características en el futuro. Además, el uso de archivos CSV permite un registro persistente de los detalles de los pedidos y usuarios.




### El código del programa es el siguiente: 
```


from menu_selector import*
from postre_builder import *
from cliente import *
import csv


from abc import ABC, abstractmethod

class ComponenteMenu(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

    @abstractmethod
    def obtener_presentacion(self):
        pass



class ItemMenu:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def operation(self):
        return self.descripcion

class MenuComposite:
    def __init__(self, nombre):
        self.nombre = nombre
        self._items = []

    def add(self, item):
        self._items.append(item)

    def operation(self):
        results = [item.operation() for item in self._items]
        return f"{self.nombre}({'+'.join(results)})"

    def get_opciones_tipo(self, tipo):
        return [item for item in self._items if tipo in item.operation()]


def elegir_opcion_menu():
    print("¿Qué desea ordenar?")
    print("1. Pizza personalizada")
    print("2. Menú predefinido")
    opcion = input("Seleccione la opción (1 o 2): ")
    return opcion

opcion_menu= elegir_opcion_menu()
    
     

if opcion_menu == "1":
            
            def mostrar_detalles_del_menu(menu_seleccionado, nombre_usuario):
                print(f"\nDetalles del Menú de {nombre_usuario}:")
                mostrar_menu(menu_seleccionado)
                print(f"\nPrecio Total: ${menu_seleccionado.obtener_precio():.2f}")

            if __name__ == "__main__":
                registrar_nuevo_usuario()  # Registra un nuevo usuario

                nombre_usuario = input("Nombre de usuario: ")
                contraseña = input("Contraseña: ")

                if autenticar_usuario(nombre_usuario, contraseña):
                    # Crear un menú compuesto para gestionar la elección entre pizza personalizada y menú predefinido
                    menu_pedido = MenuComposite("Pedido")

        
            
            
            pizza_personalizada = MenuComposite("Pizza Personalizada")

            masa_builder = MasaPizzaBuilder()
            salsa_builder = SalsaPizzaBuilder()
            ingredientes_builder = IngredientesPizzaBuilder()
            bebida_builder = BebidaPizzaBuilder()
            coccion_builder = CoccionPizzaBuilder()
            builder = PresentacionPizzaBuilder()
            extras_builder = ExtrasPizzaBuilder()

            cliente = Cliente()

            masa_elegida = cliente.elegir_masa(masa_builder)
            if masa_elegida:
                pizza_personalizada.add(ItemMenu(f"Elegida masa: {masa_elegida.tipo}"))

            salsa_elegida = cliente.elegir_salsa(salsa_builder)
            if salsa_elegida:
                pizza_personalizada.add(ItemMenu(f"Elegida salsa: {salsa_elegida.tipo}"))

                ingredientes_elegidos = cliente.elegir_ingredientes(ingredientes_builder)
                if ingredientes_elegidos:
                    pizza_personalizada.add(ItemMenu(f"Elegidos ingredientes: {ingredientes_elegidos}"))

                    bebida_elegida = cliente.elegir_bebida(bebida_builder)
                    if bebida_elegida:
                        pizza_personalizada.add(ItemMenu(f"Elegida bebida: {bebida_elegida.tipo}"))

                        coccion_elegida = cliente.elegir_coccion(coccion_builder)
                        if coccion_elegida:
                            pizza_personalizada.add(ItemMenu(f"Elegida técnica de cocción: {coccion_elegida.metodo}"))

                            presentacion_elegida = cliente.elegir_presentacion(builder)
                            if presentacion_elegida:
                                pizza_personalizada.add(ItemMenu(f"Elegida presentación: {presentacion_elegida.tipo}"))

                                extras_elegidos = cliente.elegir_extras(extras_builder)
                                pizza_personalizada.add(ItemMenu(f"Elegidos extras: {extras_elegidos}"))

                                # Agregar la pizza personalizada al menú compuesto de pedido
                                menu_pedido.add(pizza_personalizada)

                                

                                desea_postre = input("¿Desea añadir un postre a su pedido? (Sí/No): ").lower()
                                precio=25.0
                                if desea_postre == "sí":
                                    postre_builder = PostreBuilder()
                                    cliente.elegir_postre(postre_builder)
                                    postre = postre_builder.obtener_postre()
                                    print(f"Postre elegido: {postre}, precio t")

                                    # Calcular el precio total sumando el precio de la pizza y el precio del postre
                                    
                                    precio_total = precio + postre.precio

                                    # Guardar los detalles de la pizza y el postre en un archivo CSV (pizza-postre.csv)
                                    with open('EJERCICIO 1/storage/pizzas-postre.csv', 'a', newline='') as file:
                                        writer = csv.writer(file)
                                        writer.writerow([
                                            nombre_usuario,
                                            f"Elegida masa: {masa_elegida.tipo}",
                                            f"Elegida salsa: {salsa_elegida.tipo}",
                                            f"Elegidos ingredientes: {ingredientes_elegidos}",
                                            f"Elegida bebida: {bebida_elegida.tipo}",
                                            f"Elegida técnica de cocción: {coccion_elegida.metodo}",
                                            f"Elegida presentación: {presentacion_elegida.tipo}",
                                            f"Elegidos extras: {extras_elegidos}",
                                            f"Postre elegido: {postre.nombre}",
                                            f"Precio total: {precio_total:.2f}"
                                        ])
                                    print("Vaya!!!, has elegido",{postre.nombre},"que gran elección!!")
                                    print("El precio total por la elección de la pizza personalizada y el postre es: ",precio_total)
                                    print("Detalles de la pizza y el postre guardados en pizza-postre.csv")
                                else:
                                    # Guardar solo los detalles de la pizza en el archivo original (pizzas.csv)
                                    with open('EJERCICIO 1/storage/pizzas.csv', 'a', newline='') as file:
                                        writer = csv.writer(file)
                                        writer.writerow([
                                            nombre_usuario,
                                            f"Elegida masa: {masa_elegida.tipo}",
                                            f"Elegida salsa: {salsa_elegida.tipo}",
                                            f"Elegidos ingredientes: {ingredientes_elegidos}",
                                            f"Elegida bebida: {bebida_elegida.tipo}",
                                            f"Elegida técnica de cocción: {coccion_elegida.metodo}",
                                            f"Elegida presentación: {presentacion_elegida.tipo}",
                                            f"Elegidos extras: {extras_elegidos}",
                                            f"Precio fijo por la elección de la pizza personalizada: {precio}"
                                        ])

                                    print("Que gran elección!!! El precio total por la elección de la pizza personalizada es: ",precio)
                                    print("Detalles de la pizza guardados en pizzas.csv")

elif opcion_menu == "2":
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
                
                
                
                
                    
                


# EJERCICIO 2

## Contexto:
El SAMUR-Protección Civil, tras su proceso de digitalización, se enfrenta al reto de administrar una cantidad masiva de documentos digitales relacionados con sus activaciones y operaciones. Esta documentación no solo consiste en informes y registros, sino que también incluye imágenes, vídeos, audios y otros tipos de archivos multimedia. La necesidad de garantizar un acceso rápido pero seguro a esta información es esencial, especialmente cuando se trata de datos sensibles o confidenciales.


## Enunciado del problema:

(1)Documentos: Estos son los archivos básicos en el sistema. Cada documento tiene un nombre, un tipo (texto, imagen, video, etc.) y un tamaño. El contenido de estos documentos puede ser accedido y modificado, pero para algunos documentos sensibles, es necesario llevar un registro de quién y cuándo se accede o modifica.

(2)Enlaces (Links): Son referencias a otros documentos o carpetas en el sistema. No poseen contenido propio, pero ofrecen una forma rápida de acceder a la información referenciada. Su tamaño es simbólico, no correspondiente al tamaño real del archivo o carpeta al que apuntan.

(3)Carpetas: Contenedores que albergan varios documentos, enlaces y otras carpetas. Su tamaño es la suma de los tamaños de todos los elementos contenidos. Se pueden expandir añadiendo más elementos en cualquier momento.

(4)Proxy de Acceso: Para garantizar la seguridad y la trazabilidad en el acceso a los documentos, se implementará un proxy que actuará como intermediario. Este proxy registrará cada acceso o modificación a los documentos, especialmente aquellos que sean sensibles o confidenciales, y solo permitirá el acceso a usuarios autorizados.


## Objetivos:
(1)Utilizar el patrón de diseño Composite para modelar la estructura de documentos del sistema.
(2)Implementar el patrón Proxy para controlar y registrar el acceso a documentos específicos.
(3)Desarrollar en Python las clases y la lógica necesaria para representar y gestionar los documentos, enlaces y carpetas, garantizando la seguridad y trazabilidad mediante el uso del proxy.
(4)Implementar funciones que faciliten la navegación, creación, modificación y eliminación de elementos en el sistema.



                
## Cerpeta Composite

Dentro de esta carpeta, está uno de los puntos importantes del ejercicio, que es aplicar el Patrón Composite, ya usado en el Ejercicio 1, para modelar la estructura de documentos del sistema. Para ello, con el objetivo de una mejor comprensión, he dejado 3 archivos dentro de la carpeta, documentos.py, enlace.py y carpeta.py, simplem,ente para entender mejor que hacen cada uno individualmente, y luego está el archivo composite.py, donde ya sabiendo que hace cada clase , es mucho más fácil de entender, a continuación, se adjuntarán los códigos y una explicación un poco más amplia de cada uno de ellos.


### documentos.py:


  ![codedoc](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/0b36e28b-8d96-4f6e-940e-5e62eed48fa6)
          

El código define una clase llamada Documento en el archivo documento.py. La clase Documento representa un documento con atributos como nombre, tipo, tamaño, contenido y ruta. La idea principal es encapsular estos atributos y proporcionar métodos para acceder y modificar estos valores de manera controlada.

El constructor __init__ se utiliza para inicializar un objeto Documento con los atributos proporcionados (nombre, tipo, tamaño, contenido y ruta).
A continuación, se definen propiedades y métodos de configuración (@property y @nombre.setter, @tipo.setter, etc.) para cada atributo del documento. Estos métodos permiten acceder y modificar los atributos de la clase de manera segura, aplicando algunas validaciones simples para asegurarse de que los valores sean del tipo correcto.

La función mostrar_info imprime información formateada sobre el documento, incluyendo nombre, tipo, tamaño, contenido y ruta.
Finalmente, se presenta un ejemplo de uso de la clase Documento. Se crea un objeto documento_ejemplo con valores específicos y se imprime la información del documento utilizando el método mostrar_info().
En resumen, este código implementa una clase Documento que encapsula la información relacionada con un documento y proporciona métodos para acceder y modificar sus atributos de manera segura. El ejemplo al final del código muestra cómo crear un objeto Documento y visualizar su información.
                
                

### enlace.py:


![code-en](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/f0701edf-eb73-4f9d-aebf-35f9034cdf1e)


El código en el archivo enlace.py define una clase llamada Enlace que modela un enlace entre documentos. A continuación, se proporciona una explicación detallada:

La clase Enlace tiene tres atributos privados: _nombre, _destino, y _ruta_destino. El atributo _nombre representa el nombre del enlace, _destino representa el documento al que apunta el enlace, y _ruta_destino representa la ruta específica al destino. Estos atributos son inicializados en el método __init__ cuando se crea un objeto de la clase.

Para cada uno de estos atributos, la clase implementa propiedades (@property) que permiten obtener sus valores y métodos setter (@nombre.setter, @destino.setter, @ruta_destino.setter) que validan y asignan nuevos valores. La validación se realiza para garantizar que los valores cumplan con ciertos requisitos; por ejemplo, que el nombre del enlace sea una cadena de texto.

El método mostrar_info de la clase Enlace es responsable de generar una representación en forma de cadena del enlace. Toma un diccionario de documentos como argumento, y si la ruta de destino _ruta_destino coincide con la ruta de un documento en el diccionario, muestra la información detallada del documento. En caso contrario, simplemente muestra información básica sobre el enlace, incluyendo el nombre del enlace y el destino.

El código también incluye un ejemplo de uso al final. Se crea una instancia de la clase Documento para representar un documento de ejemplo, y luego se crea un objeto Enlace que apunta a ese documento. Posteriormente, se solicita al usuario que ingrese la ruta de destino para el enlace y se muestra la información del enlace utilizando el método mostrar_info.

En resumen, enlace.py encapsula la lógica para modelar y trabajar con enlaces entre documentos, proporcionando métodos para obtener y establecer propiedades, así como para mostrar información detallada del enlace en función de la existencia y coincidencia con documentos en un diccionario.



## carpetas.py



![codecarp](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/cd6554bb-8459-44f2-a36a-2a5a4c11c8b1)




Clase Carpeta:
La clase Carpeta representa una carpeta que contiene documentos, incluidos posiblemente enlaces a otros documentos. Tiene atributos como nombre y una lista de documentos (_documentos). La propiedad documentos y su método setter permiten acceder y modificar la lista de documentos. El método agregar_documento añade un documento a la carpeta.

El método tamaño_total calcula el tamaño total de todos los documentos dentro de la carpeta, incluyendo documentos vinculados a través de enlaces.

El método mostrar_info proporciona una representación en forma de cadena de la carpeta, incluyendo su nombre, información detallada de cada documento y el tamaño total de la carpeta, teniendo en cuenta tanto documentos como enlaces.

Ejemplo de Uso:
Se crean dos objetos de la clase Documento (documento_ejemplo y documento_ejemplo2) y un objeto de la clase Carpeta (carpeta_ejemplo) que contiene estos documentos.

Se utiliza el método mostrar_info de la carpeta para imprimir información detallada sobre la carpeta, incluyendo el nombre, la información de cada documento y el tamaño total de la carpeta, considerando tanto documentos como enlaces.

En resumen, el código de carpetas.py modela documentos y carpetas, teniendo en cuenta el tamaño total de la carpeta, incluyendo documentos y enlaces. Este enfoque permite representar jerarquías complejas de documentos y proporcionar información detallada sobre el contenido y la estructura de una carpeta.
                



## Composite.py:

![codecomp](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/bbf9a2b4-6fc9-4467-a532-52ce687732bf)


El código  implementa un patrón de diseño estructural "Composite". A continuación, se explica en detalle:

Clase Abstracta Component:
La clase Component es una clase abstracta que define la interfaz común para todos los elementos en la estructura compuesta. Cada componente tiene un enlace al componente padre (si lo tiene), métodos para agregar y quitar componentes, y un método abstracto operation que debe ser implementado por las subclases concretas.

Clases Concretas Documento, Enlace y Carpeta:
Documento: Representa un documento simple con atributos como nombre, tipo, tamaño, contenido y ruta. Implementa el método operation para proporcionar una representación en forma de cadena del documento.

Enlace: Representa un enlace que puede apuntar a otro documento. Implementa métodos add y remove, aunque en este caso imprime mensajes indicando que no se pueden agregar ni quitar componentes de un enlace. También implementa el método operation para proporcionar una representación en forma de cadena del enlace.

Carpeta: Representa una carpeta que puede contener documentos o enlaces. Implementa los métodos add, remove y is_composite. El método is_composite devuelve True para indicar que es una carpeta y puede contener más elementos. El método operation devuelve una representación en forma de cadena de la carpeta y sus contenidos.

Función client_code:
La función client_code toma un componente como parámetro y muestra su información llamando al método mostrar_info.

Lógica Principal:
En el bloque if __name__ == "__main__":, se crean instancias de Documento, Enlace y Carpeta, y se utiliza un bucle para interactuar con el usuario. El usuario puede elegir ver la información de un documento, un enlace, una carpeta o salir del programa.

En resumen, este código demuestra la implementación del patrón Composite, permitiendo la creación de estructuras jerárquicas de documentos y carpetas, donde una carpeta puede contener documentos o enlaces, y se puede acceder a la información de manera consistente a través de la interfaz común Component.


### El link del diagrama UML junto a una fotografía del mismo son los siguientes: 
uml composite: https://www.plantuml.com/plantuml/png/jL91IWGn4Bpd5Jcko7nWK5bGRuiV497UfCL0qXsI7Y_hFiet-35d9enXmpWtZrLTT5KglSy2IORW5Hop932YZOUSzJs7o8Ga-gIqFYtJixwEa92ahuhL-UtV0ewOG1pJxghN8wlEIXNJ0yBRxBUkgS6o4vo5dNbttYQaNXzSbkTVpxjf2rYxCuMvI3pkV6B2IP8my0TkgxRYFB0P0f9mYKCSZWcBPeJY8bS00Rw_Hkn89coO1CdPgaY3G06Rde_amU2geSKiZYutlZRaLhcG8WgihrvUcjkkN_wzwtgDDvzTDzz9mzMxQ0RrXzf1gR5XbmhK7iaEmVy0


<img width="901" alt="CAPTUML" src="https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/c825958e-6015-4867-af81-10df767a6ac5">



## Proxy: 


![codeproxy](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/745a34d4-767d-454e-afbf-2c25d6139086)



El código implementa un ejemplo de patrón Proxy junto con el uso de SQLite para gestionar una lista blanca de usuarios. A continuación, se explica detalladamente cómo funciona el código:

### Clases y Estructura de Datos:

#### Usuario: 
Representa un usuario con un nombre.

#### ListaBlancaSQLite: 
Gestiona la lista blanca de usuarios utilizando una base de datos SQLite. La base de datos contiene una tabla llamada usuarios con columnas id, nombre y estado. Tiene métodos para crear la tabla, agregar usuarios aleatorios y verificar si un usuario está en la lista blanca.

### Clases del Patrón Proxy:

#### Subject (Clase Abstracta): 
Define la interfaz común para los objetos reales y proxy. En este caso, representa el acceso a documentos, enlaces y carpetas.

#### RealSubjectDocumento, RealSubjectEnlace, RealSubjectCarpeta: 
Son las implementaciones reales de Subject. Cada uno de ellos tiene un método request que verifica el acceso del usuario antes de mostrar la información.

#### Proxy: 
Actúa como un intermediario para acceder a los objetos reales (RealSubject). Antes de permitir el acceso, verifica si el usuario está en la lista blanca.


### Lógica Principal:

Lógica Principal en if __name__ == "__main__"::
Se crea una instancia de ListaBlancaSQLite y se le agregan usuarios aleatorios a la lista blanca o denegada.

Se crean instancias de RealSubjectDocumento, RealSubjectEnlace, y RealSubjectCarpeta, y se crean sus respectivos proxies.

Se obtienen los usuarios de la base de datos y se verifica el acceso a través de los proxies para cada usuario.


### Ejecución del Proxy con SQLite:

#### Acceso a través del Proxy con SQLite:
Se muestra información sobre documentos, enlaces y carpetas para cada usuario.
El proxy verifica si cada usuario está en la lista blanca antes de permitir el acceso. Si no está en la lista blanca, se muestra un mensaje de acceso denegado.


### Uso de SQLite:
#### Uso de SQLite para la Lista Blanca:
Se utiliza SQLite para almacenar y gestionar la lista blanca de usuarios de manera persistente. La base de datos se crea si no existe y se agregan usuarios aleatorios.

En resumen, el código muestra cómo implementar un Proxy para controlar el acceso a documentos, enlaces y carpetas, y utiliza SQLite para gestionar dinámicamente una lista blanca de usuarios. Esto proporciona una capa adicional de seguridad al verificar el acceso a través del Proxy


### El link del diagrama UML junto a una fotografía del mismo son los siguientes: 
uml proxy: https://www.plantuml.com/plantuml/png/nPFFJiCm3CRlVOeSEy5UeE8myUUs0p1nZjp46q5fCXnd0W7lpj8sGuLsx8AujR7z-VivpY8m4CV65if22E8XH23ZnLiXn9dpJKrOYS1atARuAFgafGaCbnQSWjNTqZ2swNDTootmuo5V2Aa8WL4or1RBMTA43U46ICQkKP1W4TYdprA1OwD1Ly8uJjdoMtOvT7GkC31ed__R1kb8efFMf8-wTLdszLNccrMYzjuc9AW34oWM7Tigra-ek1i0uNF4m6FbEs_qrqJk4MnVUUrLRD2nxuOYXvRRepsJ2KnxlMJob4QfQeTaraO1IL0AWv-2IdgDJr0aZLlxyfZR6sT1uRHLZO6DyqFxaM4ay7yGLq1RP3X2aUya_Dt8GUloqASQtOWi_IlRBVcNrnw74AmCdLALrpD51XjU_NoK9ovmVl7p-OX4VWqNx_lm6D94HbwigN2-ia6ymouMw7Hix2S0


![capt proxy](https://github.com/carlospuigserver/Desarrollo-OO-2-/assets/91721643/08a7e743-9490-474c-af67-615c5296c693)
