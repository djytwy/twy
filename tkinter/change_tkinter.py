from Tkinter import *

root = Tk()

label = Label(root, text='hello world')
label.config(cursor='gumby')
label.config(width='80', height='10', fg='red', bg='blue')
label.config(font=('times', 28, 'bold'))
label.pack()
label.mainloop()
