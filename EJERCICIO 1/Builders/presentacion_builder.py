from abc import ABC, abstractmethod

# Producto
class PresentacionPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de presentación elegida: {self.tipo}"

# Builder abstracto
class BuilderPresentacionPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_tabla_madera(self):
        pass

    @abstractmethod
    def construir_plato_ceramica_clasica(self):
        pass

    @abstractmethod
    def construir_plataforma_plata(self):
        pass

    @abstractmethod
    def construir_plataforma_oro(self):
        pass

    @abstractmethod
    def construir_plato_cristal(self):
        pass

    @abstractmethod
    def construir_sobre_piedra(self):
        pass

    @abstractmethod
    def construir_plato_terracota(self):
        pass

    @abstractmethod
    def construir_plato_porcelana(self):
        pass

    @abstractmethod
    def obtener_presentacion(self):
        pass

# Concrete Builder
class PresentacionPizzaBuilder(BuilderPresentacionPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.presentacion = PresentacionPizza()

    def construir_tabla_madera(self):
        self.presentacion.tipo = "Tabla de madera"

    def construir_plato_ceramica_clasica(self):
        self.presentacion.tipo = "Plato de cerámica clásica"

    def construir_plataforma_plata(self):
        self.presentacion.tipo = "Sobre plataforma de plata"

    def construir_plataforma_oro(self):
        self.presentacion.tipo = "Sobre plataforma de oro"

    def construir_plato_cristal(self):
        self.presentacion.tipo = "Plato de cristal"

    def construir_sobre_piedra(self):
        self.presentacion.tipo = "Sobre piedra"

    def construir_plato_terracota(self):
        self.presentacion.tipo = "Plato de terracota"

    def construir_plato_porcelana(self):
        self.presentacion.tipo = "Plato de porcelana"

    def obtener_presentacion(self):
        return self.presentacion

# Director (Cliente)
class Cliente:
    def elegir_presentacion(self, builder):
        print("Opciones de presentación disponibles:")
        opciones_presentacion = [
            "Tabla de madera",
            "Plato de cerámica clásica",
            "Sobre plataforma de plata",
            "Sobre plataforma de oro",
            "Plato de cristal",
            "Sobre piedra",
            "Plato de terracota",
            "Plato de porcelana"
        ]

        print("Elija el tipo de presentación escribiendo su nombre o número:")
        for idx, opcion in enumerate(opciones_presentacion, start=1):
            print(f"{idx}. {opcion}")

        opcion_elegida = input("Su elección: ").capitalize()

        if opcion_elegida == "Tabla de madera" or opcion_elegida == "1":
            builder.construir_tabla_madera()
        elif opcion_elegida == "Plato de cerámica clásica" or opcion_elegida == "2":
            builder.construir_plato_ceramica_clasica()
        elif opcion_elegida == "Sobre plataforma de plata" or opcion_elegida == "3":
            builder.construir_plataforma_plata()
        # Continuar con las demás opciones en un flujo similar

        return builder.obtener_presentacion()

if __name__ == "__main__":
    builder = PresentacionPizzaBuilder()
    cliente = Cliente()

    presentacion_elegida = cliente.elegir_presentacion(builder)
    print(presentacion_elegida)