from menu_selector import*
if __name__ == "__main__":
    registrar_nuevo_usuario()  # Registra un nuevo usuario
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if autenticar_usuario(nombre_usuario, contraseña):
        ejecutar_pedido()