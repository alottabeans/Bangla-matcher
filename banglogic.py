import random
import json

with open('bangladata.json') as f:
    data = json.load(f)

bw = data['bangla_words'] #bangla words

tw = data['translations'] #translated words

banglalist = dict(zip(bw, tw))

gen_question = random.choice(list(banglalist.keys()))

#random buttons
gen_btn1 = random.choice(list(banglalist.values()))
gen_btn2 = random.choice(list(banglalist.values()))
gen_btn3 = random.choice(list(banglalist.values()))
gen_btn4 = banglalist[gen_question]

mult_choice_btn = [gen_btn1, gen_btn2, gen_btn3, gen_btn4]

shuffle_btn = random.shuffle(mult_choice_btn)

def check_if_correct(ins):
    if ins.text == gen_btn4:
        print("correct!")
    else:
        print("wrong") 
