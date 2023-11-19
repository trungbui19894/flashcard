from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def getSetsName(var):
    return var.split('|')[0]

#Add funtion cho button thêm từ
def addWord():
    fileObject = open('data.txt', mode="a+", encoding="utf-8")
    fileObject.write(setName.get() + '|' + word.get() + '|' + definition.get() + '\n')
    fileObject.close()
    getSets()

#Lấy list các set
def getSets():
    fileObject = open('data.txt', mode="r", encoding="utf-8")
    setsData = fileObject.read().splitlines()
    sets = list(map(getSetsName, setsData))
    setsCombobox['values'] = tuple(sets)
    fileObject.close()

#Xóa set
def delSet():
    fileObject = open('data.txt', mode="w+", encoding="utf-8")
    setsData = fileObject.read().splitlines()
    for set = 
    fileObject.close()

#Lấy cards từ set được chọn
# def selectSets():


#Đảm bảo các function được gọi trong module sẽ ko chạy trong các module khác import module này
if __name__ == '__main__':
    #Tạo giao diện
    root = ttk.Window(themename="superhero")
    root.title('Flashcards')
    root.geometry('500x400')

    #Tạo biến chứa dữ liệu từ input
    setName = ttk.StringVar()
    word = ttk.StringVar()
    definition = ttk.StringVar()

    #Kiểm soát tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    #tab tạo set
    setFrame = ttk.Frame(notebook)
    notebook.add(setFrame, text='Tạo Set')

    #label và input cho phần nhập nội dung card
    ttk.Label(setFrame, text='Tên Set:').pack(padx=5, pady=5)
    ttk.Entry(setFrame, textvariable=setName, width=30).pack(padx=5, pady=5)

    ttk.Label(setFrame, text='Từ:').pack(padx=5, pady=5)
    ttk.Entry(setFrame, textvariable=word, width=30).pack(padx=5, pady=5)
                                                             
    ttk.Label(setFrame, text='Giải Nghĩa:').pack(padx=5, pady=5)
    ttk.Entry(setFrame, textvariable=definition, width=30).pack(padx=5, pady=5)

    #Các button cho phần nhập nội dung card
    ttk.Button(setFrame, text='Thêm Từ', command=addWord).pack(padx=5, pady=10)

    #tab chọn set
    selectSetFrame = ttk.Frame(notebook)
    notebook.add(selectSetFrame, text='Chọn Set')

    #Combobox để chọn các Set đã được tạo
    setsCombobox = ttk.Combobox(selectSetFrame, state='readonly')
    setsCombobox.pack(padx=5, pady=5)

    #Các button cho phần select set
    ttk.Button(selectSetFrame, text='Chọn Set').pack(padx=5, pady=5)
    ttk.Button(selectSetFrame, text='Xóa Set').pack(padx=5, pady=5)

    #tab học cards
    learnFrame = ttk.Frame(notebook)
    notebook.add(learnFrame, text='Học Card')

    #Các biến kiểm soát cards và index
    cardIndex = 0
    currentTabs = []

    #Lables, buttons của flashcards
    wordLable = ttk.Label(learnFrame, text='', font=('TKDefaultFont', 24))
    wordLable.pack(padx=5, pady=40)
    definitionLable = ttk.Label(learnFrame, text='')
    definitionLable.pack(padx=5, pady=5)
    ttk.Button(learnFrame, text='Lật Card').pack(side='bottom', padx=5, pady=5)

    getSets()                                                         
    root.mainloop()