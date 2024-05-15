import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title('Tab Application')
    root.geometry('400x200')

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    frame1 = tk.Frame(notebook, width=400, height=200)
    frame2 = tk.Frame(notebook, width=400, height=200)
    frame3 = tk.Frame(notebook, width=400, height=200)

    label1 = tk.Label(frame1, text='You are on tab 1')
    label1.pack()

    label2 = tk.Label(frame2, text='You are on tab 2')
    label2.pack()

    button1 = tk.Button(frame2, text='Button tab 2')
    button1.pack()

    label3 = tk.Label(frame3, text='label 1')
    label3.grid(row=0, column=0)

    label4 = tk.Label(frame3, text='label 2')
    label4.grid(row=0, column=1)

    entry1 = tk.Entry(frame3)
    entry1.grid(row=1, column=0)

    entry2 = tk.Entry(frame3)
    entry2.grid(row=1, column=1)

    frame3.columnconfigure(0, weight=1)
    frame3.columnconfigure(1, weight=1)

    frame3.rowconfigure(0, weight=1)
    frame3.rowconfigure(1, weight=1)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    frame3.pack(fill='both', expand=True)

    notebook.add(frame1, text='Tab 1')
    notebook.add(frame2, text='Tab 2')
    notebook.add(frame3, text='Tab 3')

    root.mainloop()


if __name__ == '__main__':
    main()
