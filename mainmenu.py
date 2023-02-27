from tkinter import *
from AidenCode import basketballgame

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.image_start = PhotoImage(file = "midyear-project/assets/images/startbutton.png")
        self.create_widgets()
        
    
    def create_widgets(self):
        Label(self, text= "Click start to begin").grid(row=0, column = 0, columnspan = 5, sticky = N)


        Button(self, text = "start", command = self.basketballgame(), image = self.image_start).grid(row=1, column=0)


root = Tk()
root.title("basketballmenu")
view = Application
root.mainloop()