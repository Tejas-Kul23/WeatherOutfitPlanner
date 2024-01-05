#Import Required Libraries
import tkinter as tk
from tkinter import ttk, W
import hashlib

#Initialise Global Variables:
username = ''

#Define Base Class - for Other Frames and Class
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #The Container is where other frames will be stacked upon
        #The ones that need to be made visible, will be raised above others
        container = tk.Frame(self)

        #Ensures the frame will fill the entire tkinter app regardless of its size
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Create a dictionary, with keys being the names of each frame class,
        # and the values being the instances of frame classes themselves
        self.frames = {}

        for F in (RegisterUser, LoginUser, Homepage, AddClothes, EditClothes, EditListClothes,
                  EditClothesPages, DeleteClothes, DeleteListClothes):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')


    def show_frame(self, page_name: str) -> None:
        #Gets the Frame Instance by reffering to the Key Value
        frame = self.frames[page_name]
        # raises the current frame to the top
        frame.tkraise()

class RegisterUser(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Sets the title of the Application
        self.controller.title('Register User')

        #Initialise variables that will be used to get values from corresponding entry boxes
        self.user_var = tk.StringVar()
        self.pwd_var = tk.StringVar()
        self.conf_pwd_var = tk.StringVar()


        #Instantiate Labels and Entry Boxes for Username, Password and Confirmed Password
        #Each Label is aligned to the left
        #Padding of 10px is applied on the left and right

        self.user_label = ttk.Label(self, text='Username: ', anchor='w', justify='left')
        self.user_label.grid(row=0, column=0, sticky = W, padx= 10)
        self.user_entry = ttk.Entry(self, width=50, textvariable=self.user_var)
        self.user_entry.grid(row=1, column=0, padx= 10)

        #Users entry to the password is censored by the use of asterisks '*'

        self.pwd_label = ttk.Label(self, text='Password: ', anchor='w', justify='left')
        self.pwd_label.grid(row=2, column=0, sticky = W, padx= 10)
        self.pwd_entry = ttk.Entry(self, width=50, textvariable=self.pwd_var, show='*')
        self.pwd_entry.grid(row=3, column=0, padx= 10)

        self.conf_pwd_label = ttk.Label(self, text='Confirm Password: ', anchor='w', justify='left')
        self.conf_pwd_label.grid(row=4, column=0, sticky = W, padx= 10)
        self.conf_pwd_entry = ttk.Entry(self, width=50, show='*', textvariable=self.conf_pwd_var)
        self.conf_pwd_entry.grid(row=5, column=0, padx= 10)

        #Button instantiated that will run the method self.register()
        self.register_response = ttk.Label(self, text = '')
        self.register_response.grid(row=6, column=0, padx=10)

        self.register_btn = ttk.Button(self, text='Register', command=self.register)
        self.register_btn.grid(row=7, column=0, padx=10)


    def register(self) -> None:
        #Take values from the entry boxes
        global username
        username = self.user_var.get()
        password = self.pwd_var.get()
        confirm_password = self.conf_pwd_var.get()

        #Presence Check
        if username != '' and password != '' and confirm_password != '':
            #Check whether the Password is re-entered correctly
            if password == confirm_password:

                #Update register label text to confirm success
                self.register_response.config(text='Registered!')
                self.user_var.set('')

                #password string is encoded in order to be hashed, then represented in hexadecimal
                #and saved in a password.txt file
                conf_pwd_hash = hashlib.sha256(confirm_password.encode()).hexdigest()

                #Consider using csv file if possible???
                with open('password.txt', 'w', encoding='utf-8') as f:
                    f.write(conf_pwd_hash)

                confirm_password, password = '', ''
            else:
                #Update register label text to inform a failed match
                self.register_response.config(text='Confirmed Password does not match the Password')

            self.pwd_var.set('')
            self.conf_pwd_var.set('')
        else:
            #Update register label text to inform a failed presence check
            self.register_response.config(text='Please do not leave any fields empty')


class LoginUser(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller

class Homepage(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
class AddClothes(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
class EditClothes(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
class EditListClothes(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
class EditClothesPages(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
class DeleteClothes(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
class DeleteListClothes(tk.Frame):
    def __init__(self, parent,controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller

if __name__ == '__main__':
    app = App()
    app.show_frame('RegisterUser')
    app.mainloop()
