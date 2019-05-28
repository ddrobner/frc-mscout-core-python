from tkinter import *
from decoder import decoder

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.decode = decoder()
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("MScout Core")

        self.pack(fill=BOTH, expand=1)

        singleButton = Button(self, text="Single Code", command=self.decode.single)
        singleButton.place(x=150, y=0)

root = Tk()
prog = Window(root)
root.geometry("400x300")
root.mainloop()

