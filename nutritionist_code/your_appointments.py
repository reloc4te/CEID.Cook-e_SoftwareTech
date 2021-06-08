from calendar import month
from re import L
from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
import tkinter as tk
from tkcalendar import * 
from tkinter import filedialog
from tkinter import messagebox
import pymysql

class Nutricionist:
    def __init__(self,root):
        self.root = root
        self.root.title("Nutritionist's Interface") #Ο τίτλος του παραθύρου
        self.root.geometry("500x500") #H διάσταστη του παραθύρου
        #Make the app resizeable
        self.root.resizable(False, False) #Width #Height
        self.createFrames()
        self.calendar()
    
    def createFrames(self):
        self.root.img = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/nutritionist_code/Cook-e.png")
        #Show image using label
        img = Label(self.root, image = self.root.img)
        img.place(x = 0,y = 10, width=50, height=50)
        my_notebook = ttk.Notebook(self.root)
        my_notebook.pack(pady=100)

        self.my_frame1 = Frame(my_notebook, bg="white")
        self.my_frame2 = Frame(my_notebook, bg="white")
        self.my_frame3 = Frame(my_notebook, bg="white")
        self.my_frame4 = Frame(my_notebook, bg="white")

        my_notebook.add(self.my_frame1, text="Appointments")
        my_notebook.add(self.my_frame2, text="My Appointments")
        my_notebook.add(self.my_frame3, text="Settings")
        my_notebook.add(self.my_frame4, text="Meets Planner")
        my_notebook.place(x=0,y=60,width=500,height=500)
        
    def calendar(self):
        frame1 = Frame(self.my_frame1,bg="white")
        frame1.place(x=0,y=0,height=500,width=500)
        # Δημιουργώ ένα Label για το καλωσόρισμα του διατροφολόγου
        welcome = Label(self.my_frame1,text="Welcome, Dr.Phill", font=("Calibri",15),bg="white",fg="#E59A41")
        welcome.place(x=160,y=5)

        # Δημιουργώ το calendar 
        self.cal = Calendar(self.my_frame1,selectmode="day",locale="en_US",cursor="hand2",date_pattern="dd/MM/yyyy")
        self.cal.place(x=115,y=80)

        # Δημιουργώ κουμπί για να παίρνω την ημερομηνία
        getCalendarDate = Button(self.my_frame1, text="Get Date", command=self.grabDate)
        getCalendarDate.place(x=130,y=310)
    
    def grabDate(self):
        frame2 = Frame(self.my_frame1,bg="white")
        frame2.place(x=0,y=0,height=500,width=500)

        my_label = Label(self.my_frame1, text="")
        my_label.place(x=75,y=35)

        my_label.config(text=self.cal.get_date(),fg="black",height=2,width=40,font=("Calibri",12))
        # Δημιουργώ ένα Label για το καλωσόρισμα του διατροφολόγου
        welcome = Label(self.my_frame1,text="Welcome, Dr.Phill", font=("Calibri",15),bg="white",fg="#E59A41")
        welcome.place(x=160,y=5)

        goBack = Button(self.my_frame1, text="Go back", command=self.calendar)
        goBack.place(x=130,y=310)


        
















def main(): 
 root = tk.Tk()
 mainInstance = Nutricionist(root)
 root.mainloop()

if __name__ == '__main__':
   main()