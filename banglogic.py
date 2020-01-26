import random
import json

with open('bangladata.json') as f:
    data = json.load(f)

bw = data['bangla_words'] #bangla words
tw = data['translations'] #translated words

#convert lists to dict
bangladict = dict(zip(bw, tw))

gen_question = random.choice(list(bangladict.keys()))

#initialize buttons
_btn1 = random.choice(list(bangladict.values())) 
_btn2 = random.choice(list(bangladict.values())) 
_btn3 = random.choice(list(bangladict.values())) 
correct_btn = bangladict[gen_question]

mult_choice = [_btn1, _btn2, _btn3, correct_btn]

def check_if_correct(ins, _gui_lbl, _gui_btns):     
    if ins.text == correct_btn:
        _gui_lbl.color = [0, 0.99, 0, 1]            
        update_label(_gui_lbl) 
        update_buttons(_gui_btns)

    elif ins.text != correct_btn:
        _gui_lbl.color = [0.99, 0, 0, 1] 

def update_label(_lbl):   
    global gen_question    
    gen_question = random.choice(list(bangladict.keys()))
    _lbl.text = gen_question


def update_buttons(_btns):
    for wrong_btns in _btns[:-1]:
        wrong_btns.text = random.choice(list(bangladict.values()))


if __name__ == '__main__':
    update_buttons(mult_choice)
