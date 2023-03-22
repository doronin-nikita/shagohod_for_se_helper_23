from tkinter import *

window = Tk()
window.title("test")
canvas = Canvas(window, height=500, width=500)
canvas.pack()

def set_clear():
    canvas.delete("all")
    canvas.create_line(0,450,500,450,fill="red")



set_clear()
window.mainloop()
