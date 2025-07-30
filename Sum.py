from tkinter import *

divisor = []
is_prime = None
is_even = None

def sum1():
    global divisor
    global is_prime
    global is_even

    divisor.clear()

    num_a = a.get()
    num_b = b.get()
    res = int(num_a) + int(num_b)
    result.config(text="The sum of a and b is: {0}".format(res))

    for i in range(1,res+1):
        if res % i == 0:
            divisor.append(i)
    divisors['text'] = f"The divisors of {res} are: {"; ".join(map(str,divisor))}."

    is_prime = True if len(divisor) == 2 else False
    info_1["text"] = f"{res} is prime" if is_prime else f"{res} isn't prime"
    is_even = True if 2 in divisor else False
    info_2["text"] = f"{res} is even" if is_even else f"{res} is odd"
win = Tk()
win.title("BIG BOSS")
icon = PhotoImage(file="math.png")
win.iconphoto(True,icon)

message_a = Label(win,
                  text="Enter the number a:",
                  font=("Victor Mono",25,'bold'))

a = Entry(win,
          font=("Arial",25))

message_b = Label(win,
                  text="Enter the number b:",
                  font=("Victor Mono",25,'bold'))
b = Entry(win,
          font=("Arial",25))

cal = Button(win,
             text="Calculate Sum",
             font=("Victor Mono",25,'bold'),
             command=sum1)

result = Label(win,
               font=("Victor Mono",25,'bold'),
               text="The sum of a and b is:")

divisors = Label(win,
               font=("Victor Mono",25,'bold'))

info_1 = Label(win,
               font=("Victor Mono",25,'bold'))

info_2 = Label(win,
               font=("Victor Mono",25,'bold'))


message_a.grid(row=0,column=0)
a.grid(row=0,column=1)
message_b.grid(row=1,column=0)
b.grid(row=1,column=1)
cal.grid(row= 3,column=1,pady=25)
result.grid(row=4, pady=5, padx=9)
info_1.grid(row=6, pady=5, padx=9)
info_2.grid(row=7, pady=5, padx=9)
divisors.grid(row=5, pady=5, padx=9)
win.mainloop()











