#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.filechooser import FileChooserListView

class Main(Screen):
    def init(self, **kwargs):
        super(Main, self).init(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.saludar_button = Button(text='Saludar', size_hint=(1, 0.5))
        self.upload_button = Button(text='Cargar archivo', size_hint=(1, 0.5))
        self.upload_button.bind(on_press=self.upload_file)
        self.layout.add_widget(self.saludar_button)
        self.layout.add_widget(self.upload_button)
        self.add_widget(self.layout)


    def upload_file(self, instance):
        file_chooser = FileChooserListView()
        file_chooser.show()
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name='main'))
        return sm

if name == 'main':
MyApp().run()
