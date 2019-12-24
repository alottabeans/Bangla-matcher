import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.properties import NumericProperty
from kivy.config import Config

#disable window resizing
Config.set('graphics', 'resizable', False)

from banglogic import *


def bangla_app():      
    root = StackLayout(orientation='lr-bt')
    
    question = Label(text=gen_question, 
            font_name='fonts/Hind_Siliguri/HindSiliguri-Medium.ttf', font_size='50sp') 
    
    btn1 = Button(text=mult_choice_btn[0], size_hint=(1, .1)) 
    btn1.bind(on_press=callback)

    btn2 = Button(text=mult_choice_btn[1], size_hint=(1, .1)) 
    btn2.bind(on_press=callback)

    btn3 = Button(text=mult_choice_btn[2], size_hint=(1, .1))
    btn3.bind(on_press=callback)

    btn4 = Button(text=mult_choice_btn[3], size_hint=(1, .1))  
    btn4.bind(on_press=callback)
     
    #add buttons 
    root.add_widget(btn1)
    root.add_widget(btn2) 
    root.add_widget(btn3)
    root.add_widget(btn4)
    
    # add question label
    root.add_widget(question) 

    return root


class Banglapp(App):

    def build(self):
        return bangla_app()


def callback(instance):
    check_if_correct(instance) 


if __name__ == '__main__':
    Banglapp().run()
