import tkinter as tk
root = tk.Tk()
temp = tk.StringVar()
temp.set('1123')
entry = tk.Entry(root, text = temp).pack()
print()
root.mainloop()
