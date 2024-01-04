#Import Required Libraries
from tkinter import *
import tkinter as tk
from tkinter import StringVar, ttk
import hashlib

#Define Base Class - for Other Frames and Class
class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    #The Container is where other frames will be stacked upon
    #The ones that need to be made visible, will be raised above others
    container = tk.Frame(self)

    #Ensures the frame will fill the entire tkinter app regardless of its size
    container.pack(side="top", fill="both", expand=True) 
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    #Create a dictionary, with keys being the names of each frame class, and the values being the instances of frame classes themselves
    self.frames = {}

    for F in (RegisterUser, LoginUser, Homepage, AddClothes, EditClothes, EditListClothes, EditClothesPages, DeleteClothes, DeleteListClothes):
      page_name = F.__name__
      frame = F(parent=container, controller=self)
      self.frames[page_name] = frame
      frame.grid(row=0, column=0, sticky="nsew") 

    self.show_frame("RegisterUser")

  def show_frame(self, page_name):
    frame = self.frames[page_name]
    # raises the current frame to the top
    frame.tkraise()

class RegisterUser(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    self.controller.title("Register User")

    global user_var
    user_var = tk.StringVar()
    global pwd_var
    pwd_var = tk.StringVar()
    global conf_pwd_var
    conf_pwd_var = tk.StringVar()

    self.user_label = ttk.Label(self, text="Username: ", anchor="w", justify="left")
    self.user_label.grid(row=0, column=0, sticky = W, padx= 10)

    self.user_entry = ttk.Entry(self, width=50, textvariable=user_var)
    self.user_entry.grid(row=1, column=0, padx= 10)

    self.pwd_label = ttk.Label(self, text="Password: ", anchor="w", justify="left")
    self.pwd_label.grid(row=2, column=0, sticky = W, padx= 10)

    self.pwd_entry = ttk.Entry(self, width=50, textvariable=pwd_var, show="*")
    self.pwd_entry.grid(row=3, column=0, padx= 10)

    self.conf_pwd_label = ttk.Label(self, text="Confirm Password: ", anchor="w", justify="left")
    self.conf_pwd_label.grid(row=4, column=0, sticky = W, padx= 10)

    self.conf_pwd_entry = ttk.Entry(self, width=50, show="*", textvariable=conf_pwd_var)
    self.conf_pwd_entry.grid(row=5, column=0, padx= 10)

    self.register_response = ttk.Label(self, text = "")
    self.register_response.grid(row=6, column=0, padx=10)

    self.register_btn = ttk.Button(self, text="Register", command=self.register)
    self.register_btn.grid(row=7, column=0, padx=10)


  def register(self):


    if pwd_var.get() != "" and user_var.get() != "":
      if conf_pwd_var.get() == pwd_var.get():
        username = user_var.get()
        password = pwd_var.get()
        confirm_password = conf_pwd_var.get()
        
        #TODO: Figure out how to add a label here
        self.register_response.config(text="Registered!")
        user_var.set("")

        conf_pwd_hash = hashlib.sha256(confirm_password.encode()).hexdigest()

        with open("password.txt", "w") as f:
          f.write(conf_pwd_hash)

      else:

        self.register_response.config(text="Confirmed Password does not match the Password, Try Again")

        pwd_var.set("")
        conf_pwd_var.set("")
    else:
      self.register_response.config(text="Please do not leave any fields empty")


class LoginUser(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class Homepage(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class AddClothes(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class EditClothes(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class EditListClothes(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class EditClothesPages(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class DeleteClothes(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
class DeleteListClothes(tk.Frame):
  def __init__(self, parent,controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    

if __name__ == '__main__':
  app = App()
  app.mainloop()