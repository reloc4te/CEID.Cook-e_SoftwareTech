from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
#import sqlite3
import re



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
    Password_btn = Button(PersonalInformation, text="Password", padx=50, pady=10, borderwidth = 0, command = opencPassword)
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
    

    e = Entry(Username, width=30, bg="orange", fg="white")
    e.pack()
    e.insert(0, "Enter a new Username")
    myButton = Button(Username, text="Submit", padx=10, pady=2, bg="black", fg="white", borderwidth = 0)
    myButton.pack()

        # εδω πρεπει να συνδεσω βαση ωστε οταν κανει submit να πηγαινει στη βαση και να κοιταει / αποθηκευει
    # conn = sqlite3.connect('all_usernames.db')

    # #create cursor
    # c = conn.cursor()

    # #table
    # c.execute("""CREATE TABLE usernames (
    #         username text,
    # )""")

    # #commit changes in db
    # conn.commit()
    # #close connection
    # conn.close()


def opencPassword():

    cPassword = Toplevel(root)   # Toplevel object which will be treated as a new window
    cPassword.title("Password Settings")   # sets the title of the Toplevel widget
    cPassword.geometry("500x500")
    

    def close_win():
        cPassword.destroy()   # close the current window

    def get_win():
        cpassword.get()

    def new_window():
        close_win() 
        cPassword.app = openPersonalInformation() # create cPassword window
        cPassword.master.mainloop()
        
    #Create a text label
    Label(cPassword,text="Enter Current Password", font=('Helvetica',20)).pack(pady=20)

    #Create Entry Widget for password
    cpassword= Entry(cPassword,show="*",width=20)
    cpassword.pack()

    Button(cPassword, text="Submit", font=('Helvetica bold',10),command=opennPassword).pack(pady=20)
    #Close the window
    Button(cPassword, text="Quit", font=('Helvetica bold',10),command=new_window).pack(pady=20)

    # try:
    #     con=pymysql.connect(host='localhost',user='root',password='texnologia!@logismikou1998',database='pythonlogin')

    #     cur=con.cursor()

    #     cur.execute('select * from accounts where email=%s and password=%s',(cpassword.email_txt.get(),cpassword.get()))

    #     row=cur.fetchone() #cpassword ??

    #     if row == "12345": #cpassword.get() ??? τι οχι?
    #             messagebox.showinfo("Success","Password Correct",parent=cPassword.root)
    #             cPassword.regclear()
    #             opennPassword() #open window to enter the new password

    #     else:

    #             messagebox.showerror("Wrong Password.","Please enter again your Password.",parent=cPassword.root)
    #             cPassword.regclear()
    #             cPassword.entry.focus()

    # except Exception as es:
    #     messagebox.showerror("Error",f"Error due to:{str(es)}",parent=cPassword.root)

def opennPassword():
    nPassword = Toplevel(root)   # Toplevel object which will be treated as a new window
    nPassword.title("Password Settings")   # sets the title of the Toplevel widget
    nPassword.geometry("500x500")

    def close_win():
        nPassword.destroy()   # close the current window

    def get_win():
        nPassword.get()
        recover_button(fr_button) #reveil the new submit button

    def pass_ready():
        nPassword.get()
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        # compiling regex
        pat = re.compile(reg)
        # searching regex                 
        mat = re.search(pat, nPassword.get())    

        if mat:
            print("Password is valid.")
        else:
            print("Password invalid !!")   
    if __name__ == '__main__':
        pass_ready()
    
    def new_window():
        close_win() 
        nPassword.app = opencPassword() # create cPassword window6
        nPassword.master.mainloop()

    def hide_button():
        nPassword.pack_forget()

    def recover_button():
        nPassword.pack()
    #Create a text label
    Label(nPassword,text="Enter New Password", font=('Helvetica',20)).pack(pady=20)

    #Create Entry Widget for password no.1
    cpassword= Entry(nPassword,show="*",width=20)
    cpassword.pack()
    #Submit the new password
    Button(nPassword, text="Submit", font=('Helvetica bold',10),command=get_win).pack(pady=20)

    #Create Entry Widget for password no.2
    cpassword= Entry(nPassword,show="*",width=20)
    cpassword.pack()    
    #Check and finally submit the new password
    fr_button = Button(nPassword, text="Finally Ready", font=('Helvetica bold',10),command=pass_ready)
    fr_button.pack(pady=20)
    #Close the window
    Button(nPassword, text="Back", font=('Helvetica bold',10),command=new_window).pack(pady=20)

        
def openPersonal():
    Personal = Toplevel(root)   # Toplevel object which will be treated as a new window
    Personal.title("Personal Settings")   # sets the title of the Toplevel widget
    Personal.geometry("500x500")

    Label(Personal, text ="Personal Settings", font=("Comics Sans MS",20)).place(x=5 ,y=5)  # A Label widget to show in toplevel
        # Change the label text
    
    #AGE DROP DOWN MENU
    def showAge():
        Label(Personal, text = showAge.clicked.get()).place(x=160 ,y=103)  
            # Dropdown menu options
    options = [
            "0-10",
            "11-15",
            "16-18",
            "19-22",
            "23-27",
            "28-40",
            "41-50",
            "51-"
        ]
            # datatype of menu text
    showAge.clicked = StringVar()
        # initial drop down menu text
    showAge.clicked.set( "age" )                                                         #να δω πως οταν επιλεγω κατι να διαγραφεται η προηγουμενη επιλογη
            # Create Dropdown menu
    OptionMenu( Personal , showAge.clicked , *options ).place(x=20 ,y=100)    
            # Create button, it will change label text
    Button( Personal , text = "Select" , command = showAge ).place(x=100 ,y=102)

    #HEIGHT DROP DOWN MENU
    def showHeight():
        Label(Personal, text = showHeight.clicked.get()).place(x=180 ,y=133)  
            # Dropdown menu options
    options = [
            "<150",
            "150-160",
            "161-170",
            "171-180",
            "181-190",
            "190+"
        ]
            # datatype of menu text
    showHeight.clicked = StringVar()
        # initial drop down menu text
    showHeight.clicked.set( "height (cm)" )                                                         #να δω πως οταν επιλεγω κατι να διαγραφεται η προηγουμενη επιλογη
            # Create Dropdown menu
    OptionMenu( Personal ,showHeight.clicked , *options ).place(x=20 ,y=130)    
            # Create button, it will change label text
    Button( Personal , text = "Select" , command = showHeight ).place(x=133 ,y=132)

    #WEIGHT DROP DOWN MENU
    def showWeight():
        Label(Personal, text = showWeight.clicked.get()).place(x=180 ,y=163)  
            # Dropdown menu options
    options = [
            "<40",
            "40-60",
            "61-80",
            "81-100",
            "101-120",
            "121+"
        ]
            # datatype of menu text
    showWeight.clicked = StringVar()
        # initial drop down menu text
    showWeight.clicked.set( "weight (kg)" )                                                         #να δω πως οταν επιλεγω κατι να διαγραφεται η προηγουμενη επιλογη
            # Create Dropdown menu
    OptionMenu( Personal , showWeight.clicked , *options ).place(x=20 ,y=160)    
            # Create button, it will change label text
    Button( Personal , text = "Select" , command = showWeight ).place(x=133 ,y=162)


def openMedical():
    Medical = Toplevel(root)   # Toplevel object which will be treated as a new window
    Medical.title("Medical Settings")   # sets the title of the Toplevel widget
    Medical.geometry("500x500")

    Label(Medical, text ="Medical Settings", font=("Comics Sans MS",20)).place(x=5 ,y=5)  

    #MEDICAL CONDITIONS DROP DOWN MENU
    def showMedicalCon():
        Label(Medical, text = showMedicalCon.clicked.get()).place(x=230 ,y=103)  
            # Dropdown menu options
    options = [
            "leukaemia",
            "cholecystitis",
            "addison disease",
            "anaphylaxis",
            "asbestosis",
            "lactose",
            "kidney stones",
            "lyme disease"
            "osteoporosis"
        ]
            # datatype of menu text
    showMedicalCon.clicked = StringVar()
        # initial drop down menu text
    showMedicalCon.clicked.set( "medical conditions" )                                                         #να δω πως οταν επιλεγω κατι να διαγραφεται η προηγουμενη επιλογη
            # Create Dropdown menu
    OptionMenu( Medical , showMedicalCon.clicked , *options ).place(x=20 ,y=100)    
            # Create button, it will change label text
    Button( Medical , text = "Select" , command = showMedicalCon ).place(x=180 ,y=102)

    #ALLERGIES DROP DOWN MENU
    def showAllergies():
        Label(Medical, text = showAllergies.clicked.get()).place(x=180 ,y=133)  
            # Dropdown menu options
    options = [
            "milk",
            "egg",
            "peanut",
            "tree nut",
            "soy",
            "wheat"
            "fin fish"
            "sesame"
        ]
            # datatype of menu text
    showAllergies.clicked = StringVar()
        # initial drop down menu text
    showAllergies.clicked.set( "allergies" )                                                         #να δω πως οταν επιλεγω κατι να διαγραφεται η προηγουμενη επιλογη
            # Create Dropdown menu
    OptionMenu( Medical ,showAllergies.clicked , *options ).place(x=20 ,y=130)    
            # Create button, it will change label text
    Button( Medical , text = "Select" , command = showAllergies ).place(x=133 ,y=132)




def openFavoriteCuisines():
    FavoriteCuisines = Toplevel(root)   # Toplevel object which will be treated as a new window
    FavoriteCuisines.title("Favorite Cuisines Settings")   # sets the title of the Toplevel widget
    FavoriteCuisines.geometry("500x500")

    Label(FavoriteCuisines, text ="Favorite Cuisines Settings", font=("Comics Sans MS",20)).pack()  # A Label widget to show in toplevel
    label.pack(pady = 10)

    #FAVORITE CUISINES DROP DOWN MENU
    def showFavCuisines():
        Label(FavoriteCuisines, text = showFavCuisines.clicked.get()).place(x=180 ,y=133)  
            # Dropdown menu options
    options = [
            "mexican",
            "italian",
            "greek",
            "chinese",
            "spanish",
            "mediterranean",
            "american"
        ]
            # datatype of menu text
    showFavCuisines.clicked = StringVar()
        # initial drop down menu text
    showFavCuisines.clicked.set( "cuisines" )                                                         #να δω πως οταν επιλεγω κατι να διαγραφεται η προηγουμενη επιλογη
            # Create Dropdown menu
    OptionMenu( FavoriteCuisines ,showFavCuisines.clicked , *options ).place(x=20 ,y=130)    
            # Create button, it will change label text
    Button( FavoriteCuisines , text = "Select" , command = showFavCuisines ).place(x=133 ,y=132)









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