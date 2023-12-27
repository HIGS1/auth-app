from tkinter.messagebox import showwarning, showerror, showinfo
from login_system.pb_conn import PB_Manager
from .utils import resource_path
import customtkinter as ctk
from PIL import Image
from sys import exit


class AuthWindow(ctk.CTkToplevel):
    WIDTH = 900
    HEIGHT = 650

    def __init__(self, master, signin_callbck):
        super().__init__(master)
        self.resizable(False, False)
        self.signin_callbck = signin_callbck

        # If the window is closed the program will exit
        self.protocol('WM_DELETE_WINDOW', lambda: exit(0))

        # Center The Window
        x = int((self.winfo_screenwidth()/2) - (self.WIDTH/2))
        y = int((self.winfo_screenheight()/2) - (self.HEIGHT/2))
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}+{x}+{y}')

        # >>>>>>>>>>>>>>>>>>>>>> Making Widgets <<<<<<<<<<<<<<<<<<<<<<<<<:

        # Left Frame
        self.left_frame = ctk.CTkFrame(
            master=self,
            fg_color='#B2CBBA',
            corner_radius=0,
        )
        self.left_frame.pack(
            expand=True,
            fill='both',
            side='left',
        )

        # Left Frame Image
        self.cat_img = ctk.CTkLabel(
            self.left_frame,
            text='',
            image=ctk.CTkImage(
                Image.open(
                    resource_path('assets/images/green_cat.png')),
                size=(200, 200)
            )
        )
        self.cat_img.place(relx=0.5, rely=0.5, anchor='center')

        # Right Frame
        self.right_frame = ctk.CTkFrame(
            master=self,
            fg_color='#DFE8D8',
            corner_radius=0,
        )
        self.right_frame.pack(
            expand=True,
            fill='both',
            side='right',
        )

        # >>>>>>>>>>>>>>>>>>>>>>> Sign In Widgets <<<<<<<<<<<<<<<<<<<<<<<:

        # Title Label
        self.title_lbl = ctk.CTkLabel(
            self.right_frame,
            text='Log In to Your Account',
            font=ctk.CTkFont(
                'JejuGothic',
                35,
                'bold',
            ),
            text_color='#689878'
        )
        # Form Frame
        self.form_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color='transparent',
        )
        # Username or email
        self.username_lbl = ctk.CTkLabel(
            self.form_frame,
            text='Username or Email:',
            font=ctk.CTkFont(
                'JejuGothic',
                18,
                'normal',
            ),
            text_color='#689878'
        )
        # Username or email Entry
        self.username_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text='Username or E-mail',
            placeholder_text_color='#689878',
            corner_radius=15,
            border_color='#689878',
            height=38,
            font=ctk.CTkFont(
                'JejuGothic',
                16,
                'normal',
            ),
            text_color='#689878',
        )
        # Password
        self.password_lbl = ctk.CTkLabel(
            self.form_frame,
            text='Password:',
            font=ctk.CTkFont(
                'JejuGothic',
                18,
                'normal',
            ),
            text_color='#689878'
        )
        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text='Password',
            placeholder_text_color='#689878',
            border_color='#689878',
            corner_radius=15,
            height=38,
            show='•',
            font=ctk.CTkFont(
                'JejuGothic',
                16,
                'normal',
            ),
            text_color='#689878',
        )

        # Forgot Password Button
        self.forgot_password_btn = ctk.CTkButton(
            self.form_frame,
            text='Forgot my password',
            height=25,
            width=30,
            font=ctk.CTkFont(
                'Arial',
                18,
                'normal',
                underline=True,
            ),
            command=self.forgotten_password_callback,
            corner_radius=None,
            fg_color='transparent',
            hover=False,
            text_color='#689878'
        )

        self.l_sign_up_btn = ctk.CTkButton(
            self.form_frame,
            text='Don\'t have an Account? Sign Up',
            height=25,
            width=30,
            font=ctk.CTkFont(
                'Arial',
                18,
                'normal',
                underline=True,
            ),
            command=lambda: self.show_form(1),
            corner_radius=None,
            fg_color='transparent',
            hover=False,
            text_color='#689878'
        )

        # Sign In Button
        self.sign_in_btn = ctk.CTkButton(
            self.form_frame,
            text='Sign In',
            height=70,
            width=200,
            font=ctk.CTkFont(
                'JejuGothic',
                25,
                'bold',
            ),
            command=self.sign_in_btn_callback,
            corner_radius=25,
            fg_color='#689878',
            hover_color='#689878'
        )

        # >>>>>>>>>>>>>>>>>>>>>>> Sign Up Widgets <<<<<<<<<<<<<<<<<<<<<<<<:

        # Sign Up Label
        self.r_title_lbl = ctk.CTkLabel(
            self.right_frame,
            text='Register a new Account',
            font=ctk.CTkFont(
                'JejuGothic',
                35,
                'bold',
            ),
            text_color='#689878'
        )
        # Form Frame
        self.r_form_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color='transparent',
        )

        # Username
        self.r_username_lbl = ctk.CTkLabel(
            self.r_form_frame,
            text='Username:',
            font=ctk.CTkFont(
                'JejuGothic',
                18,
                'normal',
            ),
            text_color='#689878'
        )
        # Username Entry
        self.r_username_entry = ctk.CTkEntry(
            self.r_form_frame,
            placeholder_text='Username',
            placeholder_text_color='#689878',
            corner_radius=15,
            border_color='#689878',
            height=38,
            font=ctk.CTkFont(
                'JejuGothic',
                16,
                'normal',
            ),
            text_color='#689878',
        )

        # Email
        self.email_lbl = ctk.CTkLabel(
            self.r_form_frame,
            text='Email:',
            font=ctk.CTkFont(
                'JejuGothic',
                18,
                'normal',
            ),
            text_color='#689878'
        )
        # Email Entry
        self.email_entry = ctk.CTkEntry(
            self.r_form_frame,
            placeholder_text='E-mail',
            placeholder_text_color='#689878',
            corner_radius=15,
            border_color='#689878',
            height=38,
            font=ctk.CTkFont(
                'JejuGothic',
                16,
                'normal',
            ),
            text_color='#689878',
        )

        # Password
        self.r_password_lbl = ctk.CTkLabel(
            self.r_form_frame,
            text='Password:',
            font=ctk.CTkFont(
                'JejuGothic',
                18,
                'normal',
            ),
            text_color='#689878'
        )
        # Password Entry
        self.r_password_entry = ctk.CTkEntry(
            self.r_form_frame,
            placeholder_text='Password',
            placeholder_text_color='#689878',
            border_color='#689878',
            corner_radius=15,
            height=38,
            show='•',
            font=ctk.CTkFont(
                'JejuGothic',
                16,
                'normal',
            ),
            text_color='#689878',
        )

        # Confirm Password
        self.confirm_password_lbl = ctk.CTkLabel(
            self.r_form_frame,
            text='Confirm Password:',
            font=ctk.CTkFont(
                'JejuGothic',
                18,
                'normal',
            ),
            text_color='#689878'
        )
        # Confirm Password Entry
        self.confirm_password_entry = ctk.CTkEntry(
            self.r_form_frame,
            placeholder_text='Confirm Password',
            placeholder_text_color='#689878',
            border_color='#689878',
            corner_radius=15,
            height=38,
            show='•',
            font=ctk.CTkFont(
                'JejuGothic',
                16,
                'normal',
            ),
            text_color='#689878',
        )

        # Sign In Button
        self.r_sign_in_btn = ctk.CTkButton(
            self.r_form_frame,
            text='Already Have an Account? Sign In',
            height=25,
            width=30,
            font=ctk.CTkFont(
                'Arial',
                18,
                'normal',
                underline=True,
            ),
            command=lambda: self.show_form(0),
            corner_radius=None,
            fg_color='transparent',
            hover=False,
            text_color='#689878'
        )
        # Sign Up Button
        self.sign_up_btn = ctk.CTkButton(
            self.r_form_frame,
            text='Sign Up',
            height=50,
            width=200,
            font=ctk.CTkFont(
                'JejuGothic',
                25,
                'bold',
            ),
            command=self.sign_up_btn_callback,
            corner_radius=25,
            fg_color='#689878',
            hover_color='#689878'
        )

        self.show_form(0)
        self.iconbitmap(resource_path('assets/images/green_cat.ico'))

    def run(self):
        self.iconbitmap('assets/images/green_cat.ico')
        self.mainloop()

    def show_form(self, form_idx):
        """
        - 0: Sign In
        - 1: Sign up
        """
        match form_idx:
            case 0:  # Sign in
                self.title('Sign In')
                # Pack Sign In Widgets
                self.title_lbl.pack(
                    anchor='n',
                    ipady=85
                )
                self.form_frame.pack(
                    expand=False,
                    fill='both',
                )
                self.username_lbl.pack(
                    anchor='w',
                    padx=20,
                )
                self.username_entry.pack(
                    fill='x',
                    pady=10,
                    padx=100,
                )
                self.password_lbl.pack(
                    anchor='w',
                    padx=20,
                )
                self.password_entry.pack(
                    fill='x',
                    pady=10,
                    padx=100,
                )
                self.forgot_password_btn.pack(
                    pady=3,
                )
                self.l_sign_up_btn.pack(
                    pady=5,
                )
                self.sign_in_btn.pack(
                    pady=40,
                )

                # Forget Sign Up Widgets
                self.r_title_lbl.forget()
                self.r_form_frame.forget()
                self.email_lbl.forget()
                self.email_entry.forget()
                self.r_username_lbl.forget()
                self.r_username_entry.forget()
                self.r_password_lbl.forget()
                self.r_password_entry.forget()
                self.confirm_password_lbl.forget()
                self.confirm_password_entry.forget()
                self.r_sign_in_btn.forget()
                self.sign_up_btn.forget()
            case 1:  # Sign Up
                self.title('Sign Up')
                # Pack Sign Up Widgets
                self.r_title_lbl.pack(
                    anchor='n',
                    ipady=50
                )
                self.r_form_frame.pack(
                    expand=False,
                    fill='both',
                )
                self.r_username_lbl.pack(
                    anchor='w',
                    padx=20,
                )
                self.r_username_entry.pack(
                    fill='x',
                    pady=10,
                    padx=100,
                )
                self.email_lbl.pack(
                    anchor='w',
                    padx=20,
                )
                self.email_entry.pack(
                    fill='x',
                    pady=10,
                    padx=100,
                )
                self.r_password_lbl.pack(
                    anchor='w',
                    padx=20,
                )
                self.r_password_entry.pack(
                    fill='x',
                    pady=10,
                    padx=100,
                )
                self.confirm_password_lbl.pack(
                    anchor='w',
                    padx=20,
                )
                self.confirm_password_entry.pack(
                    fill='x',
                    pady=10,
                    padx=100,
                )
                self.r_sign_in_btn.pack(
                    pady=5,
                )
                self.sign_up_btn.pack(
                    pady=40,
                )

                # Forget Sign In Widgets
                self.title_lbl.forget()
                self.form_frame.forget()
                self.username_lbl.forget()
                self.username_entry.forget()
                self.password_lbl.forget()
                self.password_entry.forget()
                self.forgot_password_btn.forget()
                self.l_sign_up_btn.forget()
                self.sign_in_btn.forget()
        self.iconbitmap(resource_path('assets/images/green_cat.ico'))

    def sign_up_btn_callback(self):
        username = self.r_username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.r_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if len(username) == 0:
            showwarning('Fill All Fields', 'Type a username.')
            return

        if len(email) == 0:
            showwarning('Fill All Fields', 'Type your email adress.')
            return

        if len(password) == 0:
            showwarning('Fill All Fields', 'Type a password.')
            return

        if len(confirm_password) == 0:
            showwarning('Fill All Fields', 'Confirm your password.')
            return

        if password != confirm_password:
            showerror('Passwords Don\'t match',
                      'The passwords you entered do not match.')
            return

        result = PB_Manager.register(username, email, password)

        if result is not None:
            showerror('Authentication Error',
                      result)
        else:
            # self.signin_callbck()
            PB_Manager.login(email, password)
            self.signin_callbck()

    def sign_in_btn_callback(self):
        username_or_email = self.username_entry.get().strip()
        password = self.password_entry.get()

        if len(username_or_email) == 0:
            showwarning('Fill All Fields', 'Type your username or email.')
            return

        if len(password) == 0:
            showwarning('Fill All Fields', 'Type your password.')
            return

        result = PB_Manager.login(username_or_email, password)

        if type(result) is str:
            showerror('Authentication Error',
                      'Invalid Credentials, Failed to Authenticate.')
        else:
            # showinfo('Welcome!', f'Logged In as {result.username}!')
            self.signin_callbck()

    def forgotten_password_callback(self):
        email = self.username_entry.get()
        result = PB_Manager.send_password_reset_email(email)
        if result is not None:
            showerror('Password Reset',
                      f'Failed to send Password Reset to the email: {email}')
        else:
            showinfo('Password Reset', f'Password Reset Sent to: {email}')
