from tkinter import *
from tkinter import messagebox
import globalVariable
from controller.common import get_deck_name
from controller.deckController import get_deck_list, selected_deck
from interface.components.childWindow import create_child_window

#hiện button & label mainscreen
def show_main_label_button():
    globalVariable.label_main.place(relx = 0.5, rely = 0.3, anchor = "center")
    globalVariable.library_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    # globalVariable.import_button.place(relx = 0.5, rely = 0.85, anchor = "center")
    globalVariable.exit_button.place(relx = 0.99, rely = 0.99, anchor = "se")

def main_to_library():
    clean_main_screen()
    show_library_screen()

def clean_main_screen():
    globalVariable.label_main.place_forget()
    globalVariable.library_button.place_forget()
    # globalVariable.import_button.place_forget()
    globalVariable.exit_button.place_forget()

def show_library_screen():
    globalVariable.deck_label_frame.place(relx=0.5, rely=0.4, relwidth=2/3, relheight=2/3, anchor = "center")
    globalVariable.litomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    globalVariable.delete_deck_button.place(relx = 0.26, rely = 0.8, anchor = "center")
    globalVariable.download_button.place(relx = 0.42, rely = 0.8, anchor = "center")
    globalVariable.see_card_button.place(relx = 0.74, rely = 0.8, anchor = "center")
    globalVariable.add_deck_button.place(relx = 0.58, rely = 0.8, anchor = "center")
    globalVariable.study_button.place(relx = 0.99, rely = 0.99, anchor = "se")

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

def rename_deck_window():

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
    #tao window cho input new card
    # child_window = create_child_window("Add Card", "Enter the word and definition", "Add", lambda: save_new_card(selected_deck), close_child_window)

    # Entry widgets for word and definition
    # entry_word = Entry(child_window)
    # entry_word.place(relx=0.5, rely=0.25, anchor="center")
    # entry_definition = Entry(child_window)
    # entry_definition.place(relx=0.5, rely=0.5, anchor="center")

    # Labels for word and definition
    # label_word = Label(child_window, text="Word:", font=("Cooper Black", 12), fg="white", bg="#6E17BF")
    # label_word.place(relx=0.25, rely=0.25, anchor="center")
    # label_definition = Label(child_window, text="Definition:", font=("Cooper Black", 12), fg="white", bg="#6E17BF")
    # label_definition.place(relx=0.25, rely=0.5, anchor="center")

def show_import_screen():
    clean_main_screen()
    
    globalVariable.label_import.place(relx = 0.5, rely = 0.35, anchor = "center")
    globalVariable.imtomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    globalVariable.down_sample_button.place(relx = 0.5, rely = 0.6, anchor = "center")
    globalVariable.up_file_button.place(relx = 0.5, rely = 0.75, anchor = "center")

def sc_back_li():
    globalVariable.card_label_frame.place_forget()
    globalVariable.sctoli_back_button.place_forget()
    globalVariable.add_card_button.place_forget()
    globalVariable.delete_card_button.place_forget()
    
    show_library_screen()

def study_to_library():
    globalVariable.wordLable.place_forget()
    globalVariable.definitionLable.place_forget()
    globalVariable.button_relearn.place_forget()
    globalVariable.button_hard.place_forget()
    globalVariable.button_good.place_forget()
    globalVariable.button_easy.place_forget()
    globalVariable.button_back.place_forget()
    globalVariable.button_flip.place_forget()
    show_library_screen()