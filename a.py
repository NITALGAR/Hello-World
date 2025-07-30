from tkinter import *

nums = []

def submit():
    global nums
    if num.get().isdigit() and int(num.get()) not in nums :
        nums.append(int(num.get()))
    num.delete(0, END)


def show():
    text.config(text=";".join(map(str, nums)))
    pass

def sort():
    nums.sort()

def clear():
    nums.clear()



window = Tk()
window.title("Maths")
window.config(bg="#36454f")
icon = PhotoImage(file="math.png")
window.iconphoto(True,icon)
text = Label(window,text="YOKOSO Saka sama no sekai",
             font=("Arial",50),
             fg="#f0ffff",
             bg="#36454f")

num = Entry(window,
            font=("Arial",30),
            fg="#f0ffff",
            bg="#36454f", )

submit_but = Button(window,text="submit",
                    command=submit,
                    font=("Victor Mono",15))

show_but = Button(window,text="show",
                  command=show,
                  font=("Victor Mono",15))

sort_but = Button(window,text="sort",
                  command=sort,
                  font=("Victor Mono",15))

clear_but = Button(window,text="clear",
                  command=clear,
                  font=("Victor Mono",15))

quit_but = Button(window,text="quit",
                  command=window.destroy,
                  font=("Victor Mono",15))

text.pack()
num.pack()
submit_but.pack()
show_but.pack()
sort_but.pack()
clear_but.pack()
quit_but.pack()
window.mainloop()












