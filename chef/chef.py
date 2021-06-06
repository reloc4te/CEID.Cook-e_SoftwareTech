from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pymysql 

root = Tk() #To κύριο παράθυρό μας
root.title("Chef's Interface") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
#Make the app resizeable
root.resizable(False, False) #Width #Height


my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=50)

class FramesOfTabs:
    def __init__(self,master):
        self.my_frame1 = Frame(master, width=500, height=500, bg="white")
        self.my_frame2 = Frame(master, width=500, height=500, bg="white")
        self.my_frame3 = Frame(master, width=500, height=500, bg="white")

        self.my_frame1.pack(fill="both",expand=1)
        self.my_frame2.pack(fill="both",expand=1)
        self.my_frame3.pack(fill="both",expand=1)

        master.add(self.my_frame1, text="Home")
        master.add(self.my_frame2, text="My Recipes")
        master.add(self.my_frame3, text="Settings")


class AddContent(FramesOfTabs):
    def addTitle(self):
        self.recipesTitle = Label(self.my_frame2, text="Recipes", font=(15),borderwidth=10,width=100,bg="#E59A41",fg="white")
        self.recipesTitle.pack()

    def displayRecipes(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password = "123451", database = "project_db")
            cur = con.cursor()
            cur.execute("SELECT * FROM recipes WHERE chef_name = botrini")
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


mainInstance = AddContent(my_notebook).addTitle()



root.mainloop() 