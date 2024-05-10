#----By Benjamin Mapesa(Mapesa254)----
#The first page for the portal
#Using Object Oriented Programming

from tkinter import *
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image , ImageTk


class Login_page(Tk) :
    #Declaring the Login_page attributes that are not widgets
    def __init__(self) -> None:
        super().__init__()
        self.title('Page 1(Login)')
        self.geometry('360x640')
        self.config(bg='white')
        title_img = Image.open('Bank image.jpg').resize((200,200))
        self.photo = ImageTk.PhotoImage(image=title_img)
        self.frame = tk.Frame(self, width=300, height=300, background='white' )
        self.widgets()
        self.structure()

    def widgets(self) :   
        #Creating the widgets in the page
        
        self.profile_label = Label(self, image=self.photo, background='white' , border=None)
        self.instructions_label = Label(self.frame, text='Enter your details in the provided fields below :' ,foreground='grey', background='white', font=('Times', '10'))
        self.welcome_label = Label(self.frame, text='WELCOME TO 254 ONLINE BANKING' ,foreground='green', background='white', font=('Canvas bold', '13'))
        self.account_number = Entry(self.frame ,width=40)
        self.password = Entry(self.frame, width=40 )
        
        self.login_button = Button(self.frame, text='LOGIN' , command=self.login)
        self.in_entry_words()
        
    def structure(self) :
        #Positioning the page contents
        self.frame.place(x=30, y=230)
        self.profile_label.place(x=70, y=20)
        self.welcome_label.place(x=5, y=10)
        self.instructions_label.place(x=20, y=50)
        self.account_number.place(x=30, y=90)
        self.password.place(x=30, y=150)
        self.login_button.place(x=100, y=220)
    
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
        
    #Functions to add the contents again when the entry widgets are unclicked
    #Added a condition where the contents are not added if there is user input
    def leave(self, *args) :
        number = self.account_number.get()
        if number == '' :
            self.account_number.insert(0,'Account Number')
        self.bind()

    def leave2(self, *args) :
        password = self.password.get()
        if password == '' :
            self.password.insert(0,'Password')
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