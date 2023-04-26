#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout()
        welcome_button = Button(text='Bienvenid@', font_size=50)
        welcome_button.bind(on_press=self.switch_to_file_screen)
        layout.add_widget(welcome_button)
        self.add_widget(layout)

    def switch_to_file_screen(self, *args):
        self.manager.current = 'file'

class FileScreen(Screen):
    def __init__(self, **kwargs):
        super(FileScreen, self).__init__(**kwargs)
        layout = BoxLayout()
        file_chooser = FileChooserListView()
        select_button = Button(text='Select', size_hint=(None, 0.2), width=100)
        select_button.bind(on_press=lambda x: self.upload_file(file_chooser.path))
        file_chooser.size_hint_y = 0.8
        layout.add_widget(file_chooser)
        layout.add_widget(select_button)
        self.add_widget(layout)

    def upload_file(self, path):
        print(path)


class MyApp(App):

    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen(name='welcome')
        file_screen = FileScreen(name='file')
        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(file_screen)
        return screen_manager


if __name__ == '__main__':
    MyApp().run()

