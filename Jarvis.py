import customtkinter as ctk
from homepage import HomePage
from aboutpage import AboutPage

"""
A class that models the main homepage of the application
"""


class Jarvis(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        # App Appearance and configs
        self.btn_clicked = False
        ctk.set_default_color_theme('green')
        ctk.set_appearance_mode('dark')
        self.title('Jarvis')
        self.configure(pady=10, padx=10, ipadx=5, ipady=5)
        self.resizable(width=False, height=False)
        self.geometry('720x480')
        # ---------------------------------
        # -----------------all frame widgets to be used---------------------
        # the main frame/ body of app
        self.home_page = HomePage(self)
        self.home_page.pack()
        self.about_page = AboutPage(self)
        self.home_page.home_btn.configure(command=self.show_home_page, state="disabled")
        # self.home_page.abt_btn.configure(command=self.show_about_page, )
        # self.about_page.home_btn.configure(command=self.show_home_page, )
        # self.about_page.abt_btn.configure(command=self.show_about_page, state="disabled")

    """
    the below functions works similar to other callback functions it changes the bool variable to its
    opposite. For more detailed explanation on the function see the def callback in homepage.py 
    """

    def callback(self):
        self.btn_clicked = not self.btn_clicked
        return self.btn_clicked

    """
    The below function works to show the homepage on the click of the home button
    It works by checking if the aboutpage is currently active (using the widget.winfo_ismapped()
    function which returns True or False) the and if the callback value is not its current value
    and unpacks the aboutpage then packs the homepage
    """

    def show_home_page(self):
        if self.about_page.winfo_ismapped() and not self.callback():
            self.about_page.pack_forget()
            self.home_page.pack()

    """
    The below function works to show the aboutpage on the click of the about button
    It works by checking if the homepage is currently active (using the widget.winfo_ismapped()
    function which returns True or False) the and if the callback value is not its current value
    and unpacks the homepage then packs the aboutpage
    """

    def show_about_page(self):
        if self.home_page.winfo_ismapped() and self.callback():
            self.home_page.pack_forget()
            self.about_page.pack()


if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.mainloop()
