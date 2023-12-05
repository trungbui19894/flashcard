from tkinter import *
from tkinter import messagebox
from datetime import datetime
import globalVariable
from controller.common import get_deck_name
from interface.modal.ChildWindow import create_child_window

def selected_deck():
    selected = []
    selected_index = globalVariable.deck_listbox.curselection()
    for index in selected_index:
        selected.append(globalVariable.deck_listbox.get(index))
        
    return selected

#Lấy list các deck
def get_deck_list():
    fileObject = open('data.txt', mode="r", encoding="utf-8")
    deck_data = fileObject.read().splitlines() 
    sets = []
    for i in range(len(deck_data)):
        if get_deck_name(deck_data[i]) not in sets:
            sets.append(get_deck_name(deck_data[i]))
    fileObject.close()
    return sets

#xóa deck
def delete_deck():    
    if len(globalVariable.deck_listbox.curselection()) > 0:
        result = messagebox.askokcancel('Notification','Are you sure you want to delete the selected deck?')
        
        if result:
            index_del = globalVariable.deck_listbox.curselection()
            deleted_items = selected_deck()
            
            for index in reversed(index_del):
              
                globalVariable.deck_listbox.delete(index)
                
            if deleted_items:
                fileObject = open('data.txt', mode="r", encoding="utf-8")
                deck_data = fileObject.read().splitlines()
                fileObject.close()
                sets = ''
                for i in range(len(deck_data)):
                    if get_deck_name(deck_data[i]) not in deleted_items:
                        sets += deck_data[i] + '\n'
                fileObject = open('data.txt', mode="w+", encoding="utf-8")
                fileObject.write(sets)
                fileObject.close()
                
    else:
        messagebox.showerror('Notification', 'You have not selected the deck to delete. Please check again')

# Add deck
def add_deck_window():
    
    def add_deck():
        new_deck = add_deck_entry.get()
        
        if new_deck == "":
            messagebox.showerror('Notification', 'Please enter a deck name.')
            window_add_deck.destroy()
        elif new_deck in get_deck_list():
            messagebox.showerror('Notification', 'Deck name already exists. Please choose a different name.')
            window_add_deck.destroy()
        else:
            globalVariable.deck_listbox.insert(END, new_deck)
            fileObject = open('data.txt', mode="a+", encoding="utf-8")
            fileObject.write(new_deck + '|' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '|' + "unlearn" + "\n")
            fileObject.close()
            
            add_deck_entry.delete(0, END)
            
    def close_add_deck_window():
        window_add_deck.destroy()
        
    window_add_deck = create_child_window("Add new deck", "Add your new deck", "Add", add_deck, close_add_deck_window)
    add_deck_entry = Entry(window_add_deck)
    add_deck_entry.place(relx = 0.5, rely = 0.4, anchor = "center")

def rename_deck_window(event):
    # Thêm một nút để đổi tên bộ đã chọn
    def rename_deck():
        selected_items = selected_deck()
        if len(selected_items) == 1:
            old_name = selected_items[0]
            new_name = rename_entry.get()
            if new_name:
                fileObject = open('data.txt', mode="r", encoding="utf-8")
                deck_data = fileObject.read().splitlines()
                fileObject.close()

                # Tạo một danh sách mới với tên bộ đã được cập nhật
                updated_deck_data = []
                for line in deck_data:
                    if get_deck_name(line) == old_name:
                        line = line.replace(old_name, new_name)
                    updated_deck_data.append(line)

                # Ghi dữ liệu đã cập nhật trở lại tệp
                fileObject = open('data.txt', mode="w", encoding="utf-8")
                fileObject.write('\n'.join(updated_deck_data))
                fileObject.close()

                # Cập nhật lại danh sách các bộ trong listbox
                globalVariable.deck_listbox.delete(0, END)
                for deck in get_deck_list():
                    globalVariable.deck_listbox.insert(END, deck)
            messagebox.showinfo("Notification", "Rename deck successfully.")
            window_rename_deck.destroy()
        else:
            messagebox.showwarning("Error", "Please select only one deck to rename.")
            window_rename_deck.destroy()
            
    def close_rename_deck_window():
        window_rename_deck.destroy()

    #tạo window cho add_deck
    window_rename_deck = create_child_window("Edit deck name", "Enter the new deck name", "Save", rename_deck, close_rename_deck_window)
    rename_entry = Entry(window_rename_deck)
    rename_entry.place(relx = 0.5, rely = 0.4, anchor = "center")
