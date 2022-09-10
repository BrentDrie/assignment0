from tkinter import *

root = Tk()

e = Entry(root, width=30, borderwidth=3)
e.pack()
e.insert(0, "selecteer kat")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton=Button(root, text="enter", padx=50, pady=50, command=myClick, fg="green", bg="black")
myButton.pack()





root.mainloop()