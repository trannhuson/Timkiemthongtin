from tkinter import *
root = Tk()
label=Label(root,text="I was Hidden")
def labelactive():
    label.pack()
def labeldeactive():
    label.pack_forget()
Button(root,text="Show",command=labelactive).pack()
Button(root,text="Hide",command=labeldeactive).pack()
root.mainloop()