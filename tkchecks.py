from tkinter import *

def display():
    if x.get() == 1:
        print('You agree')
    else:
        print("You don't agree")

window = Tk()

window.geometry('420x420')
window.config(bg='blue')

x = IntVar()
check = Checkbutton(window,
                    text='I agree',
                    variable=x,
                    onvalue=1,
                    offvalue=0,
                    command=display)
check.pack()

window.mainloop()