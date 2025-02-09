from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class LoginScreen(GridLayout):  # GirdLayot is used as base class from root widget Login Screen
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "Password"))
        self.password = TextInput(password = True,multiline = False)
        self.add_widget(self.password)
        
class Space_Invaders(App):  #defining name of the app  
    def build(self): # returning the root widget 
        return LoginScreen()
    
if __name__ == "__main__":
    Space_Invaders().run()