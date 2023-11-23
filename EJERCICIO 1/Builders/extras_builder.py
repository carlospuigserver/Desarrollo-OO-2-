from abc import ABC, abstractmethod

# Producto
class ExtrasPizza:
    def __init__(self):
        self.borde_relleno = ""
        self.ingredientes_gourmet = []

    def __str__(self):
        return f"Borde relleno: {self.borde_relleno}, Ingredientes gourmet: {self.ingredientes_gourmet}"

# Builder abstracto
class BuilderExtrasPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def anadir_borde_relleno(self, opcion):
        pass

    @abstractmethod
    def anadir_ingredientes_gourmet(self, opcion):
        pass

    @abstractmethod
    def obtener_extras(self):
        pass

# Concrete Builder
class ExtrasPizzaBuilder(BuilderExtrasPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.extras = ExtrasPizza()

    def anadir_borde_relleno(self, opcion):
        self.extras.borde_relleno = opcion

    def anadir_ingredientes_gourmet(self, opcion):
        self.extras.ingredientes_gourmet.append(opcion)

    def obtener_extras(self):
        return self.extras

# Director (Cliente)
class Cliente:
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

        # Preguntar si desea borde relleno
        quiere_borde_relleno = input("¿Desea su borde relleno? (Sí/No): ")

        # Si sí, mostrar opciones y obtener elección
        if quiere_borde_relleno.lower() == "sí":
            print("Opciones de borde relleno disponibles:")
            for key, value in opciones_borde.items():
                print(f"{key}. {value}")
            borde_elegido = opciones_borde.get(input("Su elección (borde relleno) (numero 1-5): "), "")
            builder.anadir_borde_relleno(borde_elegido)

        # Preguntar si desea ingredientes gourmet
        quiere_ingredientes_gourmet = input("¿Desea algún ingrediente gourmet? (Sí/No): ")
        ingredientes_elegidos = []

        # Si sí, mostrar opciones y obtener elección
        while quiere_ingredientes_gourmet.lower() == "sí":
            print("Opciones de ingredientes gourmet disponibles:")
            for key, value in opciones_ingredientes.items():
                print(f"{key}. {value}")
            ingrediente = input("Su elección (ingrediente gourmet) (numero 1-8): ")
            ingrediente_elegido = opciones_ingredientes.get(ingrediente, "")
            if ingrediente_elegido:
                ingredientes_elegidos.append(ingrediente_elegido)
            else:
                print("Opción de ingrediente no válida.")
            quiere_ingredientes_gourmet = input("¿Desea otro ingrediente gourmet? (Sí/No): ")

        builder.anadir_ingredientes_gourmet(ingredientes_elegidos)
        return builder.obtener_extras()
if __name__ == "__main__":
    builder = ExtrasPizzaBuilder()
    cliente = Cliente()

    extras_elegidos = cliente.elegir_extras(builder)
    print(extras_elegidos)