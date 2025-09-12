from tkinter import *

#setting up main window
window = Tk()
window.geometry("250x250")
window.title("main")

#function to open new (top level) window
def topwin():
    top = Toplevel()
    top.geometry("150x100")
    top.title("toplevel")

    #adding a label to widget to top window
    L2 = Label(top, text = "This is top level window")
    L2.pack()

    top.mainloop()

#adding top label and button widget to window (Main) window
L = Label(window, text = "This is Main Window")
btn = Button(window, text = "Click here to open tope window", command = topwin)

#arranging widgets
L.pack()
btn.pack()

window.mainloop