from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk


root = Tk() #To κύριο παράθυρό μας
root.title("Settings") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
#Make the app resizeable
root.resizable(False, False) #Width #Height


def openPersonalInformation():
 
    PersonalInformation = Toplevel(root)   # Toplevel object which will be treated as a new window
    PersonalInformation.title("Personal Information")   # sets the title of the Toplevel widget
    PersonalInformation.geometry("500x500")

    Label(PersonalInformation, text ="Personal Information", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)

    Username_btn = Button(PersonalInformation, text="Username", padx=50, pady=10, borderwidth = 0, command = openUsername)
    Password_btn = Button(PersonalInformation, text="Password", padx=50, pady=10, borderwidth = 0)
    Personal_btn = Button(PersonalInformation, text="Personal", padx=50, pady=10, borderwidth = 0)
    Medical_btn = Button(PersonalInformation, text="Medical", padx=50, pady=10, borderwidth = 0)
    Food_btn = Button(PersonalInformation, text="Favorite Cuisines", padx=50, pady=10, borderwidth = 0)

    Username_btn.pack(anchor="w")
    Password_btn.pack(anchor="w")
    Personal_btn.pack(anchor="w")
    Medical_btn.pack(anchor="w")
    Food_btn.pack(anchor="w")

def openUsername():

    Username = Toplevel(root)   # Toplevel object which will be treated as a new window
    Username.title("Username Settings")   # sets the title of the Toplevel widget
    Username.geometry("500x500")

    Label(Username, text ="Username Settings", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)

    e = Entry(Username, width=100, bg="orange", fg="white")
    e.pack()
    e.insert(0, "Enter a new Username")
#e.delete(0, END)

# def openPassword():



# def openPersonal():





# def openMedical():




# def openFavoriteCuisines():











label = Label(root, text ="Settings", font=("Comics Sans MS",20))
label.pack()

myButton1 = Button(root, text="Personal Information", padx=50, pady=10, borderwidth = 0, command = openPersonalInformation)
myButton2 = Button(root, text="Notifications", padx=50, pady=10, borderwidth = 0)
myButton3 = Button(root, text="Security", padx=50, pady=10, borderwidth = 0)
myButton4 = Button(root, text="General Settings", padx=50, pady=10, borderwidth = 0)
myButton5 = Button(root, text="Payment Information", padx=50, pady=10, borderwidth = 0)
myButton6 = Button(root, text="App Information", padx=50, pady=10, borderwidth = 0)


myButton1.pack(anchor="w")
myButton2.pack(anchor="w")
myButton3.pack(anchor="w")
myButton4.pack(anchor="w")
myButton5.pack(anchor="w")
myButton6.pack(anchor="w")


root.mainloop()