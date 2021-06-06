#Initial code 


from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
from tkinter import filedialog

root = Tk() #To κύριο παράθυρό μας
root.title("Chef's Interface") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
#Make the app resizeable
root.resizable(True, True) #Width #Height

# w = 250
# h = 500

# my_canvas = Canvas(root, width=w, height=h, bg="white")
# my_canvas.pack(pady=20)

# img = PhotoImage(file="chef/7.png")
# my_image = my_canvas.create_image(0, 0, anchor=NW, image=img)

# def move(e):
#     global img
#     img = PhotoImage(file="chef/7.png")
#     my_image = my_canvas.create_image(e.x, e.y, image=img)


# my_canvas.bind('<B1-Motion>', move)


my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=50)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="white")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="white")
my_frame3 = Frame(my_notebook, width=500, height=500, bg="white")

my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)
my_frame3.pack(fill="both",expand=1)

my_notebook.add(my_frame1, text="Home")
my_notebook.add(my_frame2, text="My Recipes")
my_notebook.add(my_frame3, text="Settings")

recipesTitle = Label(my_frame2, text="Recipes",borderwidth=10,width=100,bg="#E59A41",fg="white")
recipesTitle.pack()




root.mainloop() 