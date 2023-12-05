from tkinter import *
import globalVariable
from controller.displayHandle import show_main_label_button
from interface.Home import Home
from interface.FileController import FileCtr
from interface.Stat import Stat
from interface.libraryInterface.Library import Library
from interface.libraryInterface.Study import Study
from interface.libraryInterface.SeeCard import SeeCard

if __name__ == '__main__':
    globalVariable.variableInitialize()
    window = globalVariable.window
    #tạo window
    # window = Tk()
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
    draw_rectangle(0.01, 1/60, 0.99, 59/60, "#BF17BC")
    draw_rectangle(0.02, 1/30, 0.98, 29/30, "#1A17BF")
    draw_rectangle(0.03, 0.05, 0.97, 0.95, "#6e17bf")
    draw_rectangle(0.04, 1/15, 0.08, 14/15, "#BF17BC")
    draw_rectangle(0.1, 1/15, 0.14, 14/15, "#BF17BC")
    draw_rectangle(0.16, 1/15, 0.2, 14/15, "#BF17BC")
    draw_rectangle(0.92, 1/15, 0.96, 14/15, "#BF17BC")
    draw_rectangle(0.86, 1/15, 0.9, 14/15, "#BF17BC")
    draw_rectangle(0.8, 1/15, 0.84, 14/15, "#BF17BC")
 
    Home()
    Library()
    FileCtr()
    SeeCard()
    Stat()
    Study()
    show_main_label_button()
    #chay
    window = mainloop()