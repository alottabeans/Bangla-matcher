import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

class SelectLang:
  def select_lang(self):
    self.root = StackLayout(orientation='rl-bt') 
    
    self.Lbl = Label(text='Enter URL', font_size='25sp')  
    self.ti = TextInput(text=' ')

    self.root.add_widget(self.Lbl)
    self.root.add_widget(self.ti)
    
    return self.root
   

class SelectApp(App):
  def build(self):
    sl = SelectLang() 
    return sl.select_lang()


if __name__ == '__main__':
  SelectApp().run()

