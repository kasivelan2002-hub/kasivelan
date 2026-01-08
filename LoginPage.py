from tkinter import *
import mysql.connector as mysql
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import ttk
import time
import os

class Login():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1700x800")
        self.root.title("Login Window")
        self.create_elements()
        self.root.config(bg = "azure2")
        self.root.mainloop()
        
    def create_elements(self):
        self.username = Label(self.root, text="CAFE  Login", font=('Gabriola', 40, 'bold'),fg = "black",bg = "azure2")
        self.username.place(x=570, y=80)
        
        self.username = Label(self.root, text="Username :", font=('Verdana', 14, 'bold'),bg = "azure2")
        self.username.place(x=540, y=300)
 
        self.entry_username = Entry(self.root, font=('Times New Roman', 14))
        self.entry_username.place(x=685, y=300)
 
        self.password = Label(self.root, text="Password :", font=('Verdana', 14, 'bold'),bg ="azure2")
        self.password.place(x=540, y=350)
 
        self.entry_password = Entry(self.root, font=('Times New Roman', 14),show = "*")
        self.entry_password.place(x=685, y=350)
 
        self.login_button = Button(self.root, text="Login", height=2, width=10, font=('Times New Roman',10, 'bold'),command=self.login_user,bg = "snow")
        self.login_button.place(x=660, y=420)
 
        self.new_user = Label(self.root, text="New User?", font=('Verdana', 10, 'bold'),bg = "azure2")
        self.new_user.place(x=760, y=390)
 
        self.register_button = Button(self.root, text="Sign Up", height=2, width=10, font=('Times New Roman',10, 'bold'),command=self.destroy_login,bg = "snow")
        self.register_button.place(x=760, y=420)

                                                                                       
    
        
 
    def destroy_login(self):
        self.root.destroy()
        register = Register()
 
    def login_user(self):
        username = self.entry_username.get()
        userpassword = self.entry_password.get()
 
        if(username == "" or userpassword == ""):
            showinfo("Oops!","Your information can't be empty!")
            return
 
        mydb = mysql.connect(
          host="localhost",
          user="root",
          password="",
          database = "jones"
        )
 
        mycursor = mydb.cursor()
        sql = "select user, pass from login where user=%s and pass=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        if result:
            showinfo("Success","You're logged in!")

           

          
            self.root.destroy()
            
            with open("JPmain.py") as f:
                exec(f.read())

           
            
        else:
            showinfo("Failed","You've entered wrong credentials!")
            
class Register():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1700x800")
        self.root.title("Register Window")
        self.create_elements()
        self.root.config(bg = "azure2")
        self.root.mainloop()
    def create_elements(self):
        self.username = Label(self.root, text="Register Page ", font=('Gabriola', 40, 'bold'),fg = "black",bg = "azure2")
        self.username.place(x=600, y=90)

        self.username = Label(self.root, text="Username :", font=('Verdana', 14, 'bold'),bg = "azure2")
        self.username.place(x=540, y=300)

        self.entry_username = Entry(self.root, font=('Verdana', 14))
        self.entry_username.place(x=685, y=300)

        self.password = Label(self.root, text="Password :", font=('Verdana', 14, 'bold'),bg = "azure2")
        self.password.place(x=540, y=350)
    
        self.entry_password = Entry(self.root, font=('Verdana', 14),show="*")
        self.entry_password.place(x=685, y=350)

        self.name = Label(self.root, text="Name :", font=('Verdana', 14, 'bold'),bg = "azure2")
        self.name.place(x=540, y=400)

        self.entry_name = Entry(self.root, font=('Verdana', 14))
        self.entry_name.place(x=685, y=400)

        self.register_button = Button(self.root, text="Sign Up", height=2, width=10,font=('Times New Roman',10, 'bold'),command=self.register_user,bg = "snow")
        self.register_button.place(x=660, y=470)

        self.existing_user = Label(self.root, text="Existing User?", font=('Verdana', 10, 'bold'),bg = "azure2")
        self.existing_user.place(x=760, y=440)

        self.login_button = Button(self.root, text="Login", height=2, width=10, font=('Times New Roman',10, 'bold'),command=self.destroy_register,bg = "snow")
        self.login_button.place(x=770, y=470)


                                                                      
        

    def destroy_register(self):
        self.root.destroy()
        login = Login()

    def register_user(self): 
        username = self.entry_username.get()
        userpassword = self.entry_password.get()
        name = self.entry_name.get()

        if(username == "" or userpassword == "" or name == ""):
            showinfo("Oops!","Your information can't be empty!")
            return

        mydb = mysql.connect(
          host="localhost",
          user="root",
          password="",
          database = "Jones"
        )

        mycursor = mydb.cursor()

        mycursor.execute("select count(*) from jp_cafe")
        result = mycursor.fetchone()
        old_count = result[0]

        sql = "INSERT INTO jp_cafe(Username, Password, Name) VALUES (%s, %s, %s)"
        val = (username, userpassword, name)
        mycursor.execute(sql, val)
        mydb.commit()
        
        mycursor.execute("select count(*) from jp_cafe")
        result = mycursor.fetchone()
        new_count = result[0]

        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_name.delete(0, END)

        if(old_count + 1 == new_count):
            showinfo("Success","Your information is saved successfully!")
        else:
            showinfo("Failed","Your information couldn't save successfully!")


if __name__ == '__main__':
    login = Login()

