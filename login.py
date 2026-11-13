from tkinter import *
from tkinter import ttk

root = Tk()
root.title(":)")
root.configure(background="white", padx=10, pady=10)

aaa = ttk.Frame(root, width=100, height=100)
aaa.place(x=10, y=10)
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=0)
ola_mundo = ttk.Label(aaa, text="Olá Mundo")
ola_mundo.place(x=10, y=10)

root.mainloop()