from asyncio import *
from tkinter import *
from datetime import *
import re

root = Tk()

with open('events.txt', 'r') as file:       
    datastring= file.read().rstrip()              #creates string from file

datalist=re.split(',|\n', datastring)              #creates datalist from datastring



days_to1 = datetime.strptime(datalist[1], '%d/%m/%y').date() - datetime.today().date()
days_to2 = datetime.strptime(datalist[3], '%d/%m/%y').date() - datetime.today().date()
days_to3 = datetime.strptime(datalist[5], '%d/%m/%y').date() - datetime.today().date()




event1=datalist[0]
event2=datalist[2]
event3=datalist[4]

display1='It is %s until %s' % (days_to1, event1)
display2='It is %s until %s' % (days_to2, event2)
display3='It is %s until %s' % (days_to3, event3)

title=Label(root, text="Brent's countdown calender")
title.grid(row=0,column=0)

datelabel1=Label(root, text=display1)
datelabel1.grid(row=1,column=0)

datelabel2=Label(root, text=display2)
datelabel2.grid(row=2,column=0)

datelabel3=Label(root, text=display3)
datelabel3.grid(row=3,column=0)








root.mainloop()