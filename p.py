import csv
from Builders.masa_builder import MasaPizzaBuilder
from Builders.salsa_builder import SalsaPizzaBuilder
from Builders.ingredientes_builder import IngredientesPizzaBuilder
from Builders.maridajes_builder import BebidaPizzaBuilder
from Builders.coccion_builder import CoccionPizzaBuilder
from Builders.presentacion_builder import PresentacionPizzaBuilder
from Builders.extras_builder import ExtrasPizzaBuilder
from menu_selector import*
def elegir_opcion_menu():
    print("¿Qué desea ordenar?")
    print("1. Pizza personalizada")
    print("2. Menú predefinido")
    opcion = input("Seleccione la opción (1 o 2): ")
   

    if opcion == "1":
        def registrar_nuevo_usuario():
            nombre_usuario = input("Introduce tu nombre de usuario: ")
            contraseña = input("Introduce tu contraseña: ")

            with open('Usuario/usuario.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nombre_usuario, contraseña])
                print(f"El usuario '{nombre_usuario}' se ha registrado con éxito.")

        # Función para autenticar un usuario
        def autenticar_usuario(nombre_usuario, contraseña):
            with open('Usuario/usuario.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 2:  # Verifica si la lista tiene al menos dos elementos
                        if row[0] == nombre_usuario and row[1] == contraseña:
                            print(f"¡Bienvenido, {nombre_usuario}!")
                            return True

            print("Nombre de usuario o contraseña incorrectos.")
            return False

        class Cliente:
            def elegir_masa(self, builder):
                print("Tipos de masa disponibles:")
                tipos_masa = [
                    "Delgada",
                    "48 Horas",
                    "Madre",
                    "Poolish",
                    "Napolitana",
                    "New York Style",
                    "Chicago Style",
                    "Siciliana",
                    "Cracker"
                ]

                print("Elija el tipo de masa escribiendo su nombre:")
                for tipo in tipos_masa:
                    print(f"- {tipo}")

                tipo_elegido = input("Su elección: ").capitalize()

                if tipo_elegido in tipos_masa:
                    if tipo_elegido == "Delgada":
                        builder.construir_masa_delgada()
                    elif tipo_elegido == "48 Horas":
                        builder.construir_masa_48_horas()
                    elif tipo_elegido == "Madre":
                        builder.construir_masa_madre()
                    elif tipo_elegido == "Poolish":
                        builder.construir_masa_poolish()
                    elif tipo_elegido == "Napolitana":
                        builder.construir_masa_napolitana()
                    elif tipo_elegido == "New York Style":
                        builder.construir_masa_new_york_style()
                    elif tipo_elegido == "Chicago Style":
                        builder.construir_masa_chicago_style()
                    elif tipo_elegido == "Siciliana":
                        builder.construir_masa_siciliana()
                    elif tipo_elegido == "Cracker":
                        builder.construir_masa_cracker()
                    else:
                        print("Tipo de salsa no válido")
                        return None

                    return builder.obtener_masa()

                else:
                    print("Tipo de masa no disponible")
                    return None
                

            def elegir_salsa(self, builder):
                print("Tipos de salsa disponibles:")
                tipos_salsa = [
                    "Tomate Clásica",
                    "Marinara",
                    "Pesto",
                    "Blanca",
                    "BBQ",
                    "Champiñones",
                    "Tomate sin gluten",
                    "Autor"
                    
                ]

                print("Elija el tipo de salsa escribiendo su nombre:")
                for tipo in tipos_salsa:
                    print(f"- {tipo}")

                tipo_elegido = input("Su elección: ").capitalize()

                if tipo_elegido in tipos_salsa:
                    if tipo_elegido == "Tomate Clásica":
                        builder.construir_salsa_tomate_clasica()
                    elif tipo_elegido == "Marinara":
                        builder.construir_salsa_marinara()
                    elif tipo_elegido == "Pesto":
                        builder.construir_salsa_pesto()
                    elif tipo_elegido == "Blanca":
                        builder.construir_salsa_blanca()
                    elif tipo_elegido == "BBQ":
                        builder.construir_salsa_bbq()
                    elif tipo_elegido == "Champiñones":
                        builder.construir_salsa_champinones()
                    elif tipo_elegido == "Tomate sin gluten":
                        builder.construir_salsa_tomate_sin_gluten()
                    elif tipo_elegido == "Autor":
                        builder.construir_salsa_autor()
                    else:
                        print("Tipo de salsa no válido")
                        return None

                    return builder.obtener_salsa()

                else:
                    print("Tipo de salsa no disponible")
                    return None

            def elegir_ingredientes(self, builder):
                while True:
                    print("Seleccione los ingredientes para la pizza:")
                    builder.anadir_queso()
                    builder.anadir_carne()
                    builder.anadir_mariscos()
                    builder.anadir_vegetales()

                    respuesta = input("¿Desea agregar más ingredientes? (Sí/No): ").lower()
                    if respuesta != 'sí' and respuesta != 'si':
                        break
                return builder.obtener_ingredientes()
            
            def elegir_bebida(self, builder):
                print("Tipos de bebidas disponibles:")
                tipos_bebida = [
                    "Vino Blanco",
                    "Vino Tinto",
                    "Vino Rosado",
                    "Cerveza",
                    "Coctel"
                ]

                print("Elija el tipo de bebida escribiendo su nombre:")
                for tipo in tipos_bebida:
                    print(f"- {tipo}")

                tipo_elegido = input("Su elección: ").capitalize()

                if tipo_elegido == "Vino Blanco":
                    builder.construir_vino_blanco()
                elif tipo_elegido == "Vino Tinto":
                    builder.construir_vino_tinto()
                elif tipo_elegido == "Vino Rosado":
                    builder.construir_vino_rosado()
                elif tipo_elegido == "Cerveza":
                    builder.construir_cerveza()
                elif tipo_elegido == "Coctel":
                    builder.construir_coctel()
                else:
                    print("Tipo de bebida no válido")

                return builder.obtener_bebida()

            
            def elegir_coccion(self, builder):
                print("Métodos de cocción disponibles:")
                metodos_coccion = [
                    "Horno de lena",
                    "Horno eléctrico",
                    "Piedra para pizzas",
                    "Parrilla para pizzas"
                ]

                print("Elija el método de cocción escribiendo su nombre:")
                for metodo in metodos_coccion:
                    print(f"- {metodo}")

                metodo_elegido = input("Su elección: ").capitalize()

                if metodo_elegido == "Horno de lena":
                    builder.construir_horno_lena()
                elif metodo_elegido == "Horno electrico":
                    builder.construir_horno_electrico()
                elif metodo_elegido == "Piedra para pizzas":
                    builder.construir_piedra_pizzas()
                elif metodo_elegido == "Parrilla para pizzas":
                    builder.construir_parrilla_pizzas()
                else:
                    print("Método de cocción no válido")

                return builder.obtener_coccion()
            
            def elegir_presentacion(self, builder):
                print("Opciones de presentación disponibles:")
                opciones_presentacion = [
                    "Tabla de madera",
                    "Plato de cerámica clasica",
                    "Sobre plataforma de plata",
                    "Sobre plataforma de oro",
                    "Plato de cristal",
                    "Sobre piedra",
                    "Plato de terracota",
                    "Plato de porcelana"
                ]

                print("Elija el tipo de presentación escribiendo su nombre :")
                for idx, opcion in enumerate(opciones_presentacion, start=1):
                    print(f"{idx}. {opcion}")

                opcion_elegida = input("Su elección: ").capitalize()

                if opcion_elegida == "Tabla de madera" :
                    builder.construir_tabla_madera()
                elif opcion_elegida == "Plato de cerámica clásica" :
                    builder.construir_plato_ceramica_clasica()
                elif opcion_elegida == "Sobre plataforma de plata" :
                    builder.construir_plataforma_plata()
                elif opcion_elegida == "Sobre plataforma de oro":
                    builder.construir_plataforma_oro()
                elif opcion_elegida == "Plato de cristal" :
                    builder.construir_plato_cristal()
                elif opcion_elegida == "Sobre piedra" :
                    builder.construir_sobre_piedra()
                elif opcion_elegida == "Plato de terracota" :
                    builder.construir_plato_terracota()
                elif opcion_elegida == "Plato de porcelana"  :
                    builder.construir_plato_porcelana()
                else:
                    print("Opción de presentación no válida")

                return builder.obtener_presentacion()
            
            def elegir_extras(self, builder):
                opciones_borde = {
                    "1": "Relleno de queso",
                    "2": "Ajo y queso parmesano",
                    "3": "Crust de queso",
                    "4": "Relleno de pepperoni o jamón",
                    "5": "Relleno de verduras"
                }

                opciones_ingredientes = {
                    "1": "Trufas",
                    "2": "Caviar",
                    "3": "Foie Gras",
                    "4": "Jamón Iberico",
                    "5": "Quesos exclusivos",
                    "6": "Setas silvestres",
                    "7": "Mariscos de alta calidad",
                    "8": "Verduras orgánicas y raras"
                }

                quiere_borde_relleno = input("¿Desea su borde relleno? (Sí/No): ")
                borde_elegido = opciones_borde.get(input("Su elección (borde relleno) (numero 1-5) : "), "")

                quiere_ingredientes_gourmet = input("¿Desea algún ingrediente gourmet? (Sí/No): ")
                ingredientes_elegidos = []
                
                while quiere_ingredientes_gourmet.lower() == "sí":
                    ingrediente = input("Su elección (ingrediente gourmet) (numero 1-8): ")
                    ingrediente_elegido = opciones_ingredientes.get(ingrediente, "")
                    if ingrediente_elegido:
                        ingredientes_elegidos.append(ingrediente_elegido)
                    else:
                        print("Opción de ingrediente no válida.")
                    quiere_ingredientes_gourmet = input("¿Desea otro ingrediente gourmet? (Sí/No): ")

                builder.anadir_borde_relleno(borde_elegido)
                builder.anadir_ingredientes_gourmet(ingredientes_elegidos)
                return builder.obtener_extras()


            

        if __name__ == "__main__":
            masa_builder = MasaPizzaBuilder()
            salsa_builder = SalsaPizzaBuilder()
            ingredientes_builder = IngredientesPizzaBuilder()
            bebida_builder = BebidaPizzaBuilder()
            coccion_builder = CoccionPizzaBuilder()
            builder = PresentacionPizzaBuilder()
            extras_builder = ExtrasPizzaBuilder()
            cliente = Cliente()

            registrar_nuevo_usuario()  # Registra un nuevo usuario

            nombre_usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")

            if autenticar_usuario(nombre_usuario, contraseña):
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

    elif opcion == "2": 
        
     if __name__ == "__main__":   
      nombre_usuario = input("Nombre de usuario: ")
      contraseña = input("Contraseña: ")
      autenticar_usuario(nombre_usuario, contraseña)

      if autenticar_usuario(nombre_usuario, contraseña):
        # Pasa el nombre de usuario como parámetro a ejecutar_pedido
         ejecutar_pedido(nombre_usuario)
      else:
        print("Usuario no autenticado. Verifique el nombre de usuario y la contraseña.")
             
            
       
         

        
                
            
            
            
            
            
            
            
            
        


if __name__ == "__main__":
    elegir_opcion_menu( )