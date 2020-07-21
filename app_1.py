from tkinter import *

root = Tk()
root.title("Simple Calculator")

my_entry = Entry(root, width=50)
my_entry.pack()

def my_click():
    hello = "Hello" + my_entry.get()
    my_label = Label(root, text=hello)
    my_label.pack()

my_button = Button(root, text="Enter Your Stock Quote", command-my_click)
my_button.pack()

root.mainloop()