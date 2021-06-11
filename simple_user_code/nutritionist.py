from calendar import month
from re import L
from tkinter import *   #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
import tkinter as tk
from tkcalendar import * 
from tkinter import messagebox
import pymysql



class Nutritionist:


    def __init__(self,root):


        self.root = root
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        self.tabs()
        self.calendar()



   

    def tabs(self):
        self.image = PhotoImage(file = "C:/Users/kleas/OneDrive/Έγγραφα/Ceid/8o ΕΞΑΜΗΝΟ/ΤΛ/pytorch-chatbot-master/nutri/Cook-e.png")
        # Show image using label
        image = Label( self.root, image = self.image)
        image.place(x = 10,y = 10, width=50, height=50)
        
        self.root.title("Nutritionist")
        tabControl = ttk.Notebook(self.root)
        tabControl.pack()
        
        self.tab1 = Frame(tabControl,bg="white")
        self.tab2 = Frame(tabControl,bg="white")
        self.tab3 = Frame(tabControl,bg="white")
        self.tab4 = Frame(tabControl,bg="white")
    
        tabControl.add(self.tab1, text ='Just for you')
        tabControl.add(self.tab2, text ='Find a recipe')
        tabControl.add(self.tab3, text ='Nutritionist')
        tabControl.add(self.tab4, text ='Mycart')
        tabControl.place(x=0,y=60,width=500,height=700)
        tabControl.select(self.tab3)

    def calendar(self):

        global inputName
        inputName = Entry(self.tab3,font=("Calibri",12),bg="white",borderwidth=5,fg="black")
        inputName.insert(0,"Insert your name...")
        inputName.place(x=160,y=330)

        con=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursor=con.cursor()
        sql = "Select dr_name, stars from recipesnot"
        global result
        result = my_cursor.execute(sql)
        result= my_cursor.fetchall()

        num=85
        global i
        button = {}
        for i in result:
            def action(x=i):
                return self.show_nutri(x)

            button[i] = Button(self.root, text=i, command=action, width=59, font=("Calibri",10), bg='orange', fg="black")
            button[i].place(x=35,y=num)
            num+=30



        self.cal=Calendar(self.tab3, selectmode="day",year=2021,locale="en_US",date_pattern="yyyy-MM-dd")
        self.cal.place(x=120,y=100)

        drophour = ttk.Combobox(self.tab3, values=['Select hour...','9:00','9:30','10:00','10:30','11:00','11:30'],width=20, font=("Calibri",12))
        drophour.current(0)
        drophour.place(x=150,y=300)

        my_button = Button(self.tab3,text="Submit", bg="orange", command=self.grab_date)
        my_button.place(x=220,y=370)

        # self.my_label = Label(self.tab3,text="")
        # self.my_label.pack(pady=20)
    

    def show_nutri(self,info):
        global nutributton
        nutributton = Label(self.tab3, text=info[0])
        #nutributton.place(x=75,y=35)
        # global nutri
        # nutri = nutributton.cget("text")


    def grab_date(self):

        name = nutributton.cget("text")
        dateap = self.cal.get_date()
        selectedhour = self.drophour.get()
        namep = inputName.get()

        con2=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursor2=con2.cursor()

        sql2 = "Insert into pendingappointments(userPatiencename, Date, hour, nutritionist) values (%s, %s, %s, %s) "

        namenutri = (name, )
        datea=(dateap, )
        hourselected=(selectedhour, )
        pname=(namep, )
        
        my_cursor2.execute(sql2,(pname,datea,hourselected,namenutri))
        con2.my_cursor2.commit()
        messagebox.showinfo(title="Insert", message="Inserted succesfully!")
        
        


    
def main(): 
 root = tk.Tk()
 app = Nutritionist(root)

 root.mainloop()

if __name__ == '__main__':
   main()
