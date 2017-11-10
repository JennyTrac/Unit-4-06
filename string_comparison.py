# Created by Jenny Trac
# Created on Nov 10 2017
# Program compares two strings to see if theyre the same (even with Upper or lower)

import ui

def compare_strings(string1, string2):
    # compares strings
    
    if str.upper(string1) == str.upper(string2):
        return True
    else:
        return False
    
def check_touch_up_inside(sender):
    # button to compare strings
    
    firstword = str(view['string1_textfield'].text)
    secondword = str(view['string2_textfield'].text)
    
    result = compare_strings(firstword, secondword)
    
    if result is True:
        view['answer_label'].text = "Good job, those are the same words!"
    else:
        view['answer_label'].text = "No silly goose, those aren't the same thing!"



view = ui.load_view()
view.present('sheet')
