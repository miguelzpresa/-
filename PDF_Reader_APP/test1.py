#!/usr/bin/python3
import kivy
#kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.label = Label(text='Main Window')
        self.button1 = Button(text='Go to Window 1')
        self.button2 = Button(text='Go to Window 2')
        self.button1.bind(on_press=self.go_to_window1)
        self.button2.bind(on_press=self.go_to_window2)

        self.add_widget(self.label)
        self.add_widget(self.button1)
        self.add_widget(self.button2)

    def go_to_window1(self, *args):
        self.parent.current = 'window1'

    def go_to_window2(self, *args):
        self.parent.current = 'window2'


class Window1(BoxLayout):
    def __init__(self, **kwargs):
        super(Window1, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.label = Label(text='Window 1')
        self.button = Button(text='Go back to Main Window')
        self.button.bind(on_press=self.go_to_main_window)

        self.add_widget(self.label)
        self.add_widget(self.button)

    def go_to_main_window(self, *args):
        self.parent.current = 'main'


class Window2(BoxLayout):
    def __init__(self, **kwargs):
        super(Window2, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.label = Label(text='Window 2')
        self.button = Button(text='Go back to Main Window')
        self.button.bind(on_press=self.go_to_main_window)

        self.add_widget(self.label)
        self.add_widget(self.button)

    def go_to_main_window(self, *args):
        self.parent.current = 'main'


class MyApp(App):
    def build(self):
        self.root = BoxLayout()
        self.sm = ScreenManager()
        self.main_window = MainWindow()
        self.window1 = Window1()
        self.window2 = Window2()

        self.sm.add_widget(self.main_window)
        self.sm.add_widget(self.window1)
        self.sm.add_widget(self.window2)

        self.root.add_widget(self.sm)

        return self.root


if __name__ == '__main__':
    MyApp().run()
