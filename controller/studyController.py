from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
import globalVariable
from controller.displayHandle import clean_library
from controller.cardController import create_card_label, show_card
from controller.common import get_deck_name, count_pipe_characters

def study_window():
    counter = 0

    if len(globalVariable.deck_listbox.curselection()) == 0:
        messagebox.showwarning("Warning", "Please select a deck to study.")
    elif len(globalVariable.deck_listbox.curselection()) == 1:
        fileObject = open('data.txt', mode='r', encoding="utf-8")
        setsData = fileObject.read().splitlines()
        fileObject.close()
        for i in range(len(setsData)):
            if get_deck_name(setsData[i]) == globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0]):
                counter += 1

        if counter == 1: 
            for i in range(len(setsData)):
                if get_deck_name(setsData[i]) == globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0]):
                    if count_pipe_characters(setsData[i]) < 4:
                        messagebox.showwarning("Warning", "Deck is empty. Please add card to deck.")
                        break
                    else:
                        clean_library()
                        create_card_label()
            
                        globalVariable.wordLable.place(relx=0.5, rely=0.2, anchor="center")
                        globalVariable.definitionLable.place(relx=0.5, rely=0.3, anchor="center")
                        globalVariable.button_relearn.place(relx=0.1, rely=0.6, anchor="center")
                        globalVariable.button_hard.place(relx=0.25, rely=0.6, anchor="center")
                        globalVariable.button_good.place(relx=0.4, rely=0.6, anchor="center")
                        globalVariable.button_easy.place(relx=0.55, rely=0.6, anchor="center")
                        globalVariable.button_back.place(relx= 0.1, rely=0.9, anchor="center")
                        globalVariable.button_flip.place(relx=0.9, rely= 0.6, anchor='center') 
        else:
            for i in range(len(setsData)):
                if get_deck_name(setsData[i]) == globalVariable.deck_listbox.get(globalVariable.deck_listbox.curselection()[0]):
                    if count_pipe_characters(setsData[i]) < 3:
                        continue
                    elif count_pipe_characters(setsData[i]) == 4:
                        clean_library()
                        create_card_label()
            
                        globalVariable.wordLable.place(relx=0.5, rely=0.2, anchor="center")
                        globalVariable.definitionLable.place(relx=0.5, rely=0.3, anchor="center")
                        globalVariable.button_relearn.place(relx=0.1, rely=0.6, anchor="center")
                        globalVariable.button_hard.place(relx=0.25, rely=0.6, anchor="center")
                        globalVariable.button_good.place(relx=0.4, rely=0.6, anchor="center")
                        globalVariable.button_easy.place(relx=0.55, rely=0.6, anchor="center")
                        globalVariable.button_back.place(relx= 0.1, rely=0.9, anchor="center")
                        globalVariable.button_flip.place(relx=0.9, rely= 0.6, anchor='center') 
    else:
        messagebox.showwarning("Warning", "Please select just one deck to study.")

def handleLevel(nminutes, ndays):    
    if globalVariable.cardIndex <= len(globalVariable.cardList):
        globalVariable.cardList[globalVariable.cardIndex-1][3] = (datetime.now() + timedelta(minutes = nminutes, days = ndays)).strftime("%m/%d/%Y, %H:%M:%S")
        globalVariable.cardList[globalVariable.cardIndex-1][4] = "learned"
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(globalVariable.cardList)):
                fileObject.write(globalVariable.cardList[ele][0] + '|' + globalVariable.cardList[ele][1] + '|' + globalVariable.cardList[ele][2] + '|' + (globalVariable.cardList[ele][3]) + '|' + globalVariable.cardList[ele][4] + '\n')
        fileObject.close()
    show_card()

def flip_card():
    if globalVariable.cardIndex <= len(globalVariable.cardList):
        globalVariable.definitionLable.config(text=globalVariable.cardList[globalVariable.cardIndex - 1][2])