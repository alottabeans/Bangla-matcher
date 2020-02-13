import random
import json
from util import get_key

with open('bangladata.json') as f:
    data = json.load(f)

bw = data['bangla_words'] 
tw = data['translations'] 

bangladict = dict(zip(tw, bw))


class BangLogic:    
    gen_question = random.choice(list(bangladict.values())) 

    correct_btn = get_key(bangladict, gen_question)
    
    _btn1 = random.choice(list(bangladict.keys())) 
    _btn2 = random.choice(list(bangladict.keys())) 
    _btn3 = random.choice(list(bangladict.keys()))  
    _btn4 = correct_btn 
    
    mult_choice = [_btn1, _btn2, _btn3, _btn4]  
    
    random.shuffle(mult_choice)


    def check_if_correct(self, _instance, _lbl, _btn_list):         
        if _instance.text == self.correct_btn:
            _lbl.color = [0, 0.99, 0, 1] 
            self.update_label(_lbl) 
            self.update_buttons(_btn_list)

        elif _instance.text != self.correct_btn:
            _lbl.color = [0.99, 0, 0, 1] 


    def update_label(self, _gui_lbl): 
        self._gui_lbl = _gui_lbl 
        self.gen_question = random.choice(list(bangladict.values())) 
        self._gui_lbl.text = self.gen_question 


    def update_buttons(self, _gui_btns):
        self.correct_btn = get_key(bangladict, self.gen_question) 
        for button in _gui_btns:
            button.text = random.choice(list(bangladict.keys()))
            if button == _gui_btns[3]:
                button.text = self.correct_btn
        random.shuffle(_gui_btns)
