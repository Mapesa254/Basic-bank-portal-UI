#----By Benjamin Mapesa(Mapesa254)----
#The first page for the portal
#Using Object Oriented Programming

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image , ImageTk


class Login_page(Tk) :
    #Declaring the Login_page attributes that are not widgets
    def __init__(self) -> None:
        super().__init__()
        self.title('Page 1(Login)')
        self.geometry('360x640')
        self.config(bg='cyan')
        img = Image.open('Profile.jpeg').resize((100,100))
        self.photo = ImageTk.PhotoImage(image=img)
       
        self.widgets()
        self.structure()

    def widgets(self) :   
        #Creating the widgets in the page
        self.profile_label = Label(self, image=self.photo, border=None, background='cyan')
        self.instructions_label = Label(self, text='Enter your details in the provided fields below' ,foreground='purple', background='cyan', font=('Times ', '10'))
        self.account_number = ttk.Entry(self, width=40 )
        self.password = ttk.Entry(self, width=40, )
        
        self.login_button = Button(self, text='LOGIN', command=self.login)
        self.in_entry_words()
        
    def structure(self) :
        #Positioning the page contents
        self.profile_label.place(x=130, y=20)
        self.instructions_label.place(x=20, y=150)
        self.account_number.place(x=50, y=200)
        self.password.place(x=50, y=250)
        self.login_button.place(x=130, y=300)
    
    #Function to insert More information in the entry widgets
    def in_entry_words(self, *args) :
        self.account_number.insert(0,'Account number')
        self.password.insert(0,'Password')
        self.bind()

    #Functions to remove information from entry widget when clicked
    def click(self, *args) :
        self.account_number.delete(0, 'end')
        self.bind()
    
    def click2(self, *args) :
        self.password.delete(0, 'end')
        self.bind()
        
    #Functions to add the contents again when the widgets unclicked
    def leave(self, *args) :
        self.account_number.insert(0,'Account Number')
        #self.focus()
        self.bind()

    def leave2(self, *args) :
        self.password.insert(0,'Password')
        #self.focus()
        self.bind()    
    
    #Function to bind the click actions to perfom the FocusIn FocusOut    
    def bind(self, *args) :
        self.account_number.bind('<FocusIn>', self.click)
        self.account_number.bind('<FocusOut>', self.leave)
        self.password.bind('<FocusIn>', self.click2)
        self.password.bind('<FocusOut>', self.leave2)      

    #Function to execute commands depending on the entry contents when login_button is pressed
    def login(self) :
        account_number = self.account_number.get()
        password = self.password.get()

        if account_number == '12345678' and password == 'mypass254' :
            messagebox.showinfo('Success','Login successful')
        else :
            messagebox.showerror('Error', 'Invalid account number or password')  


login_page = Login_page()
login_page.mainloop()