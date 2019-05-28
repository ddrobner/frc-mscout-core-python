from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from decoder import decoder

class Window(Frame):

    # Tkinter Boilerplate
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.decode = decoder()
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("MScout Core")
        self.pack(fill=BOTH, expand=1)

        singleButton = Button(self, text="Single Code", command=self.decode.single)
        singleButton.place(relx=0.5, rely=0.4, anchor=CENTER)

        multiButton = Button(self, text="QR Stream", command= lambda: messagebox.showinfo("Placeholder", "Placeholder"))
        multiButton.place(relx=0.5, rely=0.6, anchor=CENTER)

# Tkinter Boilerplate
root = Tk()
prog = Window(root)
root.geometry("400x300")
root.style = Style()
root.style.theme_use("clam")
root.mainloop()

