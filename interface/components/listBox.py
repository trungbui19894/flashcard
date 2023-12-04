from tkinter import *

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