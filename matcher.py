import random
import json
from util import get_key_from_val, get_val_from_key

with open('bangladata.json') as f:
    data = json.load(f)

bw = data['bangla_words'] 
tw = data['translations'] 

bangladict = dict(zip(tw, bw))


def init_choices():
    choices = []
    
    for i in range(4):
        i = random.choice(list(bangladict.keys()))
        choices.append(i)

    return choices


def init_question():
    question = random.choice(init_choices())
    ret = get_val_from_key(bangladict, question)
    print(ret)
    

if __name__ == "__main__":
    init_choices()
    init_question()
    
'''
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
        num_of_attempts = 0 
        if instance.text == self.correct_ans:
            lbl.color = [0, 0.99, 0, 1] 
            self.update_label(lbl) 
            self.update_buttons(btn_list)

        elif instance.text != self.correct_ans:
            lbl.color = [0.99, 0, 0, 1]
            num_of_attempts += 1
            self.count_attempts(num_of_attempts)

    def update_label(self, gui_lbl): 
        self.gen_question = random.choice(list(bangladict.values())) 
        gui_lbl.text = self.gen_question 


    def update_buttons(self, gui_btns):
        self.correct_ans = get_key(bangladict, self.gen_question) 
        for button in gui_btns:
            button.text = random.choice(list(bangladict.keys()))
            if button == gui_btns[3]:
                button.text = self.correct_ans
        random.shuffle(gui_btns)             
'''
