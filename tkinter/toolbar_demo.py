from tkinter import *

root = Tk()

def callback():
    print('callback')

toolbar = Frame(root)
b = Button(toolbar, text='new', width=6, command=callback)
b.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP, fill=X)
root.mainloop()