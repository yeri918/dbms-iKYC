#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle
from PIL import Image, ImageTk

class Login_GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Login System")
        self.root.geometry("400x300")
        self.initialView()
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.mainloop()

    def onClosing(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy() 
        quit()

    def initialView(self):
        for x in self.root.winfo_children():
            x.destroy()
        
        # welcom part
        self.canvas = Canvas(self.root, width=400, height=135, bg='green')
        photo = Image.open('database.jpg')
        photo = photo.resize((400,200))
        image_file = ImageTk.PhotoImage(photo)
        self.welcom_image = self.canvas.create_image(200, 0, anchor='n', image=image_file)
        self.canvas.pack(side='top')
        self.welcom_message = Label(self.root, text='Welcome',font=('Arial', 16)).pack()

        # user information
        self.user_message = Label(self.root, text='User name:', font=('Arial', 14)).place(x=10, y=170)
        self.password_message = Label(self.root, text='Password:', font=('Arial', 14)).place(x=10, y=210)

        # use Entry to input information
        self.var_usr_name = StringVar()
        self.var_usr_name.set('example@python.com')
        self.entry_usr_name = Entry(self.root, textvariable=self.var_usr_name, font=('Arial', 14))
        self.entry_usr_name.place(x=120,y=175)

        self.var_usr_pwd = StringVar()
        self.entry_usr_pwd = Entry(self.root, textvariable=self.var_usr_pwd, font=('Arial', 14), show='*')
        self.entry_usr_pwd.place(x=120,y=215)

        self.btn_login = Button(self.root, text='Login', command=self.usr_login)
        self.btn_login.place(x=120, y=240)
        self.btn_sign_up = Button(self.root, text='Sign up', command=self.usr_sign_up)
        self.btn_sign_up.place(x=200, y=240)
    
    # Function for user log in
    def usr_login(self):
        # get the user input for username and password
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
     
        # If the .pickle file exists, search the user information
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        # For the first time to login in, there doesn't exist a .pickle file to store information
        except FileNotFoundError:
            # create a admin
            # username: "admin", password: "admin"
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
                usr_file.close()    
     
        # If find the user in the .pickle file
        if usr_name in usrs_info:
            # the password is correct, show up the success message
            if usr_pwd == usrs_info[usr_name]:
                messagebox.showinfo(title='Welcome', message='Successfully login in！ ' + usr_name)
            # the password is incorrect, show up the error message
            else:
                messagebox.showerror(message='Error, your password is wrong, try again.')
        # The user didn't sign up         
        else:  
            is_sign_up = messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
            if is_sign_up:
                self.usr_sign_up()

    # Function for user sign up
    def usr_sign_up(self):
        def sign_to_login_system():
            # 以下三行就是获取我们注册时所输入的信息
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()
     
            # Open the .pickle file
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
            # Judge whether the password and confirmed password are the same
            if np != npf:
                messagebox.showerror('Error', 'Password and confirm password must be the same!')
     
            # If the username exists, throw error
            elif nn in exist_usr_info:
                messagebox.showerror('Error', 'The user has already signed up!')
     
            # successfully sign up
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                messagebox.showinfo('Welcome', 'You have successfully signed up!')
                # destroy the window
                window_sign_up.destroy()
 
        # Define a new window
        window_sign_up = Toplevel(self.root)
        window_sign_up.geometry('300x200')
        window_sign_up.title('Sign up window')
        
        # Entry for new username
        new_name = StringVar()  
        new_name.set('example@python.com')  
        Label(window_sign_up, text='User name: ').place(x=10, y=10)  
        entry_new_name = Entry(window_sign_up, textvariable=new_name) 
        entry_new_name.place(x=130, y=10)  
        
        # Entry for new password
        new_pwd = StringVar()
        Label(window_sign_up, text='Password: ').place(x=10, y=50)
        entry_usr_pwd = Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=130, y=50)
     
        new_pwd_confirm = StringVar()
        Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
        entry_usr_pwd_confirm = Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=130, y=90)
     
        # record the user information in the .pickle file
        btn_comfirm_sign_up = Button(window_sign_up, text='Sign up', command=sign_to_login_system)
        btn_comfirm_sign_up.place(x=180, y=120)


# -------------------
# -- Start the GUI --
# -------------------
login_gui = Login_GUI()


