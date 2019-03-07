import random
from tkinter import *
from PIL import ImageTk, Image
import tkinter.scrolledtext as tkscroll
import time
responses = ["Hey","Pretty good","Ur gay"]
def click():
    entered_text = textentry.get()
    textentry.delete(0,'end')
    output.insert(END, "User: "+entered_text+"\n")
    output.insert(END, "Autobot: " + responses.pop() + "\n")


def intro():
    output.insert(END, "Autobot: " + "Welcome to autobot, we got cars yo" + "\n")
root = Tk()
root.title("Autobot Test")
background = ImageTk.PhotoImage(Image.open("auto.jpg"))
root.configure(background="red")
Label (root, image=background, bg="black") .grid(row=0,column=0,rowspan=3, columnspan=3, sticky=W)

textentry = Entry(root, width=75,bg="white")
textentry.grid(row=2,column=1,sticky=S+E)
Button(root,text="Send", width=6, command=click) .grid(row=2,column=2,sticky=S+W)

output = tkscroll.ScrolledText(root, width = 75, height=30, wrap=WORD, background="white")
output.grid(rowspan=2,columnspan=2,row=1,column=1,sticky=N)


root.mainloop()
