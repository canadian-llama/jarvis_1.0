import customtkinter as ctk
from PIL import Image

"""
A frame model homepage of the application.
"""


class AboutPage(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        ctk.CTkFrame.__init__(self, *args, **kwargs, width=700, height=420, fg_color='transparent')
        self.text = None
        self.abt_text = None
        self.send_btn = None
        self.query = None
        self.abt_btn = None
        self.home_btn = None
        self.menu_btn = None
        self.menu = None
        self.query_frame = None
        self.side_bar_frame = None
        self.inpFrame = None
        self.send_img = None
        self.menu_img = None
        self.about_img = None
        self.home_img = None
        self.test = False

        self.setup_ui()

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
        # frame to hold the menu buttons
        self.menu = ctk.CTkFrame(self.side_bar_frame, fg_color='transparent')
        # --------------------------------------------------------------------------
        # Menubar/ sidebar frame configuration
        self.menu_btn = ctk.CTkButton(self.side_bar_frame, image=self.menu_img, command=self.reveal_menubar, width=2,
                                      text='')
        self.menu_btn.pack(pady=10, )

        self.home_btn = ctk.CTkButton(self.menu, image=self.home_img, text='', width=2, height=2,
                                      hover_color='white', bg_color='transparent',
                                      # command=self.show_homepage
                                      )
        self.home_btn.grid(row=0, column=0, pady=10)

        self.abt_btn = ctk.CTkButton(self.menu, image=self.about_img, text='', width=2, height=2,
                                     hover_color='white', bg_color='transparent',
                                     # command=self.show_aboutpage
                                     )
        self.abt_btn.grid(row=2, column=0)

        self.text = '''This is Jarvis AI Model 1.0.0. It is still a work in progress and it will be updated often till perfection.
            \nThe main aim of Jarvis AI is to get a chatbot-like friend that can keep you company, also help with information's and also automate day-to-day tasks.
            \nCREATED BY : Ogunsade Ibukun Ayomide
            \nAbout Creator:
            \nThis is an AI project created by a young aspiring software developer. And So you know this is the first of many.  

            \nCredits:
            Mosh Hamedani
            \nGeeks-For-Geeks
            \nTom Schibanski
            \nNetwork Chuck
            \nStack OverFlow
            \nChatGPT3
            \nBro Code
            \nTeeJay
            \nAll my ITD colleagues.
             '''
        self.abt_text = ctk.CTkTextbox(self, width=700, height=420,
                                       font=('consolas', 20,), activate_scrollbars=True,
                                       fg_color='gray',
                                       text_color='black', wrap='word')
        self.abt_text.pack(padx=20, pady=20)
        self.abt_text.insert('0.0', self.text)
        self.abt_text.configure(state='disabled', )
        self.pack(ipadx=10, ipady=5, padx=10, pady=10, anchor='center')

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

