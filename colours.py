from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Colours!")
root.geometry("1920x1080")

def color():
    my_colour = colorchooser.askcolor()[1]
    colour_label = Label(root, text=my_colour).pack(pady=10)
    colour_label2 = Label(root, text="You picked a colour", bg=my_colour).pack(pady=10)

colour_button = Button(root, text="Pick a Colour", command=color).pack()

root.mainloop()