from abc import ABC, abstractmethod

# Producto
class SalsaPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de salsa elegida: {self.tipo}"

# Builder abstracto
class BuilderSalsaPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_salsa_tomate_clasica(self):
        pass

    @abstractmethod
    def construir_salsa_marinara(self):
        pass

    @abstractmethod
    def construir_salsa_pesto(self):
        pass

    @abstractmethod
    def construir_salsa_blanca(self):
        pass

    @abstractmethod
    def construir_salsa_bbq(self):
        pass

    @abstractmethod
    def construir_salsa_champinones(self):
        pass

    @abstractmethod
    def construir_salsa_tomate_sin_gluten(self):
        pass

    @abstractmethod
    def construir_salsa_autor(self):
        pass

    @abstractmethod
    def construir_salsa_edicion_limitada(self):
        pass

    @abstractmethod
    def obtener_salsa(self):
        pass

# Concrete Builder
class SalsaPizzaBuilder(BuilderSalsaPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.salsa = SalsaPizza()

    def construir_salsa_tomate_clasica(self):
        self.salsa.tipo = "Tomate Clásica"

    def construir_salsa_marinara(self):
        self.salsa.tipo = "Marinara"

    def construir_salsa_pesto(self):
        self.salsa.tipo = "Pesto"

    def construir_salsa_blanca(self):
        self.salsa.tipo = "Blanca"

    def construir_salsa_bbq(self):
        self.salsa.tipo = "BBQ"

    def construir_salsa_champinones(self):
        self.salsa.tipo = "Champiñones"

    def construir_salsa_tomate_sin_gluten(self):
        self.salsa.tipo = "Tomate sin gluten"

    def construir_salsa_autor(self):
        self.salsa.tipo = "Autor"

    def construir_salsa_edicion_limitada(self):
        self.salsa.tipo = "Edición Limitada"

    def obtener_salsa(self):
        return self.salsa

# Director (Cliente)
class Cliente:
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
            "Autor",
            "Edición Limitada"
        ]

        print("Elija el tipo de salsa escribiendo su nombre:")
        for tipo in tipos_salsa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

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
        elif tipo_elegido == "Edición Limitada":
            builder.construir_salsa_edicion_limitada()
        else:
            print("Tipo de salsa no válido")

        return builder.obtener_salsa()

if __name__ == "__main__":
    builder = SalsaPizzaBuilder()
    cliente = Cliente()

    salsa_elegida = cliente.elegir_salsa(builder)
    print(salsa_elegida)