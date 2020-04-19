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

    correct_ans = get_key(bangladict, gen_question)
    
    _btn1 = random.choice(list(bangladict.keys())) 
    _btn2 = random.choice(list(bangladict.keys())) 
    _btn3 = random.choice(list(bangladict.keys()))  
    _btn4 = correct_ans
    
    mult_choice = [_btn1, _btn2, _btn3, _btn4]  
    
    random.shuffle(mult_choice)

    def check_if_correct(self, instance, lbl, btn_list):         
        if instance.text == self.correct_ans:
            lbl.color = [0, 0.99, 0, 1] 
            self.update_label(lbl) 
            self.update_buttons(btn_list)

        elif instance.text != self.correct_ans:
            lbl.color = [0.99, 0, 0, 1]

    def update_label(self, gui_lbl): 
        self.gen_question = random.choice(list(bangladict.values())) 
        gui_lbl.text = self.gen_question 


    def update_buttons(self, _gui_btns):
        self.correct_ans = get_key(bangladict, self.gen_question) 
        for button in _gui_btns:
            button.text = random.choice(list(bangladict.keys()))
            if button == _gui_btns[3]:
                button.text = self.correct_ans
        random.shuffle(_gui_btns)
