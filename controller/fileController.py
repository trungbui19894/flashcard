from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
from controller.common import get_deck_name
from controller.deckController import get_deck_list, selected_deck
import globalVariable

#export
def export(file_name):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    selected_items = selected_deck()
    if file_path:
        if file_name == "sample":
            with open(file_path, 'w') as file:
                file.write("deck|word|definition")
        
        if file_name == "export":
            if selected_items:
                fileObject = open('data.txt', mode="r", encoding="utf-8")
                deck_data = fileObject.read().splitlines()
                fileObject.close()
                
                selected_deck_data = [line for line in deck_data if get_deck_name(line) in selected_items]
                
                if selected_deck_data:
                    with open(file_path, 'w', encoding="utf-8") as file:
                        for line in selected_deck_data:
                            file.write(line + '\n')

                    messagebox.showinfo("Notification", "Downloaded successfully")
                else:
                        messagebox.showwarning("Warning", "No data found for the selected deck.")
            else:
                messagebox.showwarning("Warning", "Please select a deck to download.")

#import
def import_deck():    
    askFile =  filedialog.askopenfilename(initialdir='/', title="select a file", filetypes=(("all file", "*.*"),("png files", "*.png")))

    if askFile:
        importObject = open(askFile, mode='r', encoding="utf-8")
        importData = importObject.read().splitlines()
        importObject.close()
        fileObject = open('data.txt', mode='a+', encoding="utf-8")
        deck_added = []

        for i in range(len(importData)):
            fileObject.write(importData[i] + '|' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '|' + "unlearn" + "\n")
            if get_deck_name(importData[i]) not in get_deck_list() and get_deck_name(importData[i]) not in deck_added:
                globalVariable.deck_listbox.insert(END, get_deck_name(importData[i]))
                deck_added.append(get_deck_name(importData[i]))

        fileObject.close()
        messagebox.showinfo("Notification","Uploaded successfully")