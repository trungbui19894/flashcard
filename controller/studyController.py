from datetime import datetime
from datetime import timedelta
import globalVariable
from controller.displayHandle import clean_library
from controller.cardController import create_card_label, show_card

def study_window():
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

def handleRelearn():
    if globalVariable.cardIndex <= len(globalVariable.cardList):
        globalVariable.cardList[globalVariable.cardIndex-1][3] = (datetime.now() + timedelta(minutes=1)).strftime("%m/%d/%Y, %H:%M:%S")
        globalVariable.cardList[globalVariable.cardIndex-1][4] = "true"
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(globalVariable.cardList)):
                fileObject.write(globalVariable.cardList[ele][0] + '|' + globalVariable.cardList[ele][1] + '|' + globalVariable.cardList[ele][2] + '|' + globalVariable.cardList[ele][3] + '|' + globalVariable.cardList[ele][4] + '\n')
        fileObject.close()
    show_card()

def handleLevel(nminutes, ndays):
    if globalVariable.cardIndex <= len(globalVariable.cardList):
        globalVariable.cardList[globalVariable.cardIndex-1][3] = (datetime.now() + timedelta(minutes = nminutes, days = ndays)).strftime("%m/%d/%Y, %H:%M:%S")
        fileObject = open('data.txt', mode='w+', encoding='utf-8')
        for ele in range(len(globalVariable.cardList)):
                fileObject.write(globalVariable.cardList[ele][0] + '|' + globalVariable.cardList[ele][1] + '|' + globalVariable.cardList[ele][2] + '|' + (globalVariable.cardList[ele][3]) + '|' + globalVariable.cardList[ele][4] + '\n')
        fileObject.close()
    show_card()