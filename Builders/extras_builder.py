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
        quiere_borde_relleno = input("¿Desea su borde relleno? (Sí/No): ")
        if quiere_borde_relleno.lower() == "sí":
            print("¿Qué borde relleno desea?")
            print("1. Relleno de queso")
            print("2. Ajo y queso parmesano")
            print("3. Crust de queso")
            print("4. Relleno de pepperoni o jamón")
            print("5. Relleno de verduras")

            borde = input("Su elección (borde relleno): ")
            opciones_borde = {
                "1": "Relleno de queso",
                "2": "Ajo y queso parmesano",
                "3": "Crust de queso",
                "4": "Relleno de pepperoni o jamón",
                "5": "Relleno de verduras"
            }
            builder.anadir_borde_relleno(opciones_borde.get(borde, ""))

        quiere_ingredientes_gourmet = input("¿Desea algún ingrediente gourmet? (Sí/No): ")
        if quiere_ingredientes_gourmet.lower() == "sí":
            print("¿Qué ingrediente gourmet desea?")
            print("1. Trufas")
            print("2. Caviar")
            print("3. Foie Gras")
            print("4. Jamón Ibérico")
            print("5. Quesos exclusivos")
            print("6. Setas silvestres")
            print("7. Mariscos de alta calidad")
            print("8. Verduras orgánicas y raras")

            ingrediente = input("Su elección (ingrediente gourmet): ")
            opciones_ingredientes = {
                "1": "Trufas",
                "2": "Caviar",
                "3": "Foie Gras",
                "4": "Jamón Ibérico",
                "5": "Quesos exclusivos",
                "6": "Setas silvestres",
                "7": "Mariscos de alta calidad",
                "8": "Verduras orgánicas y raras"
            }
            builder.anadir_ingredientes_gourmet(opciones_ingredientes.get(ingrediente, ""))

        return builder.obtener_extras()

if __name__ == "__main__":
    builder = ExtrasPizzaBuilder()
    cliente = Cliente()

    extras_elegidos = cliente.elegir_extras(builder)
    print(extras_elegidos)