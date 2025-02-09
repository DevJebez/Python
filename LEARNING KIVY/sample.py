import kivy
from kivy.app import App    
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Grids(GridLayout):
    def __init__(self,**kwargs):
        super(Grids,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="NAME "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
        self.add_widget(Label(text = "EMAIL"))

class myApp(App):
    def build(self):
        return Label(text="Hello World",font_size = "40")
if __name__ == "__main__":
    myApp().run()   