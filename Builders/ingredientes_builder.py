from abc import ABC, abstractmethod

# Producto
class IngredientesPizza:
    def __init__(self):
        self.queso = []
        self.carne = []
        self.mariscos = []
        self.vegetales = []
        
    def __str__(self):
        return (f"Ingredientes elegidos: "
                f"\nQueso: {', '.join(self.queso) if self.queso else 'Ninguno'}"
                f"\nCarne: {', '.join(self.carne) if self.carne else 'Ninguno'}"
                f"\nMariscos: {', '.join(self.mariscos) if self.mariscos else 'Ninguno'}"
                f"\nVegetales: {', '.join(self.vegetales) if self.vegetales else 'Ninguno'}")

# Builder abstracto
class BuilderIngredientesPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def anadir_queso(self):
        pass

    @abstractmethod
    def anadir_carne(self):
        pass

    @abstractmethod
    def anadir_mariscos(self):
        pass

    @abstractmethod
    def anadir_vegetales(self):
        pass

    @abstractmethod
    def obtener_ingredientes(self):
        pass

# Concrete Builder
class IngredientesPizzaBuilder(BuilderIngredientesPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.ingredientes = IngredientesPizza()

    def anadir_queso(self):
        print("¿Desea agregar queso? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            quesos = [
                "Mozzarella", "Parmesano", "Cheddar", "Gouda", "Provolone"
            ]
            print("Tipos de queso disponibles:")
            for queso in quesos:
                print(f"- {queso}")
            queso_elegido = input("Elija el tipo de queso: ").capitalize()
            if queso_elegido in quesos:
                self.ingredientes.queso.append(queso_elegido)
            else:
                print("Tipo de queso no válido")

    def anadir_carne(self):
        print("¿Desea agregar carne? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            carnes = [
                "Pepperoni", "Pollo", "Jamon", "Tocino"
            ]
            print("Tipos de carne disponibles:")
            for carne in carnes:
                print(f"- {carne}")
            carne_elegida = input("Elija el tipo de carne: ").capitalize()
            if carne_elegida in carnes:
                self.ingredientes.carne.append(carne_elegida)
            else:
                print("Tipo de carne no válido")

    def anadir_mariscos(self):
        print("¿Desea agregar mariscos? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            mariscos = [
                "Anchoas", "Camarones", "Mejillones", "Calamares"
            ]
            print("Tipos de mariscos disponibles:")
            for marisco in mariscos:
                print(f"- {marisco}")
            marisco_elegido = input("Elija el tipo de marisco: ").capitalize()
            if marisco_elegido in mariscos:
                self.ingredientes.mariscos.append(marisco_elegido)
            else:
                print("Tipo de marisco no válido")

    def anadir_vegetales(self):
        print("¿Desea agregar vegetales? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            vegetales = [
                "Champiñones", "Pimientos", "Cebolla", "Aceitunas", "Tomate", "Espinacas", "Alcachofas", "Berenjena"
            ]
            print("Tipos de vegetales disponibles:")
            for vegetal in vegetales:
                print(f"- {vegetal}")
            vegetal_elegido = input("Elija el tipo de vegetal: ").capitalize()
            if vegetal_elegido in vegetales:
                self.ingredientes.vegetales.append(vegetal_elegido)
            else:
                print("Tipo de vegetal no válido")

    def obtener_ingredientes(self):
        return self.ingredientes

# Cliente
# Cliente
class Cliente:
    def elegir_ingredientes(self, builder):
        print("Seleccione los ingredientes:")
        builder.anadir_queso()
        builder.anadir_carne()
        builder.anadir_mariscos()
        builder.anadir_vegetales()
        return builder.obtener_ingredientes()

if __name__ == "__main__":
    builder = IngredientesPizzaBuilder()
    cliente = Cliente()

    ingredientes_elegidos = cliente.elegir_ingredientes(builder)
    print(ingredientes_elegidos)