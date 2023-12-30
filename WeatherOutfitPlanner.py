#Import Required Libraries
import tkinter as tk
from tkinter import ttk

#Define Base Class - Basis for Other Frames and Class
class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)


    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}

    for page in (RegisterUser, LoginUser, Homepage, AddClothes, EditClothes, EditListClothes, EditClothesPages, DeleteClothes, DeleteListClothes):
      frame = page(container, self)
      self.frames[page] = frame
      frame.grid(row=0, column=0, sticky="nsew") 


class RegisterUser(tk.Frame):
  pass
class LoginUser(tk.Frame):
  pass
class Homepage(tk.Frame):
  pass
class AddClothes(tk.Frame):
  pass
class EditClothes(tk.Frame):
  pass
class EditListClothes(tk.Frame):
  pass
class EditClothesPages(tk.Frame):
  pass
class DeleteClothes(tk.Frame):
  pass
class DeleteListClothes(tk.Frame):
  pass
    