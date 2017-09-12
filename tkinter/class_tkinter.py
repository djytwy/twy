#from tkinter import *
import tkinter as tk
class APP():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.button1 = tk.Button(frame, text='exit', fg='blue', command=frame.quit)
        self.button1.pack()

        self.button2 = tk.Button(frame, text='hello tk', fg='red', command=self.print)
        self.button2.pack()

    def print(self):
        print('hello tk')

root = tk.Tk()
app = APP(root)
root.mainloop()
