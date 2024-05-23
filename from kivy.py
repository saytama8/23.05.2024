from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
class ScrButoon(Button):
    def __init__(self,screen, direction = "right", goal = "main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        v1 = BoxLayout(orientation = "vertical", padding = 8 , spacing = 8)
        h1 = BoxLayout()
        txt = Label(text="Вибери екран")
        but1 = ScrButoon(self, direction="right", goal = "first"  , text="1")
        but2 = ScrButoon(self, direction="left", goal = "second"  , text="2")
        but3 = ScrButoon(self, direction="up", goal = "third"  , text="3")
        but4 = ScrButoon(self, direction="down", goal = "fourth"  , text="4")
        v1.add_widget(but1)
        v1.add_widget(but2)
        v1.add_widget(but3)
        v1.add_widget(but4)
        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)



class FirstScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        v1 = BoxLayout(orientation = "vertical",size_hint=(.5,.5), pos_hint = {"center_x":0.5, "center_y":0.5})

        but = Button(text="Текст",size_hint = (.5,1), pos_hint = {"left":0})
        but_back = ScrButoon(self, direction="up",goal="main",text="назад",size_hint=(.5,1), pos_hint = {"right":1})

        v1.add_widget(but)
        v1.add_widget(but_back)
        self.add_widget(v1)



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name="main"))
        sm.add_widget(FirstScr(name="first"))

        return sm
    
MyApp().run()


