import Tkinter
import tkMessageBox
from Tkinter import *
import calendar

top = Tkinter.Tk()


# Code to add widgets will go here...

def helloCallBack():
    myLen = int(me.get())
    s = calendar.month_name[myLen]
    st = s[:3]
    tkMessageBox.showinfo("Hello Python", "Selected Month:" + st)


me = Entry(top)
me.pack()

B = Tkinter.Button(top, text="Submit", command=helloCallBack)
B.pack()

top.mainloop()
