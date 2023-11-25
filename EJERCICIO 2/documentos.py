class Documento:
    def __init__(self, nombre, tipo, tamaño, contenido):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.contenido = contenido
        self.accesos = []

    def acceder(self, usuario):
        self.accesos.append((usuario, "Acceso"))
        return self.contenido

    def modificar(self, usuario, nuevo_contenido):
        if self.tipo == "Texto":
            self.contenido = nuevo_contenido
            self.accesos.append((usuario, "Modificación"))
            print("Documento modificado exitosamente.")
        else:
            print("No se puede modificar este tipo de documento.")

    def operation(self) -> str:
        return f"Documento {self.tipo} {self.nombre}"

# Agregar funciones para manejar las crónicas, imágenes y videos

def acceder_documento(documento):
    usuario = input("Ingresa tu nombre de usuario: ")
    contenido = documento.acceder(usuario)
    print(f"Contenido del documento:\n{contenido}")

    opcion_modificar = input("¿Quieres modificar el documento? (si/no): ").lower()
    if opcion_modificar == "si" and documento.tipo == "Texto":
        modificar_documento(documento)

def modificar_documento(documento):
    usuario = input("Ingresa tu nombre de usuario: ")
    nuevo_contenido = input("Ingresa el nuevo contenido: ")
    documento.modificar(usuario, nuevo_contenido)

class DocumentoTexto(Documento):
    def __init__(self, nombre, tamaño, contenido):
        super().__init__(nombre, "Texto", tamaño, contenido)

# Crear documentos de texto específicos (Cronicas)
cronica1 = DocumentoTexto("Real Madrid vs Psg (vuelta)", 1324,"""
                           El Real Madrid y Benzema escribieron una nueva página en la leyenda de nuestro equipo en Europa. 
                           Cuando todo estaba en contra tras el gol de Mbappé en la primera mitad, el Bernabéu llevó en volandas al equipo, 
                           que le correspondió con tres goles que dan el acceso a los cuartos de final de la Champions League. 
                           Los tres llevaron la firma de un impresionante Benzema, que ya ha marcado 30 esta temporada y se convirtió en el tercer máximo goleador en los 120 años de historia del club tras superar a Di Stéfano.""")

cronica2 = DocumentoTexto("Real Madrid vs chelsea (vuelta)", 2048, """
                          Hasta el final vamos Real. Mejor no se puede resumir la tremenda personalidad de nuestro equipo y 
    la influencia que ejerce el estadio Santiago Bernabéu en la Copa de Europa. Cuando todo estaba en contra 
    con el 0-3 en el minuto 79 tras los goles de Mount, Rüdiger y Werner, apareció la mística de este estadio 
    y la fuerza de un equipo dispuesto siempre a luchar hasta la extenuación. Rodrygo mandó el partido a la 
    prórroga al marcar en el minuto 80 después de un majestuoso pase con el exterior de Modrić. Y en el minuto 96, 
    Benzema nos llevó hasta las semifinales con una nueva demostración de su tremendo olfato goleador. 
    El Real Madrid se enfrentará al Manchester City por un puesto en la final.""")

cronica3 = DocumentoTexto("Real Madrid vs Manchester City (vuelta)", 1972, """
              El rey de Europa volverá a estar en una final de la Champions. En otra noche memorable de las que solo se 
    viven en el Santiago Bernabéu, el Real Madrid dio la vuelta al duelo frente al Manchester City. 
    Nuestro equipo perdía 0-1 en el minuto 89, pero entonces apareció la magia de este estadio y la leyenda de este club 
    para firmar otro capítulo histórico e inolvidable. Con todo perdido, un doblete de Rodrygo forzó la prórroga, 
    en la que un gol de penalti de Benzema resolvió la eliminatoria. El 28 de mayo, los de Ancelotti buscarán conquistar 
    ante el Liverpool la Decimocuarta en París.
""")           

class DocumentoImagenCronica(Documento):
    def __init__(self, nombre, tamaño, contenido):
        super().__init__(nombre, "Imagen", tamaño, contenido)

# Crear documentos de imagen específicos (Imágenes para crónicas)
imagenes_cronica1 = [
    DocumentoImagenCronica("ImagenCronica1_1", 1024, "Celebración gol Mbappe(1) (0-1)"),
    DocumentoImagenCronica("ImagenCronica1_2", 2048, "Celebración gol de Benzema(1) (1-1)"),
    DocumentoImagenCronica("ImagenCronica1_3", 3072, "Celebración gol de Benzema(2) (2-1)"),
    DocumentoImagenCronica("ImagenCronica1_4", 4096, "Celebración gol de Benzema(3) (3-1)")
]

imagenes_cronica2 = [
    DocumentoImagenCronica("ImagenCronica2_1", 512, "Celebración gol  Rüdiger(1) (0-2) "),
    DocumentoImagenCronica("ImagenCronica2_2", 1024, "Celebración gol  Werner(1) (0-3)"),
    DocumentoImagenCronica("ImagenCronica2_3", 1536, "Celebración gol  Rodrygo(1) (1-3)"),
    DocumentoImagenCronica("ImagenCronica2_4", 2048, "Celebración gol  Benzema(1) (2-3)")
]

imagenes_cronica3 = [
    DocumentoImagenCronica("ImagenCronica3_1", 768, "Celebración gol  Mahrez(1) (0-1)"),
    DocumentoImagenCronica("ImagenCronica3_2", 1536, "Celebración gol  Rodrygo(1) (1-1)"),
    DocumentoImagenCronica("ImagenCronica3_3", 2304, "Celebración gol  Rodrygo(2) (2-1)"),
    DocumentoImagenCronica("ImagenCronica3_4", 3072, "Celebración gol  Benzema(1) (3-1)")
]

# documentos.py
class DocumentoVideoCronica(Documento):
    def __init__(self, nombre, tamaño, contenido):
        super().__init__(nombre, "Video", tamaño, contenido)

# Crear documentos de video específicos (Videos para crónicas)
videos_cronica1 = [
    DocumentoVideoCronica("VideoCronica1_1", 10240, "Resumen y goles del Real Madrid 3-1 PSG"),
]

videos_cronica2 = [
    DocumentoVideoCronica("VideoCronica2_1", 8120, "Resumen y goles del Real Madrid 2-3 Chelsea"),
]

videos_cronica3 = [
    DocumentoVideoCronica("VideoCronica3_1", 7680, "Resumen y goles del Real Madrid 3-1 Manchester City"),
]

if __name__ == "__main__":
    print("Bienvenido al gestor de documentos del Real Madrid.")
    
    while True:
        opcion = input("¿Quieres acceder a algún documento? (si/no): ").lower()
        
        if opcion == "si":
            print("Tipos de documentos disponibles:")
            print("1. Documento de Texto")
            print("2. Documento de Imagen")
            print("3. Documento de Video")

            tipo_documento = int(input("Selecciona un tipo de documento (1, 2 o 3): "))

            if tipo_documento == 1:
                # Acceder a documentos de texto
                print("Títulos de las crónicas:")
                print("1. Real Madrid vs Psg (vuelta)")
                print("2. Real Madrid vs Chelsea (vuelta)")
                print("3. Real Madrid vs Manchester City (vuelta)")

                seleccion_cronica = int(input("Selecciona una crónica (1, 2 o 3): "))
                if seleccion_cronica == 1:
                    acceder_documento(cronica1)
                    print("El tamaño del documento es: ",cronica1.tamaño,"KB")
                elif seleccion_cronica == 2:
                    acceder_documento(cronica2)
                    print("El tamaño del documento es: ",cronica2.tamaño,"KB")
                elif seleccion_cronica == 3:
                    acceder_documento(cronica3)
                    print("El tamaño del documento es: ",cronica3.tamaño,"KB")
                else:
                    print("Opción no válida. Inténtelo de nuevo.")

            elif tipo_documento == 2:
                 print("A que documento de imagen quiere acceder:")
                 print("1. Imágebnes Real Madrid vs Psg (vuelta)")
                 print("2. Imágenes Real Madrid vs Chelsea (vuelta)")
                 print("3. Imágenes Real Madrid vs Manchester City (vuelta)")
                 
                 seleccion_imagen = int(input("Selecciona un documento de Imágenes (1, 2 o 3): "))
                 if seleccion_imagen == 1:
                     acceder_documento(imagenes_cronica1)
                     print("El tamaño del documento es: ",imagenes_cronica1.tamaño,"KB")
                 elif seleccion_imagen == 2: 
                        acceder_documento(imagenes_cronica2)
                        print("El tamaño del documento es: ",imagenes_cronica2.tamaño,"KB")
                 elif seleccion_imagen == 3:
                        acceder_documento(imagenes_cronica3)
                        print("El tamaño del documento es: ",imagenes_cronica3.tamaño,"KB")
                 else:
                      print("Opción no válida. Inténtelo de nuevo.")
                

            elif tipo_documento == 3:
                print("A que documento de video quiere acceder:")
                print("1. Videos Real Madrid vs Psg (vuelta)")
                print("2. Videos Real Madrid vs Chelsea (vuelta)")
                print("3. Videos Real Madrid vs Manchester City (vuelta)")
                
                seleccion_video = int(input("Selecciona un documento de Video (1, 2 o 3): "))
                if seleccion_video == 1:
                    acceder_documento(videos_cronica1)
                    print("El tamaño del documento es: ",videos_cronica1.tamaño,"KB")
                elif seleccion_video == 2:
                    acceder_documento(videos_cronica2)
                    print("El tamaño del documento es: ",videos_cronica2.tamaño,"KB")
                elif seleccion_video == 3:
                    acceder_documento(videos_cronica3)
                    print("El tamaño del documento es: ",videos_cronica3.tamaño,"KB")
                else:
                    print("Opción no válida. Inténtelo de nuevo.")

        else:
            break
