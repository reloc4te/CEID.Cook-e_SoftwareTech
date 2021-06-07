from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
from tkinter import filedialog
import pymysql

root = Tk() #To κύριο παράθυρό μας
root.title("Chef's Interface") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
#Make the app resizeable
root.resizable(False, False) #Width #Height

root.img = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-e.png")
#Show image using label
img = Label(root, image = root.img)
img.place(x = 0,y = 10, width=50, height=50)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=100)

def addNewRecipe():
    # Εδώ δημιουργούμε τη συνάρτηση για το add new button και θα μας εμφανίζεται ένα καινούργιο παράθυρο
    # όπου θα υπάρχουν δύο νέα κουμπία για να επιλεχθεί ο τρόπος που θα εισαχθεί η καινούργια συνταγή
    top = Toplevel()
    top.title("Add New Recipe")
    top.geometry("200x120")
    addNewFrame = Label(top, text="Choose your way",borderwidth=5,width=100,bg="#E59A41",fg="white")
    addNewFrame.pack()
    addFromFilesButton = Button(top, text="Add from file",bg="#FAC978",width=20,fg="white",command=openFile)
    addFromFilesButton.pack(pady=10)
    addFromScratch = Button(top, text="Add from scratch",width=20,bg="#FAC978",fg="white")
    addFromScratch.pack()

def openFile():
    # Έχουμε αυτή τη συνάρτηση για να εισάγουμε μια συνταγή απο τα αρχεία του συστήματος του χρήστη
    # Σε περίπτωση που ο χρήστης έχει διαφορετικό initialdir θα πρέπει να αλλαχθεί απο εδώ για να ανοίξει το αρχείο του
    # Στην περίπτωση μας ο έλεγχος του αρχείου θα γίνεται απο τον διαχειριστή της βάσης
    # Αν τα απαραίτητα πεδία έχουν συμπληρωθεί ο διαχειριστής θα εισάγει τα στοιχεία στην βάση, αλλιώς θα τα απορρίπτει.
    filename = filedialog.askopenfilename(initialdir="C:/",title="Select File")


    

class FramesOfTabs:
    def __init__(self,master):
        self.my_frame1 = Frame(master, bg="white")
        self.my_frame2 = Frame(master, bg="white")
        self.my_frame3 = Frame(master, bg="white")

        master.add(self.my_frame1, text="Home")
        master.add(self.my_frame2, text="My Recipes")
        master.add(self.my_frame3, text="Settings")
        master.place(x=0,y=60,width=500,height=500)

        self.my_frame2.img2 = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/7.png")
        # Show image using label
        img2 = Label(self.my_frame2, image = self.my_frame2.img2,bg="white")
        img2.place(x = 1,y = 180, width=180, height=170)

        self.my_frame2.img3 = PhotoImage(file = "C:/Users/Windows/Documents/ΜΑΘΗΜΑΤΑ CEID/Τεχνολογία Λογισμικού/Project_code/CEID.Cook-e_SoftwareTech-1/chef/Cook-eold.png")
        # Show image using label
        img3 = Label(self.my_frame2, image = self.my_frame2.img3,bg="white")
        img3.place(x = 315,y = 180, width=180, height=170)

    def addContent(self):

        def show_recipes():
            searched = self.inputName.get()
            con=pymysql.connect(host="localhost",user="root",password="texnologia!@logismikou1998",database="pythonlogin")
            my_cursor=con.cursor()
            sql = "Select recipe_name from recipes where chef_name=%s"
            name=(searched, )
            result = my_cursor.execute(sql,name)
            result= my_cursor.fetchall()
        
            num=35
            num2=80
            for w in result:
               
                resultLabel = Button(self.my_frame2, text=w,font=("Calibri",12), width=52,bg="white")
                resultLabel.place(x=num,y=num2)
                num2+=30

        # Δημιουργήσαμε το entry kαι το button προκειμένουν να μην χρειαστεί να κάνουμε το log-in και για τον chef.
        # Οπότε παίρνουμε το όνομα του chef για να μπορέσουμε να έχουμε πρόσβαση στην βάση με τις συνταγές του
        # και ο χρήστης για να δεί οτι λειτουργεί αρκεί να γράψει το όνομα του chef όπως το έχουμε δηλώσει στην βάση
        # Μια ενδεικτική τιμή για να εμφανιστούν οι συνταγές ειναι το botrini.Σε περίπτωση που δεν υπάρχει ενα ονομα στην βάση
        # τότε το σύστημα δεν κάνει τίποτα και περιμένει ένα σωστό όνομα για να εμφανίσει τις συνταγές.
        self.inputName = Entry(self.my_frame2,bg="white",borderwidth=5)
        self.inputName.insert(0,"Insert your name")
        self.inputName.place(x=5, y=5)
        self.inputButton = Button(self.my_frame2,text="Show Recipes",bg="#E59A41",borderwidth=3, command=show_recipes)
        self.inputButton.place(x=150,y=5)

        # Εδώ δημιουργούμε το τίτλο για το Recipes pου εμφανίζεται κάτω απο το entry και button
        self.recipesTitle = Label(self.my_frame2, text="Recipes", font=(15),borderwidth=10,width=53,bg="#E59A41",fg="white")
        self.recipesTitle.place(x=0,y=35)

        # Εδώ δημιουργόυμε το κουμπί αdd new όπου μας παραπέμπει να δημιουργήσουμε μια συνταγή απο την αρχή ή μέσω αρχείου
        self.addRecipesButton = Button(self.my_frame2, text="Add New",width=10,bg="#E59A41",command=addNewRecipe,fg="white")
        self.addRecipesButton.place(x=210,y=300) 

        

mainInstance = FramesOfTabs(my_notebook).addContent()


root.mainloop() 