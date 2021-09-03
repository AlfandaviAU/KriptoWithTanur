# Modul layar utama
# Referensi : https://gitlab.informatika.org/ChristianGunawan/rpl/-/blob/master/src/modules/mainscreen.py

# Import library
import tkinter as tk
from PIL import ImageTk, Image

import ctypes
import pathlib
import os


# Main screen interface
class Mainscreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # self.create_splash_screen()
        self.create_login_button()
        self.master.geometry("540x440")
        for i in range(30):
            self.master.rowconfigure(i, weight=1)
            self.master.columnconfigure(i, weight=1)
        self.master.columnconfigure(0, weight=1000) # Digunakan untuk whitespace

    def app_loop(self):
        self.mainloop()

    def create_login_button(self):
        self.login_button = tk.Button(self, text="Login", command=lambda:core.login.login_window(self))
        self.login_button.grid(row=50, column=15)

    # def create_splash_screen(self):
        # my_pic = Image.open("../img/barbell.gif")
        # resized = my_pic.resize((250,250), Image.ANTIALIAS)
        # image_splash = ImageTk.PhotoImage(resized)
        # splash_label = tk.Label(self, image=image_splash)
        # splash_label.image = image_splash
        # splash_label.grid(row = 4,column = 15,padx = 10, pady = 30)

    def login_success_procedure(self, login_window_obj, login_username, account_type):
        login_window_obj.login_exit_protocol()
        core.mainmenu.switch_to_mainmenu(self, login_username, account_type)





def start_app():
    main_app = Mainscreen()
    main_app.master.title("Kripto")
    main_app.app_loop()

start_app()








# librarytype = ""
# if ctypes.sizeof(ctypes.c_voidp) == 4:
#     librarytype = "exvig32.so"
# else:
#     librarytype = "exvig64.so"
#
# # libname = str(pathlib.Path().absolute() / librarytype)
# os.chdir(os.getcwd())
# libname = str(os.getcwd() + "\\" + librarytype)
#
# c_lib = ctypes.CDLL(libname)
#
# filetype       = ".xlsx"
# sourcefilename = "q" + filetype
# targetfilename = "enctext" + filetype
# key            = "abc"
# encrypt        = 1
#
# sourcefilename = ctypes.c_char_p(sourcefilename.encode("utf-8"))
# targetfilename = ctypes.c_char_p(targetfilename.encode("utf-8"))
# key            = ctypes.c_char_p(key.encode("utf-8"))
# encrypt        = ctypes.c_int(encrypt)
#
# c_lib.extendedViginereBinary(sourcefilename, targetfilename, key, encrypt)
#
# c_lib.extendedViginereBinary(targetfilename, ctypes.c_char_p(("decrypt" + filetype).encode("utf-8")), key, not encrypt)
