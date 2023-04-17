#!/usr/bin/python3
# Importar modelo y vista
from model import Model
from view import View

# Clase Controlador
class Controller:
    def __init__(self):
        # Crear objeto del modelo y vista
        self.model = Model()
        self.view = View(self)

        # Establecer vista en controlador
        self.set_view()

    def handle_button_press(self):
        # Actualizar modelo
        self.model.increment_count()

        # Actualizar vista
        self.view.update_count(self.model.count)

    def set_view(self):
        # Establecer vista en controlador
        self.view.controller = self

