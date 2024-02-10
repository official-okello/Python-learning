from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfile(title='Select File', filetypes=(('text files', '*.txt'), ('all files', '*.*')))
    with open (filepath,'r') as file:
        file.read()
 
window = Tk()

button = Button(window, text='Open file', command=openFile)
button.pack()

window.mainloop()