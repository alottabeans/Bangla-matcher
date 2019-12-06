import random
import json

with open('bangladata.json') as f:
    data = json.load(f)

bd = data['bangla_words']
td = data['translations']


banglalist = dict(zip(bd, td)) 

gen_question = random.choice(list(banglalist.keys()))

#check if button pressed was the correct answer
def check_if_correct():
    pass 

print(gen_question)
