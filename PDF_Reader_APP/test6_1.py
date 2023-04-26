#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView


class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        select_button = Button(text='Select', size_hint=(None, 0.2), width=100)
        select_button.bind(on_press=lambda x: self.upload_file(file_chooser.path))
        file_chooser.size_hint_y = 0.8
        layout.add_widget(file_chooser)
        layout.add_widget(select_button)
        return layout

    def upload_file(self, path):
        print(path)


if __name__ == '__main__':
    MyApp().run()
