import globalVariable

def close_window():
    globalVariable.window.destroy()

#hàm lấy tên deck được chọn 
def get_deck_name(var):
    return var.split('|')[0]

def get_words(var):
    return var.split('|')[1]

def get_definition(var):
    return var.split('|')[2]

#hàm lấy cả nội dung deck
def get_card_infor(var):
    info = var.split("|")
    return info