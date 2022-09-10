from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Mooo")
    myLabel.pack()

myButton=Button(root, text="kat", padx=50, pady=50, command=myClick, fg="green", bg="black")
myButton.pack()





root.mainloop()