import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.HelloButton = tk.Button(self.frame, text = 'Hello', width = 25, command = self.new_window,)
        self.HelloButton.pack()
        self.frame.pack()
    #def close_windows(self):
        #self.master.destroy()
        #self.new_window
    def new_window(self):
        self.master.destroy() # close the current window
        self.master = tk.Tk() # create another Tk instance
        self.app = Demo2(self.master) # create Demo2 window
        self.master.mainloop()


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()







 #  def new_window(self):
   #    self.master.destroy() # close the current window
   #    self.master = tk.Tk() # create another Tk instance
   #    self.app = UserProfile(self.master) # create Demo2 window
   #    self.master.mainloop()

   #  def appscreen(self):
   #    Frame_login=Frame(self.root,bg="white")
   #    Frame_login.place(x=0,y=0,height=700,width=800)
      
   #    btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("Comics Sans MS",8),fg="white",bg="gold",bd=0,width=10,height=1)
   #    btn2.place(x=500,y=10)

   #  def Close(self):
   #      self.root.destroy()

   #  def openNewWindow(self):
     
   #   # Toplevel object which will 
   #   # be treated as a new window
   #   newWindow = Toplevel(root)

   #   # sets the title of the
   #   # Toplevel widget
   #   newWindow.title("New Window")

   #   # sets the geometry of toplevel
   #   newWindow.geometry("200x200")

   #   # A Label widget to show in toplevel
   #   Label(newWindow, text ="This is a new window").pack()
