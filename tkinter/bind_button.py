from tkinter import messagebox
import tkinter as tk

root= tk.Tk()

def show_xy(event):
    frame.focus_set()
    print('x_y is:', event.x, event.y)

def key_show(event):
    print('You press :', repr(event.char))

def closeWindow():
    if messagebox.askokcancel('Quit','确定退出？'):
        root.destroy()

frame = tk.Frame(root, width=200, height=200)
frame.bind('<Button-1>', show_xy)
frame.bind('<Key>', key_show)
frame.pack()

root.protocol('WM_DELETE_WINDOW', closeWindow)
root.mainloop()
