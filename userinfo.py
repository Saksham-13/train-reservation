
from tkinter import *
import json
def but():
    
    global window2,e1,enn2,enn3,enn4,e5,e6,enn7,enn8,enn9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,v2,v3,v4,v5,v6,v7,v8,v9
    list1 = [["1","2","3","4"],
            [enn7.get(),e12.get(),e17.get(),e22.get()],
            [enn8.get(),e13.get(),e18.get(),e23.get()],
            [v2.get(),v3.get(),v4.get(),v5.get()],
            [v6.get(),v7.get(),v8.get(),v9.get()]
            ]
    dictionary = {"Sr No.":list1[0],"Name":list1[1],"Age":list1[2],"Gender":list1[3],"Id Proof":list1[4]}
    print(dictionary)
    json_object = json.dumps(dictionary, indent = 5)
    with open("userinfo1.json", "w") as outfile:
                        outfile.write(json_object)
    
    
    
    window2.after(2000, window2.destroy)

def PassengerDetails():
                global window2,e1,enn2,enn3,enn4,e5,e6,enn7,enn8,enn9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,v2,v3,v4,v5,v6,v7,v8,v9
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config()
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 800
                height = 150
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Entry(window2, justify="center", font=('Slab Serif', 10) )
                        enn2 = Entry(window2, justify="center", font=('Slab Serif', 10) )
                        enn3 = Entry(window2, justify="center", font=('Slab Serif', 10) )
                        enn4 = Entry(window2, justify="center", font=('Slab Serif', 10) )
                        e5 = Entry(window2, justify="center", font=('Slab Serif', 10) )
                        e6 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e11 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e12 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e16 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e17 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e21 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e22 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 9))
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))

                        e1.insert(10, "S.no")
                        enn2.insert(10, "Name")
                        enn3.insert(10, "Age")
                        enn4.insert(10, "Gender")
                        e5.insert(10, "IdProof")
                        e6.insert(10, "1")

                        e11.insert(10, "2")
                        e16.insert(10, "3")
                        e21.insert(10, "4")

                        e1.grid(row=0, column=0)
                        enn2.grid(row=0, column=1)
                        enn3.grid(row=0, column=2)
                        enn4.grid(row=0, column=3)
                        e5.grid(row=0, column=4)
                        e6.grid(row=1, column=0)
                        enn7.grid(row=1, column=1)
                        enn8.grid(row=1, column=2)
                        enn9.grid(row=1, column=3)
                        e10.grid(row=1, column=4)

                        e11.grid(row=2, column=0)
                        e12.grid(row=2, column=1)
                        e13.grid(row=2, column=2)
                        e14.grid(row=2, column=3)
                        e15.grid(row=2, column=4)

                        e16.grid(row=3, column=0)
                        e17.grid(row=3, column=1)
                        e18.grid(row=3, column=2)
                        e19.grid(row=3, column=3)
                        e20.grid(row=3, column=4)

                        e21.grid(row=4, column=0)
                        e22.grid(row=4, column=1)
                        e23.grid(row=4, column=2)
                        e24.grid(row=4, column=3)
                        e25.grid(row=4, column=4)

                        

                        v2 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v2.set('Select')
                        
                        popupMenu1 = OptionMenu(window2, v2, *gender)
                        popupMenu1.config(font=('Slab Serif', 9), bg="purple")
                        popupMenu1.grid(row=1, column=3)

                        v3 = StringVar(window2)
                        gender1 = {'Male', 'Female'}
                        v3.set('Select')
                        
                        popupMenu2 = OptionMenu(window2, v3, *gender1)
                        popupMenu2.config(font=('Slab Serif', 9), bg="purple")
                        popupMenu2.grid(row=2, column=3)

                        v4 = StringVar(window2)
                        gender2 = {'Male', 'Female'}
                        v4.set('Select')
                        
                        popupMenu3 = OptionMenu(window2, v4, *gender2)
                        popupMenu3.config(font=('Slab Serif', 9), bg="purple")
                        popupMenu3.grid(row=3, column=3)

                        v5 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v5.set('Select')
                        
                        popupMenu4 = OptionMenu(window2, v5, *gender)
                        popupMenu4.config(font=('Slab Serif', 9), bg="purple")
                        popupMenu4.grid(row=4, column=3)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=1, column=4)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                    
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=2, column=4)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=3, column=4)

                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=4, column=4)
                        
                        
                        B1 = Button(window2, text="SUBMIT",command = but, width=10, height=1)
                        B1.grid(row=5, column=2)
        
                window2.mainloop()
PassengerDetails()