from asyncore import read
from tkinter import *
from datetime import *

root = Tk()

file = open('C:\python text files\events.txt', 'r')

events = file.readlines()

modified_events = []

days_to = []
eventsname=[]

for line in events:
   modified_events.append(line.strip('\n'))  #removes all \n characters



for line in modified_events:
   datessplit = line.split(",")
   days_to = datetime.strptime(datessplit[1], '%d/%m/%y').date() - date.today()
   event1=datessplit[0]

#datessplit=modified_events.split(",")




events=Label(root, text=days_to)
title=Label(root, text="Brent's countdown calender")


events.grid(row=1, column=0)
title.grid(row=0, column=0)

print(datessplit[1])
#print(modified_events)
#print(datessplit)

root.mainloop()




        



print(modified_events)