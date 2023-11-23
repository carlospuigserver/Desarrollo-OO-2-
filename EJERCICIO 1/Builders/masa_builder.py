from abc import ABC, abstractmethod

# Producto
class MasaPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de masa elegida: {self.tipo}"

# Builder abstracto
class BuilderMasaPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_masa_delgada(self):
        pass

    @abstractmethod
    def construir_masa_48_horas(self):
        pass

    @abstractmethod
    def construir_masa_madre(self):
        pass

    @abstractmethod
    def construir_masa_poolish(self):
        pass

    @abstractmethod
    def construir_masa_napolitana(self):
        pass

    @abstractmethod
    def construir_masa_new_york_style(self):
        pass

    @abstractmethod
    def construir_masa_chicago_style(self):
        pass

    @abstractmethod
    def construir_masa_siciliana(self):
        pass

    @abstractmethod
    def construir_masa_cracker(self):
        pass

    @abstractmethod
    def obtener_masa(self):
        pass

# Concrete Builder
class MasaPizzaBuilder(BuilderMasaPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.masa = MasaPizza()

    def construir_masa_delgada(self):
        self.masa.tipo = "Delgada"

    def construir_masa_48_horas(self):
        self.masa.tipo = "48 Horas"

    def construir_masa_madre(self):
        self.masa.tipo = "Madre"

    def construir_masa_poolish(self):
        self.masa.tipo = "Poolish"

    def construir_masa_napolitana(self):
        self.masa.tipo = "Napolitana"

    def construir_masa_new_york_style(self):
        self.masa.tipo = "New York Style"

    def construir_masa_chicago_style(self):
        self.masa.tipo = "Chicago Style"

    def construir_masa_siciliana(self):
        self.masa.tipo = "Siciliana"

    def construir_masa_cracker(self):
        self.masa.tipo = "Cracker"

    def obtener_masa(self):
        return self.masa

# Director (Cliente)
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
            print("Tipo de masa no válido")

        return builder.obtener_masa()

if __name__ == "__main__":
    builder = MasaPizzaBuilder()
    cliente = Cliente()

    masa_elegida = cliente.elegir_masa(builder)
    print(masa_elegida)