from tkinter import *
from tkinter import filedialog

def saveFile():
    textfile = str(text.get(1.0, END))
    filepath = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[
        ('Text file', '.txt'),
        ('HTML file', '.html'),
        ('All files', '.*'),
    ])
    if filepath is None:
        return
    
    filepath.write(textfile)
    filepath.close()
 
window = Tk()

button = Button(window, text='Save', command=saveFile)
button.pack()

text = Text()
text.pack()

window.mainloop()