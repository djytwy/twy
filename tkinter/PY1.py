from collections import Counter
import tkinter as tk

lis1t = [123,3,4]
lis2t = []
dic = {0:2,2:3,3:4,5:2,6:1}
dic2 = {'w':1,'a':2,'e':4 }
dic3 = {1:0,2:3,3:1,4:0}
find = 1
find2='e'
re=0
new={}
print(dic)
dic.pop(2)
print(dic)


from tkinter import *

def prin():
    print(a)

master = Tk()
#c = Button(master, text="red", fg="red").pack()
Label(master, text="First").grid(row=0, sticky = W)
Label(master, text="Second").grid(row=1, sticky = W)
a = IntVar()
b = IntVar()
e1 = Entry(master, textvariable=a)
e2 = Entry(master, textvariable=b)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
button = Button(master,text = "button",command = prin)
button.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5, sticky = W + E + N + S)
mainloop()
# # a='aas'
# root = tk.Tk()
# renshu = tk.getint()
# enter_renshu = tk.Entry(root, textvariable=renshu).pack()
# a = renshu
# print(type(a))
# root.mainloop()
# T = tk.Text(root, height=15, width=30)
# T.insert(tk.END, 'aaaa')    #必须为浮点数
# T.pack()
# tk.mainloop()

# root = tk.Tk()
# T = tk.Text(root, height=10, width=30).pack()
# tk.Text.insert(END,"Just a text Widget\nin two lines\n")
# tk.mainloop()
# root.title("Entry Test")
# v1 = tk.StringVar()
# v2 = tk.StringVar()
# v3 = tk.StringVar()

# tk.Entry(root, width=30,textvariable=v1, stat="readonly").pack()
# v1.set("readonly")

# tk.Entry(root, width=30,textvariable=v2).pack()
# v2.set("normal")

# entry = tk.Entry(root, width=30,textvariable=v3)
# v3.set("password")
# entry.pack()
# entry["show"] = "*"
# root.mainloop()
# def printentry():
#     print (var.get())
# root=tk.Tk()
# var = tk.StringVar()
# tk.Entry(root, textvariable=var).pack()
# tk.Button(root, text="print entry",command=printentry).pack()
# tk.mainloop()
#if find2 in dic2:
#    del dic2[find2]
#print(dic2)
#print(dic3.keys())
#print(type(dic3.keys()))
#for i, v in enumerate(dic):
#    print(i)
#for i, v in enumerate(lis1t):
#    if v==find:
#        print(i)
#j=Counter(lis1t)
#for i in dic2:
    #re+=1
    #a=input('skdjal')
 #   find=input('wae')
  #  if find in dic2:
   #     print('zai')
    #print(re)
#lis1t.sort()
       # re=re-len(lis1t)
#print(lis1t)

