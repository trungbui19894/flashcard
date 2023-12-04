import globalVariable
from interface.components.label import create_label
from interface.components.button import create_button
from controller.common import close_window
from controller.displayHandle import main_to_library, show_import_screen

def Home():
    #tạo label main screen
    globalVariable.label_main = create_label("FLASHCARD", 80)
    #tạo button
    globalVariable.library_button = create_button("Library",25,10,main_to_library)
    globalVariable.import_button = create_button("Import", 25,10,show_import_screen)
    globalVariable.exit_button = create_button("Exit", 12, 5, close_window)
