import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from bangla import gen_question


def callback(instance):
    print('button <%s> was chosen' % (instance))
    
    
def bangla_game():
    root = StackLayout(orientation='lr-bt')
    question = Label(text=gen_question, font_name='Kalpurush.ttf', font_size='50sp') 
    
    btn1 = Button(text='1', size_hint=(1, .1)) 
    btn1.bind(on_press=callback)

    btn2 = Button(text='2', size_hint=(1, .1)) 
    btn2.bind(on_press=callback)

    btn3 = Button(text='3', size_hint=(1, .1))
    btn3.bind(on_press=callback)

    btn4 = Button(text='4', size_hint=(1, .1))  
    btn4.bind(on_press=callback)
    
   
    #add buttons to gui
    root.add_widget(btn1)
    root.add_widget(btn2) 
    root.add_widget(btn3)
    root.add_widget(btn4)
    
    #add question to gui
    root.add_widget(question)
    
    return root
    
class Banglapp(App):

    def build(self):
        return bangla_game()


if __name__ == '__main__':
    Banglapp().run()

