from tkinter import *

def openFile():
    print('File opened')
def saveFile():
    print('File saved')
 
window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=menubar)

fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

window.mainloop()