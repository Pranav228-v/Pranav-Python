from tkinter import *
from datetime import date

#create window
window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

def display(): #function to display a message
    name = name_entry.get()

    #declaring a global variable
    #to make it accessible anywhere in the program
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"

    #display details in a text box
    #specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#create widgets
label = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)

name_label = Label(text="Enter your full name below", bg="blue", fg="white")
name_entry = Entry() #text input

text_box = Text(height=3)

btn = Button(text="Display message", command=display, height=1, bg="red", fg="white")


#attaching all the widgets in the window
label.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()