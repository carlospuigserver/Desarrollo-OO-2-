# restaurante.py

from cliente import *

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
        opcion_menu = elegir_opcion_menu()

        if opcion_menu == "1":  # Pizza personalizada
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
             print(f"El usuario {nombre_usuario} ha elegido la masa {masa_elegida.tipo}")

            salsa_elegida = cliente.elegir_salsa(salsa_builder)
            if salsa_elegida:
                print(f"El usuario {nombre_usuario} ha elegido la salsa {salsa_elegida.tipo}")

                ingredientes_elegidos = cliente.elegir_ingredientes(ingredientes_builder)
                if ingredientes_elegidos:
                    print(f"El usuario {nombre_usuario} ha elegido los siguientes ingredientes:")
                    print(ingredientes_elegidos)

                    bebida_elegida = cliente.elegir_bebida(bebida_builder)
                    if bebida_elegida:
                        print(f"El usuario {nombre_usuario} ha elegido la bebida {bebida_elegida.tipo}")

                        coccion_elegida = cliente.elegir_coccion(coccion_builder)
                        if coccion_elegida:
                            print(f"El usuario {nombre_usuario} ha elegido la técnica de cocción {coccion_elegida.metodo}")

                            presentacion_elegida = cliente.elegir_presentacion(builder)
                            if presentacion_elegida:
                                print(f"El usuario {nombre_usuario} ha elegido la presentación {presentacion_elegida.tipo}")

                                extras_elegidos = cliente.elegir_extras(extras_builder)
                                print(f"Elegidos extras: {extras_elegidos}")

                                # Guardar los detalles del pedido en un archivo CSV (pizzas.csv)
                                with open('storage/pizzas.csv', 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow([
                                        nombre_usuario,
                                        f"Elegida masa: {masa_elegida.tipo}",
                                        f"Elegida salsa: {salsa_elegida.tipo}",
                                        f"Elegidos ingredientes: {ingredientes_elegidos}",
                                        f"Elegida bebida: {bebida_elegida.tipo}",
                                        f"Elegida tecnica de coccion: {coccion_elegida.metodo}",
                                        f"Elegida presentación: {presentacion_elegida.tipo}",
                                        f"Elegidos extras: {extras_elegidos}"
                                    ])
                                print("Detalles del pedido guardados en pizzas.csv")

            # Resto del código para la pizza personalizada...

        elif opcion_menu == "2":  # Menú predefinido
            # Agrega aquí el código para manejar el menú predefinido si es necesario
            print("Opción de menú predefinido seleccionada.")

        else:
            print("Opción no válida. Saliendo.")






                                