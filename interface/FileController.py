import globalVariable
from interface.components.label import create_label
from interface.components.button import create_button
from controller.fileController import export, import_deck
from controller.displayHandle import back_main_screen

def FileCtr():
    #tạo label
    globalVariable.label_import = create_label("Please upload your file similar to the sample file below", 35)
    #tạo button
    globalVariable.down_sample_button = create_button(globalVariable.window, "Download Sample File", 20, 20,lambda: export("sample"))
    globalVariable.up_file_button = create_button(globalVariable.window, "Upload Your File", 20, 20, import_deck)
    globalVariable.imtomain_back_button = create_button(globalVariable.window, "Back", 12, 5, lambda: back_main_screen("import"))