#----By Benjamin Mapesa(Mapesa254)----
#The first page for the portal
#Using Object Oriented Programming

from tkinter import *
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

        #Creating the widgets in the page
        self.profile_label = Label(self, image=self.photo, border=None, background='cyan')
        self.instructions_label = Label(self, text='Enter your details in the provided fields below' ,foreground='purple', background='cyan', font=('Times ', '10'))
        self.account_number = Entry(self, width=40, )
        self.password = Entry(self, width=40)
        self.login_button = Button(self, text='LOGIN', command=self.login)
        
        #Positioning the page contents
        self.profile_label.place(x=130, y=20)
        self.instructions_label.place(x=20, y=150)
        self.account_number.place(x=20, y=200)
        self.password.place(x=20, y=250)
        self.login_button.place(x=130, y=300)

    #Function to execute commands depending on the entry contents when login_button is pressed
    def login(self) :
        self.account_number.get()
        self.password.get()

        if self.account_number == '12345678' and self.password == 'mypass254' :
            messagebox.showinfo('Success','Login successful')
        else :
            messagebox.showerror('Error', 'Invalid account number or password')  

if __name__ == "__main__" :
    login_page = Login_page()
    login_page.mainloop()