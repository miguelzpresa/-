#!/usr/bin/python3
# Importar librerías de Kivy y el controlador
from kivy.uix.button import Button

# Clase Vista
class View(Button):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def on_press(self):
        # Manejar evento de botón presionado
        self.controller.handle_button_press()

    def update_count(self, count):
        # Actualizar texto de botón con el valor del contador
        self.text = "Contador: {}".format(count)

