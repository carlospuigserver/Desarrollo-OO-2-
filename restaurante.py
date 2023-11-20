from Menus.menu_combo_pareja import *
from Menus.menu_halloween import *
from Menus.menu_ninos import *
from Menus.menu_simple import *
from Menus.menu_sanvalentin import *

from cliente import *
import csv






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

if __name__ == "__main__":
    registrar_nuevo_usuario()  # Registra un nuevo usuario

    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if autenticar_usuario(nombre_usuario, contraseña):
        # Crear un menú compuesto para gestionar la elección entre pizza personalizada y menú predefinido
        menu_pedido = MenuComposite("Pedido")

        opcion_menu = elegir_opcion_menu()

        if opcion_menu == "1":  # Pizza personalizada
            # Crear un menú compuesto para gestionar la pizza personalizada
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

                                # Mostrar el resumen del pedido
                                print(f"Resumen del Pedido: {menu_pedido.operation()}")

                                # Guardar los detalles de la pizza personalizada en un archivo CSV (pizzas.csv)
                                with open('storage/pizzas.csv', 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow([
                                        nombre_usuario,
                                        f"Elegida masa: {masa_elegida.tipo}",
                                        f"Elegida salsa: {salsa_elegida.tipo}",
                                        f"Elegidos ingredientes: {ingredientes_elegidos}",
                                        f"Elegida bebida: {bebida_elegida.tipo}",
                                        f"Elegida técnica de cocción: {coccion_elegida.metodo}",
                                        f"Elegida presentación: {presentacion_elegida.tipo}",
                                        f"Elegidos extras: {extras_elegidos}"
                                    ])
                                print("Detalles de la pizza personalizada guardados en pizzas.csv")

        elif opcion_menu == "2":  # Menú predefinido
            print("Seleccione un menú predefinido:")
            print("1. Menú Normal")
            print("2. Menú Niños")
            print("3. Menú Combo Pareja")
            print("4. Menú Halloween")
            print("5. Menú San Valentín")

            opcion_menu_predefinido = input("Seleccione la opción (1-5): ")

            if opcion_menu_predefinido in ["1", "2", "3", "4", "5"]:
                # Crear un menú compuesto para gestionar el menú predefinido seleccionado
                menu_predefinido = MenuComposite("Menú Predefinido")

                if opcion_menu_predefinido == "1":
                    for componente in bebidas_n + primeros_platos_n + segundos_platos_n + postres_n:
                        menu_predefinido.add(componente)
                elif opcion_menu_predefinido == "2":
                    for componente in bebidas_ninos + primeros_platos_ninos + segundos_platos_ninos + postres_ninos:
                        menu_predefinido.add(componente)
                elif opcion_menu_predefinido == "3":
                    for componente in bebidas_pareja + primeros_platos_pareja + segundos_platos_pareja + postres_pareja:
                        menu_predefinido.add(componente)
                elif opcion_menu_predefinido == "4":
                    for componente in bebidas_halloween + primeros_platos_halloween + segundos_platos_halloween + postres_halloween:
                        menu_predefinido.add(componente)
                elif opcion_menu_predefinido == "5":
                    for componente in bebidas_san_valentin + primeros_platos_valentin + segundo_platos_valentin + postres_san_valentin:
                        menu_predefinido.add(componente)

                # Solicitar al cliente que elija opciones del menú predefinido
                bebida_cliente = mostrar_opciones(menu_predefinido.get_opciones_tipo("Bebida"), "Bebida")
                primer_plato_cliente = mostrar_opciones(menu_predefinido.get_opciones_tipo("Primer Plato"), "Primer Plato")
                segundo_plato_cliente = mostrar_opciones(menu_predefinido.get_opciones_tipo("Segundo Plato"), "Segundo Plato")
                postre_cliente = mostrar_opciones(menu_predefinido.get_opciones_tipo("Postre"), "Postre")
                # Mostrar el resumen del menú predefinido
                print(f"Resumen del Menú Predefinido: {menu_predefinido.operation()}")

                # Guardar los detalles del menú predefinido en un archivo CSV (menus.csv)
                with open('storage/menus.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        nombre_usuario,
                        f"Menú Predefinido: {menu_predefinido.nombre}",
                        f"Detalles: {menu_predefinido.operation()}"
                    ])
                print("Detalles del menú predefinido guardados en menus.csv")

    else:
        print("Opción no válida. Saliendo.")
