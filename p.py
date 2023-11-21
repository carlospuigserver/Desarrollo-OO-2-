from menu_selector import*
from postre_builder import *
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
                                

                                #preguntar si quiere postre
                                print("¿Desea agregar un postre?")
                                print("1. Si")
                                print("2. No")
                                opcion = input("Seleccione la opción (1 o 2): ")
                                if opcion == "1":
                                            from abc import ABC, abstractmethod

                                            # Producto
                                            class Postre:
                                                def __init__(self, nombre, precio):
                                                    self.nombre = nombre
                                                    self.precio = precio

                                                def __str__(self):
                                                    return f"{self.nombre} - ${self.precio:.2f}"

                                            class BuilderPostre(ABC):
                                                @abstractmethod
                                                def reset(self):
                                                    pass

                                                @abstractmethod
                                                def construir_mochi_ice_cream(self):
                                                    pass

                                                @abstractmethod
                                                def construir_baklava(self):
                                                    pass

                                                @abstractmethod
                                                def construir_dulce_tres_leches_coco(self):
                                                    pass

                                                @abstractmethod
                                                def construir_sorvete_acai(self):
                                                    pass

                                                @abstractmethod
                                                def construir_anmitsu(self):
                                                    pass

                                                @abstractmethod
                                                def construir_kulfi(self):
                                                    pass

                                                @abstractmethod
                                                def construir_knafeh(self):
                                                    pass

                                                @abstractmethod
                                                def construir_tiramisu(self):
                                                    pass

                                                @abstractmethod
                                                def construir_panna_cotta(self):
                                                    pass

                                                @abstractmethod
                                                def construir_pastel_chocolate(self):
                                                    pass

                                                @abstractmethod
                                                def construir_cheesecake(self):
                                                    pass

                                                @abstractmethod
                                                def construir_mousse_frambuesa(self):
                                                    pass

                                                @abstractmethod
                                                def construir_tarta_limon(self):
                                                    pass

                                                @abstractmethod
                                                def construir_profiteroles(self):
                                                    pass

                                                def obtener_postre(self):
                                                    pass

                                            # Concrete Builder
                                            class PostreBuilder(BuilderPostre):
                                                def __init__(self):
                                                    self.reset()

                                                def reset(self):
                                                    self.postre = Postre("", 0.0)

                                                def construir_mochi_ice_cream(self):
                                                    self.postre = Postre("Mochi Ice Cream", 5.99)

                                                def construir_baklava(self):
                                                    self.postre = Postre("Baklava", 7.99)

                                                def construir_dulce_tres_leches_coco(self):
                                                    self.postre = Postre("Dulce de Tres Leches con Coco", 6.99)

                                                def construir_sorvete_acai(self):
                                                    self.postre = Postre("Sorvete de Açaí", 8.99)

                                                def construir_anmitsu(self):
                                                    self.postre = Postre("Anmitsu", 7.49)

                                                def construir_kulfi(self):
                                                    self.postre = Postre("Kulfi", 6.79)

                                                def construir_knafeh(self):
                                                    self.postre = Postre("Knafeh", 9.99)

                                                def construir_tiramisu(self):
                                                    self.postre = Postre("Tiramisú", 8.49)

                                                def construir_panna_cotta(self):
                                                    self.postre = Postre("Panna Cotta", 7.29)

                                                def construir_pastel_chocolate(self):
                                                    self.postre = Postre("Pastel de Chocolate", 10.99)

                                                def construir_cheesecake(self):
                                                    self.postre = Postre("Cheesecake", 9.79)

                                                def construir_mousse_frambuesa(self):
                                                    self.postre = Postre("Mousse de Frambuesa", 8.99)

                                                def construir_tarta_limon(self):
                                                    self.postre = Postre("Tarta de Limón", 7.89)

                                                def construir_profiteroles(self):
                                                    self.postre = Postre("Profiteroles", 6.49)

                                                def obtener_postre(self):
                                                    return self.postre


                                            class Cliente:
                                                def elegir_postre(self, builder):
                                                    print("Tipos de postres disponibles:")
                                                    tipos_postres = [
                                                        "Mochi Ice Cream",
                                                        "Baklava",
                                                        "Dulce de Tres Leches con Coco",
                                                        "Sorvete de Açaí",
                                                        "Anmitsu",
                                                        "Kulfi",
                                                        "Knafeh",
                                                        "Tiramisú",
                                                        "Panna Cotta",
                                                        "Pastel de Chocolate",
                                                        "Cheesecake",
                                                        "Mousse de Frambuesa",
                                                        "Tarta de Limón",
                                                        "Profiteroles"
                                                    ]
                                                    print("Elija el tipo de postre escribiendo su nombre:")
                                                    for tipo in tipos_postres:
                                                        print(f"- {tipo}")

                                                    tipo_elegido = input("Su elección: ").capitalize()
                                                    if tipo_elegido == "Mochi Ice Cream":
                                                        builder.construir_mochi_ice_cream()
                                                    elif tipo_elegido == "Baklava":
                                                        builder.construir_baklava()
                                                    elif tipo_elegido == "Dulce de Tres Leches con Coco":
                                                        builder.construir_dulce_tres_leches_coco()
                                                    elif tipo_elegido == "Sorvete de Açaí":
                                                        builder.construir_sorvete_acai()
                                                    elif tipo_elegido == "Anmitsu":
                                                        builder.construir_anmitsu()
                                                    elif tipo_elegido == "Kulfi":
                                                        builder.construir_kulfi()
                                                    elif tipo_elegido == "Knafeh":
                                                        builder.construir_knafeh()
                                                    elif tipo_elegido == "Tiramisú":
                                                        builder.construir_tiramisu()
                                                    elif tipo_elegido == "Panna Cotta":
                                                        builder.construir_panna_cotta()
                                                    elif tipo_elegido == "Pastel de Chocolate":
                                                        builder.construir_pastel_chocolate()
                                                    elif tipo_elegido == "Cheesecake":
                                                        builder.construir_cheesecake()
                                                    elif tipo_elegido == "Mousse de Frambuesa":
                                                        builder.construir_mousse_frambuesa()
                                                    elif tipo_elegido == "Tarta de Limón":
                                                        builder.construir_tarta_limon()
                                                    elif tipo_elegido == "Profiteroles":
                                                        builder.construir_profiteroles()
                                                    else:
                                                        print("No se ha encontrado el tipo de postre elegido.")


                                            if __name__ == "__main__":
                                                builder = PostreBuilder()
                                                director = Cliente()
                                                director.elegir_postre(builder)
                                                postre = builder.obtener_postre()
                                                print(f"Postre elegido: {postre}")

                                            # Calcular precio total
                                            precio_pizza = 25  # Precio fijo por la elección de la pizza personalizada
                                            precio_postre = postre.precio if postre else 0
                                            precio_total = precio_pizza + precio_postre

                                            # Agregar el postre al menú compuesto de pedido
                                            menu_pedido.add(postre)

                                            # Mostrar el resumen del pedido
                                            print(f"Resumen del Pedido: {menu_pedido.operation()}")
                                            print(f"El precio total es de: ${precio_total:.2f}")

                                            # Guardar los detalles del pedido en un archivo CSV (pedidos.csv)
                                            with open('storage/pedidos.csv', 'a', newline='') as file:
                                                writer = csv.writer(file)
                                                writer.writerow([
                                                    nombre_usuario,
                                                    f"Detalles de la pizza personalizada: {pizza_personalizada.operation()}",
                                                    f"Postre elegido: {postre.operation() if postre else 'Ninguno'}",
                                                    f"Precio total: ${precio_total:.2f}"
                                                ])
                                            print("Detalles del pedido guardados en pedidos.csv")

                                        