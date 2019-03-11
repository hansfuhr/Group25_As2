import random
from tkinter import *
from PIL import ImageTk, Image
import tkinter.scrolledtext as tkscroll
import time

root = Tk()
root.title("Autobot Test")
background = ImageTk.PhotoImage(Image.open("auto.jpg"))
root.configure(background="red")
Label(root, image=background, bg="black") .grid(row=0,column=0,rowspan=3, columnspan=3, sticky=W)

textentry = Entry(root, width=75,bg="white")
textentry.grid(row=2,column=1,sticky=S+E)


output = tkscroll.ScrolledText(root, width = 75, height=30, wrap=WORD, background="white")
output.grid(rowspan=2,columnspan=2,row=1,column=1,sticky=N)

output.insert("end-1c","Welcome to autobot pussy")

def autobot(event = None):
    enteredtext = textentry.get()
    output.insert("end-1c",enteredtext)
    textentry.delete(0,"end")
textentry.bind("<Return>", autobot())
root.mainloop()
