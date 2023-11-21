
from menu_selector import*

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

        elif opcion_menu == "2":
            
            
            
            class Restaurante:
                def restaurante(self):
                    
                    print("Excelente elección, a continuación se le mostrarán los menús disponibles")
                    ejecutar_pedido()
                    
                    


            
            
            
            
            
            
            
            
            
            
            if __name__ == "__main__":
                restaurante = Restaurante()
                restaurante.restaurante()


            