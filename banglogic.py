import random
import json

with open('bangladata.json') as f:
    data = json.load(f)

bw = data['bangla_words'] 
tw = data['translations']

bangladict = dict(zip(bw, tw))


class BangLogic:
    
    def __init__(self):
        self.gen_question = random.choice(list(bangladict.keys()))
         
        self._btn1 = random.choice(list(bangladict.values())) 
        self._btn2 = random.choice(list(bangladict.values())) 
        self._btn3 = random.choice(list(bangladict.values())) 
        self.correct_btn = bangladict[self.gen_question]

        self.mult_choice = [self._btn1, self._btn2, self._btn3, self.correct_btn] 

    
    def check_if_correct(self, _instance, _lbl, _btn_list):      
        if _instance.text == self.correct_btn:
            _lbl.color = [0, 0.99, 0, 1]                    
            self.update_buttons(_btn_list)
            self.update_label(_lbl) 

        elif _instance.text != self.correct_btn:
            _lbl.color = [0.99, 0, 0, 1] 
            self.update_buttons(_btn_list)
            self.update_label(_lbl)
            print(self.correct_btn, self.gen_question)


    def update_label(self, gui_lbl):
        self.gui_lbl = gui_lbl 
        self.gui_lbl.text = self.gen_question

    def update_buttons(self, _gui_btns): 
        self._gui_btns = _gui_btns 
        for btn in _gui_btns[:-1]:
            btn = random.choice(list(bangladict.values()))
        shuffle_btns = random.shuffle(self._gui_btns) 
