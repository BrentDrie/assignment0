from asyncore import read
from tkinter import *
from datetime import *

root = Tk()

file = open('C:\python text files\events.txt', 'r')

events = file.readlines()

modified_events= []
splitted_events= []
splitted_dates1= []
splitted_dates2= []
splitted_dates3= []


for line in events:
    modified_events.append(line.strip('\n'))  #removes all \n characters
    

for line in modified_events:
    splitted_events.append(line.split(","))

for line in splitted_events[0]:
    splitted_dates1.append(line.split(", "))
    
    


for line in splitted_events[1]:
    splitted_dates2.append(line.split(", "))

for line in splitted_events[2]:
    splitted_dates3.append(line.split(", "))






   

print(events)
print(modified_events)
print(splitted_events)
print(splitted_dates1[1])
print(splitted_dates2[1])
print(splitted_dates3[1])




        





