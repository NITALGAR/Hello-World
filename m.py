from tkinter import *
from fractions import Fraction as Fra
from math import sqrt as sr

def second_degree():
    a = Fra(coe_a.get())
    if a == 0:
        result["text"] = 'The equation has no solution in ℝ.'
        result["state"] = "active"
        solution["state"] = "disabled"
        solution["text"] = ""
    else:
        b = Fra(coe_b.get())
        c = Fra(coe_c.get())
        d = pow(b, 2) - 4 * a * c
        if d < 0:
            result["text"] ='The equation has no solution in ℝ.'
            result["state"] = "active"
            solution["state"] = "disabled"
            solution["text"] = ""
        elif d == 0:
            result["text"] ='The equation has one solution:'
            s = Fra(-b / (2*a))
            solution["text"] = " x = {0}".format(s)
            solution["state"] = "active"
        elif d > 0:
            result["text"]='So,The equation has two solutions:'
            result["state"] = "active"
            s1 =Fra((-b - sr(d)) /( 2 * a))
            s2 = Fra((-b + sr(d)) / (2 * a))
            solution["text"] = "x = {0} , x'= {1}".format(s1,s2)
            solution["state"] = "active"




win = Tk()
win.geometry("600x600")
win.title("Equation solver")
icon = PhotoImage(file="math.png")
win.iconphoto(True,icon)

message_a = Label(win,
                  text="Enter the coefficient a:",
                  font=("Victor Mono",25,'bold'))
message_a.place(x= 10,y=125)

coe_a = Entry(win,
          font=("Arial",25),
          width=5)
coe_a.place(x= 450,y=129)

message_b = Label(win,
                  text="Enter the coefficient b:",
                  font=("Victor Mono",25,'bold'))
message_b.place(x= 10,y=200)

coe_b = Entry(win,
          font=("Arial",25),
          width=5)
coe_b.place(x= 450,y=204)

message_c = Label(win,
                  text="Enter the coefficient c:",
                  font=("Victor Mono",25,'bold'))
message_c.place(x= 10,y=270)

coe_c = Entry(win,
          font=("Arial",25),
          width=5)
coe_c.place(x= 450,y=274)

calc = Button(win,
              text="Solve equation",
              font=("Victor Mono",16),
              command=second_degree)
calc.place(x=200,y=360)

result = Label(win,
               state="disabled",
               font=("Victor Mono",20,'bold'))
result.place(x=20,y=420)

solution = Label(win,
                 state="disabled",
                 font=("Victor Mono",20,'bold'))
solution.place(relx=0.3,y=460)

win.mainloop()