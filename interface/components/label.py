from tkinter import *
import globalVariable

#tạo label
def create_label(ntext, fs):
    
    new_label = Label(globalVariable.window, text = ntext,
                font = ("Cooper Black", fs),  #forn, size
                fg = "white",                 # Màu chữ
                bg = "#6E17BF",               #Màu background
                justify = CENTER, wraplength = 800)              
     
    return new_label