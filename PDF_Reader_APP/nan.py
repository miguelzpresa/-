import kivy
kivy.require('2.1.0') # Verifica que la versión de Kivy sea compatible

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='¡Hola, mundo!')

if __name__ == '__main__':
    MyApp().run()
