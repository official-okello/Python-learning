from tkinter import *


def submit():
    value = entry.get()
    print(f'You typed: {value}')

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) -1 , END)

window = Tk()

window.geometry('420x420')
window.config(bg='blue')

entry = Entry(window, font=('Arial', 18))
entry.pack()

submit = Button(window, text='Submit', command=submit)
submit.pack()

delete = Button(window, text='Delete', command=delete)
delete.pack()

backspace = Button(window, text='Backspace', command=backspace)
backspace.pack()

window.mainloop()