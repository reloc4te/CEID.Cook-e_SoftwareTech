from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter import ttk

class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("Login/Sign up System")
        self.root.geometry("800x700")
        self.root.resizable(False,False)
        self.loginform()


    def loginform(self): #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, width=900, height=700)

        # Add image file
        self.bg = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/cookie.png")
        # Show image using label
        bg = Label( self.root, image = self.bg)
        bg.place(x = 0,y = 0, width=800, height=500)

        frame_input=Frame(self.root, bg='white')
        frame_input.place(x=200,y=130,height=450,width=350)

        label1=Label(frame_input,text="Login Here",font=('Calibri',32,'bold'),fg="orange",bg='white')
        label1.place(x=30,y=20)

        label2=Label(frame_input,text="Email",font=("Comics Sans MS",20,),fg='brown',bg='white')
        label2.place(x=30,y=95)

        self.email_txt=Entry(frame_input,font=("Comics Sans MS",15),bg='white')
        self.email_txt.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input,text="Password",font=("Comics Sans MS",20),fg='brown',bg='white')
        label3.place(x=30,y=195)

        self.password=Entry(frame_input,font=("Comics Sans MS",15),bg='white')
        self.password.config(show="*");
        self.password.place(x=30,y=245,width=270,height=35)

        btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
        btn1.place(x=125,y=305)

        btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("Calibri",15),fg="white",bg="orange",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)

        btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
        btn3.place(x=110,y=390)



    def login(self):

      if self.email_txt.get()=="" or self.password.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='texnologia!@logismikou1998',database='pythonlogin')

            cur=con.cursor()

            cur.execute('select * from accounts where email=%s and password=%s',(self.email_txt.get(),self.password.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)

               self.loginclear()

               self.email_txt.focus()

            else:

               #self.appscreen()
               newWindow = Toplevel(self.root)

               # sets the title of the
               # Toplevel widget
               newWindow.title("New Window")
  
               # sets the geometry of toplevel
               newWindow.geometry("200x200")
  
               # A Label widget to show in toplevel
               Label(newWindow, text ="This is a new window").pack()

               self.root.destroy() # close the current window
               self.root = tk.Tk() # create another Tk instance
               self.app = UserProfile(self.root) # create Demo2 window
               self.root.mainloop()
               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)
    


    def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=700)

      self.img=PhotoImage(file="C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/cookie.png")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=800,height=500)

      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=150,y=130,height=450,width=520)

      label1=Label(frame_input2,text="Good to have you on board!",font=('Calibri',32,'bold'), fg="orange",bg='white')
      label1.place(x=5,y=20)


      label2=Label(frame_input2,text="Username",font=("Comics Sans MS",20), fg='brown',bg='white')
      label2.place(x=10,y=95)

      self.entry=Entry(frame_input2,font=("Calibri",15),bg='white')
      self.entry.place(x=10,y=145,width=200,height=35)


      label3=Label(frame_input2,text="Password",font=("Comics Sans MS",20), fg='brown',bg='white')
      label3.place(x=10,y=195)

      self.entry2=Entry(frame_input2,font=("Calibri",15),bg='white')
      self.entry2.config(show="*");
      self.entry2.place(x=10,y=235,width=200,height=35)


      label4=Label(frame_input2,text="Email",font=("Comics Sans MS",20), fg='brown',bg='white')
      label4.place(x=250,y=95)

      self.entry3=Entry(frame_input2,font=("Calibri",15), bg='white')
      self.entry3.place(x=250,y=145,width=200,height=35)


      label5=Label(frame_input2,text="Confirm Password",font=("Comics Sans MS",20),fg='brown',bg='white')
      label5.place(x=250,y=195)

      self.entry4=Entry(frame_input2,font=("Calibri",15),bg='white')
      self.entry4.config(show="*");
      self.entry4.place(x=250,y=235,width=200,height=35)


      btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("Calibri",15),fg="white",bg="orange",bd=0,width=15,height=1)
      btn2.place(x=160,y=340)

      btn3=Button(frame_input2,command=self.loginform, text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=170,y=390)
    

    def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.entry2.get()!=self.entry4.get():
         messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)
      else:
         try:
            con=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
            cur=con.cursor()
            cur.execute("select * from accounts where email=%s",self.entry3.get())
            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
               self.regclear()
               self.entry.focus()

            else:

               cur.execute("insert into accounts values(%s,%s,%s,%s)",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))
               con.commit()
               con.close()

               messagebox.showinfo("Success","Register Succesfull",parent=self.root)
               self.regclear()

         except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


    def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)

    def loginclear(self):
      self.email_txt.delete(0,END)
      self.password.delete(0,END)
     

class UserProfile():

   def __init__(self, root):
        self.root = root
        self.root.title("Login/Sign up System")
        self.root.geometry("370x550")
        self.root.resizable(False,False)
      #   self.Profile()
        self.tabs()
        
        
      #   self.frame = tk.Frame(self.root)
      #   self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
      #   self.quitButton.pack()
      #   self.frame.pack()

   # def Profile(self):
   #    Frame_profile = Frame(self.root, bg="whitesmoke")
   #    Frame_profile.place(x=0, y=0, width=370, height=550)
   #    # tabControl = ttk.Notebook(self.root)
   #    # tab1=ttk.Frame(tabControl)
   #    # tab2=ttk.Frame(tabControl)
   #    # # tab3=ttk.Frame(tabControl)
   #    # # tab4=ttk.Frame(tabControl)

   #    # tabControl.add(tab1, text ='Just for you')
   #    # tabControl.add(tab2, text ='Find a recipe')
   #    # tabControl.add(tab3, text ='Nutritionist')
   #    # tabControl.add(tab4, text ='Mycart')
   #    # Add image file
   #    self.image = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/Cook-e.png")
   #    # Show image using label
   #    image = Label( self.root, image = self.image)
   #    image.place(x = 10,y = 30, width=50, height=50)
   
   def tabs(self):
      #Frame_tabs = Frame(self.root, bg="blue")
      #Frame_tabs.place(x=0, y=80)
      # s = ttk.Style(self.root)
      # notebook = ttk.Notebook(self.root)
      # frame1 = ttk.Frame(self.root, width=1000, height=2000)
      # frame2 = ttk.Frame(self.root)
      # notebook.add(frame1, text="Just for you")
      # ttk.Label(frame1, text ="Welcome to GeeksForGeeks")
      # notebook.add(frame2, text="Find a recipe")
      # s.configure("TNotebook", tabposition='n')
      # notebook.pack()
      #s = ttk.Style(self.root)
      self.image = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/Cook-e.png")
      # Show image using label
      image = Label( self.root, image = self.image)
      image.place(x = 10,y = 10, width=50, height=50)
      
      self.root.title("Tab Widget")
      tabControl = ttk.Notebook(self.root)
  
      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
      tab3 = ttk.Frame(tabControl)
      tab4 = ttk.Frame(tabControl)
  
      tabControl.add(tab1, text ='Just for you')
      tabControl.add(tab2, text ='Find a recipe')
      tabControl.add(tab3, text ='Nutritionist')
      tabControl.add(tab4, text ='Mycart')
      tabControl.place(x=0,y=60,width=500,height=700)
      #s.configure("TNotebook", tabposition='n')
      #tabContro%l.pack(expand = 1, fill ="both")
  
      ttk.Label(tab1, text ="Welcome to GeeksForGeeks").grid(column = 0, row = 0,padx = 30,pady = 30)  
      ttk.Label(tab2,text ="Lets dive into the world of computers").grid(column = 0,row = 0, padx = 30,pady = 30)
      
   def close_windows(self):
      self.root.destroy()



def main(): 
 root = tk.Tk()
 app = Login(root)
 root.mainloop()

if __name__ == '__main__':
   main()
   

     
#root = Tk()
#ob = Login(root)
#root.mainloop()
