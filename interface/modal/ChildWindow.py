from tkinter import *
from tkinter import messagebox
from datetime import datetime
from interface.components.button import create_button
import globalVariable

def create_child_window(name_window, text_label, text_button, add_def, cacel_def):
    
    child_window = Toplevel(globalVariable.window)
    child_window.title(name_window)
    child_window.configure(bg='#6E17BF')
    #child_window.iconbitmap('icon.ico')
    child_window.resizable(False, False)

    child_x = globalVariable.window.winfo_x() + (globalVariable.window.winfo_width() - 300) // 2
    child_y = globalVariable.window.winfo_y() + (globalVariable.window.winfo_height() - 200) // 2
    
    child_window.geometry(f"{300}x{200}+{child_x}+{child_y}")
    
    child_label = Label(child_window, text = text_label,
                font = ("Cooper Black", 15), fg = "white", bg = "#6E17BF")
    child_label.place(relx = 0.5, rely = 0.25, anchor = "center")
    child_button = create_button(child_window, text_button, 10, 5, add_def)
    child_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    cancel_button = create_button(child_window, "Cancel", 10, 5, cacel_def)
    cancel_button.place(relx = 0.5, rely = 0.85, anchor = "center")
    
    return child_window

def window_add_card():

    def add_card():
        new_word = add_word_entry.get()
        new_def = add_def_entry.get()
        
        if new_word == "" or new_def == "":
            messagebox.showerror('Notification', 'Please enter a deck name.')
            add_card_window.destroy()
            
        else :
            globalVariable.see_card_listbox.insert(END, f"{new_word}: {new_def}")
            fileObject = open('data.txt', mode="a+", encoding="utf-8")
            fileObject.write(str(globalVariable.deck_name[0]) + '|' + new_word + '|' + new_def + '|' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '|' + "unlearn" + "\n")
            fileObject.close()
            
            add_word_entry.delete(0, END)
            add_def_entry.delete(0, END)
    
    
    def close_add_card_window():
        add_card_window.destroy()
    
    add_card_window = create_child_window("Add new card", "Add your new card", "Add", add_card, close_add_card_window)
    add_word_entry = Entry(add_card_window)
    add_word_entry.place(relx = 0.5, rely = 0.38, anchor = "center")
    add_def_entry = Entry(add_card_window)
    add_def_entry.place(relx = 0.5, rely = 0.49, anchor = "center")