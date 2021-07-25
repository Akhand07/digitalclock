from tkinter import *
from tkinter.ttk import *

from time import strftime

# now creating a UI for our clock

root = Tk()

# title for clock
root.title("Digital Clock")

# now defining a funtion to get our time

def time():
    # now taking string for storing our time
    string = strftime('%H:%M:%S %p')

    # now setting time to this label
    label.config(text=string)
    label.after(1000, time)


# now creating label to store our clock

label = Label(root, font=("ds-digital", 100), background="black", foreground="red")

# now packing our label

label.pack(anchor="center")

# outside the funion, now calling our function

time()
mainloop()

