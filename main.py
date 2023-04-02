import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.lang import Builder

kv ="""
BoxLayout:
    canvas:
        Color:
            rgb: 1,1,3
        Rectangle:
            pos:self.pos
            size:self.size
    Image:
        size_hint: None, None
        size: dp(500), dp(56)
        source:'Users/siddhibrahmbhatt/Desktop/Sid_Kivy/main.png'
        
"""

class Language_Tech(App):
    def build(self):
        return Builder.load_string(kv)

Language_Tech().run()

