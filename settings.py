from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox


root = Tk() #To κύριο παράθυρό μας
root.title("Settings") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
root.resizable(False, False) #Width #Height


def openPersonalInformation():
 
    PersonalInformation = Toplevel(root)   # Toplevel object which will be treated as a new window
    frame = tk.Frame()
    PersonalInformation.title("Personal Information")   # sets the title of the Toplevel widget
    PersonalInformation.geometry("500x500")
    frame.pack()

    Label(PersonalInformation, text ="Personal Information", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)

    Username_btn = Button(PersonalInformation, text="Username", padx=50, pady=10, borderwidth = 0, command = openUsername)
    Password_btn = Button(PersonalInformation, text="Password", padx=50, pady=10, borderwidth = 0, command = openPassword)
    Personal_btn = Button(PersonalInformation, text="Personal", padx=50, pady=10, borderwidth = 0, command = openPersonal)
    Medical_btn = Button(PersonalInformation, text="Medical", padx=50, pady=10, borderwidth = 0, command= openMedical)
    Food_btn = Button(PersonalInformation, text="Favorite Cuisines", padx=50, pady=10, borderwidth = 0, command= openFavoriteCuisines)

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

    hello = "Hello " #να προσθεσω να τραβαει απο τη βαση το current username του user, ωστε να του δειχνει τι εχει εκεινη τη στιγμη
    Label(Username, text =hello).pack()
    label.pack()

    e = Entry(Username, width=30, bg="orange", fg="white")
    e.pack()
    e.insert(0, "Enter a new Username")

    myButton = Button(Username, text="Submit", padx=10, pady=2, bg="black", fg="white", borderwidth = 0)
    myButton.pack()

    # εδω πρεπει να συνδεσω βαση ωστε οταν κανει submit να πηγαινει στη βαση και να κοιταει / αποθηκευει



    if e == None:

               messagebox.showerror("Error","Username already Exists",parent=Username.root)
               Username.regclear()
               Username.entry.focus()

        #     else:

        #        cur.execute("insert into accounts values(%s,%s,%s,%s)",(Username.entry.get(),Username.entry3.get(),Username.entry2.get(),Username.entry4.get()))
        #        con.commit()
        #        con.close()

        #        messagebox.showinfo("Success","Register Succesfull",parent=Username.root)
        #        Username.regclear()

        #  except Exception as es:
        #     messagebox.showerror("Error",f"Error due to:{str(es)}",parent=Username.root)
#e.delete(0, END)

def openPassword():

    Password = Toplevel(root)   # Toplevel object which will be treated as a new window
    Password.title("Password Settings")   # sets the title of the Toplevel widget
    Password.geometry("500x500")

    Label(Password, text ="Password Settings", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)

    
def openPersonal():
    Personal = Toplevel(root)   # Toplevel object which will be treated as a new window
    Personal.title("Personal Settings")   # sets the title of the Toplevel widget
    Personal.geometry("500x500")

    Label(Personal, text ="Personal Settings", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    # label.pack(pady = 10)
    # Change the label text
    def show(self):
        #label.config( text = clicked.get() )
        Label(Personal, text = clicked.get()).pack()
        
        
        # Dropdown menu options
    options = [
        "0-10",
        "10-15",
        "16-18",
        "19-22",
        "23-27",
        "28-40",
        "41-50",
        "51+"
    ]
        # datatype of menu text
    clicked = StringVar()
        # initial drop down menu text
    clicked.set( "age" )
        # Create Dropdown menu
    drop = OptionMenu( Personal , clicked , *options )
    drop.pack()      
        # Create button, it will change label text
    button = Button( Personal , text = "Select" , command = show )
    # button.grid(row = 0, column = 2)
    button.pack()
        
        # Create Label
    Label( show , text = " " ).pack()
    # # label.grid(row = 0, column = 3, columnspan=2)
    # label.pack(pady = 10)





def openMedical():
    Medical = Toplevel(root)   # Toplevel object which will be treated as a new window
    Medical.title("Medical Settings")   # sets the title of the Toplevel widget
    Medical.geometry("500x500")

    Label(Medical, text ="Medical Settings", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)




def openFavoriteCuisines():
    FavoriteCuisines = Toplevel(root)   # Toplevel object which will be treated as a new window
    FavoriteCuisines.title("Favorite Cuisines Settings")   # sets the title of the Toplevel widget
    FavoriteCuisines.geometry("500x500")

    Label(FavoriteCuisines, text ="Favorite Cuisines Settings", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)











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