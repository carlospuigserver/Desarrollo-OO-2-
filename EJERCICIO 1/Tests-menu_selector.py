import unittest
from unittest.mock import patch
from io import StringIO
from menu_selector import*
class TestMenus(unittest.TestCase):
    
    def test_obtener_usuarios(self):
        # Asegurarse de que la función obtener_usuarios devuelva un conjunto no vacío
        usuarios = obtener_usuarios()
        self.assertIsInstance(usuarios, set)
        self.assertTrue(len(usuarios) > 0)

    def test_autenticar_usuario(self):
        # Crear un usuario de prueba
        nombre_usuario_prueba = "usuario_prueba"
        contraseña_prueba = "contraseña_prueba"
        with open('EJERCICIO 1/Usuario/usuario.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre_usuario_prueba, contraseña_prueba])

        # Probar la autenticación con el usuario de prueba
        resultado = autenticar_usuario(nombre_usuario_prueba, contraseña_prueba)
        self.assertTrue(resultado)

    @patch('builtins.input', side_effect=["usuario_prueba", "contraseña_prueba"])
    def test_registrar_nuevo_usuario(self, mock_input):
        # Crear un usuario de prueba
        nombre_usuario_prueba = "usuario_prueba"
        contraseña_prueba = "contraseña_prueba"

        # Ejecutar la función de registro
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            registrar_nuevo_usuario()

        # Verificar la salida para asegurarse de que el usuario se registró con éxito
        output = mock_stdout.getvalue()
        self.assertIn("Usuario registrado con éxito.", output)

        # Verificar que el usuario de prueba se agregó al archivo CSV
        usuarios = obtener_usuarios()
        self.assertTrue((nombre_usuario_prueba, contraseña_prueba) in usuarios)

    def test_menu_simple(self):
        # Crear un menú simple de prueba
        menu_simple = MenuSimple("Menú de Prueba")
        opciones = [
            Componente("Plato 1", 10.0),
            Componente("Plato 2", 15.0),
            Componente("Plato 3", 12.5)
        ]
        menu_simple.agregar_opcion(*opciones)

        # Verificar que la obtención de precio y presentación funcione correctamente
        self.assertEqual(menu_simple.obtener_precio(), sum(op.obtener_precio() for op in opciones))
        presentacion_esperada = "Menú de Prueba:\n  - Plato 1 - $10.00\n  - Plato 2 - $15.00\n  - Plato 3 - $12.50"
        self.assertEqual(menu_simple.obtener_presentacion(), presentacion_esperada)

if __name__ == '__main__':
    unittest.main()
