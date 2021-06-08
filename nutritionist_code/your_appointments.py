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
        # Δημιουργώ ένα Label για το καλωσόρισμα του διατροφολόγου
        welcome = Label(self.my_frame1,text="Welcome, Dr.", font=("Calibri",15),bg="white",fg="#E59A41")
        welcome.place(x=130,y=5)

        # Δημιουργώ το calendar 
        self.cal = Calendar(self.my_frame1,selectmode="day")
        self.cal.place(x=115,y=80)

        # Δημιουργώ κουμπί για να παίρνω την ημερομηνία
        getCalendarDate = Button(self.my_frame1, text="Get Date", command=self.grabDate)
        getCalendarDate.place(x=130,y=310)

        self.my_Label = Label(self.my_frame1, text="")
        self.my_Label.place(x=120,y=340)
    
    def grabDate(self):
        self.my_Label.config(text=self.cal.get_date())

        
















def main(): 
 root = tk.Tk()
 mainInstance = Nutricionist(root)
 root.mainloop()

if __name__ == '__main__':
   main()