# Import module
from pydoc import describe
from tkinter import *
from tkcalendar import Calendar, DateEntry
import json

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )
root.title("Destination")

# Change the label text
def show():
    global label,clicked,clicked1,cal
    label.config( text = clicked.get()+" TO "+clicked1.get() )
    des = clicked1.get()
    source = clicked.get()
    dt=cal.get_date()
    str=dt.strftime("%d-%B-%Y")
    str = str.split("-")
    print(str)
    dictionary ={
	"source" : source,
	"destination" : des,
	"date" :str}
    json_object = json.dumps(dictionary, indent = 4)

    # Writing to sample.json
    with open("dest.json", "w") as outfile:
        outfile.write(json_object)
    root.after(2000, root.destroy)
    import train
    train.search()
def main():
    global label,clicked,clicked1,cal
    options = [
        "KOLKATA",
        "DELHI"
    ]

    # datatype of menu text
    clicked = StringVar()
    clicked1 = StringVar()
    # initial menu text
    clicked.set( " " )
    clicked1.set( " " )

    # Create Dropdown menu
    drop1 = OptionMenu( root , clicked , *options )
    drop1.pack()
    label1 = Label( root , text = "TO" )
    label1.pack()
    drop2 = OptionMenu( root , clicked1 , *options )
    drop2.pack()
    cal = DateEntry(root, width= 16, background= "magenta3", foreground= "white",bd=2)
    cal.pack(pady=20)
    # Create Label
    label = Label( root , text = " " )
    label.pack()
    # Create button, it will change label text
    button = Button( root , text = "SELECT" , command = show ).pack()

    # Execute tkinter
    root.mainloop()
main()