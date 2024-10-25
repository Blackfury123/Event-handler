from tkinter import *
window=Tk()
window.title("Event handler")
window.geometry("500x500")

def handle_keypress(event):
    print("The key",event.char,"is pressed!!!")

window.bind("<Key>",handle_keypress)

window.mainloop()