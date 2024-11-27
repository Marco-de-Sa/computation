# import a the module
from tkinter import *

# create root window
root = Tk()

# root window title and dimensions
root.title("welcome")
# sets the Width x Height
root.geometry('40   0x200')

# menu bar for the root window
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label
lbl = Label(root, text = "how are you :)")
lbl.grid()

# adding an entry field
txt = Entry(root, width=10)
txt.grid(column=0, row= 1)

# function to display user text when button is clicked
def clicked():
    res = "You wrote: " + txt.get()
    lbl.configure(text= res)

# button widget with red coloured text inside
btn = Button(root, text = "Click me", fg= "red", command= clicked)

# set the button grid
btn.grid(column=1, row=1)

# all widgets will be here
# execute Tkinter
root.mainloop()