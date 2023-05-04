
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window #You must import this
Window.size = (900, 600)
Window.clearcolor = (0, 0.6, 0.1, 0.1)

class MyGridLayout(GridLayout):

    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)

        self.cols = 1

        self.row_force_default = True
        self.row_default_height = 100
        self.col_force_default = True
        self.col_default_width = 900

        self.add_widget(Label(text = "President office",font_size = 50))

        #################################################################
        self.top_grid = GridLayout(row_force_default = True,
                                   row_default_height = 40,
                                   col_force_default = True,
                                   col_default_width = 50)
        self.top_grid.cols = 2


        self.add_widget(self.top_grid)
        #################################################




class MyApp(App):

    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()