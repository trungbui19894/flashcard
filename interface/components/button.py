from tkinter import *
import globalVariable

def create_button(name_button,fs, nwidth, ndef):
    
    new_button = Button(globalVariable.window, text = name_button, 
                        font = ("Cooper Black", fs),
                        width = nwidth, pady = 5,
                        fg = "white",
                        bg = "#bd46bd",
                        relief="raise",
                        activebackground = "#BF17BC",
                        command = ndef,
                        cursor = "hand2")   #kiểu button
    
    return new_button