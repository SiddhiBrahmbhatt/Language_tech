from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox



root = Tk( )
root.title("Language_Tech")
root.iconbitmap('Users/siddhibrahmbhatt/Sid_Kivy/LT.png')
root. geometry ("880x300")

def translate_it ():
    pass

 # Text Boxes
#text.grid(row=0, column=0, pady=20, padx=10)
text = Text(root, height=10, width=40)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

#ttext.grid(row=0, column=2, pady=20, padx=10)
ttext = Text(root, height=10, width=40)
