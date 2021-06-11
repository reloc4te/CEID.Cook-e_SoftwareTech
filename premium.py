from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
#import pymysql
import re
from PIL import ImageTk, Image



root = Tk() #To κύριο παράθυρό μας
root.title("Premium") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
root.resizable(False, False) #Width #Height
root.tabs()
root.showContents()
root.myCart()


def tabs(self):
    self.root.title("Your Profile")
    tabControl = ttk.Notebook(self.root)
       
    self.tab1 = Frame(tabControl,bg="white")
    self.tab2 = Frame(tabControl,bg="white")
    self.tab3 = Frame(tabControl,bg="white")
    self.tab4 = Frame(tabControl,bg="white")
    self.tab5 = Frame(tabControl,bg="white")
  
    tabControl.add(self.tab1, text ='Just for you')
    tabControl.add(self.tab2, text ='Find a recipe')
    tabControl.add(self.tab3, text ='Nutritionist')
    tabControl.add(self.tab4, text ='Mycart')
    tabControl.add(self.tab5, text ='Premium')
    tabControl.place(x=0,y=60,width=500,height=700)
    #s.configure("TNotebook", tabposition='n')
    #tabControl.pack(expand = 1, fill ="both")

def showPremiumScreen(self):
    Frame_recipe2 = Frame(self.tab2, bg="white")
    Frame_recipe2.place(x=0, y=0, width=370, height=550)
    
    img = ImageTk.PhotoImage(Image.open("D:\Users\makis\Documents\CEID\ΤΛ\Project Code\CEID.Cook-e_SoftwareTech\Premium.png"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

def showPaymentPlanScreen():

    PaymentPlanScreen = Toplevel(root)   # Toplevel object which will be treated as a new window
    PaymentPlanScreen.title("Payment Plan Screen")   # sets the title of the Toplevel widget
    PaymentPlanScreen.geometry("500x500")

    Label(PaymentPlanScreen, text ="Why go Premium?", font=("Comics Sans MS",20)).pack(pady = 10)  # A Label widget to show in toplevel
    
def showPaymentScreen():

    PaymentScreen = Toplevel(root)   # Toplevel object which will be treated as a new window
    PaymentScreen.title("Payment Screen")   # sets the title of the Toplevel widget
    PaymentScreen.geometry("500x500")

    Label(PaymentScreen, text ="Username Settings", font=("Comics Sans MS",20)).pack(pady = 10)  # A Label widget to show in toplevel


def showCreditCardScreen():

    CreditCardScreen = Toplevel(root)   # Toplevel object which will be treated as a new window
    CreditCardScreen.title("Credit Card Screen")   # sets the title of the Toplevel widget
    CreditCardScreen.geometry("500x500")

    Label(CreditCardScreen, text ="Username Settings", font=("Comics Sans MS",20)).pack(pady = 10)  # A Label widget to show in toplevel


















root.mainloop()