from tkinter import *
from fractions import Fraction as Fra


win = Tk()
win.title("Calculator")
icon = PhotoImage(file="calc.png")
win.iconphoto(True,icon)
win.geometry("500x500")


zone = Entry(win,
             font=("Arial",50),
             width=11)
zone.grid(columnspan=4)

but_1 = Button(win,
               text=1,
               font=("Cascadia Code",50))
but_1.grid(column=0,row=1)

but_2 = Button(win,
               text=2,
               font=("Cascadia Code",50))
but_2.grid(column=1,row=1)

but_3 = Button(win,
               text=3,
               font=("Cascadia Code",50))
but_3.grid(column=2 ,row=1)
but_sum = Button(win,
               text="+",
               font=("Cascadia Code",50))

but_sum.grid(column=3 ,row=1)















win.mainloop()