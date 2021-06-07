from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

class Vending_machine_image:
    """The class represents a label with image of vending machine with drinks.
     """
    def __init__(self, master):
        """ Constructs the label with image
        Parameters
        ----------
            master: a window, where this whole label will be placed"""
        self.__img = PhotoImage(file="images/maszynaFin.png")
        self.__machine_image_label = Label(master, image=self.__img)
        self.__machine_image_label.grid(column=0, row=0)

