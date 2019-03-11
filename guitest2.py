import tkinter as tk
import random
from PIL import ImageTk, Image

root = tk.Tk()
import tkinter.scrolledtext as tkscroll
entry_label = tk.Label(root, text = "Guess a number between 1 and 5: ")
entry_label.grid(row = 0, column = 0)
root.title("Autobot Test")
background = ImageTk.PhotoImage(Image.open("auto.jpg"))
root.configure(background="red")
tk.Label(root, image=background, bg="black") .grid(row=0,column=0,rowspan=3, columnspan=3)

entry_label = tk.Label(root, text = "User input:  ",bg="red",fg="white")

entry_label.grid(row = 2, column = 1, sticky = "w")

#Entry field for user guesses.
user_entry = tk.Entry(root, width=75,bg="white")
user_entry.grid(row = 2, column = 1)

text_box = tkscroll.ScrolledText(root, width = 75, height = 30)
text_box.grid(row = 1, column = 0, columnspan = 2)

text_box.insert("end-1c", "Autobot: Welcome!")



def guess_number(event = None):
    #Get the string of the user_entry widget
    guess = user_entry.get()



    text_box.insert("end-1c", "\n"+guess)

    user_entry.delete(0, "end")
# binds the enter widget to the guess_number function
# while the focus/cursor is on the user_entry widget
user_entry.bind("<Return>", guess_number)
root.mainloop()