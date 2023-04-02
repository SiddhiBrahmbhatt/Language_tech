from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    canvas:
        Color:
            rgb: 1,1, 3
        Rectangle:
         pos:self.pos
         size:self.size
    AsyncImage:
        size_hint: None, None
        size: dp(500), dp(56)
        source: '/Users/siddhibrahmbhatt/Desktop/Sid_Kivy/main.png'
"""

class Language_TechApp(App):
    def build(self):
        return Builder.load_string(kv)

Language_TechApp().run()
