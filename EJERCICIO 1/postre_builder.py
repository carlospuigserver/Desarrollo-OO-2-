from abc import ABC, abstractmethod

# Producto
class Postre:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class BuilderPostre(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_mochi_ice_cream(self):
        pass

    @abstractmethod
    def construir_baklava(self):
        pass

    @abstractmethod
    def construir_dulce_tres_leches_coco(self):
        pass

    @abstractmethod
    def construir_sorvete_acai(self):
        pass

    @abstractmethod
    def construir_anmitsu(self):
        pass

    @abstractmethod
    def construir_kulfi(self):
        pass

    @abstractmethod
    def construir_knafeh(self):
        pass

    @abstractmethod
    def construir_tiramisu(self):
        pass

    @abstractmethod
    def construir_panna_cotta(self):
        pass

    @abstractmethod
    def construir_pastel_chocolate(self):
        pass

    @abstractmethod
    def construir_cheesecake(self):
        pass

    @abstractmethod
    def construir_mousse_frambuesa(self):
        pass

    @abstractmethod
    def construir_tarta_limon(self):
        pass

    @abstractmethod
    def construir_profiteroles(self):
        pass

    def obtener_postre(self):
        pass

# Concrete Builder
class PostreBuilder(BuilderPostre):
    def __init__(self):
        self.reset()

    def reset(self):
        self.postre = Postre("", 0.0)

    def construir_mochi_ice_cream(self):
        self.postre = Postre("Mochi Ice Cream", 5.99)

    def construir_baklava(self):
        self.postre = Postre("Baklava", 7.99)

    def construir_dulce_tres_leches_coco(self):
        self.postre = Postre("Dulce de Tres Leches con Coco", 6.99)

    def construir_sorvete_acai(self):
        self.postre = Postre("Sorvete de Açaí", 8.99)

    def construir_anmitsu(self):
        self.postre = Postre("Anmitsu", 7.49)

    def construir_kulfi(self):
        self.postre = Postre("Kulfi", 6.79)

    def construir_knafeh(self):
        self.postre = Postre("Knafeh", 9.99)

    def construir_tiramisu(self):
        self.postre = Postre("Tiramisú", 8.49)

    def construir_panna_cotta(self):
        self.postre = Postre("Panna Cotta", 7.29)

    def construir_pastel_chocolate(self):
        self.postre = Postre("Pastel de Chocolate", 10.99)

    def construir_cheesecake(self):
        self.postre = Postre("Cheesecake", 9.79)

    def construir_mousse_frambuesa(self):
        self.postre = Postre("Mousse de Frambuesa", 8.99)

    def construir_tarta_limon(self):
        self.postre = Postre("Tarta de Limón", 7.89)

    def construir_profiteroles(self):
        self.postre = Postre("Profiteroles", 6.49)

    def obtener_postre(self):
        return self.postre


class Cliente:
    def elegir_postre(self, builder):
        print("Tipos de postres disponibles:")
        tipos_postres = [
            "Mochi Ice Cream - 5.99$",
            "Baklava - 7.99$",
            "Dulce de Tres Leches con Coco - 6.99$",
            "Sorvete de Açaí - 8.99$",
            "Anmitsu - 7.49$",
            "Kulfi - 6.79$",
            "Knafeh - 9.99$",
            "Tiramisú - 8.49$",
            "Panna Cotta - 7.29$",
            "Pastel de Chocolate - 10.99$",
            "Cheesecake - 9.79$",
            "Mousse de Frambuesa - 8.99$",
            "Tarta de Limón - 7.89$",
            "Profiteroles - 6.49$"
        ]
        print("Elija el tipo de postre escribiendo su nombre:")
        for tipo in tipos_postres:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()
        tipo_elegido_lower = tipo_elegido.lower()
        if tipo_elegido_lower == "mochi ice cream":
            builder.construir_mochi_ice_cream()
        elif tipo_elegido_lower == "baklava":
            builder.construir_baklava()
        elif tipo_elegido_lower == "dulce de tres leches con coco":
            builder.construir_dulce_tres_leches_coco()
        elif tipo_elegido_lower == "sorvete de açaí":
            builder.construir_sorvete_acai()
        elif tipo_elegido_lower == "anmitsu":
            builder.construir_anmitsu()
        elif tipo_elegido_lower == "kulfi":
            builder.construir_kulfi()
        elif tipo_elegido_lower == "knafeh":
            builder.construir_knafeh()
        elif tipo_elegido_lower == "tiramisú":
            builder.construir_tiramisu()
        elif tipo_elegido_lower == "panna cotta":
            builder.construir_panna_cotta()
        elif tipo_elegido_lower == "pastel de chocolate":
            builder.construir_pastel_chocolate()
        elif tipo_elegido_lower == "cheesecake":
            builder.construir_cheesecake()
        elif tipo_elegido_lower == "mousse de frambuesa":
            builder.construir_mousse_frambuesa()
        elif tipo_elegido_lower == "tarta de limón":
            builder.construir_tarta_limon()
        elif tipo_elegido_lower == "profiteroles":
            builder.construir_profiteroles()
        else:
            print("No se ha encontrado el tipo de postre elegido.")

if __name__ == "__main__":
    builder = PostreBuilder()
    director = Cliente()
    director.elegir_postre(builder)
    postre = builder.obtener_postre()
    print(f"Postre elegido: {postre}")