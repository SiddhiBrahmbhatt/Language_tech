import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy. lang import Builder
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Window.size = (350, 580)


class Language_Tech(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        #screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.main, 5)

    def main(self, *args):
        screen_manager.current = "main"


Language_Tech().run()
