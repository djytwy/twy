from tkinter import *

root = Tk()

status = Label(root, text='这是一个status', bd=1, relief=SUNKEN, anchor='w')
status.pack(side=BOTTOM, fill=X)

root.mainloop()