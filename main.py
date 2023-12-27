from customtkinter import set_appearance_mode
from login_system.pb_conn import PB_Manager
from widgets.main_window import MainWindow


def main():
    set_appearance_mode('light')

    PB_Manager.Initialize()

    MainWindow().mainloop()


if __name__ == '__main__':
    main()
