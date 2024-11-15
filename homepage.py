"""
import all necessary modules that will be used in the file
"""
import time
from tkinter import END
import customtkinter as ctk
from PIL import Image

"""
A frame model homepage of the application.
"""


class HomePage(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        ctk.CTkFrame.__init__(self, *args, **kwargs, width=700, height=420, fg_color='transparent')
        self.output_box = None
        self.input_box = None
        self.query = None
        self.abt_btn = None
        self.home_btn = None
        self.menu_btn = None
        self.menu = None
        self.query_frame = None
        self.inpFrame = None
        self.side_bar_frame = None
        self.menu_img = None
        self.send_img = None
        self.about_img = None
        self.send_btn = None
        self.home_img = None
        self.returned_output = None
        self.test = False
        self.setup_ui()

    """
    The method that contains all widgets
    """

    def setup_ui(self):
        # loading images and other variables
        self.home_img = ctk.CTkImage(dark_image=Image.open('icons8-home-page-60.png'), size=(40, 40))
        self.about_img = ctk.CTkImage(dark_image=Image.open('icons8-about-50.png'), size=(44, 40))
        self.send_img = ctk.CTkImage(dark_image=Image.open('icons8-email-send-48.png'))
        self.menu_img = ctk.CTkImage(dark_image=Image.open('icons8-menu-48.png'), size=(40, 40))
        # ---------------------------------

        self.side_bar_frame = ctk.CTkFrame(self, width=100,
                                           height=self.winfo_height(), fg_color='transparent')
        self.side_bar_frame.pack(side="left", anchor="nw", pady=10)
        # frame to hold the conversation with the bot
        self.inpFrame = ctk.CTkScrollableFrame(self, width=600, height=350, fg_color='aliceblue')
        self.inpFrame.pack(pady=15, padx=5)
        # Frame for the query box, mic button , send.
        self.query_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.query_frame.pack(side="bottom", )
        # frame to hold the menu buttons
        self.menu = ctk.CTkFrame(self.side_bar_frame, fg_color='transparent')
        # --------------------------------------------------------------------------
        # Menubar/ sidebar frame configuration
        self.menu_btn = ctk.CTkButton(self.side_bar_frame, image=self.menu_img, command=self.reveal_menubar, width=2,
                                      text='')
        self.menu_btn.pack(pady=10, padx=5)

        self.home_btn = ctk.CTkButton(self.menu, image=self.home_img, text='', width=2, height=2,
                                      hover_color='white', bg_color='transparent',
                                      # command=self.show_homepage
                                      )
        self.home_btn.grid(row=0, column=0, pady=10)

        self.query = ctk.CTkEntry(self.query_frame, width=500, height=40, corner_radius=20, placeholder_text='Type a '
                                                                                                             'query',
                                  font=('comic sans', 14))
        self.query.grid(row=0, column=0, padx=5)

        self.send_btn = ctk.CTkButton(self.query_frame, image=self.send_img, text='', width=3, height=3,
                                      hover_color='white', fg_color='transparent', command=self.display_output_on_ui
                                      )
        self.send_btn.grid(row=0, column=1, padx=2)

    """
    a variable named self.test is defined as a boolean and takes False as it current value
    the function Callback checks the value of self.test everytime it is invoked and makes it 
    the opposite value, i.e from False to True and from True to False based on the number 
    of times the function is called it then returns the current value of self.test.
    """

    def callback(self):
        self.test = not self.test
        return self.test

    """
    the reveal function uses the value returned by the callback function to evaluates its conditions
    if the callback function returns True it packs the self.menu widget else it unpacks it.
    """

    def reveal_menubar(self):
        if self.callback():
            self.menu.pack()
        else:
            self.menu.pack_forget()
        # --------------------------------

    """This function gets the text in the entry box and returns it"""

    def get_query(self):
        user_input = self.query.get()
        return user_input

    """This is the main function that the send btn invokes."""

    def jarvis_functionality(self):
        user_prompt = self.get_query()
        from main_functions import determine_output
        self.returned_output = determine_output(user_prompt)
        return self.returned_output

    """This deals with displaying the output box and input box on the screen"""

    def display_output_on_ui(self):
        query = self.get_query()
        result = self.jarvis_functionality()
        input_box = ctk.CTkTextbox(self.inpFrame, height=5, width=500, wrap='word', font=('congenial', 15),
                                   text_color='black', fg_color='green')
        output_box = ctk.CTkTextbox(self.inpFrame, width=500, wrap='word', font=('congenial', 15),
                                    fg_color='white', text_color='black', )

        if self.get_query() == "":
            input_box.pack(pady=5)
            input_box.insert('0.0', query)
            input_box.configure(state='disabled')
            time.sleep(1.5)
            output_box.pack(pady=5, )
            output_box.insert('0.0', 'Invalid Statement, Try a valid command!')
            output_box.configure(height=80, state='disabled')
        else:
            input_box.pack(pady=5)
            input_box.insert('0.0', query)
            input_box.configure(state='disabled')
            self.query.delete("0", END)
            time.sleep(1.5)
            output_box.pack(pady=5)
            output_box.insert('0.0', result)
            output_box.configure(state='disabled')
