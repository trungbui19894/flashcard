from tkinter import *
from tkinter import messagebox
import globalVariable
# from controller.common import get_deck_name
from controller.deckController import get_deck_list, selected_deck
# from interface.components.childWindow import create_child_window
from controller.statController import stat_function

#xóa button & label mainscreen, hiện export
def main_to_library():
    clean_main_screen()
    show_library_screen()

def clean_main_screen():
    globalVariable.label_main.place_forget()
    globalVariable.library_button.place_forget()
    globalVariable.import_button.place_forget()
    globalVariable.exit_button.place_forget()

def show_library_screen():
    globalVariable.deck_label_frame.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor = "center")
    globalVariable.litomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    globalVariable.delete_deck_button.place(relx = 0.26, rely = 0.8, anchor = "center")
    globalVariable.download_button.place(relx = 0.38, rely = 0.8, anchor = "center")
    globalVariable.add_deck_button.place(relx = 0.50, rely = 0.8, anchor = "center")
    globalVariable.stat_button.place(relx=0.62, rely=0.8, anchor="center")
    globalVariable.see_card_button.place(relx = 0.74, rely = 0.8, anchor = "center")
    globalVariable.study_button.place(relx = 0.99, rely = 0.99, anchor = "se")

#xóa button & label mainscreen, hiện import
def show_import_screen():
    clean_main_screen()
    globalVariable.label_import.place(relx = 0.5, rely = 0.35, anchor = "center")
    globalVariable.imtomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    globalVariable.down_sample_button.place(relx = 0.5, rely = 0.6, anchor = "center")
    globalVariable.up_file_button.place(relx = 0.5, rely = 0.75, anchor = "center")
    
#quay lại mainscreen   
def back_main_screen(screen):
    #từ import về main
    if screen == "import":
        globalVariable.label_import.place_forget()
        globalVariable.imtomain_back_button.place_forget()
        globalVariable.down_sample_button.place_forget()
        globalVariable.up_file_button.place_forget()
    #từ library về main
    if screen == "library":
        clean_library()
        
    show_main_label_button()

def clean_library():
    globalVariable.deck_label_frame.place_forget()
    globalVariable.litomain_back_button.place_forget()
    globalVariable.delete_deck_button.place_forget()
    globalVariable.download_button.place_forget()
    globalVariable.see_card_button.place_forget()
    globalVariable.add_deck_button.place_forget()
    globalVariable.study_button.place_forget()
    globalVariable.stat_button.place_forget()

#hiện button & label mainscreen
def show_main_label_button():
    globalVariable.label_main.place(relx = 0.5, rely = 0.3, anchor = "center")
    globalVariable.library_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    globalVariable.import_button.place(relx = 0.5, rely = 0.85, anchor = "center")
    globalVariable.exit_button.place(relx = 0.99, rely = 0.99, anchor = "se")

#stat
def stat_window():
    if len(globalVariable.deck_listbox.curselection()) == 0:
        messagebox.showwarning("Warning", "Please select a deck to study.")
    elif len(globalVariable.deck_listbox.curselection()) == 1:
        clean_library()
        stat_function()

        globalVariable.deck_label_frame_1.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor="center")
        globalVariable.total_label.place(relx=0.50, rely=0.2, anchor="center")
        globalVariable.learned_label.place(relx=0.50, rely=0.3, anchor="center")
        globalVariable.Due_label.place(relx=0.50, rely=0.4, anchor="center")
        globalVariable.progress_label.place(relx=0.50, rely=0.5, anchor="center")
        globalVariable.lb_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    else:
        messagebox.showwarning("Warning", "Please select just one deck to study.")

def stat_back_to_library():
    globalVariable.deck_label_frame_1.place_forget()
    globalVariable.total_label.place_forget()
    globalVariable.learned_label.place_forget()
    globalVariable.Due_label.place_forget()
    globalVariable.progress_label.place_forget()
    globalVariable.lb_button.place_forget()

    show_library_screen()

def study_to_library():
    global deck_listbox
    global wordLable 
    global definitionLable 

    globalVariable.wordLable.place_forget()
    globalVariable.definitionLable.place_forget()
    globalVariable.button_relearn.place_forget()
    globalVariable.button_hard.place_forget()
    globalVariable.button_good.place_forget()
    globalVariable.button_easy.place_forget()
    globalVariable.button_back.place_forget()
    globalVariable.button_flip.place_forget()
    globalVariable.wordLable.place_forget()
    globalVariable.definitionLable.place_forget()
    show_library_screen()

def sc_back_li():
    
    globalVariable.card_label_frame.place_forget()
    globalVariable.sctoli_back_button.place_forget()
    globalVariable.add_card_button.place_forget()
    globalVariable.delete_card_button.place_forget()
    
    show_library_screen()