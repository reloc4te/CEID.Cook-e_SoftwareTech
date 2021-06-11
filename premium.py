from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
#import pymysql
import re
# from PIL import ImageTk, Image



root = Tk() #To κύριο παράθυρό μας
root.title("Premium") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
root.resizable(False, False) #Width #Height


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


Label(root, text ="Why go Premium?", font=("Comics Sans MS",20)).pack(pady = 10)  # A Label widget to show in toplevel
    
# root.image = PhotoImage(file = "D:\Users\makis\Documents\CEID\ΤΛ\Project Code\CEID.Cook-e_SoftwareTech\Premium.png")
# # Show image using label
# image = Label( root.root, image = root.image)
# image.place(x = 10,y = 10, width=50, height=50)

def close_win():
    root.destroy()   # close the current window


Button(root, text="Payment Plan", font=('Calibri (Body)',10),command=showPaymentPlanScreen).pack(pady=20)
#Close the window
Button(root, text="Back", font=('Helvetica bold',10),command=close_win).pack(pady=20)


root.mainloop()