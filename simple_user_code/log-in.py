from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter.messagebox as MessageBox

class Login:
    def __init__(self, root):

        self.root = root
        self.root.title("Login System")
        self.root.geometry("800x600+100+50")
        self.root.resizable(False,False)
        
        #Background image
        #self.bg=PhotoImage(file="cookie.png")
        #self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=120, width=500, height=400)

        #title & sub
        title=Label(Frame_login, text='Sign in', font=("Calibri",35,"bold"), fg="orange", bg="white").place(x=90, y=30)
        subtitle=Label(Frame_login, text='Hey there! Nice to see you.', font=("Comic Sans MS",13,"bold"), fg="brown", bg="white").place(x=90, y=100)
        
        #username
        lbl_user=Label(Frame_login, text='Username', font=("Comic Sans MS",10,"bold"), fg="grey", bg="white").place(x=90, y=140)
        self.username=Entry(Frame_login, font=("Comic Sans MS",15), bg="white")
        self.username.place(x=90,y=170, width=320, height=35)

        #password
        lbl_password=Label(Frame_login, text='Password', font=("Comic Sans MS",10,"bold"), fg="grey", bg="white").place(x=90, y=210)
        self.password=Entry(Frame_login, font=("Comic Sans MS",15), bg="white")
        self.password.config(show="*");
        self.password.place(x=90,y=240, width=320, height=35)

        #Button
        forget = Button(Frame_login, text='forgot password?',bd=0 ,font=("Comic Sans MS",8), fg="grey", bg="white").place(x=90, y=280)

        #Login Button
        submit = Button(Frame_login, text='Sign In',bd=0 ,font=("Comic Sans MS",12), fg="brown", bg="orange").place(x=160, y=320, width=180, height=40)

root = Tk()
obj = Login(root)
root.mainloop()