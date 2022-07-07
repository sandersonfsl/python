import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MygGridLayout(GridLayout) :
    def __init__(self, **kwargs) :
        super(MygGridLayout, self).__init__(**kwargs)

        self.cols = 2

    
        self.add_widget(Label(text="Name :"))
        self.name = TextInput(multiline = True)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza :"))
        self.pizza = TextInput(multiline = False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color :"))
        self.color = TextInput(multiline = False)
        self.add_widget(self.color)

        self.submit = Button(text="Submit", font_size = 32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance) :
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color} ! '))

        
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App) :
    def build(self) :
        return MygGridLayout()

if __name__ == '__main__' :
    MyApp().run()

''' PYTHON CODE

 import random as rd
print(' ----- MEGASENA : BIGGEST BRAZILIAN LOTTERY  ----- ')

## Making the user choice
userlist = []
print(' Pick  SIX numbers between 1 and 60 ')

for c in range (0,6) :
    n = int(input(f' Pick the {c + 1} number  : '))
    userlist.insert(c, n)

## Showing the user choice
print('The list of your Numbers : ', userlist)

## System choice 
list = list(range(1,61))
pick = rd.sample(list, k=6)
print(f'Numbers Drawn : {pick} ')

## Counting...
d = 0

for j in range(0, 6) :
    if pick[j] in userlist :
        d += 1


print(f'You got {d} number(s) right ')'''