from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pymysql

    
class Chef:
    def __init__(self,root):
        self.root = root
        self.root.title("Chef's Interface") #Ο τίτλος του παραθύρου
        self.root.geometry("500x500") #H διάσταστη του παραθύρου
        #Make the app resizeable
        self.root.resizable(False, False) #Width #Height
        self.createFrames()
        self.addContent()

    def createFrames(self):
        self.root.img = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-e.png")
        #Show image using label
        img = Label(self.root, image = self.root.img)
        img.place(x = 0,y = 10, width=50, height=50)
        my_notebook = ttk.Notebook(self.root)
        my_notebook.pack(pady=100)

        self.my_frame1 = Frame(my_notebook, bg="white")
        self.my_frame2 = Frame(my_notebook, bg="white")
        self.my_frame3 = Frame(my_notebook, bg="white")

        my_notebook.add(self.my_frame1, text="Home")
        my_notebook.add(self.my_frame2, text="My Recipes")
        my_notebook.add(self.my_frame3, text="Settings")
        my_notebook.place(x=0,y=60,width=500,height=500)

        self.my_frame2.img2 = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/7.png")
        # Show image using label
        img2 = Label(self.my_frame2, image = self.my_frame2.img2,bg="white")
        img2.place(x = 1,y = 180, width=180, height=170)

        self.my_frame2.img3 = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-eold.png")
        # Show image using label
        img3 = Label(self.my_frame2, image = self.my_frame2.img3,bg="white")
        img3.place(x = 315,y = 180, width=180, height=170)
    
    
    def addContent(self):

        # Δημιουργήσαμε το entry kαι το button προκειμένουν να μην χρειαστεί να κάνουμε το log-in και για τον chef.
        # Οπότε παίρνουμε το όνομα του chef για να μπορέσουμε να έχουμε πρόσβαση στην βάση με τις συνταγές του
        # και ο χρήστης για να δεί οτι λειτουργεί αρκεί να γράψει το όνομα του chef όπως το έχουμε δηλώσει στην βάση
        # Μια ενδεικτική τιμή για να εμφανιστούν οι συνταγές ειναι το botrini.Σε περίπτωση που δεν υπάρχει ενα ονομα στην βάση
        # τότε το σύστημα δεν κάνει τίποτα και περιμένει ένα σωστό όνομα για να εμφανίσει τις συνταγές.
        self.inputName = Entry(self.my_frame2,bg="white",borderwidth=5)
        self.inputName.insert(0,"Insert your name")
        self.inputName.place(x=5, y=5)
        self.inputButton = Button(self.my_frame2,text="Show Recipes",bg="#E59A41",borderwidth=3, command=self.show_recipes)
        self.inputButton.place(x=150,y=5)

        # Εδώ δημιουργούμε το τίτλο για το Recipes pου εμφανίζεται κάτω απο το entry και button
        self.recipesTitle = Label(self.my_frame2, text="Recipes", font=(15),borderwidth=10,width=44,bg="#E59A41",fg="white")
        self.recipesTitle.place(x=0,y=35)

        # Εδώ δημιουργόυμε το κουμπί αdd new όπου μας παραπέμπει να δημιουργήσουμε μια συνταγή απο την αρχή ή μέσω αρχείου
        self.addRecipesButton = Button(self.my_frame2, text="Add New",width=10,bg="#E59A41",command=self.addNewRecipe,fg="white")
        self.addRecipesButton.place(x=210,y=300) 

    def addNewRecipe(self):
        # Εδώ δημιουργούμε τη συνάρτηση για το add new button και θα μας εμφανίζεται ένα καινούργιο παράθυρο
        # όπου θα υπάρχουν δύο νέα κουμπία για να επιλεχθεί ο τρόπος που θα εισαχθεί η καινούργια συνταγή
        self.top = Toplevel()
        self.top.title("Add New Recipe")
        self.top.geometry("200x120")
        addNewFrame = Label(self.top, text="Choose your way",borderwidth=5,width=100,bg="#E59A41",fg="white")
        addNewFrame.pack()
        addFromFilesButton = Button(self.top, text="Add from file",bg="#FAC978",width=20,fg="white",command=self.openFile)
        addFromFilesButton.pack(pady=10)
        addFromScratch = Button(self.top, text="Add from scratch",width=20,bg="#FAC978",fg="white",command=self.createByScratch)
        addFromScratch.pack()

    def openFile(self):
        # Έχουμε αυτή τη συνάρτηση για να εισάγουμε μια συνταγή απο τα αρχεία του συστήματος του χρήστη
        # Σε περίπτωση που ο χρήστης έχει διαφορετικό initialdir θα πρέπει να αλλαχθεί απο εδώ για να ανοίξει το αρχείο του
        # Στην περίπτωση μας ο έλεγχος του αρχείου θα γίνεται απο τον διαχειριστή της βάσης
        # Αν τα απαραίτητα πεδία έχουν συμπληρωθεί ο διαχειριστής θα εισάγει τα στοιχεία στην βάση, αλλιώς θα τα απορρίπτει.
        filename = filedialog.askopenfilename(initialdir="C:/",title="Select File")
    
    def createByScratch(self):
        self.top.destroy() 
        self.root.destroy()
        self.root = tk.Tk()
        self.mainInstance = CreateRecipe(self.root)
        self.root.mainloop()
        

    def show_recipes(self):
        searched = self.inputName.get()
        con=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
        my_cursor=con.cursor()
        sql = "Select recipe_name from recipes where chef_name=%s"
        name=(searched, )
        result = my_cursor.execute(sql,name)
        result= my_cursor.fetchall()
        if not result:
            messagebox.showerror("Error","This chef doesn't exist, please select another one")
        else:
            num=35
            num2=80
            for w in result:
                
                resultLabel = Button(self.my_frame2, text=w,font=("Calibri",12), width=52,bg="white")
                resultLabel.place(x=num,y=num2)
                num2+=30
            

class CreateRecipe:
    def __init__(self,root):
        self.root = root
        self.root.title("Chef's Interface") #Ο τίτλος του παραθύρου
        self.root.geometry("500x500") #H διάσταστη του παραθύρου
        #Make the app resizeable
        self.root.resizable(False, False) #Width #Height
        self.createFrames()
        self.createDrop()
    
    def createFrames(self):
        self.root.img = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-e.png")
        #Show image using label
        img = Label(self.root, image = self.root.img)
        img.place(x = 0,y = 10, width=50, height=50)
        my_notebook = ttk.Notebook(self.root)
        my_notebook.pack(pady=100)

        self.my_frame1 = Frame(my_notebook, bg="white")
        self.my_frame2 = Frame(my_notebook, bg="#FFEE8E")
        self.my_frame3 = Frame(my_notebook, bg="white")
        
        my_notebook.add(self.my_frame1, text="Home")
        my_notebook.add(self.my_frame2, text="My Recipes")
        my_notebook.add(self.my_frame3, text="Settings")
        my_notebook.place(x=0,y=60,width=500,height=500)

        my_notebook.select(self.my_frame2) # Χρησιμοποιώ αυτή τη γραμμή κώδικα ώστε το νέο παράθυρο να ανοίξει στο frame2 δηλαδή το frame του My Recipes
    
    def createDrop(self):
        # Δημιουργώ το Entry για να πληκτρολογεί ο chef το όνομα της συνταγής
        inputName = Entry(self.my_frame2,font=("Calibri",12),bg="#E59A41",width=62,borderwidth=5,fg="white")
        inputName.insert(0,"Choose a name for your recipe:")
        inputName.place(x=0,y=0)

        # Δημιουργώ το Label για το cookware
        inputCookware = Label(self.my_frame2,text="Choose cookware", font=("Calibri",12),bg="#E59A41",fg="white",width=62,borderwidth=3)
        inputCookware.place(x=0,y=40)

        # Δημιουργώ το Drop-down για το cookware
        dropCW = ttk.Combobox(self.my_frame2,values=["Search...","pot","pan","stock-pot","grill-pan","casserole","baking-sheet"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropCW.current(0)
        dropCW.place(x=0,y=70)

        # Δημιουργώ το Label για το type of meal
        inputMeal = Label(self.my_frame2,text="Choose type of meal", font=("Calibri",12),bg="#E59A41",fg="white",width=62,borderwidth=3)
        inputMeal.place(x=0,y=100)

        # Δημιουργώ το Drop-down για το type of meal
        dropMeal = ttk.Combobox(self.my_frame2,values=["Search...","breakfast","branch","lunch","snack","dinner"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropMeal.current(0)
        dropMeal.place(x=0,y=130)

        # Δημιουργώ το Label για το ingridients
        inputMeal = Label(self.my_frame2,text="Choose ingridients", font=("Calibri",12),bg="#E59A41",fg="white",width=62,borderwidth=3)
        inputMeal.place(x=0,y=160)

        # Δημιουργώ το Drop-down για το vegetables
        dropMeal = ttk.Combobox(self.my_frame2,values=["Vegetables..","cabbage","tomato","cucumber","potato","carrot"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropMeal.current(0)
        dropMeal.place(x=0,y=190)

        # Δημιουργώ το Drop-down για το Meat-chicken-seafood
        dropMeal = ttk.Combobox(self.my_frame2,values=["Meat-Chicken-Seafood..","chicken","lamb","beef","pork","shrimps","tuna"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropMeal.current(0)
        dropMeal.place(x=0,y=220)
        
        # Δημιουργώ το Drop-down για το Dairy
        dropMeal = ttk.Combobox(self.my_frame2,values=["Dairy..","milk","cheese","yoghurt","butter","soft-cheese"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropMeal.current(0)
        dropMeal.place(x=0,y=250)

        # Δημιουργώ το Drop-down για το Fruits
        dropMeal = ttk.Combobox(self.my_frame2,values=["Fruit..","apple","banana","strawberry","avocado","peach"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropMeal.current(0)
        dropMeal.place(x=0,y=280)

        # Δημιουργώ το Drop-down για το Others
        dropMeal = ttk.Combobox(self.my_frame2,values=["Others..","gluten-free","dairy-free"],width=59,font=("Calibri",12),foreground="black",background="white")
        dropMeal.current(0)
        dropMeal.place(x=0,y=310)

        # Δημιουργώ κουμπί που θα λειτουργεί σαν swipe left

        swipeLeft = Button(self.my_frame2,text="Swipe Left",bg="#E59A41",fg="white",borderwidth=2,command=self.swipe)
        swipeLeft.place(x=210,y=360)

    def swipe(self):
        self.new = Toplevel()
        self.new.title("Add New Recipe")
        self.new.geometry("500x500")
        self.new.img = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-e.png")
        #Show image using label
        img = Label(self.new, image = self.new.img)
        img.place(x = 0,y = 10, width=50, height=50)
        my_notebook = ttk.Notebook(self.new)
        my_notebook.pack(pady=100)

        self.my_frame1 = Frame(my_notebook, bg="white")
        self.my_frame2 = Frame(my_notebook, bg="#FFEE8E")
        self.my_frame3 = Frame(my_notebook, bg="white")
        
        my_notebook.add(self.my_frame1, text="Home")
        my_notebook.add(self.my_frame2, text="My Recipes")
        my_notebook.add(self.my_frame3, text="Settings")
        my_notebook.place(x=0,y=60,width=500,height=500)

        my_notebook.select(self.my_frame2) # Χρησιμοποιώ αυτή τη γραμμή κώδικα ώστε το νέο παράθυρο να ανοίξει στο frame2 δηλαδή το frame του My Recipes
    
        # Δημιουργώ το Label για το image
        inputImage = Label(self.my_frame2,text="Select an image for your recipe", font=("Calibri",12),bg="#E59A41",fg="white",width=62,borderwidth=3)
        inputImage.place(x=0,y=0)

        # Δημιουργώ κουμπί για το upload image from system
        systemImageButton = Button(self.my_frame2,text="Upload image from system",bg="white",width=40,fg="black",borderwidth=2,command=self.systemImage)
        systemImageButton.place(x=0,y=30)

        # Δημιουργώ κουμπί για το upload image from cooke's ideas
        systemImageButton = Button(self.my_frame2,text="Upload image from from cooke's ideas",bg="white",width=40,fg="black",borderwidth=2)
        systemImageButton.place(x=0,y=60)

        # Δημιουργώ το πεδίο που θα εμφανίζεται η εικόνα
        self.my_frame2.img4 = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-e.png")
        img4 = Label(self.my_frame2, image = self.my_frame2.img4,bg="grey")
        img4.place(x = 320,y = 30,width=150,height=150)

        # Δημιουργώ το Label για το Instructions
        inputInst = Label(self.my_frame2,text="Your Instructions", font=("Calibri",12),bg="#E59A41",fg="white",width=62,borderwidth=3)
        inputInst.place(x=0,y=200)

        # Δημιουργώ Entry για τα σχόλια
        comments = Entry(self.my_frame2,font=("Calibri",12),bg="white",fg="black",width=61,borderwidth=3)
        comments.insert(0,"Write your comments is this section")
        comments.place(x=0,y=230,height=120)

        # Δημιουργώ κουμπί για το upload 
        systemImageButton = Button(self.my_frame2,text="Upload",bg="white",background="#E59A41",fg="white",borderwidth=2)
        systemImageButton.place(x=220,y=370)

    def systemImage(self):
        filename2 = filedialog.askopenfilename(initialdir="C:/",title="Select Image")

    




def main(): 
 root = tk.Tk()
 mainInstance = Chef(root)
 root.mainloop()

if __name__ == '__main__':
   main()

