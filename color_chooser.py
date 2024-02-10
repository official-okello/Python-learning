from tkinter import *
from tkinter import colorchooser

def change_bg():
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()

window.geometry('420x420')

button = Button(window, text='choose color', command=change_bg)
button.pack()

window.mainloop()