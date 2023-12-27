from login_system.pb_conn import PB_Manager
from .auth_window import AuthWindow
from .utils import resource_path
import customtkinter as ctk


class MainWindow(ctk.CTk):
    WIDTH = 1080
    HEIGHT = 720

    def __init__(self):
        super().__init__()
        self.title('Main')
        self.resizable(False, False)
        self.iconbitmap(resource_path('assets/images/green_cat.ico'))

        # Center The Window
        x = int((self.winfo_screenwidth()/2) - (self.WIDTH/2))
        y = int((self.winfo_screenheight()/2) - (self.HEIGHT/2))
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}+{x}+{y}')

        self.login_win = AuthWindow(self, self.on_logged_in)

        self.message = ctk.CTkLabel(self, text='')
        self.message.pack()

        self.verify_btn = ctk.CTkButton(
            self, text='Send Verification E-mail', command=lambda: PB_Manager.verify_user())

        self.withdraw()

    def on_logged_in(self):
        self.login_win.destroy()
        self.deiconify()
        self.message.configure(
            text=f'Welcome to your Dashboard, {PB_Manager.user.username}.')

        if PB_Manager.user.verified is False:
            self.verify_btn.pack()
