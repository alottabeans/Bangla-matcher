import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class Menu:
  def main_menu(self):
    self.root = StackLayout(orientation='rl-bt')
    self.menubtn = Button(text='Select Language', size_hint=(1, .5))
    self.gamebtn = Button(text='Play', size_hint=(1, .5))
    
    self.menubtn.bind(on_press=self.callback)
    self.gamebtn.bind(on_press=self.callback)
    
    self.root.add_widget(self.menubtn)
    self.root.add_widget(self.gamebtn) 
    
    return self.root


  def callback(self, instance):       
    from subprocess import Popen, PIPE
    if instance == self.menubtn:
      process = Popen(['python3', 'selectlang.py'], stdout=PIPE, stderr=PIPE)
    
    elif instance == self.gamebtn:      
      process = Popen(['python3', 'bangui.py'], stdout=PIPE, stderr=PIPE)

class MenuApp(App):
  def build(self):
    mm = Menu() 
    return mm.main_menu()


if __name__ == "__main__":
  MenuApp().run()
