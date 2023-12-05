from tkinter import *
# import globalVariable

#tạo button
def create_button(child_window, name_button,fs, nwidth, ndef):
    
    new_button = Button(child_window, text = name_button, 
                        font = ("Cooper Black", fs),
                        width = nwidth, pady = 5,
                        fg = "white",
                        bg = "#bd46bd",
                        relief="raise",
                        activebackground = "#BF17BC",
                        command = ndef,
                        cursor = "hand2")   #kiểu button
    
    return new_button