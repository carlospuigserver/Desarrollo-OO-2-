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
    with open('Usuario/usuario.csv', 'a', newline='') as file:
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
    with open('Usuario/usuario.csv', 'r') as file:
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
    nombre_archivo = "storage/menus.csv"

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