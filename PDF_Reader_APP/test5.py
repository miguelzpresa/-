#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.filechooser import FileChooserListView

class Main(Screen):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.upload_button = Button(text='Cargar archivo', size_hint=(1, 1))
        self.upload_button.bind(on_press=self.upload_file)
        self.layout.add_widget(self.upload_button)
        self.add_widget(self.layout)

    def upload_file(self, instance):
        file_chooser = FileChooserListView()
        file_chooser.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
