from tkinter import *
from tkinter import filedialog
from datetime import datetime
from datetime import timedelta
from tkinter import messagebox
from tkinter import ttk

#hàm lấy tên deck được chọn 
def get_deck_name(var):
    return var.split('|')[0]

def get_words(var):
    return var.split('|')[1]

def get_definition(var):
    return var.split('|')[2]

#hàm lấy cả nội dung deck
def get_card_infor(var):
    info = var.split("|")
    return info

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

#import
def import_deck():
    
    global deck_listbox
    
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
                deck_listbox.insert(END, get_deck_name(importData[i]))
                deck_added.append(get_deck_name(importData[i]))

        fileObject.close()
        messagebox.showinfo("Notification","Uploaded successfully")

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

def selected_deck():
    global deck_listbox
    
    selected = []
    selected_index = deck_listbox.curselection()
    for index in selected_index:
        selected.append(deck_listbox.get(index))
        
    return selected
    
#xóa deck
def delete_deck():
    global deck_listbox
    
    if len(deck_listbox.curselection()) > 0:
        result = messagebox.askokcancel('Notification','Are you sure you want to delete the selected deck?')
        
        if result:
            index_del = deck_listbox.curselection()
            deleted_items = selected_deck()
            
            for index in reversed(index_del):
              
                deck_listbox.delete(index)
                
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
        
def create_child_window(name_window, text_label, text_button, add_def, cacel_def):
    
    child_window = Toplevel(window)
    child_window.title(name_window)
    child_window.configure(bg='#6E17BF')
    #child_window.iconbitmap('icon.ico')
    child_window.resizable(False, False)

    child_x = window.winfo_x() + (window.winfo_width() - 300) // 2
    child_y = window.winfo_y() + (window.winfo_height() - 200) // 2
    
    child_window.geometry(f"{300}x{200}+{child_x}+{child_y}")
    
    child_label = Label(child_window, text = text_label,
                font = ("Cooper Black", 15), fg = "white", bg = "#6E17BF")
    child_label.place(relx = 0.5, rely = 0.25, anchor = "center")
    child_button = create_button(child_window, text_button, 10, 5, add_def)
    child_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    cancel_button = create_button(child_window, "Cancel", 10, 5, cacel_def)
    cancel_button.place(relx = 0.5, rely = 0.85, anchor = "center")
    
    return child_window
        
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
                deck_listbox.delete(0, END)
                for deck in get_deck_list():
                    deck_listbox.insert(END, deck)
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
            deck_listbox.insert(END, new_deck)
            fileObject = open('data.txt', mode="a+", encoding="utf-8")
            fileObject.write(new_deck + '|' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '|' + "unlearn" + "\n")
            fileObject.close()
            
            add_deck_entry.delete(0, END)
            
    def close_add_deck_window():
        window_add_deck.destroy()
        
    window_add_deck = create_child_window("Add new deck", "Add your new deck", "Add", add_deck, close_add_deck_window)
    add_deck_entry = Entry(window_add_deck)
    add_deck_entry.place(relx = 0.5, rely = 0.4, anchor = "center")

    
def see_card():
    global deck_listbox
    # Get the selected deck name
    selected_deck = deck_listbox.get(deck_listbox.curselection()[0])

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

def window_add_card():

    def add_card():
        new_word = add_word_entry.get()
        new_def = add_def_entry.get()
        
        if new_word == "" or new_def == "":
            messagebox.showerror('Notification', 'Please enter a deck name.')
            add_card_window.destroy()
            
        else :
            see_card_listbox.insert(END, f"{new_word}: {new_def}")
            fileObject = open('data.txt', mode="a+", encoding="utf-8")
            fileObject.write(str(deck_name[0]) + '|' + new_word + '|' + new_def + '|' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '|' + "unlearn" + "\n")
            fileObject.close()
            
            add_word_entry.delete(0, END)
            add_def_entry.delete(0, END)
    
    
    def close_add_card_window():
        add_card_window.destroy()
    
    add_card_window = create_child_window("Add new card", "Add your new card", "Add", add_card, close_add_card_window)
    add_word_entry = Entry(add_card_window)
    add_word_entry.place(relx = 0.5, rely = 0.38, anchor = "center")
    add_def_entry = Entry(add_card_window)
    add_def_entry.place(relx = 0.5, rely = 0.49, anchor = "center")
    
def delete_card():
    
    if len(see_card_listbox.curselection()) > 0:
        result = messagebox.askokcancel('Notification', 'Are you sure you want to delete the selected card?')
        
        if result:
            index = see_card_listbox.curselection()
            word = []
            defi = []
            
            for i in reversed(index):
                card = see_card_listbox.get(i)  # Use i instead of index
                word_def = card.split(":")
                word.append(word_def[0])
                defi.append(word_def[1])
                see_card_listbox.delete(i)  # Use i instead of index
            
            if deck_name:
                fileObject = open('data.txt', mode="r", encoding="utf-8")
                _data = fileObject.read().splitlines()
                fileObject.close()
                sets = ''
                for i in range(len(_data)):
                    print(get_words(_data[i]))
                    print(get_definition(_data[i]))
                    if (get_words(_data[i]) not in word and get_definition(_data[i]) not in defi) or (get_words(_data[i]) in word and get_definition(_data[i]) in defi and get_deck_name(_data[i]) not in deck_name):
                        sets += _data[i] + '\n'
                fileObject = open('data.txt', mode="w+", encoding="utf-8")
                fileObject.write(sets)
                fileObject.close()
    else:
        messagebox.showerror('Notification', 'You have not selected the card to delete. Please check again')

#tạo listbox
def create_listbox(name_labelframe, ndef):
    
    listbox = Listbox(name_labelframe, selectmode=MULTIPLE, bg = "#cba3f0",
                      font = ("Cooper Black", 20), fg = "white",
                      selectbackground = "#eb83c1", cursor = "hand2",
                      activestyle = 'none', justify = LEFT)
    listbox.place(relx=0.01, rely=0, relwidth=4/5, relheight=1)

    #tạo thanh trượt
    scroll_bar = Scrollbar(listbox, orient="vertical")
    scroll_bar.pack(side="right", fill="y")
    scroll_bar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scroll_bar.set)
    
    for content in ndef:
        listbox.insert(END, content)
    
    def all_button(name_button, ndef, rely_button):
        button = Button(name_labelframe, text = name_button, cursor = "hand2", 
                               bg = "#eb83c1", fg = "white", font = ("Cooper Black", 10),
                               command = ndef)   
        button.place(relx=0.9, rely = rely_button, relwidth=0.15, height = 30, anchor = "center")
    
    all_button("Select All", lambda : listbox.select_set(0, END), 0.1)
    all_button("Deselect All", lambda : listbox.select_clear(0, END), 0.2)

    return listbox

#study
#Học lại 1 phút
# def handleRelearn():
#     global cardIndex
#     global cardList
#     if cardIndex <= len(cardList):
#         cardList[cardIndex-1][3] = (datetime.now() + timedelta(minutes=1)).strftime("%m/%d/%Y, %H:%M:%S")
#         cardList[cardIndex-1][4] = "learned"
#         fileObject = open('data.txt', mode='w+', encoding='utf-8')
#         for ele in range(len(cardList)):
#                 fileObject.write(cardList[ele][0] + '|' + cardList[ele][1] + '|' + cardList[ele][2] + '|' + cardList[ele][3] + '|' + cardList[ele][4] + '\n')
#         fileObject.close()
#     show_card()
    
def handleLevel(nminutes, ndays):
    
    global cardIndex
    global cardList
    
    if cardIndex <= len(cardList):
        cardList[cardIndex-1][3] = (datetime.now() + timedelta(minutes = nminutes, days = ndays)).strftime("%m/%d/%Y, %H:%M:%S")
        cardList[cardIndex-1][4] = "learned"
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(cardList)):
                fileObject.write(cardList[ele][0] + '|' + cardList[ele][1] + '|' + cardList[ele][2] + '|' + (cardList[ele][3]) + '|' + cardList[ele][4] + '\n')
        fileObject.close()
    show_card()
    
def show_card():
    global cardIndex
    global cardList
    global wordLable 
    global definitionLable 

    if cardIndex < len(cardList):
        if datetime.strptime(cardList[cardIndex][3], "%m/%d/%Y, %H:%M:%S") < datetime.now() and cardList[cardIndex][0] == deck_listbox.get(deck_listbox.curselection()[0]):
            wordLable.config(text=cardList[cardIndex][1])
            definitionLable.config(text='')
            cardIndex += 1
        else:
            cardIndex += 1
            show_card()
    else:
        cardIndex += 1
        wordLable.config(text='Done!!!')
        definitionLable.config(text='')
        

def create_card_label():
    global deck_listbox
    global wordLable 
    global definitionLable 
    global cardIndex
    global cardList
    global total
    global readed
    readed = 0
    total = 0
    cardIndex = 0
    cardList = []

    wordLable = create_label("", 20)
    definitionLable = create_label("", 15)

    fileObject = open('data.txt', mode='r', encoding="utf-8")
    setsData = fileObject.read().splitlines()
    fileObject.close()
    if len(setsData) > 0:
        for i in range(len(setsData)):
            if count_pipe_characters(setsData[i]) == 4:
                cardList.append(get_card_infor(setsData[i]))
                if get_deck_name(setsData[i]) == deck_listbox.get(deck_listbox.curselection()[0]):
                    total += 1
                    if setsData[i] and get_card_infor(setsData[i])[4] == 'learned':
                        readed += 1
        if selected_deck():
            show_card()
        else:    
            wordLable.config(text="No card")
            definitionLable.config(text='')

def flip_card():
    if cardIndex <= len(cardList):
        definitionLable.config(text=cardList[cardIndex - 1][2])
        
        
#stat
def stat_window():
    global selected_deck

    if len(deck_listbox.curselection()) == 0:
        messagebox.showwarning("Warning", "Please select a deck to study.")
    elif len(deck_listbox.curselection()) == 1:
        clean_library()
        stat_function()

        deck_label_frame_1.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor="center")
        total_label.place(relx=0.50, rely=0.2, anchor="center")
        learned_label.place(relx=0.50, rely=0.3, anchor="center")
        Due_label.place(relx=0.50, rely=0.4, anchor="center")
        progress_label.place(relx=0.50, rely=0.5, anchor="center")
        lb_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    else:
        messagebox.showwarning("Warning", "Please select just one deck to study.")


def stat_function():
    global window
    global deck_listbox
    global deck
    global selected_deck

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

        progressbar = ttk.Progressbar(deck_label_frame_1, length=600, mode='determinate', orient='horizontal')
        progressbar.place(relx=0.50, rely=0.75, anchor="center")

        if total_deck_cards > 0:
            progress_percentage = (learned_deck_cards / total_deck_cards) * 100
        else:
            progress_percentage = 0

        # Set the value of the progress bar
        progressbar['value'] = progress_percentage

    total_label.config(text=f'Total: {total_cards}')
    learned_label.config(text=f'Learned: {learned_cards}')
    Due_label.config(text=f'Due: {due_cards}')

    if total_cards > 0:
        progress_label.config(text=f'Progress: {(learned_cards / total_cards) * 100:.2f}%')
    else:
        progress_label.config(text='Progress: 0.00%')

def stat_back_to_library():
    deck_label_frame_1.place_forget()
    total_label.place_forget()
    learned_label.place_forget()
    Due_label.place_forget()
    progress_label.place_forget()
    lb_button.place_forget()

    show_library_screen()

#GIAO DIỆN
#tạo label
def create_label(ntext, fs):
    
    new_label = Label(window, text = ntext,
                font = ("Cooper Black", fs),  #forn, size
                fg = "white",                 # Màu chữ
                bg = "#6E17BF",               #Màu background
                justify = CENTER, wraplength = 800)              
     
    return new_label
    
#tạo button
def create_button(child_window, name_button,fs, nwidth, ndef):
    
    new_button = Button(child_window, text = name_button, 
                        font = ("Cooper Black", fs),
                        width = nwidth, pady = 5,
                        fg = "white",
                        bg = "#bd46bd",
                        relief="raise",
                        activebackground = "#BF17BC",
                        command = ndef,
                        cursor = "hand2")   #kiểu button
    
    return new_button

#MAIN
#hiện button & label mainscreen
def show_main_label_button():
    label_main.place(relx = 0.5, rely = 0.3, anchor = "center")
    library_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    import_button.place(relx = 0.5, rely = 0.85, anchor = "center")
    exit_button.place(relx = 0.99, rely = 0.99, anchor = "se")
    
#Xóa label & button mainscreen
def clean_main_screen():
    label_main.place_forget()
    library_button.place_forget()
    import_button.place_forget()
    exit_button.place_forget()

#quay lại mainscreen   
def back_main_screen(screen):
    #từ import về main
    if screen == "import":
        label_import.place_forget()
        imtomain_back_button.place_forget()
        down_sample_button.place_forget()
        up_file_button.place_forget()
    #từ library về main
    if screen == "library":
        clean_library()
        
    show_main_label_button()
    
#IMPORT
#xóa button & label mainscreen, hiện import
def show_import_screen():
    clean_main_screen()
    
    label_import.place(relx = 0.5, rely = 0.35, anchor = "center")
    imtomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    down_sample_button.place(relx = 0.5, rely = 0.6, anchor = "center")
    up_file_button.place(relx = 0.5, rely = 0.75, anchor = "center")
    
#LIBRARY
#xóa button & label mainscreen, hiện export
def main_to_library():
    clean_main_screen()
    show_library_screen()
    
def show_library_screen():
    
    deck_label_frame.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor = "center")
    litomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    delete_deck_button.place(relx = 0.26, rely = 0.8, anchor = "center")
    download_button.place(relx = 0.38, rely = 0.8, anchor = "center")
    add_deck_button.place(relx = 0.50, rely = 0.8, anchor = "center")
    stat_button.place(relx=0.62, rely=0.8, anchor="center")
    see_card_button.place(relx = 0.74, rely = 0.8, anchor = "center")
    study_button.place(relx = 0.99, rely = 0.99, anchor = "se")

def clean_library():
    deck_label_frame.place_forget()
    litomain_back_button.place_forget()
    delete_deck_button.place_forget()
    download_button.place_forget()
    see_card_button.place_forget()
    add_deck_button.place_forget()
    study_button.place_forget()
    stat_button.place_forget()

#see_card
def show_see_card():
    global see_card_listbox
    global deck_name
    clean_library()
    
    card_label_frame.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor = "center")
    sctoli_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    add_card_button.place(relx = 0.65, rely = 0.8, anchor = "center")
    delete_card_button.place(relx = 0.35, rely = 0.8, anchor = "center")
    see_card_listbox = create_listbox(card_label_frame, see_card())
    deck_name = selected_deck()
    
def sc_back_li():
    
    card_label_frame.place_forget()
    sctoli_back_button.place_forget()
    add_card_button.place_forget()
    delete_card_button.place_forget()
    
    show_library_screen()

def count_pipe_characters(input_string):
    return input_string.count("|")

def study_window():
    global wordLable 
    global definitionLable 
    counter = 0

    if len(deck_listbox.curselection()) == 0:
        messagebox.showwarning("Warning", "Please select a deck to study.")
    elif len(deck_listbox.curselection()) == 1:
        fileObject = open('data.txt', mode='r', encoding="utf-8")
        setsData = fileObject.read().splitlines()
        fileObject.close()
        for i in range(len(setsData)):
            if get_deck_name(setsData[i]) == deck_listbox.get(deck_listbox.curselection()[0]):
                counter += 1

        if counter == 1: 
            for i in range(len(setsData)):
                if get_deck_name(setsData[i]) == deck_listbox.get(deck_listbox.curselection()[0]):
                    if count_pipe_characters(setsData[i]) < 4:
                        messagebox.showwarning("Warning", "Deck is empty. Please add card to deck.")
                        break
                    else:
                        clean_library()
                        create_card_label()
            
                        wordLable.place(relx=0.5, rely=0.2, anchor="center")
                        definitionLable.place(relx=0.5, rely=0.3, anchor="center")
                        button_relearn.place(relx=0.1, rely=0.6, anchor="center")
                        button_hard.place(relx=0.25, rely=0.6, anchor="center")
                        button_good.place(relx=0.4, rely=0.6, anchor="center")
                        button_easy.place(relx=0.55, rely=0.6, anchor="center")
                        button_back.place(relx= 0.1, rely=0.9, anchor="center")
                        button_flip.place(relx=0.9, rely= 0.6, anchor='center') 
        else:
            for i in range(len(setsData)):
                if get_deck_name(setsData[i]) == deck_listbox.get(deck_listbox.curselection()[0]):
                    if count_pipe_characters(setsData[i]) < 3:
                        continue
                    elif count_pipe_characters(setsData[i]) == 4:
                        clean_library()
                        create_card_label()
            
                        wordLable.place(relx=0.5, rely=0.2, anchor="center")
                        definitionLable.place(relx=0.5, rely=0.3, anchor="center")
                        button_relearn.place(relx=0.1, rely=0.6, anchor="center")
                        button_hard.place(relx=0.25, rely=0.6, anchor="center")
                        button_good.place(relx=0.4, rely=0.6, anchor="center")
                        button_easy.place(relx=0.55, rely=0.6, anchor="center")
                        button_back.place(relx= 0.1, rely=0.9, anchor="center")
                        button_flip.place(relx=0.9, rely= 0.6, anchor='center') 
    else:
        messagebox.showwarning("Warning", "Please select just one deck to study.")

def study_to_library():
    global deck_listbox
    global wordLable 
    global definitionLable 

    wordLable.place_forget()
    definitionLable.place_forget()
    button_relearn.place_forget()
    button_hard.place_forget()
    button_good.place_forget()
    button_easy.place_forget()
    button_back.place_forget()
    button_flip.place_forget()
    wordLable.place_forget()
    definitionLable.place_forget()
    show_library_screen()

#MAIN

#tạo window
window = Tk()
#set size (wxh)
#position (width x high + a + b)
window.geometry("1000x600")
#window.attributes('-fullscreen', True)
#tên app
window.title("Flash Card App")
#set icon
#window.iconbitmap('icon.ico')
#set background color
#window.configure(bg='#6E17BF')
#khả năng thay đổi kích thước của cửa sổ
window.resizable(False, False)
# Lấy chiều dài và chiều rộng của màn hình

#vẽ background
def draw_rectangle(relx1, rely1, relx2, rely2, color):
    global screen_width
    global screen_height
    global the_canvas
    
    x1 = relx1 * screen_width
    y1 = rely1 * screen_height
    x2 = relx2 * screen_width
    y2 = rely2 * screen_height
    
    the_canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = "")
    
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
screen_width = 1000
screen_height = 600

the_canvas = Canvas(window,width=screen_width,height=screen_height, highlightthickness=0)
the_canvas.place(x=0,y=0)

draw_rectangle(0, 0, 1, 1, "#1A17BF")
draw_rectangle(0.01, 1/60 , 0.99, 59/60, "#BF17BC")
draw_rectangle(0.02, 1/30, 0.98, 29/30, "#1A17BF")
draw_rectangle(0.03, 0.05, 0.97, 0.95, "#6e17bf")
draw_rectangle(0.04, 1/15, 0.08, 14/15, "#BF17BC")
draw_rectangle(0.1, 1/15, 0.14, 14/15, "#BF17BC")
draw_rectangle(0.16, 1/15, 0.2, 14/15, "#BF17BC")
draw_rectangle(0.92, 1/15, 0.96, 14/15, "#BF17BC")
draw_rectangle(0.86, 1/15, 0.9, 14/15, "#BF17BC")
draw_rectangle(0.8, 1/15, 0.84, 14/15, "#BF17BC")

#Mainscreen
#tạo label main screen
label_main = create_label("FLASHCARD", 80)
#tạo button
library_button = create_button(window, "Library",25,10,main_to_library)
import_button = create_button(window, "Import", 25,10,show_import_screen)
def close_window():
    window.destroy()
exit_button = create_button(window, "Exit", 12, 5, close_window)
#hiển thị mainscreen
show_main_label_button()

#Import    
#tạo label
label_import = create_label("Please upload your file similar to the sample file below", 35)
#tạo button
down_sample_button = create_button(window, "Download Sample File", 20, 20,lambda: export("sample"))
up_file_button = create_button(window, "Upload Your File", 20, 20, import_deck)
imtomain_back_button = create_button(window, "Back", 12, 5, lambda: back_main_screen("import"))

#Library
#labelframe chứa select option
deck_label_frame = LabelFrame(window, text = "Yours deck", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
#button của libirary
litomain_back_button = create_button(window, "Back", 12, 5, lambda: back_main_screen("library"))
delete_deck_button = create_button(window, "Delete", 12, 10, delete_deck)
download_button = create_button(window, "Download", 12, 10, lambda : export("export"))
see_card_button = create_button(window, "See Card", 12, 10, show_see_card)
add_deck_button = create_button(window, "Add deck", 12, 10, add_deck_window)
stat_button = create_button(window, "Stat", 12, 10, stat_window)
study_button = create_button(window, "STUDY", 12, 10, study_window)
deck_listbox = create_listbox(deck_label_frame, get_deck_list())
deck_listbox.bind("<Double-Button-1>", rename_deck_window)
#see card
card_label_frame = LabelFrame(window, text = "Yours cards", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
sctoli_back_button = create_button(window, "Back", 12, 5, sc_back_li)
add_card_button = create_button(window, "Add Card", 15, 10, window_add_card)
delete_card_button = create_button(window, "Delete Card", 15, 10, delete_card)

#study
# Create 4 study buttons
button_relearn = create_button(window,"Relearn", 15, 10,lambda: handleLevel(1, 0))
button_hard = create_button(window,"Hard", 15, 10, lambda: handleLevel(6, 0))
button_good = create_button(window,"Good", 15, 10, lambda: handleLevel(10, 0))
button_easy = create_button(window,"Easy", 15, 10, lambda: handleLevel(0, 4))
button_back = create_button(window,"Back", 15, 10, study_to_library)
button_flip = create_button(window,"FLip", 15, 10, flip_card)

#button của stat:
deck_label_frame_1 = LabelFrame(window, text = f"Learning progression of deck", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
lb_button = create_button(window, "Back", 12, 5, stat_back_to_library)
learned_label = create_label('Learned: ', 20)
Due_label = create_label('Due: ', 20)
progress_label = create_label('Progress: ', 20)
total_label = create_label('total: ', 15)


#chay
window = mainloop()