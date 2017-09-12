from tkinter import *

def callback():
    print('callback')

def show():
    print('show')

def About():
    print('About...')

root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='callback', command=callback)
filemenu.add_separator()
filemenu.add_command(label='show', command=show)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...', command=About)

root.mainloop()
