#Initial code 


from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
from tkinter import filedialog

root = Tk() #To κύριο παράθυρό μας
root.title("Chef's Interface") #Ο τίτλος του παραθύρου
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=20)

my_frame1 = Frame(my_notebook, width=400, height=500, bg="white")
my_frame2 = Frame(my_notebook, width=400, height=500, bg="white")
my_frame3 = Frame(my_notebook, width=400, height=500, bg="white")

my_frame1.grid(row=250, column=498)
my_frame2.grid(row=250, column=499)
my_frame3.grid(row=250, column=500)

my_notebook.add(my_frame1, text="Home")
my_notebook.add(my_frame2, text="My Recipes")
my_notebook.add(my_frame3, text="Settings")


root.mainloop() 