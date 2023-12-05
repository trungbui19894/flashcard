from tkinter import *
import globalVariable
from interface.components.button import create_button
from interface.components.label import create_label
from controller.displayHandle import stat_back_to_library

def Stat():
    #button của stat:
    globalVariable.deck_label_frame_1 = LabelFrame(globalVariable.window, text = f"Learning progression of deck", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white", relief="raise")
    globalVariable.lb_button = create_button(globalVariable.window, "Back", 12, 5, stat_back_to_library)
    globalVariable.learned_label = create_label('Learned: ', 20)
    globalVariable.Due_label = create_label('Due: ', 20)
    globalVariable.progress_label = create_label('Progress: ', 20)
    globalVariable.total_label = create_label('total: ', 15)