#!/usr/bin/python3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

class Main(Screen):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.saludar_button = Button(text='Saludar', size_hint=(1, 0.5))
        self.saludar_button.bind(on_press=self.saludar)
        self.ir_a_despedida_button = Button(text='Ir a despedida', size_hint=(1, 0.5))
        self.ir_a_despedida_button.bind(on_press=self.ir_a_despedida)
        self.layout.add_widget(self.saludar_button)
        self.layout.add_widget(self.ir_a_despedida_button)
        self.add_widget(self.layout)

    def saludar(self, instance):
        self.manager.current = 'saludo'
        self.manager.get_screen('saludo').saludo.text = "¡Hola, mundo!"

    def ir_a_despedida(self, instance):
        self.manager.current = 'despedida'

class Saludo(Screen):
    def __init__(self, **kwargs):
        super(Saludo, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.saludo = Label(text="")
        self.button = Button(text='Volver', size_hint=(1, 0.5))
        self.button.bind(on_press=self.go_to_main)
        self.layout.add_widget(self.saludo)
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'

class Despedida(Screen):
    def __init__(self, **kwargs):
        super(Despedida, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.despedir_button = Button(text='Despedirse', size_hint=(1, 0.5))
        self.despedir_button.bind(on_press=self.despedirse)
        self.ir_a_main_button = Button(text='Ir a inicio', size_hint=(1, 0.5))
        self.ir_a_main_button.bind(on_press=self.ir_a_main)
        self.layout.add_widget(self.despedir_button)
        self.layout.add_widget(self.ir_a_main_button)
        self.add_widget(self.layout)

    def despedirse(self, instance):
        self.manager.current = 'saludo'
        self.manager.get_screen('saludo').saludo.text = "¡Hasta luego!"

    def ir_a_main(self, instance):
        self.manager.current = 'main'

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(Main(name='main'))
        sm.add_widget(Saludo(name='saludo'))
        sm.add_widget(Despedida(name='despedida'))
        return sm

if __name__ == '__main__':
    MyApp().run()
