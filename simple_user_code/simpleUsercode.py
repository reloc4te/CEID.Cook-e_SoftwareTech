from os import name
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
        self.password.config(show="*")
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
      self.entry2.config(show="*")
      self.entry2.place(x=10,y=235,width=200,height=35)


      label4=Label(frame_input2,text="Email",font=("Comics Sans MS",20), fg='brown',bg='white')
      label4.place(x=250,y=95)

      self.entry3=Entry(frame_input2,font=("Calibri",15), bg='white')
      self.entry3.place(x=250,y=145,width=200,height=35)


      label5=Label(frame_input2,text="Confirm Password",font=("Comics Sans MS",20),fg='brown',bg='white')
      label5.place(x=250,y=195)

      self.entry4=Entry(frame_input2,font=("Calibri",15),bg='white')
      self.entry4.config(show="*")
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
        self.root.title("Your Profile")
        self.root.geometry("370x550")
        self.root.resizable(False,False)
        self.tabs()
        self.showContents()
        self.myCart()


   def tabs(self):
      self.image = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/Cook-e.png")
      # Show image using label
      image = Label( self.root, image = self.image)
      image.place(x = 10,y = 10, width=50, height=50)
      
      self.root.title("Your Profile")
      tabControl = ttk.Notebook(self.root)
       
      self.tab1 = Frame(tabControl,bg="white")
      self.tab2 = Frame(tabControl,bg="white")
      self.tab3 = Frame(tabControl,bg="white")
      self.tab4 = Frame(tabControl,bg="white")
  
      tabControl.add(self.tab1, text ='Just for you')
      tabControl.add(self.tab2, text ='Find a recipe')
      tabControl.add(self.tab3, text ='Nutritionist')
      tabControl.add(self.tab4, text ='Mycart')
      tabControl.place(x=0,y=60,width=500,height=700)
      #s.configure("TNotebook", tabposition='n')
      #tabControl.pack(expand = 1, fill ="both")
       

    #TAB "JUST FOR YOU" 
      ttk.Label(self.tab1, text ="Week's Recipe!",background="orange",width=90).grid(column = 0, row = 0)
      
      self.tab1.img2 = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/food.png")
      # Show image using label
      img2 = Label( self.tab1, image = self.tab1.img2)
      img2.place(x =0,y =20, width=400, height=80)

      con=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
      self.my_cursor=con.cursor()
      sql = "Select recipe_name from recipes order by rand() limit 1"
      result = self.my_cursor.execute(sql)
      result=self.my_cursor.fetchall()
      sql2 = "Select chef_name from recipes where recipe_name=%s "
      recipe_name=(result, )
      result2 = self.my_cursor.execute(sql2, recipe_name)
      result2=self.my_cursor.fetchall()
      sql3 = "Select your_instructions from recipes where recipe_name=%s "
      result3 = self.my_cursor.execute(sql3,recipe_name)
      result3=self.my_cursor.fetchall()


      #Μορφοποίηση αποτελεσμάτων

       #Ονομα συνατγής retrieved from database
      recipeName = Label(self.tab1, text="Your week's recipe is:",font=("Calibri",20,'bold'), fg="orange", bg="white")
      recipeName.place(x=0, y=100)
      searched_result = Label(self.tab1, text=result,background="white",font=('Calibri',15),fg="brown")
      searched_result.place(x=255, y=105)

       #Όνομα chef της retrieved συνταγής 
      chefName = Label(self.tab1, text="Inspired by:",font=("Calibri",15,'bold'), fg="orange", bg="white")
      chefName.place(x=0, y=130)
      searched_result2 = Label(self.tab1, text=result2,background="white",font=('Calibri',12),fg="brown")
      searched_result2.place(x=110, y=133)

       #Οδηγίες εκτέλεσης της retrieved συνταγής 
      instructions = Label(self.tab1, text="Instructions for you",font=("Calibri",20,'bold','underline'), fg="orange", bg="white")
      instructions.place(x=60, y=155)
      searched_result3 = Label(self.tab1, text=result3,background="white",font=('Calibri',12),fg="brown")
      searched_result3.place(x=0, y=200)

   #TAB "FIND A RECIPE"
   
   def showresults(self):
      Frame_recipe2 = Frame(self.tab2, bg="white")
      Frame_recipe2.place(x=0, y=0, width=370, height=550)

      self.tab2.img7 = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/7.png")
      # Show image using label
      img7 = Label( self.tab2, image = self.tab2.img7, bg="white")
      img7.place(x=0, y=200, width=180, height=170)

      selectedCW = self.dropCW.get()
      selectedmeal = self.dropmeal.get()
      selectedveg = self.dropveg.get()
      selectedmeat = self.dropmeat.get()
      selecteddairy = self.dropdairy.get()
      selectedfruit = self.dropfruit.get()
      # selectedothers = self.dropothers.get()

      if selectedCW == "Cookware..." :
         messagebox.showerror(title="Error", message="Cookware must be filled ")
      elif selecteddairy == "Dairy.." or selectedveg=="Vegetables.." or selectedmeat=="Meat-Chicken-Seafood.." or selectedfruit=="Fruit..":
         messagebox.showerror(title="Error", message="Ingridients must be filled ")
      elif  selectedCW == "Cookware..." and selecteddairy == "Dairy.." and selectedveg=="Vegetables.." and selectedmeat=="Meat-Chicken-Seafood.." and selectedfruit=="Fruit..":
         messagebox.showerror(title="Error", message="Cookware and ingridients are not optional!")




      sqlrecipe = "Select recipe_name from recipes where cookware=%s and type_of_meal=%s and vegetables=%s and meat=%s and dairy=%s and fruit=%s" # and others=%s"
      cookWare= (selectedCW, )
      meal = (selectedmeal, )
      veg = (selectedveg, )
      meat = (selectedmeat, )
      dairy = (selecteddairy, )
      fruit = (selectedfruit, )
      # others = (selectedothers, )

      self.resultrecipe = self.my_cursor.execute(sqlrecipe, (cookWare, meal,veg, meat, dairy, fruit))#, others))
      self.resultrecipe = self.my_cursor.fetchall()

      if not self.resultrecipe:
         messagebox.showerror(title="Error",message="No such recipe")
         back = Button(self.tab2,text="Back...",command=self.showContents,cursor="hand2",font=("Calibri",15),fg="white",bg="orange",bd=0,width=10)
         back.place(x=130, y=120)
      else:
         label2 = Label(self.tab2, text="Recipes found for you...", bg="white", font=("calibri",20,"bold"), fg="orange" )
         label2.place(x=40 , y=10)
         num=84
         # global i
         button = {}
         for i in self.resultrecipe:
            def action(x=i):
               return self.text_updation(x)
            
            button[i] = Button(self.tab2, text=i, command=action, width=39, height=1, font=("Calibri",12), bg='orange', fg="black")
            button[i].place(x=20,y=num)
            num+=35

         goBack3 = Button(self.tab2, text="Go Back", command=self.showContents, cursor="hand2",bg="orange",fg="white",font=("Calibri",12),borderwidth=3)
         goBack3.place(x=140,y=300)



   def text_updation(self,info):

      frame3 = Frame(self.tab2, bg="white")
      frame3.place(x=0,y=0,height=370,width=550)
      self.tab2.img6 = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/7.png")
      # Show image using label
      img6 = Label( self.tab2, image = self.tab2.img6, bg="white")
      img6.place(x=0, y=200, width=180, height=170)

      self.tab2.img5 = PhotoImage(file = "C:/Users/Marianna/Desktop/CEID/Τεχνολογία Λογισμικού/project_Code/CEID.Cook-e_SoftwareTech-1/simple_user_code/Cook-eold.png")
      # Show image using label
      img5 = Label( self.tab2, image = self.tab2.img5, bg="white")
      img5.place(x=200, y=300, width=180, height=170)

      recName = info[0]

      con2=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
      self.my_cursor2=con2.cursor()
      sql2 = "Select your_instructions from recipes where recipe_name=%s "

      namerec = (recName, )
      result2 = self.my_cursor2.execute(sql2, namerec)
      result2=self.my_cursor2.fetchall()

      searched_label = Label(self.tab2, text="Here's your instructions!",background="white",font=('Calibri',20,"bold"),fg="brown")
      searched_label.place(x=0, y=10)
      searched_label2 = Label(self.tab2, text="Enjoy cooking!",background="white",font=('Calibri',15),fg="brown")
      searched_label2.place(x=0, y=43)
      searched_result2 = Label(self.tab2, text=result2,background="white",font=('Calibri',15),fg="brown")
      searched_result2.place(x=0, y=80)



      # self.labletext = Label(self.tab2, text=info[0], bg="#E59A41",fg="black",width=22,borderwidth=3,height=1)
      # self.labletext.place(x=45,y=100)

      goBack2 = Button(self.tab2, text="Go Back", command=self.showresults, bg="orange",fg="white",font=("Calibri",12),borderwidth=3)
      goBack2.place(x=150,y=300)
      
            
   def showContents(self):

      Frame_recipe = Frame(self.tab2, bg="#FFEE8E")
      Frame_recipe.place(x=0, y=0, width=370, height=550)

      ttk.Label(self.tab2, text ="Let's find you something to cook..",background="orange",width=90,font=(20),padding=5).grid(column = 0, row = 0)


      #Drop down box for search: cookware 
      labelCW = Label(self.tab2,text="Cookware",background="DarkGoldenrod1",font=("Calibri",15),width=38)
      labelCW.place(x=0,y=35)
      self.dropCW = ttk.Combobox(self.tab2, values=["Cookware...","pot","pan","stock-pot","grill-pan","casserole","baking-sheet"],width=58)
      self.dropCW.current(0)
      self.dropCW.place(x=0, y=68)

      #Drop down box for search: type of meal 
      labelmeal = Label(self.tab2,text="Type of meal",background="DarkGoldenrod1",font=("Calibri",15),width=38)
      labelmeal.place(x=0,y=97)
      self.dropmeal = ttk.Combobox(self.tab2, values=["Type of meal...","breakfast","branch","lunch","snack","dinner"],width=58)
      self.dropmeal.current(0)
      self.dropmeal.place(x=0, y=130)

      #Drop down box for search: ingredients
      labelingr = Label(self.tab2,text="Ingridients",background="DarkGoldenrod1",font=("Calibri",15),width=38)
      labelingr.place(x=0,y=160)
      self.dropveg = ttk.Combobox(self.tab2, values=["Vegetables..","cabbage","tomato","cucumber","potato","carrot"],width=58)
      self.dropveg.current(0)
      self.dropveg.place(x=0, y=194)

      self.dropmeat = ttk.Combobox(self.tab2, values=["Meat-Chicken-Seafood..","chicken","lamb","beef","pork","shrimps","tuna"],width=58)
      self.dropmeat.current(0)
      self.dropmeat.place(x=0, y=220)

      self.dropdairy = ttk.Combobox(self.tab2, values=["Dairy..","milk","cheese","yoghurt","butter","soft-cheese"],width=58)
      self.dropdairy.current(0)
      self.dropdairy.place(x=0, y=245)

      self.dropfruit = ttk.Combobox(self.tab2, values=["Fruit..","apple","banana","strawberry","avocado","peach"],width=58)
      self.dropfruit.current(0)
      self.dropfruit.place(x=0, y=270)

      # self.dropothers = ttk.Combobox(self.tab2, values=["Others..","gluten-free","dairy-free"],width=58)
      # self.dropothers.current(0)
      # self.dropothers.place(x=0, y=295)

      searchRecipe = Button(self.tab2,text="Search..",command=self.showresults,cursor="hand2",font=("Calibri",15),fg="white",bg="orange",bd=0,width=10)
      searchRecipe.place(x=130, y=330)
   
   def myCart(self):
      Frame_cart = Frame(self.tab4,bg="#FFEE8E")
      Frame_cart.place(x=0, y=0, width=370, height=550)

      cartLabel = Label(self.tab4,text="Choose a store",bg="orange",fg="white",width=46,height=2,font=("Calibri",12))
      cartLabel.place(x=0,y=1)

      # Δημιουργώ drop-down menu για την εύρεση καταστήματος
      dropStore = ttk.Combobox(self.tab4,values=["Search...","ΣουπερΜαρκετ1","ΣουπερΜάρκετ2","ΣουπερΜαρκετ3","ΣουπερΜαρκετ4","ΣουπερΜαρκετ5"],width=43,font=("Calibri",12),foreground="black",background="white")
      dropStore.current(0)
      dropStore.place(x=0,y=46) 

      cartLabel2 = Label(self.tab4,text="Add to your cart",bg="orange",fg="white",width=46,height=2,font=("Calibri",12))
      cartLabel2.place(x=0,y=73)

      # Δημιουργώ το Drop-down για το vegetables
      dropMeal = ttk.Combobox(self.tab4,values=["Vegetables..","cabbage","tomato","cucumber","potato","carrot"],width=43,font=("Calibri",12),foreground="black",background="white")
      dropMeal.current(0)
      dropMeal.place(x=0,y=118)

      # Δημιουργώ το Drop-down για το Meat-chicken-seafood
      dropMeal = ttk.Combobox(self.tab4,values=["Meat-Chicken-Seafood..","chicken","lamb","beef","pork","shrimps","tuna"],width=43,font=("Calibri",12),foreground="black",background="white")
      dropMeal.current(0)
      dropMeal.place(x=0,y=145)

      # Δημιουργώ το Drop-down για το Dairy
      dropMeal = ttk.Combobox(self.tab4,values=["Dairy..","milk","cheese","yoghurt","butter","soft-cheese"],width=43,font=("Calibri",12),foreground="black",background="white")
      dropMeal.current(0)
      dropMeal.place(x=0,y=172)

      # Δημιουργώ το Drop-down για το Fruits
      dropMeal = ttk.Combobox(self.tab4,values=["Fruit..","apple","banana","strawberry","avocado","peach"],width=43,font=("Calibri",12),foreground="black",background="white")
      dropMeal.current(0)
      dropMeal.place(x=0,y=198)

      checkoutButton = Button(self.tab4,text="Checkout",bg="orange",fg="white",width=10,font=("Calibri",12),command=self.checkout)
      checkoutButton.place(x=130,y=280)

   def checkout(self):
      # Εδώ δημιουργούμε τη συνάρτηση για το add new button και θα μας εμφανίζεται ένα καινούργιο παράθυρο
      # όπου θα υπάρχουν δύο νέα κουμπία για να επιλεχθεί ο τρόπος που θα εισαχθεί η καινούργια συνταγή
      self.top = Toplevel()
      self.top.title("Checkout")
      self.top.geometry("200x140")
      addNewFrame = Label(self.top, text="Choose your payment method",borderwidth=5,width=100,bg="orange",fg="black",font=("Calibri",12))
      addNewFrame.pack()
      addFromFilesButton = Button(self.top, text="With Credit Card..",bg="orange",width=20,fg="black",font=("Calibri",12),command=self.payCredit)
      addFromFilesButton.pack(pady=10)
      addFromScratch = Button(self.top, text="PayPal..",width=20,bg="orange",fg="black",font=("Calibri",12))
      addFromScratch.pack()
    
   def payCredit(self):

        self.top.destroy() 
        self.new = Toplevel()
        self.new.title("Pay with credit..")
        self.new.geometry("370x550")
        self.new.resizable(False,False)
      

        Frame_credit = Frame(self.new,bg="#FFEE8E")
        Frame_credit.place(x=0, y=0, width=370, height=550)

        labelcardholdersName = Label(self.new, text="CARDHOLDERS NAME" ,bg="orange",fg="white",font=("Calibri",15), width=30)
        labelcardholdersName.place(x=10,y=30)

        labelcardNameEntry = Entry(self.new,font=("Calibri",15) )
        labelcardNameEntry.place(x=10 , y=70, width=300, height=25)

        labelcardNumber = Label(self.new, text="CARD NUMBER" ,bg="orange",fg="white",font=("Calibri",15), width=30)
        labelcardNumber.place(x=10,y=110)

        labelcardNumberEntry = Entry(self.new,bg="white",font=("Calibri",15), width=30 )
        labelcardNumberEntry.place(x=10 , y=150, width=300, height=30)

        labelcardExpirationDate = Label(self.new, text="EXPERATION DATE" ,bg="orange",fg="white",font=("Calibri",15))
        labelcardExpirationDate.place(x=10,y=190)

        labelcardExpirationDateEntry= ttk.Combobox(self.new,values=["January","February","March","April","May","June","July","August","September","October","November","December"])
        labelcardExpirationDateEntry.place(x=10 , y=230, width=100, height=30)

        labelcardExpirationEntry= ttk.Combobox(self.new, values=["2021","2022","2023","2024","2025","2026","2027","2028"] )
        labelcardExpirationEntry.place(x=120 , y=230, width=70, height=30)

        labelcardCVVCVC = Label(self.new, text="CVV/CVC" ,bg="orange",fg="white",font=("Calibri",15))
        labelcardCVVCVC.place(x=10,y=270)

        labelcardCVVCVCEntry = Entry(self.new,bg="white",font=("Calibri",15), width=30 )
        labelcardCVVCVCEntry.place(x=10 , y=310, width=60, height=30)

        completePayment = Button(self.new, text="Complete Payment",width=20,bg="orange",fg="white",font=("Calibri",14))
        completePayment.place(x=70, y=360)

   def close_windows(self):
      self.root.destroy()

def main(): 
 root = tk.Tk()
 app = Login(root)
 root.mainloop()

if __name__ == '__main__':
   main()
   
