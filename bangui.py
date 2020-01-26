import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.properties import NumericProperty
from kivy.config import Config

Config.set('graphics', 'resizable', False)

from banglogic import *


class BanglaGame:

    def bangla_game(self):
        root = StackLayout(orientation='lr-bt')
        
        self.question = Label(text=gen_question, 
                font_name='fonts/Hind_Siliguri/HindSiliguri-Medium.ttf', font_size='50sp') 

        self.btn1 = Button(text=mult_choice[0], size_hint=(1, .1)) 
        self.btn1.bind(on_press=self.callback)

        self.btn2 = Button(text=mult_choice[1], size_hint=(1, .1)) 
        self.btn2.bind(on_press=self.callback)

        self.btn3 = Button(text=mult_choice[2], size_hint=(1, .1))
        self.btn3.bind(on_press=self.callback)

        self.btn4 = Button(text=mult_choice[3], size_hint=(1, .1))  
        self.btn4.bind(on_press=self.callback)
        
        root.add_widget(self.btn1)
        root.add_widget(self.btn2) 
        root.add_widget(self.btn3)
        root.add_widget(self.btn4)
        
        self.btn_list = [self.btn1, self.btn2, self.btn3, self.btn4]

        root.add_widget(self.question) 
        
        return root 
 
    def callback(self, instance):
        check_if_correct(instance, self.question, self.btn_list) 

class Banglapp(App):
    
    def build(self):
        bg = BanglaGame() 
        return bg.bangla_game()


if __name__ == '__main__':
    Banglapp().run()
