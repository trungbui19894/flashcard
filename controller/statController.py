from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from controller.deckController import selected_deck
from controller.common import get_deck_name, get_card_infor
import globalVariable

def stat_function():
    selected_decks = selected_deck()
    if not selected_decks:
        messagebox.showwarning("Warning", "Please select at least one deck.")
        return

    # Calculate statistics for selected decks
    total_cards = 0
    learned_cards = 0
    due_cards = 0

    fileObject = open('data.txt', mode="r", encoding="utf-8")
    deck_data = fileObject.read().splitlines()
    fileObject.close()

    for deck in selected_decks:
        total_deck_cards = 0
        learned_deck_cards = 0
        due_deck_cards = 0

        for line in deck_data:
            if get_deck_name(line) == deck:
                total_deck_cards += 1
                if get_card_infor(line)[4] == 'learned':
                    learned_deck_cards += 1
                    if datetime.strptime(get_card_infor(line)[3], "%m/%d/%Y, %H:%M:%S") < datetime.now() :
                        due_deck_cards += 1

        total_cards += total_deck_cards
        learned_cards += learned_deck_cards
        due_cards += due_deck_cards

        progressbar = ttk.Progressbar(globalVariable.deck_label_frame_1, length=600, mode='determinate', orient='horizontal')
        progressbar.place(relx=0.50, rely=0.75, anchor="center")

        if total_deck_cards > 0:
            progress_percentage = (learned_deck_cards / total_deck_cards) * 100
        else:
            progress_percentage = 0

        # Set the value of the progress bar
        progressbar['value'] = progress_percentage

    globalVariable.total_label.config(text=f'Total: {total_cards}')
    globalVariable.learned_label.config(text=f'Learned: {learned_cards}')
    globalVariable.Due_label.config(text=f'Due: {due_cards}')

    if total_cards > 0:
        globalVariable.progress_label.config(text=f'Progress: {(learned_cards / total_cards) * 100:.2f}%')
    else:
        globalVariable.progress_label.config(text='Progress: 0.00%')