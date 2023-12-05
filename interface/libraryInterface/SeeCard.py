from tkinter import *
import globalVariable
from interface.components.button import create_button
from interface.modal.ChildWindow import window_add_card
from controller.displayHandle import sc_back_li
from controller.cardController import delete_card

def SeeCard():
    globalVariable.card_label_frame = LabelFrame(globalVariable.window, text = "Yours cards", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
    globalVariable.sctoli_back_button = create_button(globalVariable.window, "Back", 12, 5, sc_back_li)
    globalVariable.add_card_button = create_button(globalVariable.window, "Add Card", 15, 10, window_add_card)
    globalVariable.delete_card_button = create_button(globalVariable.window, "Delete Card", 15, 10, delete_card)