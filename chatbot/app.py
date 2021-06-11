from tkinter import *
from tkinter import messagebox

from chat import get_response, bot_name
from PIL import ImageTk, Image





GOLD="goldenrod"
WHITE= "snow2"
BLACK="gray1"

FONT="Helvetica 14"
FONT_B="Helvetica 12 bold"
#Cookie= PhotoImage("photo.jpg")



class ChatApplication:
    
    def __init__(self):
        self.window=Tk()
        
        self._setup_main_window()

    def run(self):
        self.window.mainloop()



    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=WHITE)

        #head label
        head_label= Label(self.window, bg=GOLD, fg=BLACK, text="Welcome to Cook-e Chatbot", font=FONT_B, pady=10)
        head_label.place(relwidth=1)


        #tiny divider
        line= Label(self.window, width=450, bg=GOLD)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        
        
        
    

        #text widget
        self.text_widget=Text(self.window, width=20, height=2, bg=WHITE, fg=BLACK, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)


        #scroll bar
        scrollbar= Scrollbar(self.text_widget)
        scrollbar.place( relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        #bottom Label

        button_label= Label(self.window, bg=GOLD, height=80)
        button_label.place(relwidth=1,rely=0.825)


        #message box
        self.msg_entry=Entry(button_label, bg=WHITE, fg=BLACK, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, relx=0.011,rely=0.008)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send buttom
        send_button=Button(button_label,text="Send", font=FONT, width=20, bg=GOLD, 
                            command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relwidth=0.22, relheight=0.06)



    def _on_enter_pressed(self,event):
        msg=self.msg_entry.get()
        self._insert_message(msg,"You" )


    
    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0,END)
        msg1=f"{sender}: {msg}\n\n"
        self.text_widget.configure( state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure( state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure( state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure( state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app= ChatApplication()
    app.run()

