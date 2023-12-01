import customtkinter as ctk

class LoginWindow(ctk.CTk):
    WIDTH = 800
    HEIGHT = 540
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('Log In')
        # self.geometry(f'{self.WIDTH}x{self.HEIGHT}')

        x = int((self.winfo_screenwidth()/2) - (self.WIDTH/2))
        y = int((self.winfo_screenheight()/2) - (self.HEIGHT/2))

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}+{x}+{y}')

        # >>> Making Widgets <<<

        # Left Frame
        self.left_frame = ctk.CTkFrame(
            master=self,
            fg_color='#B2CBBA', 
        )
        self.left_frame.pack(
            expand=True,
            fill='both',
            side='left',
        )

        # Right Frame
        self.right_frame = ctk.CTkFrame(
            master=self,
            fg_color='#DFE8D8', 
        )

        self.right_frame.pack(
            expand=True,
            fill='both',
            side='right',
        )

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

        self.title_lbl.pack(
            anchor='n',
            ipady=85
        )

        # Form Frame
        self.form_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color='transparent'
        )

        self.form_frame.pack(
            expand=False,
            fill='none',
        )

        # Username or email
        self.username_lbl = ctk.CTkLabel(
            self.form_frame, 
            text='Username or Email:',
            font=ctk.CTkFont(
                'JejuGothic',
                25,
                'normal',
            ),
            text_color='#689878'
        )
        self.username_lbl.grid(column=0, row=1)

        # Entry
        self.username_entry = ctk.CTkLabel(
            self.form_frame, 
            text='Password:',
            font=ctk.CTkFont(
                'JejuGothic',
                25,
                'normal',
            ),
            text_color='#689878'
        )
        self.username_entry.grid(column=0, row=2)



win = LoginWindow()
win.mainloop()