import Tkinter
import tkMessageBox
from Tkinter import *

top = Tkinter.Tk()


# Code to add widgets will go here...

def helloCallBack():
    if len(le.get()) <= 7:
        st = fe.get()[0] + le.get()[:]
    else:
        st = fe.get()[0] + le.get()[:7]
    tkMessageBox.showinfo("Hello Python", "Your username is:" + st)


fe = Entry(top)
fe.pack()
le = Entry(top)
le.pack()

B = Tkinter.Button(top, text="Get my new username", command=helloCallBack)
B.pack()

top.mainloop()
