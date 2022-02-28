import imp


from tkinter import *
root = Tk()
photo = PhotoImage(file = "bg.gif")
w = Label(root, image=photo)
w.pack()
ent = Entry(root)
ent.pack()
ent.focus_set() 
root.mainloop()