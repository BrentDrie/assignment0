from tkinter import *
import re

editblock = Tk()
#popupblock= Tk()

inputfield = Entry(editblock, width=30, borderwidth=3)
inputfield.grid(row=1,column=0)



def Enterbutton():
    with open ('capitolFile.txt', 'a') as writecapital:
        writecapital.writelines(inputfield.get())
        writecapital.write("\n")

def compare_answer():
    with open ('capitolFile.txt', 'r') as readcapital:
        datastring= readcapital.read().rstrip()
        


    

questionlable=Label(editblock, text="enter country here:" )
questionlable.grid(row=0, column=0)

enterbutton=Button(editblock, text="enter", padx=30, pady=10, command=Enterbutton, fg="black", bg="white")
enterbutton.grid(row=2,column=0)



editblock.mainloop()