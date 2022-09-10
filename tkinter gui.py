from tkinter import *

root = Tk()

#creating label widget
myLabel1 = Label(root, text="dikke lul")
myLabel2 = Label(root, text="badaap")
#putting it on the screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()