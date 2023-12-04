from tkinter import *
from interface.components.button import create_button

import globalVariable

def create_child_window(name_window, text_label, text_button, add_def, cacel_def):
    
    name_window = Toplevel(globalVariable.window)
    name_window.title(text_label)
    name_window.configure(bg='#6E17BF')
    name_window.iconbitmap('icon.ico')
    name_window.resizable(False, False)

    child_x = globalVariable.window.winfo_x() + (globalVariable.window.winfo_width() - 300) // 2
    child_y = globalVariable.window.winfo_y() + (globalVariable.window.winfo_height() - 200) // 2
    
    name_window.geometry(f"{300}x{200}+{child_x}+{child_y}")
    
    child_label = Label(name_window, text = "Add your new deck",
                font = ("Cooper Black", 15), fg = "white", bg = "#6E17BF")
    child_label.place(relx = 0.5, rely = 0.25, anchor = "center")
    child_button = create_button(name_window, text_button, 10, 5, add_def)
    child_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    cancel_button = create_button(name_window, "Cancel", 10, 5, cacel_def)
    cancel_button.place(relx = 0.5, rely = 0.85, anchor = "center")
    
    return name_window