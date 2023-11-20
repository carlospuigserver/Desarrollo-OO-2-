from abc import ABC, abstractmethod

# Producto
class CoccionPizza:
    def __init__(self):
        self.metodo = ""
        
    def __str__(self):
        return f"Método de cocción elegido: {self.metodo}"

# Builder abstracto
class BuilderCoccionPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_horno_lena(self):
        pass

    @abstractmethod
    def construir_horno_electrico(self):
        pass

    @abstractmethod
    def construir_piedra_pizzas(self):
        pass

    @abstractmethod
    def construir_parrilla_pizzas(self):
        pass

    @abstractmethod
    def obtener_coccion(self):
        pass

# Concrete Builder
class CoccionPizzaBuilder(BuilderCoccionPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.coccion = CoccionPizza()

    def construir_horno_lena(self):
        self.coccion.metodo = "Horno de leña"

    def construir_horno_electrico(self):
        self.coccion.metodo = "Horno eléctrico"

    def construir_piedra_pizzas(self):
        self.coccion.metodo = "Piedra para pizzas"

    def construir_parrilla_pizzas(self):
        self.coccion.metodo = "Parrilla para pizzas"

    def obtener_coccion(self):
        return self.coccion

# Director (Cliente)
class Cliente:
    def elegir_coccion(self, builder):
        print("Métodos de cocción disponibles:")
        metodos_coccion = [
            "Horno de leña",
            "Horno eléctrico",
            "Piedra para pizzas",
            "Parrilla para pizzas"
        ]

        print("Elija el método de cocción escribiendo su nombre:")
        for metodo in metodos_coccion:
            print(f"- {metodo}")

        metodo_elegido = input("Su elección: ").capitalize()

        if metodo_elegido == "Horno de leña":
            builder.construir_horno_lena()
        elif metodo_elegido == "Horno eléctrico":
            builder.construir_horno_electrico()
        elif metodo_elegido == "Piedra para pizzas":
            builder.construir_piedra_pizzas()
        elif metodo_elegido == "Parrilla para pizzas":
            builder.construir_parrilla_pizzas()
        else:
            print("Método de cocción no válido")

        return builder.obtener_coccion()

if __name__ == "__main__":
    builder = CoccionPizzaBuilder()
    cliente = Cliente()

    coccion_elegida = cliente.elegir_coccion(builder)
    print(coccion_elegida)