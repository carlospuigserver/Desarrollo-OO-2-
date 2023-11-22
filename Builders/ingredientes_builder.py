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
        print("¿Desea agregar queso? (Sí-1/No-2)")
        respuesta = input()
        if respuesta.lower() == "1" or respuesta.lower() == "1":
            quesos = [
                "Mozzarella", "Parmesano", "Cheddar", "Gouda", "Provolone"
            ]
            print("Tipos de queso disponibles:")
            for i, queso in enumerate(quesos, start=1):
                print(f"{i}. {queso}")

            opcion = input("Elija el tipo de queso escribiendo el número o el nombre: ")
            queso_elegido = quesos[int(opcion) - 1] if opcion.isdigit() and 1 <= int(opcion) <= len(quesos) else opcion.capitalize()

            if queso_elegido in quesos:
                self.ingredientes.queso.append(queso_elegido)
            else:
                print("Tipo de queso no válido")

    def anadir_carne(self):
        print("¿Desea agregar carne? (Sí-1/No-2)")
        respuesta = input()
        if respuesta.lower() == "1" or respuesta.lower() == "1":
            carnes = [
                "Pepperoni", "Pollo", "Jamon", "Tocino"
            ]
            print("Tipos de carne disponibles:")
            for i, carne in enumerate(carnes, start=1):
                print(f"{i}. {carne}")

            opcion = input("Elija el tipo de carne escribiendo el número o el nombre: ")
            carne_elegida = carnes[int(opcion) - 1] if opcion.isdigit() and 1 <= int(opcion) <= len(carnes) else opcion.capitalize()

            if carne_elegida in carnes:
                self.ingredientes.carne.append(carne_elegida)
            else:
                print("Tipo de carne no válido")

    def anadir_mariscos(self):
        print("¿Desea agregar mariscos? (Sí-1/No-2)")
        respuesta = input()
        if respuesta.lower() == "1" or respuesta.lower() == "1":
            mariscos = [
                "Anchoas", "Camarones", "Mejillones", "Calamares"
            ]
            print("Tipos de mariscos disponibles:")
            for i, marisco in enumerate(mariscos, start=1):
                print(f"{i}. {marisco}")

            opcion = input("Elija el tipo de marisco escribiendo el número o el nombre: ")
            marisco_elegido = mariscos[int(opcion) - 1] if opcion.isdigit() and 1 <= int(opcion) <= len(mariscos) else opcion.capitalize()

            if marisco_elegido in mariscos:
                self.ingredientes.mariscos.append(marisco_elegido)
            else:
                print("Tipo de marisco no válido")

    def anadir_vegetales(self):
        print("¿Desea agregar vegetales? (Sí-1/No-2)")
        respuesta = input()
        if respuesta.lower() == "1" or respuesta.lower() == "1":
            vegetales = [
                "Champiñones", "Pimientos", "Cebolla", "Aceitunas", "Tomate", "Espinacas", "Alcachofas", "Berenjena"
            ]
            print("Tipos de vegetales disponibles:")
            for i, vegetal in enumerate(vegetales, start=1):
                print(f"{i}. {vegetal}")

            opcion = input("Elija el tipo de vegetal escribiendo el número o el nombre: ")
            vegetal_elegido = vegetales[int(opcion) - 1] if opcion.isdigit() and 1 <= int(opcion) <= len(vegetales) else opcion.capitalize()

            if vegetal_elegido in vegetales:
                self.ingredientes.vegetales.append(vegetal_elegido)
            else:
                print("Tipo de vegetal no válido")

    def obtener_ingredientes(self):
        return self.ingredientes



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