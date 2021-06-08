from calendar import month
from re import L
from tkinter import *   #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
import tkinter as tk
from tkcalendar import * 
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
        self.myAppointments()
    
    def createFrames(self):
        self.root.img = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/Cook-e.png")
        #Show image using label
        img = Label(self.root, image = self.root.img)
        img.place(x = 0,y = 10, width=50, height=50)
        my_notebook = ttk.Notebook(self.root)
        my_notebook.pack(pady=100)

        self.my_frame1 = Frame(my_notebook, bg="#E59A41")
        self.my_frame2 = Frame(my_notebook, bg="#E59A41")
        self.my_frame3 = Frame(my_notebook, bg="#E59A41")
        self.my_frame4 = Frame(my_notebook, bg="#E59A41")

        my_notebook.add(self.my_frame1, text="Appointments")
        my_notebook.add(self.my_frame2, text="My Appointments")
        my_notebook.add(self.my_frame3, text="Settings")
        my_notebook.add(self.my_frame4, text="Meals Planner")
        my_notebook.place(x=0,y=60,width=500,height=500)
        
    def calendar(self):
        frame1 = Frame(self.my_frame1,bg="#E59A41")
        frame1.place(x=0,y=0,height=500,width=500)
        self.my_frame1.img2 = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/7.png")
        
        #Show image using label
        img2 = Label(self.my_frame1, image = self.my_frame1.img2, bg="#E59A41")
        img2.place(x = 1,y = 270, width=180, height=170)

        self.my_frame1.img3 = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/Cook-eold.png")
        #Show image using label
        img3 = Label(self.my_frame1, image = self.my_frame1.img3, bg="#E59A41")
        img3.place(x = 320,y = 270, width=180, height=170)

        # Δημιουργώ ένα Label για το καλωσόρισμα του διατροφολόγου
        welcome = Label(self.my_frame1,text="Welcome, Dr.Phill", font=("Calibri",15,"bold"),bg="#E59A41",fg="white")
        welcome.place(x=160,y=5)

        # Δημιουργώ το calendar 
        self.cal = Calendar(self.my_frame1,selectmode="day",locale="en_US",cursor="hand2",date_pattern="yyyy-MM-dd")
        self.cal.place(x=115,y=80)

        # Δημιουργώ κουμπί για να παίρνω την ημερομηνία
        getCalendarDate = Button(self.my_frame1, text="Get Date", command=self.grabDate, bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3)
        getCalendarDate.place(x=205,y=310)

    
    def grabDate(self):
        frame2 = Frame(self.my_frame1,bg="#E59A41")
        frame2.place(x=0,y=0,height=500,width=500)

        # Δημιουργώ ένα Label για το καλωσόρισμα του διατροφολόγου
        welcome2 = Label(self.my_frame1,text="Welcome, Dr.Phill", font=("Calibri",15,"bold"),bg="#E59A41",fg="white")
        welcome2.place(x=160,y=5)

        my_label = Label(self.my_frame1, text="", bg="#FFEE8E")
        my_label.place(x=75,y=35)

        my_label.config(text=self.cal.get_date(),fg="black",height=2,width=40,font=("Calibri",12))

        con=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursor=con.cursor()
        sql = "Select userPatiencename, hour from pendingAppointments where Date=%s and nutritionist = 'DrPhill'"
        dateap=(self.cal.get_date(), )
        global result
        result = my_cursor.execute(sql, dateap)
        result= my_cursor.fetchall()


        num=84
        # global i
        button = {}
        for i in result:
            def action(x=i):
                return self.text_updation(x)
            
            button[i] = Button(self.my_frame1, text=i, command=action, width=39, height=1, font=("Calibri",12), bg='#FFEE8E', fg="black")
            button[i].place(x=77,y=num)
            num+=35

        goBack = Button(self.my_frame1, text="Go Back", command=self.calendar, bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3)
        goBack.place(x=205,y=350)
    
    def text_updation(self,info):
        
        frame3 = Frame(self.my_frame1,bg="#E59A41")
        frame3.place(x=0,y=0,height=500,width=500)

        my_label = Label(self.my_frame1, text="", bg="#FFEE8E")
        my_label.place(x=75,y=35)

        my_label.config(text=self.cal.get_date(),fg="black",height=2,width=40,font=("Calibri",12))
        # Δημιουργώ ένα Label για το καλωσόρισμα του διατροφολόγου
        welcome = Label(self.my_frame1,text="Welcome, Dr.Phill", font=("Calibri",15,"bold"),bg="#E59A41",fg="white")
        welcome.place(x=160,y=5)

        global labletext
        self.labletext = Label(self.my_frame1, text=info[0], bg="#FFEE8E",fg="black",width=22,borderwidth=3,height=1)
        self.labletext.place(x=85,y=150)

        global labletext2
        self.labletext2 = Label(self.my_frame1, text=info[1], bg="#FFEE8E",fg="black",width=22,borderwidth=3,height=1)
        self.labletext2.place(x=235,y=150)

        acceptButton = Button(self.my_frame1, text="Accept", width=10,bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3, command=self.registerAppointment)
        acceptButton.place(x=140,y=310)
       
        rejectButton = Button(self.my_frame1, text="Reject", width=10,bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3, command=self.deleteAppointment)
        rejectButton.place(x=240,y=310)

        goBack2 = Button(self.my_frame1, text="Go Back", command=self.grabDate, bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3)
        goBack2.place(x=205,y=350)

    def registerAppointment(self):

        
        dateA = self.cal.get_date()
        pname = self.labletext.cget("text")
        ptime = self.labletext2.cget("text")

        conAppointment=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursorAppointment=conAppointment.cursor()
        sqlaccept = "Insert into nutriAppointments (userPatiencename, Date, hour) values (%s,  %s,  %s)"
        sqldelete = "Delete from pendingAppointments where userPatiencename =%s "

        mypname = (pname, )
        mydateA = (dateA, )
        myptime = (ptime, )
        
        
        my_cursorAppointment.execute(sqlaccept,(mypname, mydateA, myptime))
        
        conAppointment.commit()
        messagebox.showinfo(title="UPLOADED ", message="Uploaded successfully!")

        my_cursorAppointment.execute(sqldelete,mypname)
        conAppointment.commit()

        
    def deleteAppointment(self):

        pname3 = self.labletext.cget("text")

        conAppointment2=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursorDelete=conAppointment2.cursor()

        sqldelete2 = "Delete from pendingAppointments where userPatiencename =%s "
        mypname2 = (pname3, )

        my_cursorDelete.execute(sqldelete2, mypname2)
        conAppointment2.commit()
        messagebox.showinfo(title="Deletation ", message="You have successfully deleted the appointment!")

    def myAppointments(self):

        frame3 = Frame(self.my_frame2,bg="#E59A41")
        frame3.place(x=0,y=0,height=500,width=500)

        welcome3 = Label(self.my_frame2,text="Welcome, Dr.Phill", font=("Calibri",15,"bold"),bg="#E59A41",fg="white")
        welcome3.place(x=160,y=5)

        con3=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursor3=con3.cursor()
        sqlmyap = "Select userPatiencename, Date, hour from nutriAppointments where nutritionist = 'DrPhill'"
        result3 = my_cursor3.execute(sqlmyap)
        result3= my_cursor3.fetchall()


        num3=84
        button3 = {}
        for j in result3:
            def action(x=j):
                return self.editAppointments(x)
            
            button3[j] = Button(self.my_frame2, text=j, command=action, width=39, height=1, font=("Calibri",12), bg='#FFEE8E', fg="black")
            button3[j].place(x=77,y=num3)
            num3+=35

    def editAppointments(self,info):

        frame4 = Frame(self.my_frame2,bg="#E59A41")
        frame4.place(x=0,y=0,height=500,width=500)
        # global labletext
        self.labletext3 = Label(self.my_frame2, text=info[0], bg="#FFEE8E",fg="black",width=22,borderwidth=3,height=1)
        self.labletext3.place(x=85,y=150)

        # global labletext2
        self.labletext4 = Label(self.my_frame2, text=info[1], bg="#FFEE8E",fg="black",width=22,borderwidth=3,height=1)
        self.labletext4.place(x=235,y=150)
       
        rejectButton2 = Button(self.my_frame2, text="Reject", width=10,bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3)
        rejectButton2.place(x=200,y=310)

        goBack3 = Button(self.my_frame2, text="Go Back", command=self.myAppointments,bg="#FFEE8E",fg="black",font=("Calibri",12),borderwidth=3)
        goBack3.place(x=205,y=350)
    
    
        



def main(): 
 root = tk.Tk()
 mainInstance = Nutricionist(root)
 root.mainloop()

if __name__ == '__main__':
   main()