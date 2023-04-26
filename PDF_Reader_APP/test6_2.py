#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.filechooser import FileChooserListView

class WelcomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        welcome_button = Button(text="Bienvenid@", size_hint=(None, None), size=(200, 100))
        welcome_button.bind(on_press=self.go_to_next_screen)
        self.add_widget(welcome_button)

    def go_to_next_screen(self, instance):
        self.parent.current = "file_screen"


class FileScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        file_chooser = FileChooserListView()
        select_button = Button(text='Select', size_hint=(None, None), size=(200, 100))
        select_button.bind(on_press=lambda x: self.upload_file(file_chooser.path))
        file_chooser.size_hint_y = 0.8
        self.add_widget(file_chooser)
        self.add_widget(select_button)

    def upload_file(self, path):
        print(path)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen()
        file_screen = FileScreen()
        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(file_screen)
        return screen_manager


if __name__ == '__main__':
    MyApp().run()

