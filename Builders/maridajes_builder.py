from abc import ABC, abstractmethod

# Producto
class BebidaPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de bebida elegida: {self.tipo}"

# Builder abstracto
class BuilderBebidaPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_vino_blanco(self):
        pass

    @abstractmethod
    def construir_vino_tinto(self):
        pass

    @abstractmethod
    def construir_vino_rosado(self):
        pass

    @abstractmethod
    def construir_cerveza(self):
        pass

    @abstractmethod
    def construir_coctel(self):
        pass

    @abstractmethod
    def obtener_bebida(self):
        pass

# Concrete Builder
class BebidaPizzaBuilder(BuilderBebidaPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.bebida = BebidaPizza()

    def construir_vino_blanco(self):
        self.bebida.tipo = "Vino Blanco"

    def construir_vino_tinto(self):
        self.bebida.tipo = "Vino Tinto"

    def construir_vino_rosado(self):
        self.bebida.tipo = "Vino Rosado"

    def construir_cerveza(self):
        self.bebida.tipo = "Cerveza"

    def construir_coctel(self):
        self.bebida.tipo = "Coctel"

    def obtener_bebida(self):
        return self.bebida

# Cliente
class Cliente:
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

if __name__ == "__main__":
    builder = BebidaPizzaBuilder()
    cliente = Cliente()

    bebida_elegida = cliente.elegir_bebida(builder)
    print(bebida_elegida)