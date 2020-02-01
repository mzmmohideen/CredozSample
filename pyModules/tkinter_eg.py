# pip install python-tk
from tkinter import Tk, Label, Button, Entry
# from tkinter import *

class MyFirstGUI:
    counter = 0
    def __init__(self, master):
        self.master = master
        self.master.title("A simple GUI")

        self.label = Label(self.master, text="Hello World!")        
        self.label.pack()

        self.greet_button = Button(self.master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

    def greet(self):
        self.counter += 1
        print("Button click %s times!"%(self.counter))
        # self.label.__setitem__("text", "Greetings!")

# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

def tkinterForm(master):
    master.title("Sample Label")    
    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

# mainloop( )

e = None
def printtext():
    # global e
    string = e.get() 
    # print dir(l)
    l.__setitem__("text", "Welcome %s" %string.upper())
    # print string.upper()

# from Tkinter import *
def tkinterBox(root):
    global e
    global l
    root.title('Name')

    e = Entry(root)
    l = Label(root, text="Something will override")
    e.pack()
    l.pack()
    # print help(e.pack)
    e.focus_set() #default mouse click on text box

    b = Button(root,text='okay',command=printtext)
    b.pack(side='bottom')
    # root.mainloop()
# tkinterBox()

import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="bisque")
        self.canvas = tk.Canvas(self, width=400, height=400)

        board = TicTacToe(self)
        board.pack(padx=20, pady=20)

class TicTacToe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background='black')

        self.player = "X"
        self.cell = {}
        for row in range(3):
            for col in range(3):
                cell = tk.Label(self, background="darkgray", foreground="white", width=2)
                cell.bind("<1>", lambda event, col=col, row=row: self.on_click(row, col))
                cell.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
                self.cell[(row,col)] = cell

    def on_click(self, row, col):
        current = self.cell[(row, col)].cget("text")
        if current == "X" or current == "O":
            self.bell()
            return
        self.cell[(row, col)].configure(text=self.player)
        self.player = "X" if self.player == "O" else "O"

if __name__ == "__main__":
    root = Tk()
    # pass
    #1 
    # my_gui = MyFirstGUI(root)
    # root.mainloop()

    #2
    # tkinterForm(root)
    # root.mainloop()

    #3
    tkinterBox(root)
    root.mainloop()

    #4
    # Example(root).pack(fill="both", expand=True)
    # root.mainloop()

    # root = tk.Tk()
    # Example(root).pack(fill="both", expand=True)
    # root.mainloop()