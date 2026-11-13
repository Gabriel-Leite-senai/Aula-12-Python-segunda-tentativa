from tkinter import *
from tkinter import ttk

root = Tk()
root.title(":)")
root.configure(background="white")

aaa = ttk.Frame(root)
aaa.grid(row=0, column=0)
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=0)

root.mainloop()