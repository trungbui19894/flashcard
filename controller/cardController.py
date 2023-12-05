from datetime import datetime
from tkinter import messagebox
import globalVariable
from interface.components.listBox import create_listbox
from interface.components.label import create_label
from controller.displayHandle import clean_library
from controller.common import get_deck_name, get_card_infor, count_pipe_characters, get_words, get_definition
from controller.deckController import selected_deck

#see_card
def show_see_card():
    clean_library()
    globalVariable.card_label_frame.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor = "center")
    globalVariable.sctoli_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    globalVariable.add_card_button.place(relx = 0.65, rely = 0.8, anchor = "center")
    globalVariable.delete_card_button.place(relx = 0.35, rely = 0.8, anchor = "center")
    globalVariable.see_card_listbox = create_listbox(globalVariable.card_label_frame, see_card())
    globalVariable.deck_name = selected_deck()

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
            if count_pipe_characters(setsData[i]) == 4:
                globalVariable.cardList.append(get_card_infor(setsData[i]))
                if get_deck_name(setsData[i]) == globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0]):
                    globalVariable.total += 1
                    if setsData[i] and get_card_infor(setsData[i])[4] == 'learned':
                        globalVariable.readed += 1
        if selected_deck():
            show_card()
        else:    
            globalVariable.wordLable.config(text="No card")
            globalVariable.definitionLable.config(text='')

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
        globalVariable.wordLable.config(text='Done!!!')
        globalVariable.definitionLable.config(text='')

def delete_card():
    if len(globalVariable.see_card_listbox.curselection()) > 0:
        result = messagebox.askokcancel('Notification', 'Are you sure you want to delete the selected card?')
        
        if result:
            index = globalVariable.see_card_listbox.curselection()
            word = []
            defi = []
            
            for i in reversed(index):
                card = globalVariable.see_card_listbox.get(i)  # Use i instead of index
                word_def = card.split(":")
                word.append(word_def[0])
                defi.append(word_def[1])
                globalVariable.see_card_listbox.delete(i)  # Use i instead of index
            
            if globalVariable.deck_name:
                fileObject = open('data.txt', mode="r", encoding="utf-8")
                _data = fileObject.read().splitlines()
                fileObject.close()
                sets = ''
                for i in range(len(_data)):
                    print(get_words(_data[i]))
                    print(get_definition(_data[i]))
                    if (get_words(_data[i]) not in word and get_definition(_data[i]) not in defi) or (get_words(_data[i]) in word and get_definition(_data[i]) in defi and get_deck_name(_data[i]) not in globalVariable.deck_name):
                        sets += _data[i] + '\n'
                fileObject = open('data.txt', mode="w+", encoding="utf-8")
                fileObject.write(sets)
                fileObject.close()
    else:
        messagebox.showerror('Notification', 'You have not selected the card to delete. Please check again')
