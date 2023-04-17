#!/usr/bin/python3
from kivy.app import App
from controller import Controller

# Clase principal de la aplicación
class MyApp(App):
    def build(self):
        # Crear controlador y devolver vista como widget principal
        return Controller().view

if __name__ == '__main__':
    # Iniciar aplicación
    MyApp().run()
