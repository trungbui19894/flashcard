from tkinter import *
import globalVariable
from interface.components.button import create_button
from interface.components.listBox import create_listbox
from controller.displayHandle import stat_window, back_main_screen
from controller.deckController import delete_deck, add_deck_window, get_deck_list, rename_deck_window
from controller.fileController import export
from controller.cardController import show_see_card
from controller.studyController import study_window

def Library():
    #labelframe chứa select option
    globalVariable.deck_label_frame = LabelFrame(globalVariable.window, text = "Yours deck", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
    #button của libirary
    globalVariable.litomain_back_button = create_button(globalVariable.window, "Back", 12, 5, lambda: back_main_screen("library"))
    globalVariable.delete_deck_button = create_button(globalVariable.window, "Delete", 12, 10, delete_deck)
    globalVariable.download_button = create_button(globalVariable.window, "Download", 12, 10, lambda : export("export"))
    globalVariable.see_card_button = create_button(globalVariable.window, "See Card", 12, 10, show_see_card)
    globalVariable.add_deck_button = create_button(globalVariable.window, "Add deck", 12, 10, add_deck_window)
    globalVariable.stat_button = create_button(globalVariable.window, "Stat", 12, 10, stat_window)
    globalVariable.study_button = create_button(globalVariable.window, "STUDY", 12, 10, study_window)
    globalVariable.deck_listbox = create_listbox(globalVariable.deck_label_frame, get_deck_list())
    globalVariable.deck_listbox.bind("<Double-Button-1>", rename_deck_window)