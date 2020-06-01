import kivy

kivy.require('1.11.1')

from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '680')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from banglogic import BangLogic


class LangGame:
  bl = BangLogic()  
   
  def lang_game(self): 
      self.root = StackLayout(orientation='rl-bt')
       
      self.ques_lbl = Label(text=self.bl.gen_question, 
              font_name='fonts/Hind_Siliguri/HindSiliguri-Regular.ttf', 
              font_size='50sp'
              )   
      
      self.btn1 = Button(text=self.bl.mult_choice[0], size_hint=(1, .1)) 
      self.btn2 = Button(text=self.bl.mult_choice[1], size_hint=(1, .1)) 
      self.btn3 = Button(text=self.bl.mult_choice[2], size_hint=(1, .1))
      self.btn4 = Button(text=self.bl.mult_choice[3], size_hint=(1, .1))  
      
      self.btn1.bind(on_press=self.callback)
      self.btn2.bind(on_press=self.callback) 
      self.btn3.bind(on_press=self.callback) 
      self.btn4.bind(on_press=self.callback)
      
      ''' 
      self.redx1 = Image(source="images/greyx.png", size_hint=(None, 0.05))  
      self.redx2 = Image(source="images/greyx.png", size_hint=(None, 0.05))
      self.redx3 = Image(source="images/greyx.png", size_hint=(None, 0.05))
      '''
      self.root.add_widget(self.btn1)
      self.root.add_widget(self.btn2) 
      self.root.add_widget(self.btn3)
      self.root.add_widget(self.btn4)
      
      ''' 
      self.root.add_widget(self.redx1)
      self.root.add_widget(self.redx2)
      self.root.add_widget(self.redx3)
      ''' 
      self.root.add_widget(self.ques_lbl)

      self.btn_list = [self.btn1, self.btn2, self.btn3, self.btn4] 
      
      return self.root 

  def callback(self, instance):
      self.bl.check_if_correct(instance, self.ques_lbl, self.btn_list) 


class Langapp(App):   
  
  def build(self):
    lg = LangGame() 
    return lg.lang_game()

   
if __name__ == '__main__':
    Langapp().run()


