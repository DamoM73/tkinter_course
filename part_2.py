from tkinter import *

root = Tk()

# creating a Label Widget
my_label_1 = Label(root, text="Hello World")
my_label_2 = Label(root, text="My name is Damien Murtagh")

my_label_1.grid(row=0,column=0)
my_label_2.grid(row=0,column=2)

root.mainloop()