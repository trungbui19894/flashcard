from tkinter import *

def variableInitialize():
    global window
    window = Tk()

    global selected_deck
    global deck_listbox
    global card_label_frame
    global cardIndex
    global cardList
    global wordLable 
    global definitionLable
    global total
    global readed

    global screen_width
    global screen_height
    global the_canvas

    # home
    global label_main, library_button, import_button, exit_button
    # library
    global deck_label_frame, litomain_back_button, delete_deck_button, download_button, see_card_button, add_deck_button, study_button, stat_button
    # see card
    global sctoli_back_button, add_card_button, delete_card_button, see_card_listbox, deck_name
    # study
    global button_relearn, button_hard, button_good, button_easy, button_back, button_flip
    # file
    global label_import, down_sample_button, up_file_button, imtomain_back_button
    # stat
    global deck_label_frame_1, total_label, learned_label, Due_label, progress_label, lb_button, deck