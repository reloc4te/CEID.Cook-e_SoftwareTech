from calendar import month
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkcalendar import *

import tkinter as tk
from tkinter import ttk




class Nutritionist():


    def __init__(self):

        #root = Tk()

        self.root = root
        self.root.geometry("370x550")
        self.root.resizable(False,False)
        

        self.tabs()
    

    def run(self):
        self.root.mainloop()

   
    



    def tabs(self):
        self.image = PhotoImage(file = "C:/Users/kleas/OneDrive/Έγγραφα/Ceid/8o ΕΞΑΜΗΝΟ/ΤΛ/pytorch-chatbot-master/nutri/Cook-e.png")
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
	tabControl.select(self.tab3)
	
     





        style = ttk.Style()
#Pick a theme
        style.theme_use("default")
# Configure our treeview colors

        style.configure("Treeview", 
	        background="#D3D3D3",
	        foreground="black",
	        rowheight=25,
	        fieldbackground="#D3D3D3"
	        )
# Change selected color
        style.map('Treeview', 
	        background=[('selected', 'blue')])

# Create Treeview Frame
        tree_frame = Frame(root)
        tree_frame.place(x=90,y=120,width=200,height=100)

# Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the screen
        my_tree.pack()

#Configure the scrollbar
        tree_scroll.config(command=my_tree.yview)

# Define Our Columns
        my_tree['columns'] = ("Name","Stars")

# Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Name", anchor=W, width=140)
        my_tree.column("Stars", anchor=CENTER, width=100)


# Create Headings 
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Name", text="Nutritionist", anchor=W)
        my_tree.heading("Stars", text="Stars", anchor=CENTER)


# Add Data
        data = [
	["John", 1, ],
	["Mary", 2],
	["Tim", 3 ],
	["Erin", 4],
	["Bob", 5],
	["Steve", 6],
	["Tina", 7],
	["Mark", 8],
	["John", 1],
	["Mary", 2],
	["Tim", 3],
	["Erin", 4],

]

# Create striped row tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="gold")

        global count
        count=0

        for record in data:
                if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1]), tags=('evenrow',))
                else:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1]), tags=('oddrow',))

                count += 1






       




        # Move Row up
        def up():
                rows = my_tree.selection()
                for row in rows:
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

        # Move Row Down
        def down():
                rows = my_tree.selection()
                for row in reversed(rows):
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)




        

        


        


        #Calendar
        cal=Calendar(root, selectmode="day",year=2021,month=6,day=8)
        cal.place(x=30,y=250,width=300,height=200)


        



        def grab_date():
            my_label.config(text=cal.get_date())
        


        my_button = Button(root,text="Submit", command=grab_date)
        my_button.place(x=155,y=500,width=50,height=20)

        my_label = Label(root,text="")
        my_label.pack(pady=20)

        

    



if __name__ == '__main__':
    root = tk.Tk()
    nu=Nutritionist()
   
    nu.run()
   
