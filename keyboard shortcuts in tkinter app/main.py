import sys
import tkinter as tk
from tkinter.messagebox import showinfo


class MyApplication:

    def __init__(self):
        self.root = tk.Tk()

        self.entry = tk.Entry()
        self.entry.pack()
        self.entry.bind("<Return>", lambda event: showinfo('Message', self.entry.get()))

        self.entry2 = tk.Entry()
        self.entry2.pack()

        self.button = tk.Button(text='Show', command=lambda: showinfo('Message', self.entry.get()))
        self.button.pack()

        self.root.bind("<Control-m>", lambda event: showinfo('Message', "You pressed CTRL+m"))
        self.root.bind("<Control-x>", lambda event: sys.exit())

        self.root.mainloop()


if __name__ == '__main__':
    MyApplication()
