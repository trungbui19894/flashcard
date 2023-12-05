import globalVariable
from interface.components.button import create_button
from controller.studyController import handleLevel, flip_card
from controller.displayHandle import study_to_library

def Study():
    # Create 4 study buttons
    globalVariable.button_relearn = create_button(globalVariable.window,"Relearn", 15, 10,lambda: handleLevel(1, 0))
    globalVariable.button_hard = create_button(globalVariable.window,"Hard", 15, 10, lambda: handleLevel(6, 0))
    globalVariable.button_good = create_button(globalVariable.window,"Good", 15, 10, lambda: handleLevel(10, 0))
    globalVariable.button_easy = create_button(globalVariable.window,"Easy", 15, 10, lambda: handleLevel(0, 4))
    globalVariable.button_back = create_button(globalVariable.window,"Back", 15, 10, study_to_library)
    globalVariable.button_flip = create_button(globalVariable.window,"FLip", 15, 10, flip_card)