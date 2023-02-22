import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class LanguageTechApp(App):

    def build(self):
        print("Test--------------------")
        return Label(text='Language_Tech')



if __name__ == '__main__':
    LanguageTechApp().run()