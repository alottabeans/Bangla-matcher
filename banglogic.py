import random
import json

with open('bangladata.json') as f:
    data = json.load(f)

bw = data['bangla_words'] #bangla words
tw = data['translations'] #translated words

#convert lists to dict
banglalist = dict(zip(bw, tw))

gen_question = random.choice(list(banglalist.keys()))

#random answers
wrong_btn1 = random.choice(list(banglalist.values()))
wrong_btn2 = random.choice(list(banglalist.values()))
wrong_btn3 = random.choice(list(banglalist.values()))
correct_btn = banglalist[gen_question]

mult_choice = [wrong_btn1, wrong_btn2, wrong_btn3, correct_btn]

#shuffle buttons 
shuffle_choices = random.shuffle(mult_choice)

def check_if_correct(ins, ques): 
     
    if ins.text == correct_btn:
        ques.color=[0, 0.99, 0, 1]

    elif ins.text != correct_btn:
        ques.color=[0.99, 0, 0, 1]
