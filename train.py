from re import search
from tkinter import *
import json
def but():
        global window1,e1,e2,e3,e4,e5,e6,e7,en8,e9,e10,e11,e12,e13,e14,en15,e16,e17,e18,e19,e20,e21,en22,e23,e24,e25,e26,e27,e28,en29,e30,e31,e32,e33,e34,e35,clicked3,clicked2,clicked1,clicked
        optinos = ["1A","2A","3A"]
        print("saksham")
        a1 = clicked3.get()
        a2 = clicked.get()
        a3 = clicked1.get()
        a4 = clicked2.get()
        if a1 in optinos:
                a = clicked3.get()
                print (a )
                dict = {"Train number":en8.get(),"Train Name":e9.get(),
                "Source":e10.get(),"Departure Time":e11.get(),"Destination":e12.get(),"Arrival":e13.get(),"Class":a1}
                print(dict)
                json_object = json.dumps(dict, indent = 7)
                with open("trains.json", "w") as outfile:
                        outfile.write(json_object)
                window1.after(2000, window1.destroy)
                import userinfo
        if a2 in optinos:
                a = clicked.get()
                print (a) 
                dict = {"Train number":en15.get(),"Train Name":e16.get(),
                "Source":e17.get(),"Departure Time":e18.get(),"Destination":e19.get(),"Arrival":e20.get(),"Class":a2}
                print(dict)
                json_object = json.dumps(dict, indent = 7)
                with open("trains.json", "w") as outfile:
                        outfile.write(json_object)
                window1.after(2000, window1.destroy)
                import userinfo

        if a3 in optinos:
                a = clicked1.get()
                print (a) 
                dict = {"Train number":en8.get(),"Train Name":e9.get(),
                "Source":e24.get(),"Departure Time":e25.get(),"Destination":e26.get(),"Arrival":e27.get(),"Class":a3}
                print(dict)
                json_object = json.dumps(dict, indent = 7)
                with open("trains.json", "w") as outfile:
                        outfile.write(json_object)
                window1.after(2000, window1.destroy)
                import userinfo

        if a4 in optinos:
                a = clicked2.get()
                print (a) 
                dict = {"Train number":en29.get(),"Train Name":e30.get(),
                "Source":e31.get(),"Departure Time":e32.get(),"Destination":e33.get(),"Arrival":e34.get(),"Class":a4}
                print(dict)
                json_object = json.dumps(dict, indent = 7)
                with open("trains.json", "w") as outfile:
                        outfile.write(json_object)
                window1.after(2000, window1.destroy)
                import userinfo
                userinfo.PassengerDetails()

def Search():
        global window1,e1,e2,e3,e4,e5,e6,e7,en8,e9,e10,e11,e12,e13,e14,en15,e16,e17,e18,e19,e20,e21,en22,e23,e24,e25,e26,e27,e28,en29,e30,e31,e32,e33,e34,e35,clicked3,clicked2,clicked1,clicked

        window1=Tk()
        window1.title("RAILWAY SCHEDULE")
        window1.config()
        screen_width = window1.winfo_screenwidth()
        screen_height = window1.winfo_screenheight()
        width = 1160
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window1.resizable(0, 0)

        height = 5
        width = 7
        clicked = StringVar()
        clicked.set("None")
        clicked1 = StringVar()
        clicked1.set("None")
        clicked2 = StringVar()
        clicked2.set("None")
        clicked3 = StringVar()
        clicked3.set("None")
        optinos = ["1A","2A","3A"]

        e1 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue",fg="white")
        e2 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
        e3 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
        e4 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
        e5 = Entry(window1, justify="center",font=('Slab Serif',10),bg="blue", fg="white")
        e6 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
        e7 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")

        en8 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e9 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e10 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e11 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e12 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e13 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e14 = OptionMenu(window1,clicked3,*optinos,)

        en15 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e16 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e17 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e18 = Entry(window1, justify="center",font=('Slab Serif',9),bg="sky blue")
        e19 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e20 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e21 = OptionMenu(window1,clicked,*optinos)

        en22 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e23 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e24 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e25 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e26 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e27 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e28 = OptionMenu(window1,clicked1,*optinos)

        en29 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e30 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e31 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e32 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e33 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e34 = Entry(window1, justify="center",font=('Slab Serif',9), bg="sky blue")
        e35 = OptionMenu(window1,clicked2,*optinos)

        e1.grid(row=0, column=0)
        e2.grid(row=0, column=1)
        e3.grid(row=0, column=2)
        e4.grid(row=0, column=3)
        e5.grid(row=0, column=4)
        e6.grid(row=0, column=5)
        e7.grid(row=0, column=6)
        en8.grid(row=1, column=0)
        e9.grid(row=1, column=1)
        e10.grid(row=1, column=2)
        e11.grid(row=1, column=3)
        e12.grid(row=1, column=4)
        e13.grid(row=1, column=5)
        e14.grid(row=1, column=6)
        en15.grid(row=2, column=0)
        e16.grid(row=2, column=1)
        e17.grid(row=2, column=2)
        e18.grid(row=2, column=3)
        e19.grid(row=2, column=4)
        e20.grid(row=2, column=5)
        e21.grid(row=2, column=6)
        en22.grid(row=3, column=0)
        e23.grid(row=3, column=1)
        e24.grid(row=3, column=2)
        e25.grid(row=3, column=3)
        e26.grid(row=3, column=4)
        e27.grid(row=3, column=5)
        e28.grid(row=3, column=6)
        en29.grid(row=4, column=0)
        e30.grid(row=4, column=1)
        e31.grid(row=4, column=2)
        e32.grid(row=4, column=3)
        e33.grid(row=4, column=4)
        e34.grid(row=4, column=5)
        e35.grid(row=4, column=6)

        e1.insert(10, "Train number")
        e2.insert(10, "Train name")
        e3.insert(10, "Source")
        e4.insert(10, "Departure time")
        e5.insert(10, "Destination")
        e6.insert(10, "Arrival")
        e7.insert(10, "class")


    
        en8.insert(10, "12238")
        e9.insert(10, "Rajdhani Express")
        e10.insert(10, "Howrah")
        e11.insert(10, "14:30")
        e12.insert(10, "New Delhi")
        e13.insert(10, "7:55")
        

        en15.insert(10, "12236")

        e16.insert(10, "Howrah Juntion")
        e17.insert(10, "Howrah")
        e18.insert(10, "16:30")
        e19.insert(10, "New Delhi")
        e20.insert(10, "5:50")
        

        en22.insert(10, "12237")
        e23.insert(10, "New Delhi Duronto")
        e24.insert(10, "Howrah")
        e25.insert(10, "8:35")
        e26.insert(10, "New Delhi")
        e27.insert(10, "15:50")
        

        en29.insert(10, "12238")
        e30.insert(10, "Anand Vihar")
        e31.insert(10, "Howrah")
        e32.insert(10, "12:30")
        e33.insert(10, "New Delhi")
        e34.insert(10, "7:20")
        B1 = Button(window1, text="SUBMIT",command = but, width=10, height=1)
        B1.grid(row=5, column=3)
        window1.mainloop()

Search()