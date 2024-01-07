# Import Required Libraries
import tkinter as tk
from tkinter import ttk
import hashlib

# Initialise Global Variables:
username = ''


# Define Base Class - for Other Frames and Class
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # The Container is where other frames will be stacked upon
        # The ones that need to be made visible, will be raised above others
        container = tk.Frame(self)

        # Ensures the frame will fill the entire tkinter app regardless of its size
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a dictionary, with keys being the names of each frame class,
        # and the values being the instances of frame classes themselves
        self.frames = {}

        for F in (RegisterUser, LoginUser, Homepage, AddClothes, EditClothes, EditListClothes,
                  EditClothesPages, DeleteClothes, DeleteListClothes):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, page_name: str) -> None:
        # Gets the Frame Instance by referring to the Key Value
        frame = self.frames[page_name]
        # raises the current frame to the top
        frame.tkraise()


class RegisterUser(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Initialise variables that will be used to get values from corresponding entry boxes
        self.user_var = tk.StringVar()
        self.pwd_var = tk.StringVar()
        self.conf_pwd_var = tk.StringVar()

        # Instantiate Labels and Entry Boxes for Username, Password and Confirmed Password
        # Each Label is aligned to the left
        self.user_label = ttk.Label(self, text='Username: ', anchor='w', justify='left')
        self.user_entry = ttk.Entry(self, width=50, textvariable=self.user_var)

        # Users entry to the password is censored by the use of asterisks '*'
        self.pwd_label = ttk.Label(self, text='Password: ', anchor='w', justify='left')
        self.pwd_entry = ttk.Entry(self, width=50, textvariable=self.pwd_var, show='*')
        self.conf_pwd_label = ttk.Label(self, text='Confirm Password: ', anchor='w', justify='left')
        self.conf_pwd_entry = ttk.Entry(self, width=50, show='*', textvariable=self.conf_pwd_var)

        # Padding of 10px is applied on the x-axis
        self.user_label.pack(side=tk.TOP, padx=10)
        self.user_entry.pack(side=tk.TOP, padx=10)
        self.pwd_label.pack(side=tk.TOP, padx=10)
        self.pwd_entry.pack(side=tk.TOP, padx=10)
        self.conf_pwd_label.pack(side=tk.TOP, padx=10)
        self.conf_pwd_entry.pack(side=tk.TOP, padx=10)

        # Button instantiated that will run the method self.register()
        self.register_response = ttk.Label(self, text='')
        self.register_btn = ttk.Button(self, text='Register', command=self.register_user)

        self.register_response.pack(side=tk.TOP, padx=10)
        self.register_btn.pack(side=tk.TOP, padx=10)

    def register_user(self) -> None:
        # Take values from the entry boxes
        global username
        username = self.user_var.get()
        password = self.pwd_var.get()
        confirm_password = self.conf_pwd_var.get()

        # Presence Check
        if username != '' and password != '' and confirm_password != '':
            # Check whether the Password is re-entered correctly
            if password == confirm_password:

                # Update register label text to confirm success
                self.register_response.config(text='Registered!')
                self.user_var.set('')
                self.pwd_var.set('')
                self.conf_pwd_var.set('')

                # password string is encoded in order to be hashed, then represented in hexadecimal
                # and saved in a password.txt file
                conf_pwd_hash = hashlib.sha256(confirm_password.encode()).hexdigest()

                # Consider using csv file if possible???
                with open('password.txt', 'w', encoding='utf-8') as f:
                    f.write(conf_pwd_hash)

                confirm_password, password = '', ''

                self.controller.show_frame("LoginUser")
            else:
                # Update register label text to inform a failed match
                self.register_response.config(text='Confirmed Password does not match the Password')
                self.pwd_var.set('')
                self.conf_pwd_var.set('')

        else:
            # Update register label text to inform a failed presence check
            self.register_response.config(text='Please do not leave any fields empty')


class LoginUser(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user_var = tk.StringVar()
        self.pwd_var = tk.StringVar()

        # Create Entry Boxes and Labels for Login Page
        self.user_label = ttk.Label(self, text='Username: ')
        self.user_entry = ttk.Entry(self, width=50, textvariable=self.user_var)

        # Users entry to the password is censored by the use of asterisks '*'
        self.pwd_label = ttk.Label(self, text='Password: ')
        self.pwd_entry = ttk.Entry(self, width=50, textvariable=self.pwd_var, show='*')

        # Response Label Updated to inform any error within the data
        self.login_response = ttk.Label(self, text='')
        # Runs Login()
        self.login_btn = ttk.Button(self, text='Login', command=self.login)

        # Packing all widgets, padding of 10px on the x-axis
        self.user_label.pack(side=tk.TOP, padx=10, anchor=tk.W)
        self.user_entry.pack(side=tk.TOP)
        self.pwd_label.pack(side=tk.TOP, padx=10, anchor=tk.W)
        self.pwd_entry.pack(side=tk.TOP)
        self.login_response.pack(side=tk.TOP)
        self.login_btn.pack(side=tk.TOP)

    # Future Potential Additions, Change password, or username

    def login(self) -> None:
        login_user_var = self.user_var.get()
        login_pwd_var = self.pwd_entry.get()
        # Presence Check
        if login_user_var == '':
            self.login_response.config(text='Username entry field must be filled')
            return
        if login_pwd_var == '':
            self.login_response.config(text='Password entry field must be filled')
            return

        # The string entered in pwd_entry is accessed, encoded, hashed and converted to a hexadecimal
        pwd_hash = hashlib.sha256(login_pwd_var.encode()).hexdigest()

        # text file is open, and the hash is read and saved to variable
        pwd_txt_hash = open('password.txt', encoding='utf-8').read()

        # Username and Variable Compared
        if login_user_var == username and pwd_hash == pwd_txt_hash:
            self.login_response.config(text='Logged in successfully!')
            self.controller.show_frame('Homepage')
        else:
            self.login_response.config(text='Incorrect password/username, Try again.')
        return


class Homepage(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


class AddClothes(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


class EditClothes(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


class EditListClothes(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


class EditClothesPages(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


class DeleteClothes(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


class DeleteListClothes(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller


if __name__ == '__main__':
    app = App()
    app.title('Weather Outfit Planner')
    app.show_frame('RegisterUser')
    app.mainloop()
