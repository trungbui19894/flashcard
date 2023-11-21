from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime
from datetime import timedelta

#function hỗ trợ lấy tên set
def getSetsName(var):
    return var.split('|')[0]
#function hỗ trợ nội dung card
def getCardInfo(var):
    ele = var.split("|")
    return (ele)

#Lấy list các set
def getSets():
    fileObject = open('data.txt', mode="r", encoding="utf-8")
    setsData = fileObject.read().splitlines()
    sets = []
    for i in range(len(setsData)):
        if getSetsName(setsData[i]) not in sets:
            sets.append(getSetsName(setsData[i]))
    setsCombobox['values'] = tuple(sets)
    fileObject.close()

#Add funtion cho button thêm từ
def addWord():
    fileObject = open('data.txt', mode="a+", encoding="utf-8")
    fileObject.write(setName.get() + '|' + word.get() + '|' + definition.get() + '|' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '|' + "false" + '\n')
    fileObject.close()
    getSets()
    word.set("")
    definition.set("")
    
#Xóa set
def delSet():
    fileObject = open('data.txt', mode="r", encoding="utf-8")
    setsData = fileObject.read().splitlines()
    fileObject.close()
    sets = ''
    for i in range(len(setsData)):
        if getSetsName(setsData[i]) != setsCombobox.get():
            sets += setsData[i] + '\n'
    fileObject = open('data.txt', mode="w+", encoding="utf-8")
    fileObject.write(sets)
    fileObject.close()
    getSets()
    setsCombobox.set("")

#Lấy cards từ set được chọn
def selectSet():
    global cardIndex
    global cardList
    global total
    global readed
    total = 0
    readed = 0
    cardIndex = 0
    cardList = []
    fileObject = open('data.txt', mode='r', encoding="utf-8")
    setsData = fileObject.read().splitlines()
    fileObject.close()
    if len(setsData) > 0:
        for i in range(len(setsData)):
            cardList.append(getCardInfo(setsData[i]))
            if getSetsName(setsData[i]) == setsCombobox.get():
                total += 1
                if setsData[i] and getCardInfo(setsData[i])[4] == 'true':
                    readed += 1
        if setsCombobox.get():
            showFlashcards()
            handleMeter()
        else:
            wordLable.config(text="Ko có card đâu nhé cưng :3")
            definitionLable.config(text='')
    

#Hiển thị flashcards
def showFlashcards():
    global cardIndex
    global cardList
    if cardIndex < len(cardList):
        if datetime.strptime(cardList[cardIndex][3], "%m/%d/%Y, %H:%M:%S") < datetime.now() and cardList[cardIndex][0] == setsCombobox.get():
            wordLable.config(text=cardList[cardIndex][1])
            definitionLable.config(text='')
            cardIndex += 1
        else:
            cardIndex += 1
            showFlashcards()
    else:
        wordLable.config(text='Oh yeah, học hết card trong set này rồi (^O^)')
        definitionLable.config(text='')

#Lật card
def flipCard():
    if cardIndex <= len(cardList):
        definitionLable.config(text=cardList[cardIndex - 1][2])

#Học lại 1 phút
def handleRelearn():
    global cardIndex
    global cardList
    if cardIndex <= len(cardList):
        cardList[cardIndex-1][3] = (datetime.now() + timedelta(minutes=1)).strftime("%m/%d/%Y, %H:%M:%S")
        cardList[cardIndex-1][4] = "true"
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(cardList)):
                fileObject.write(cardList[ele][0] + '|' + cardList[ele][1] + '|' + cardList[ele][2] + '|' + cardList[ele][3] + '|' + cardList[ele][4] + '\n')
        fileObject.close()
    showFlashcards()

#Khó 6 phút
def handleHard():
    global cardIndex
    global cardList
    if cardIndex <= len(cardList):
        cardList[cardIndex-1][3] = (datetime.now() + timedelta(minutes=6)).strftime("%m/%d/%Y, %H:%M:%S")
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(cardList)):
                fileObject.write(cardList[ele][0] + '|' + cardList[ele][1] + '|' + cardList[ele][2] + '|' + (cardList[ele][3]) + '|' + cardList[ele][4] + '\n')
        fileObject.close()
    showFlashcards()

#Tốt 10 phút
def handleGood():
    global cardIndex
    global cardList
    if cardIndex <= len(cardList):
        cardList[cardIndex-1][3] = (datetime.now() + timedelta(minutes=10)).strftime("%m/%d/%Y, %H:%M:%S")
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(cardList)):
                fileObject.write(cardList[ele][0] + '|' + cardList[ele][1] + '|' + cardList[ele][2] + '|' + (cardList[ele][3]) + '|' + cardList[ele][4] + '\n')
        fileObject.close()
    showFlashcards()

#Dễ 4 ngày
def handleEasy():
    global cardIndex
    global cardList
    if cardIndex <= len(cardList):
        cardList[cardIndex-1][3] = (datetime.now() + timedelta(days=4)).strftime("%m/%d/%Y, %H:%M:%S")
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(cardList)):
                fileObject.write(cardList[ele][0] + '|' + cardList[ele][1] + '|' + cardList[ele][2] + '|' + (cardList[ele][3]) + '|' + cardList[ele][4] + '\n')
        fileObject.close()
    showFlashcards()

def handleMeter():
    global total
    global readed
    if total > 0 and readed > 0: percent = (readed/total)*100 
    else: percent = 0
    meterProcessor.configure(amountused=percent)
    processLable.config(text=setsCombobox.get())

def handleImportFile():
    askFile =  filedialog.askopenfilename(initialdir='/', title="select a file", filetypes=(("all file", "*.*"),("png files", "*.png")))
    if askFile:
        importObject = open(askFile, mode='r', encoding="utf-8")
        importData = importObject.read().splitlines()
        importObject.close()
        fileObject = open('data.txt', mode='a+', encoding="utf-8")
        for i in range(len(importData)):
            fileObject.write(importData[i] + "\n")
        fileObject.close()
        Messagebox.ok("Import thành công rồi đấy ʕ•ᴥ•ʔ")
    else: Messagebox.ok("Import ko thành công, có gì đó sai sai -_-!")

def handleExportFile():
    askFolder = filedialog.askdirectory()
    if askFolder:
        exportObject = open('data.txt', mode="r", encoding="utf-8")
        exportData = exportObject.read()
        exportObject.close()
        exportDirection = open((askFolder + '/data.txt'), mode="w+", encoding="utf-8")
        exportDirection.write(exportData)
        exportDirection.close()
        Messagebox.ok("File export thành công với tốc độ bàn thờ (~˘▾˘)~")
    else: Messagebox.ok("Có lỗi rồi, chịu ko export được đâu ¯\_(ツ)_/¯")



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
    ttk.Button(selectSetFrame, text='Chọn Set', command=selectSet).pack(padx=5, pady=5)
    ttk.Button(selectSetFrame, text='Xóa Set', command=delSet).pack(padx=5, pady=5)

    #tab học cards
    learnFrame = ttk.Frame(notebook)
    notebook.add(learnFrame, text='Học Card')

    #Lables, buttons của flashcards
    wordLable = ttk.Label(learnFrame, text='', font=('TKDefaultFont', 24))
    wordLable.pack(padx=5, pady=40)
    definitionLable = ttk.Label(learnFrame, text='')
    definitionLable.pack(padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="danger", text='<1 phút\nHọc Lại', command=handleRelearn).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="warning", text='<6 phút\nKhó', command=handleHard).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="info", text='<10 phút\nTốt', command=handleGood).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="success", text='<4 ngày\nDễ', command=handleEasy).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, text='Lật Card', command=flipCard).pack(side='right', padx=5, pady=5)
                                                      
    #Tab tiến độ
    meterProcessor = ttk.Meter(
        notebook, 
        metersize=180,
        padding=30,
        textright="%",
        metertype="semi",
        subtext="process",
    )
    notebook.add(meterProcessor, text='Tiến Độ')

    #Lables, buttons của Tiến Độ
    processLable = ttk.Label(meterProcessor, text='', font=('TKDefaultFont', 24))
    processLable.pack(padx=10, pady=5)

    #Tab nhập xuất
    fileHandleFrame = ttk.Frame(notebook)
    notebook.add(fileHandleFrame, text="Nhập xuất")

    #Lables, buttons
    ttk.Button(fileHandleFrame, text='Import', command=handleImportFile).pack(padx=5, pady=5)
    ttk.Button(fileHandleFrame, text='Export', command=handleExportFile).pack(padx=5, pady=5)

    getSets()
    selectSet()
    root.mainloop()