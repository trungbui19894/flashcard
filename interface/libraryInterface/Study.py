import globalVariable
from interface.components.button import create_button
from controller.studyController import handleRelearn, handleLevel
from controller.displayHandle import study_to_library
from controller.cardController import flip_card

def Study():
    globalVariable.button_relearn = create_button("Relearn", 15, 10, handleRelearn)
    globalVariable.button_hard = create_button("Hard", 15, 10, lambda: handleLevel(6, 0))
    globalVariable.button_good = create_button("Good", 15, 10, lambda: handleLevel(10, 0))
    globalVariable.button_easy = create_button("Easy", 15, 10, lambda: handleLevel(0, 4))
    globalVariable.button_back = create_button("Back", 15, 10, study_to_library)
    globalVariable.button_flip = create_button("FLip", 15, 10, flip_card)