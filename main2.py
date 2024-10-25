from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x500")

def message():
    messagebox.askretrycancel("ALERT","stop! virus found!!!")
    messagebox.askquestion("ALERT","stop! virus found!!!")
    messagebox.askokcancel("ALERT","stop! virus found!!!")
    messagebox.askyesno("ALERT","stop! virus found!!!")
    messagebox.askyesnocancel("ALERT","stop! virus found!!!")
    messagebox.showerror("ALERT","stop! virus found!!!")
    messagebox.showinfo("ALERT","stop! virus found!!!")
    messagebox.showwarning("ALERT","stop! virus found!!!")


button = Button(root,text="scan the virus",command=message)
button.place(x=150,y=150)

root.mainloop()
