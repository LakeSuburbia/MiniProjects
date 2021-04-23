import os
from tkinter import *
import time

global timer_end
global timer_begin


def starttimer():
    global timer_begin
    timer_begin = time.perf_counter()

def stoptimer():
    global timer_end
    timer_end = time.perf_counter()

#def gettime():
    #return timer_end - timer_begin
    

root = Tk()
root.title("Daan's supercoole writetracker")
root.geometry("400x600")

myButton = Button(root, text="start", command=starttimer())
myButton.pack()
myButton = Button(root, text="stop", command=starttimer())
myButton.pack()
#myLabel = Label(root, text=gettime())
#myLabel.pack()
myButton = Button(root, text="start again", command=starttimer())
myButton.pack()

root.mainloop() 
