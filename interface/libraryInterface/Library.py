from tkinter import *
import globalVariable
from interface.components.button import create_button
from interface.components.listBox import create_listbox
from controller.displayHandle import *
from controller.deckController import delete_deck, add_deck_window, get_deck_list
from controller.fileController import export
from controller.cardController import show_see_card
from controller.studyController import study_window

def Library():
    #labelframe chứa select option
    globalVariable.deck_label_frame = LabelFrame(globalVariable.window, text = "Yours deck", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
    #button của libirary
    globalVariable.litomain_back_button = create_button("Back", 12, 5, lambda: back_main_screen("library"))
    globalVariable.delete_deck_button = create_button("Delete", 15, 10, delete_deck)
    globalVariable.download_button = create_button("Download", 15, 10, lambda : export("export"))
    globalVariable.see_card_button = create_button("See Card", 15, 10, show_see_card)
    globalVariable.add_deck_button = create_button("Add deck", 15, 10, add_deck_window)
    globalVariable.study_button = create_button("STUDY", 20, 10, study_window)
    globalVariable.deck_listbox = create_listbox(globalVariable.deck_label_frame, get_deck_list())
    globalVariable.deck_listbox.bind("<Double-Button-1>", rename_deck_window)