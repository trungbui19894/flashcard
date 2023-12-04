from datetime import datetime
from tkinter import messagebox
import globalVariable
from interface.components.listBox import create_listbox
from interface.components.label import create_label
from controller.displayHandle import clean_library
from controller.common import get_deck_name, get_card_infor
from controller.deckController import selected_deck

def create_card_label():
    globalVariable.readed = 0
    globalVariable.total = 0
    globalVariable.cardIndex = 0
    globalVariable.cardList = []

    globalVariable.wordLable = create_label("", 20)
    globalVariable.definitionLable = create_label("", 15)

    fileObject = open('data.txt', mode='r', encoding="utf-8")
    setsData = fileObject.read().splitlines()
    fileObject.close()
    if len(setsData) > 0:
        for i in range(len(setsData)):
            globalVariable.cardList.append(get_card_infor(setsData[i]))
            if get_deck_name(setsData[i]) == globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0]):
                total += 1
                if setsData[i] and get_card_infor(setsData[i])[4] == 'true':
                    readed += 1
        if selected_deck():
            show_card()
        else:    
            globalVariable.wordLable.config(text="Ko có card đâu nhé cưng :3")
            globalVariable.definitionLable.config(text='')

def show_see_card():
    clean_library()
    globalVariable.card_label_frame.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor = "center")
    globalVariable.sctoli_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    globalVariable.add_card_button.place(relx = 0.65, rely = 0.8, anchor = "center")
    globalVariable.delete_card_button.place(relx = 0.35, rely = 0.8, anchor = "center")
    create_listbox(globalVariable.card_label_frame, see_card())

def see_card():
    # Get the selected deck name
    selected_deck = globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0])

    # Open the deck file
    with open('data.txt', mode='r', encoding='utf-8') as file:
        deck_data = file.read().splitlines()

    # Find the cards for the selected deck
    cards = []
    for line in deck_data:
        if get_deck_name(line) == selected_deck:
            info = get_card_infor(line)
            if len(info) == 5:
                cards.append(f"{info[1]}: {info[2]}")
            
    return cards

def show_card():
    if globalVariable.cardIndex < len(globalVariable.cardList):
        if datetime.strptime(globalVariable.cardList[globalVariable.cardIndex][3], "%m/%d/%Y, %H:%M:%S") < datetime.now() and globalVariable.cardList[globalVariable.cardIndex][0] == globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0]):
            globalVariable.wordLable.config(text=globalVariable.cardList[globalVariable.cardIndex][1])
            globalVariable.definitionLable.config(text='')
            globalVariable.cardIndex += 1
        else:
            globalVariable.cardIndex += 1
            show_card()
    else:
        globalVariable.cardIndex += 1
        globalVariable.wordLable.config(text='Oh yeah, học hết card trong set này rồi (^O^)')
        globalVariable.definitionLable.config(text='')

def add_card():
    # Get the selected deck
    selected_deck = globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0])
    if not selected_deck:
        messagebox.showwarning("Error", "Please select a deck to add a card.")
    return

def delete_card():
    # Get the selected deck
    selected_deck = globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0])
    if not selected_deck:
        messagebox.showwarning("Error", "Please select a deck to delete a card.")
        return

    # Get the selected card index
    selected_card_index = globalVariable.card_label_frame.curselection()
    if not selected_card_index:
        messagebox.showwarning("Error", "Please select a card to delete.")
        return

    # Ask for confirmation
    result = messagebox.askokcancel('Notification', 'Are you sure you want to delete the selected card?')

    if result:
        # Delete the selected card
        index_del = globalVariable.card_label_frame.curselection()

        # Update the data.txt file
        fileObject = open('data.txt', mode='r', encoding="utf-8")
        deck_data = fileObject.read().splitlines()
        fileObject.close()

        deleted_cards = []

        for index in reversed(index_del):
            deleted_cards.append(get_card_infor(globalVariable.card_label_frame.get(index)))

            globalVariable.card_label_frame.delete(index)

        # Remove the deleted cards from the deck data
        updated_deck_data = [line for line in deck_data if get_deck_name(line) != selected_deck or get_card_infor(line) not in deleted_cards]

        # Write the updated deck data back to the file
        with open('data.txt', mode='w', encoding="utf-8") as file:
            file.write('\n'.join(updated_deck_data))

        messagebox.showinfo("Notification", "Card deleted successfully.")

def flip_card():
    if globalVariable.cardIndex <= len(globalVariable.cardList):
        globalVariable.definitionLable.config(text=globalVariable.cardList[globalVariable.cardIndex - 1][2])