
from kivy.app import App
from kivy.base import runTouchApp
from kivy. lang import Builder
runTouchApp(Builder.load_string("""

        
GridLayout:
    rows:2
    spacing: 10
    
    Button:
        text: ('[b][color=ff0033]Speech To Speech[/color][/b]')
        font_size:'20pt'
        markup: True
    Button:
        text: ('[b][color=ff0033]Speech To Text[/color][/b]')
        markup: True
        font_size:'20pt'
    Button:
        text: ('[b][color=ff0033]Camera Translation[/color][/b]')
        markup: True
        font_size:'20pt'
    Button:                                                         
        text: ('[b][color=ff0033]Real-time Translation[/color][/b]')
        markup: True
        font_size:'20pt'
          
"""))

