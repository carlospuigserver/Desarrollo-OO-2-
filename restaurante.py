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
                    def ejecutar_pedido():
                        
                        print("Excelente elección!!!")
                        print("¿Qué menú desea ver?")
                        print("1. Menú Normal")
                        print("2. Menú Niños")
                        print("3. Menú Halloween")
                        print("4. Menú San Valentín")
                        print("5. Menú Combo Pareja")
                        
                        opcion = int(input("Ingrese el número del menú que desea tomar: "))

                        if opcion == 1:
                         if __name__ == "__main__":
                            # Crear el menú normal
                            menu_normal = MenuSimple("Menú Simple")

                            # Agregar opciones al menú normal
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
                            

                            
                            
                        elif opcion == 2:
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


                        elif opcion == 3:
                            if __name__ == "__main__":
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

                        
                        elif opcion == 4:
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


                        elif opcion == 5:
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

                    ejecutar_pedido()

                