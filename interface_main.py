
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from vending_machine_label import Vending_machine_image
from vending_machine import Vending_Machine
from decimal import *
import pygame

vend = Vending_Machine(2)
pygame.mixer.init()


def play_coin():
    """The function responsible for playing the coin falling sound once, using pygame """

    pygame.mixer.music.load("sounds\coin_sound.mp3")
    pygame.mixer.music.play(loops=0)

def play_button():
    """The function responsible for playing the button click sound once, using pygame """
    pygame.mixer.music.load("sounds\\button_click.mp3")
    pygame.mixer.music.play(loops=0)

class ButtonFrame:
    """This class represents a panel with buttons with which we enter the product number and check product price 
    """


    def __init__(self):

        """ Constructs the window with vending machine image and frame with buttons and display screen

            Parameters
            ----------
                
         """

        ##CREATS A WINDOW
        self.__root = Tk()
        self.__root.title("Vending Machine with drinks")
        self.__win_width = 1400
        self.__win_height = 800
        self.__screen_width = self.__root.winfo_screenwidth()
        self.__screen_height = self.__root.winfo_screenheight()
        self.__x = (self.__screen_width/2) - (self.__win_width/2)
        self.__y = (self.__screen_height/2) - (self.__win_height/2)
        self.__root.geometry("{}x{}+{}+{}".format(self.__win_width, self.__win_height, int(self.__x), int(self.__y)))
        self.__root.iconbitmap('images\icon1.ico')
        self.__vend_image = Vending_machine_image(self.__root)

        ##CREATS A FRAME WITH BUTTONS
        self.__frame_buttons = LabelFrame(self.__root, padx=5, pady=5, bg = "#cfcfcf")
        self.__frame_buttons.grid(column=1, row=0)

        ##CREATS CUSTOM FONT
        self.__font_Entry = font.Font(family="Ticking Timebomb BB", size=14)
        
        ##CREATS LABEL, WITH DISPLAY INFORMATION FOR USER/WHICH USER INPUTS
        self.__entry_display = Entry(self.__frame_buttons, width=50, borderwidth=5, font=self.__font_Entry, justify="center")
        self.__entry_display.insert(0, "Wprowadz numer produktu, ktory chcesz zakupic")
        self.__entry_display.grid(column =0, row=0, columnspan=3, padx = 10, pady = 10)

        ##CREATS BUTTONS
        self.__button_1 = Button(self.__frame_buttons, text="1", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(1))
        self.__button_1.grid(column=0, row=1)

        self.__button_2 = Button(self.__frame_buttons, text="2", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(2))
        self.__button_2.grid(column=1, row=1)

        self.__button_3 = Button(self.__frame_buttons, text="3", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(3))
        self.__button_3.grid(column=2, row=1)

        self.__button_4 = Button(self.__frame_buttons, text="4", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(4))
        self.__button_4.grid(column=0, row=2)

        self.__button_5 = Button(self.__frame_buttons, text="5", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(5))
        self.__button_5.grid(column=1, row=2)

        self.__button_6 = Button(self.__frame_buttons, text="6",height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(6))
        self.__button_6.grid(column=2, row=2)

        self.__button_7 = Button(self.__frame_buttons, text="7",height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(7))
        self.__button_7.grid(column=0, row=3)

        self.__button_8 = Button(self.__frame_buttons, text="8", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(8))
        self.__button_8.grid(column=1, row=3)

        self.__button_9 = Button(self.__frame_buttons, text="9", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(9))
        self.__button_9.grid(column=2, row=3)
        
        self.__button_0 = Button(self.__frame_buttons, text="0", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_click(0))
        self.__button_0.grid(column=1, row=4)

        self.__button_OK = Button(self.__frame_buttons, text="Approve\nProduct", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= self.__button_ok)
        self.__button_OK.grid(column=0, row=5)

        self.__button_C = Button(self.__frame_buttons, text="C", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= self.__button_clear)
        self.__button_C.grid(column=0, row=4)

        self.__button_close = Button(self.__frame_buttons, text="Quit", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__root.destroy())
        self.__button_close.grid(column=2, row=5)
        
        self.__button_check_price = Button(self.__frame_buttons, text="Check\nPrice", height=5, width=10, bg="#4f4e4e", fg = "white", borderwidth=5, command= self.__check_price)
        self.__button_check_price.grid(column=1, row=5)
        
  
    
    def __check_price(self):
        """Plays sound from play_button function. In the try block method gets the number provided by user, if there is no such a number, it informs user about it.
            If the number is correct, method gives the price of the product to the Entry label.

            Excepts
            ------
            ValueError: If in the Entry label was anything other than a number, for example a different message to the user, the except ValueError catches this exception and
                        informs the user to enter the product again
                

         """
        play_button()
        try:
            current = int(self.__entry_display.get())
            if vend.check_product_number(current) == False:
                self.__entry_display.delete(0, END)
                self.__entry_display.insert(0, "Nie ma takiego produktu")
            else:
                self.__entry_display.delete(0, END)
                self.__entry_display.insert(0, "Cena produktu nr {} to: {}".format(current, vend.return_product_price(current)))
        except ValueError:
                self.__entry_display.delete(0, END)
                self.__entry_display.insert(0, "Wprowadz numer produktu")

    def __button_click(self, num):
        """Plays sound from play_button function. Method enters digits provided by user on the display screen.

            Parameters
            ----------
            num: a single digit entered by the user for the product number
        """
        play_button()
        tmp = self.__entry_display.get()

        if tmp.isdigit():
            self.__entry_display.delete(0, END)
            self.__entry_display.insert(0, str(tmp)+str(num))
        else:
            self.__entry_display.delete(0, END)
            self.__entry_display.insert(0, str(num))
    
    def __button_clear(self):
        """Plays sound from play_button function. Clears the display screen(__entry_display) and enters new information to the user: "Wprowadz numer produktu, ktory chcesz zakupic"

        """
        
        play_button()
        

        self.__entry_display.delete(0, END)
        self.__entry_display.insert(0, "Wprowadz numer produktu, ktory chcesz zakupic")
    
    def __button_ok(self):
        """Plays sound from play_button function. Gets the number entered by the user from display screen. Checks if the product with given number exists and informs user about it.
            If the number is correct, it informs user about it and opens a new window responsible for paying.


            Except
            ------
            ValueError: If in the Entry label was anything other than a number, for example a different message to the user, the except ValueError catches this exception and
                        informs the user to enter the product again
        """
        
        play_button()
        
        try:
            current = int(self.__entry_display.get())
            if vend.check_product_number(current) == False:
                self.__entry_display.delete(0, END)
                self.__entry_display.insert(0, "Nie ma takiego produktu")
            else:
                self.__entry_display.delete(0, END)
                self.__entry_display.insert(0, "Wybrales produkt nr {}".format(current))
                self.__button_clear()
                vend.set_product_number(current)
                t = Pay_window(self.__root, current)
                t.start()
                
        except ValueError:
                self.__entry_display.delete(0, END)
                self.__entry_display.insert(0, "Wprowadz numer produktu") 

    def start(self):
        """Starts the loop of the window """
        self.__root.mainloop()
    




class Pay_window:
    """This class represents a panel with buttons with which we enter the product number and check product price 
    """
    def __init__(self, master, product_number):
        """Creates the window with buttons(coins) and display screen  
            Parameters
            ----------
            master: "reference" to previous winndow 
            product_number: int
                            product number chosen by the user
            
            """

        ##HIDES PREVIOUS WINDOW
        master.withdraw()
        
        ##CREATS A WINDOW
        self.__root = Toplevel(master)
        self.__root.title("Zaplac za produkt")
        self.__root.config(bg= "#ffffff")
        self.__root.iconbitmap('images\icon1.ico')
        self.__win_width = 500
        self.__win_height = 300
        self.__screen_width = self.__root.winfo_screenwidth()
        self.__screen_height = self.__root.winfo_screenheight()
        self.__x = self.__screen_width/2 - self.__win_width/2
        self.__y = self.__screen_height/2 - self.__win_height/2
        self.__root.geometry("{}x{}+{}+{}".format(self.__win_width, self.__win_height, int(self.__x), int(self.__y)))

        ##CREATS A FRAME WITH BUTTONS
        self.__frame_buttons = LabelFrame(self.__root, padx=5, pady=5)
        self.__frame_buttons.place(relx = 0.5, rely = 0.5, anchor="center")

        ##CREATS CUSTOM FONT
        self.__font_Entry = font.Font(family="Ticking Timebomb BB", size=14)

        ##CREATS LABEL, WITH DISPLAY INFORMATION FOR USER/WHICH USER INPUTS
        self.__entry_display = Entry(self.__frame_buttons, width=50, borderwidth=5, font=self.__font_Entry, justify="center")
        self.__entry_display.insert(0, "Produkt numer {}\t cena: {}".format(product_number, vend.return_product_price(product_number)))
        self.__entry_display.grid(column =0, row=0, columnspan=3, padx = 10, pady = 10)

        ##CREATES IMAGES OF BUTTONS
        self.__img_button1 = PhotoImage(file = "images/1gr.png")
        self.__img_button2 = PhotoImage(file = "images/2gr.png")
        self.__img_button3 = PhotoImage(file = "images/5gr.png")
        self.__img_button4 = PhotoImage(file = "images/10gr.png")
        self.__img_button5 = PhotoImage(file = "images/20gr.png")
        self.__img_button6 = PhotoImage(file = "images/50gr.png")
        self.__img_button7 = PhotoImage(file = "images/1zl.png")
        self.__img_button8 = PhotoImage(file = "images/2zl.png")
        self.__img_button9 = PhotoImage(file = "images/5zl.png")


        ##CREATS BUTTONS
        self.__button_1 = Button(self.__frame_buttons, image=self.__img_button1, borderwidth=0, command= lambda: self.__button_click(0.01))
        self.__button_1.grid(column=0, row=1)
    
        self.__button_2 = Button(self.__frame_buttons, image=self.__img_button2, borderwidth=0, command= lambda: self.__button_click(0.02))
        self.__button_2.grid(column=1, row=1)

        self.__button_3 = Button(self.__frame_buttons, image=self.__img_button3, borderwidth=0, command= lambda: self.__button_click(0.05))
        self.__button_3.grid(column=2, row=1)

        self.__button_4 = Button(self.__frame_buttons, image=self.__img_button4, borderwidth=0, command= lambda: self.__button_click(0.1))
        self.__button_4.grid(column=0, row=2)

        self.__button_5 = Button(self.__frame_buttons, image=self.__img_button5, borderwidth=0, command= lambda: self.__button_click(0.2))
        self.__button_5.grid(column=1, row=2)
        
        self.__button_6 = Button(self.__frame_buttons, image=self.__img_button6, borderwidth=0, command= lambda: self.__button_click(0.5))
        self.__button_6.grid(column=2, row=2)

        self.__button_7 = Button(self.__frame_buttons, image=self.__img_button7, borderwidth=0, command= lambda: self.__button_click(1))
        self.__button_7.grid(column=0, row=3)

        self.__button_8 = Button(self.__frame_buttons, image=self.__img_button8, borderwidth=0, command= lambda: self.__button_click(2))
        self.__button_8.grid(column=1, row=3)

        self.__button_9 = Button(self.__frame_buttons, image=self.__img_button9 ,borderwidth=0, command= lambda: self.__button_click(5))
        self.__button_9.grid(column=2, row=3)
        

        self.__button_OK = Button(self.__frame_buttons, text="Pay", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5, command= lambda: self.__button_ok(master))
        self.__button_OK.grid(column=2, row=4)

        self.__button_close = Button(self.__frame_buttons, text = "Resign", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5, command=lambda: self.__resign_from_pay(master))
        self.__button_close.grid(column=0, row=4)


    def __button_click(self, val):
        """Plays coind drop sound using play_coin() function.  Method responsible for entering the amount by user to purchase the item. It also returns information on display screen
            about the remaining amount to pay.
            
            Parameters
            ----------
            val: float, int
                    value of coin

            """
        play_coin()

        ##CLEARS DISPLAY WINDOW
        self.__entry_display.delete(0, END)

        ##ADDS COINS PROVIDED BY USER TO MACHINE
        vend.add_coin_to_machine(val)

        ##CHECKS THE REST AND DISPLAYS INFORMATION TO USER
        rest = vend.return_rest()
        if rest < Decimal("0"):
            self.__entry_display.insert(0, "Do zaplaty pozostalo {:.2f}".format(-rest))
        else:
            self.__entry_display.insert(0, "Reszta do wydania: {:.2f}".format(rest))

    
    
    def __button_ok(self, master):
        """Plays coind drop sound using play_coin() function. Depending on the result of the but method from Vending_Machine class, the method, using one of
            the functions: __not_enough_money_info, __no_products_left_info, __no_rest_info, __good_buy_info creates a new window with informations.
            
            Parameters
            ----------
            master: "reference" to previous window

            """

        play_button()

        
        status, text = vend.buy()

        ##CREATES WINDOW WITH INFORMATIONS, DEPENDING ON THE OUTPUT "status" FROM "vend.buy"
        if status == -1:
            self.__not_enough_money_info(text)
        elif status == -2:
            self.__no_products_left_info(master, text)
        elif status == -3:
            self.__no_rest_info(master, text)
        else:
            self.__good_buy_info(master, text)
        

    def __resign_from_pay(self, master):
        """Responsible for interruption of payment and return of coins for user
            
            Parameters
            ----------
            master: "reference" to previous window
        """
        play_button()
        _, text1 = vend.resign()

        ##HIDES PAYMENT WINDOW
        self.__root.withdraw()
        
        ##CREATES WINDOW ABOUT RESIGN PAY
        wind = Toplevel(self.__root)
        wind.title("Resign")
        my_font = font.Font(family="Ticking Timebomb BB", size=14)
        win_width = 500
        win_height = 500
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = (screen_width/2) - (win_width/2)
        y = (screen_height/2) - (win_height/2)
        wind.geometry("{}x{}+{}+{}".format(win_width, win_height, int(x), int(y)))

        ##CREATES ICON OF WINDOW
        wind.iconbitmap('images\icon1.ico')

        ##CREATES LABEL WITH INFORMATION TEXT
        info_label = Label(wind, text=text1, font=my_font, bg = "#ffffff", borderwidth=5, bd=1, relief = "sunken")
        info_label.pack(pady=20)

        ##CREATES BUTTON
        close_button = Button(wind, text = "Quit", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5, command=lambda: self.__quit_d(master))
        close_button.pack(pady=20)

    def __quit_d(self, master):
        """Responsible for closing information window and payment window

            Parameters
            ----------
            master: "Reference" to previous window
         """

        ##"UNLOCKS" "master" WINDOW
        master.deiconify()

        ##DESTROYS "__root" WINDOW
        self.__root.destroy()

    def __quit(self, master, now):
        """Responsible for closing information window, returns to payment window

            Parameters
            ----------
            master: "Reference" to previous window
         """

        ##"UNLOCKS" "master" WINDOW
        master.deiconify()

        ##DESTROYS "now" window
        now.destroy()


    def __not_enough_money_info(self, text):
        """Creates new window with information about insufficient payment
            
            Parameters
            ----------
            text: str
                    text to display to user

            """

        ##HIDES PREVIOUS WINDOW
        self.__root.withdraw()

        ##CREATES WINDOW
        info_text = text
        wind = Toplevel(self.__root)
        wind.title("Info")
        my_font = font.Font(family="Ticking Timebomb BB", size=14)
        win_width = 500
        win_height = 500
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = (screen_width/2) - (win_width/2)
        y = (screen_height/2) - (win_height/2)
        wind.geometry("{}x{}+{}+{}".format(win_width, win_height, int(x), int(y)))

        ##CREATES ICON OF WINDOW
        wind.iconbitmap('images\icon1.ico')

        ##CREATES LABEL WITH INFORMATION FOR USER
        info_label = Label(wind, text=info_text, font=my_font, bg = "#ffffff", borderwidth=5, bd=1, relief = "sunken")
        info_label.pack(pady=20)

        ##CREATES BUTTON
        close_button = Button(wind, text = "Quit", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5, command=lambda: self.__quit(self.__root, wind))
        close_button.pack(pady=20)
 
        wind.mainloop()
    
    def __no_products_left_info(self, master, text):

        """Creates new window with information about lack of products with given number
            
            Parameters
            ----------
            text: str
                    text to display to user

            """

        ##HIDES PREVIOUS WINDOW
        self.__root.withdraw()

        ##CREATES WINDOW
        info_text = text
        wind = Toplevel(self.__root)
        wind.title("Info")
        my_font = font.Font(family="Ticking Timebomb BB", size=14)
        win_width = 500
        win_height = 500
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = (screen_width/2) - (win_width/2)
        y = (screen_height/2) - (win_height/2)
        wind.geometry("{}x{}+{}+{}".format(win_width, win_height, int(x), int(y)))

        ##CREATES ICON OF WINDOW
        wind.iconbitmap('images\icon1.ico')

        ##CREATES LABEL WITH INFORMATION FOR USER
        info_label = Label(wind, text=info_text, font=my_font, bg = "#ffffff", borderwidth=5, bd=1, relief = "sunken")
        info_label.pack(pady=20)
        
        ##CREATES BUTTON
        close_button = Button(wind, text = "Quit", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5,command=lambda: self.__quit_d(master))
        close_button.pack(pady=20)
 
        wind.mainloop()
    
    def __good_buy_info(self, master, text):
        """Creates new window with information about the purchase, displays product number, price and rest returned
            
            Parameters
            ----------
            text: str
                    text to display to user

            """
        ##HIDES PREVIOUS WINDOW
        self.__root.withdraw()

        ##CREATES WINDOW
        info_text = text
        wind = Toplevel(self.__root)
        wind.title("Info")
        my_font = font.Font(family="Ticking Timebomb BB", size=14)
        win_width = 500
        win_height = 500
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = (screen_width/2) - (win_width/2)
        y = (screen_height/2) - (win_height/2)
        wind.geometry("{}x{}+{}+{}".format(win_width, win_height, int(x), int(y)))

        ##CREATES ICON OF WINDOW
        wind.iconbitmap('images\icon1.ico')


        ##CREATES LABEL WITH INFORMATION FOR USER
        info_label = Label(wind, text=info_text, font=my_font, bg = "#ffffff", borderwidth=5, bd=1, relief = "sunken")
        info_label.pack(pady=20)


        ##CREATES BUTTON
        close_button = Button(wind, text = "Quit", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5, command=lambda: self.__quit_d(master))
        close_button.pack(pady=20)
 
        wind.mainloop()

    def __no_rest_info(self, master, text):
        """Creates new window with information about the lack of rest in the machine
            
            Parameters
            ----------
            text: str
                    text to display to user

            """

         ##HIDES PREVIOUS WINDOW
        self.__root.withdraw()

        ##CREATES WINDOW
        info_text = text
        wind = Toplevel(self.__root)
        wind.title("Info")
        my_font = font.Font(family="Ticking Timebomb BB", size=14)
        win_width = 500
        win_height = 500
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = (screen_width/2) - (win_width/2)
        y = (screen_height/2) - (win_height/2)
        wind.geometry("{}x{}+{}+{}".format(win_width, win_height, int(x), int(y)))

        ##CREATES ICON OF WINDOW
        wind.iconbitmap('images\icon1.ico')
        
        ##CREATES LABEL WITH INFORMATION FOR USER
        info_label = Label(wind, text=info_text, font=my_font, bg = "#ffffff", borderwidth=5, bd=1, relief = "sunken")
        info_label.pack(pady=20)
        
        ##CREATES BUTTON
        close_button = Button(wind, text = "Quit", height=3, width=6, bg="#4f4e4e", fg = "white", borderwidth=5, command=lambda: self.__quit_d(master))
        close_button.pack(pady=20)
 
        wind.mainloop()

    def start(self):
        self.__root.mainloop()




buttons = ButtonFrame()
buttons.start()