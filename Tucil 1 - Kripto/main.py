# Modul layar utama
# Referensi : https://gitlab.informatika.org/ChristianGunawan/rpl/-/blob/master/src/modules/mainscreen.py

# Import library
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import classiccipher

import ctypes
import pathlib
import os

# Main screen interface
class Mainscreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.create_input_box()
        self.create_output_box()
        self.create_key_box()
        self.create_file_select_button()
        self.create_crypt_button()
        self.create_cipher_option()
        self.create_view_option()
        self.create_source_option()

        self.master.geometry("540x440")
        for i in range(30):
            self.master.rowconfigure(i, weight=1)
            self.master.columnconfigure(i, weight=1)
        self.master.columnconfigure(0, weight=1000) # Digunakan untuk whitespace




    def app_loop(self):
        self.mainloop()

    def create_view_option(self):
        viewOption = [
            "full text",
            "5-char group"
            ]

        self.viewSelect = tk.StringVar(self.master)
        self.viewSelect.set(viewOption[0])
        self.viewOption = tk.OptionMenu(self.master, self.viewSelect, *viewOption)
        self.viewOption.grid(row=3, column=5)

    def create_source_option(self):
        srcOption = [
            "textbox",
            "file"
            ]

        self.srcSelect = tk.StringVar(self.master)
        self.srcSelect.set(srcOption[0])
        self.srcOption = tk.OptionMenu(self.master, self.srcSelect, *srcOption)
        self.srcOption.grid(row=2, column=5)

    def create_cipher_option(self):
        cipherOption = [
            "viginere",
            "full viginere",
            "autokey viginere",
            "extended viginere",
            "playfair",
            "affine",
            "hill"
            ]

        self.cipherSelect = tk.StringVar(self.master)
        self.cipherSelect.set(cipherOption[0])
        self.cipherOption = tk.OptionMenu(self.master, self.cipherSelect, *cipherOption)
        self.cipherOption.grid(row=5, column=5)

    def create_crypt_button(self):
        self.encrypt_button = tk.Button(self, text="Encrypt", command=self.encrypt_callback)
        self.encrypt_button.grid(row=30, column=15)
        self.decrypt_button = tk.Button(self, text="Decrypt", command=self.decrypt_callback)
        self.decrypt_button.grid(row=20, column=15)

    def create_file_select_button(self):
        self.file_button = tk.Button(self, text="Choose file", command=self.fileselect_callback)
        self.file_button.grid(row=50, column=15)
        self.file_string = tk.StringVar(self.master)
        self.file_label  = tk.Label(self, textvariable=self.file_string)
        self.file_label.grid(row=50, column=16)
        self.targetfilename = None

    def create_output_box(self):
        self.output_box = tk.Text(self.master, height=5, width=10)
        self.output_box.grid(row=40, column=10)
        self.output_box.config(state=tk.DISABLED)

    def create_input_box(self):
        self.input_box = tk.Text(self.master, height=5, width=10)
        self.input_box.grid(row=40, column=5)

    def create_key_box(self):
        self.key_box = tk.Text(self.master, height=5, width=10)
        self.key_box.grid(row=40, column=15)


    def fileselect_callback(self):
        sourcefilename = askopenfilename()
        filename = sourcefilename[sourcefilename.rfind("/") + 1:len(sourcefilename)]
        self.file_string.set(filename)
        self.targetfilename = sourcefilename

    def encrypt_callback(self):
        cipherType   = self.cipherSelect.get()
        plaintextsrc = self.srcSelect.get()
        key          = self.key_box.get("1.0", tk.END).rstrip()

        self.output_box.config(state="normal")
        self.output_box.delete("1.0", tk.END)
        if len(key) <= 0:
            self.output_box.insert(tk.END, "Invalid key")
        else:
            plaintext = ""
            filename  = ""
            if plaintextsrc == "textbox":
                plaintext = self.input_box.get("1.0", tk.END).rstrip()
            elif plaintextsrc == "file" and cipherType == "extended viginere":
                absoluteWinPath  = self.targetfilename.replace("/", "\\")
                extendedViginereBinaryBinding(absoluteWinPath, key, True)
                self.output_box.insert(tk.END, "Encryption completed")
            else:
                plaintext = getPlaintextFromFile(self.targetfilename)

            if cipherType != "extendedViginere":
                plaintext = classiccipher.alphabetSanitize(plaintext)

            ciphertext = ""
            if cipherType == "viginere":
                ciphertext = classiccipher.viginere(plaintext, key)
            elif cipherType == "full viginere":
                ciphertext = classiccipher.fullViginere(plaintext, key)
            elif cipherType == "autokey viginere":
                ciphertext = classiccipher.autoKeyViginere(plaintext, key)
            elif cipherType == "extended viginere" and plaintextsrc == "textbox":
                ciphertext = classiccipher.extendedViginere(plaintext, key)
            elif cipherType == "playfair":
                if len(key) != 25:
                    self.output_box.insert(tk.END, "Invalid playfair key")
                else:
                    playfairMatrix = classiccipher.strToKeyMatrix(key, 5)
                    ciphertext     = classiccipher.playfair(plaintext, playfairMatrix)
            elif cipherType == "affine":
                affineParam = key.split(" ")
                affineM = int(affineParam[0].rstrip())
                affineB = int(affineParam[1].rstrip())
                try:
                    ciphertext = classiccipher.affineCipher(plaintext, (affineM, affineB))
                except AssertionError:
                    self.output_box.insert(tk.END, "Invalid affine key")
            elif cipherType == "hill":
                if len(key) != 9:
                    self.output_box.insert(tk.END, "Invalid hill m=3 key")
                else:
                    hillMatrix     = classiccipher.strToKeyMatrix(key, 3)
                    ciphertext     = classiccipher.hillCipher(plaintext, hillMatrix)


            self.output_box.insert(tk.END, ciphertext)
        self.output_box.config(state=tk.DISABLED)

    def decrypt_callback(self):
        cipherType    = self.cipherSelect.get()
        ciphertextsrc = self.srcSelect.get()
        key           = self.key_box.get("1.0", tk.END).rstrip()

        self.output_box.config(state="normal")
        self.output_box.delete("1.0", tk.END)
        if len(key) <= 0:
            self.output_box.insert(tk.END, "Invalid key")
        else:
            ciphertext = ""
            filename  = ""
            if ciphertextsrc == "textbox":
                ciphertext = self.input_box.get("1.0", tk.END).rstrip()
            elif ciphertextsrc == "file" and cipherType == "extended viginere":
                absoluteWinPath  = self.targetfilename.replace("/", "\\")
                extendedViginereBinaryBinding(absoluteWinPath, key, False)
                self.output_box.insert(tk.END, "Decryption completed")
            else:
                ciphertext = getPlaintextFromFile(self.targetfilename)


            plaintext = ""
            if cipherType == "viginere":
                plaintext = classiccipher.viginere(ciphertext, key, False)
            elif cipherType == "full viginere":
                plaintext = classiccipher.fullViginere(ciphertext, key, False)
            elif cipherType == "autokey viginere":
                plaintext = classiccipher.autoKeyViginere(ciphertext, key, False)
            elif cipherType == "extended viginere" and ciphertextsrc == "textbox":
                plaintext = classiccipher.extendedViginere(ciphertext, key, False)
            elif cipherType == "playfair":
                if len(key) != 25:
                    self.output_box.insert(tk.END, "Invalid playfair key")
                else:
                    playfairMatrix = classiccipher.strToKeyMatrix(key, 5)
                    plaintext      = classiccipher.playfair(ciphertext, playfairMatrix, False)
            elif cipherType == "affine":
                affineParam = key.split(" ")
                affineM = int(affineParam[0].rstrip())
                affineB = int(affineParam[1].rstrip())
                try:
                    plaintext = classiccipher.affineCipher(ciphertext, (affineM, affineB), False)
                except AssertionError:
                    self.output_box.insert(tk.END, "Invalid affine key")
            elif cipherType == "hill":
                if len(key) != 9:
                    self.output_box.insert(tk.END, "Invalid hill key")
                else:
                    hillMatrix     = classiccipher.strToKeyMatrix(key, 3)
                    plaintext      = classiccipher.hillCipher(ciphertext, hillMatrix, False)

            self.output_box.insert(tk.END, plaintext)
        self.output_box.config(state=tk.DISABLED)











def getPlaintextFromFile(abspathsrc : str) -> str:
    plaintext = ""
    with open(abspathsrc, "r") as file:
        plaintext = file.read()
    return plaintext


def extendedViginereBinaryBinding(absolutePathSrc, key, isEncrypt):
    librarytype = ""
    if ctypes.sizeof(ctypes.c_voidp) == 4:
        librarytype = "exvig32.so"
    else:
        librarytype = "exvig64.so"

    # libname = str(pathlib.Path().absolute() / librarytype)
    os.chdir(os.getcwd())
    libname = str(os.getcwd() + "\\" + librarytype)

    c_lib   = ctypes.CDLL(libname)

    # filetype        = ".xlsx"
    # absolutePathSrc = "q" + filetype

    targetfilename = None
    encrypt        = None
    if isEncrypt:
        targetfilename = absolutePathSrc + "-enc"
        encrypt        = ctypes.c_int(1)
    else:
        targetfilename = absolutePathSrc + "-dec"
        encrypt        = ctypes.c_int(0)
    # key             = "abc"
    # encrypt         = 1

    absolutePathSrc = ctypes.c_char_p(absolutePathSrc.encode("utf-8"))
    targetfilename  = ctypes.c_char_p(targetfilename.encode("utf-8"))
    key             = ctypes.c_char_p(key.encode("utf-8"))

    retcode = c_lib.extendedViginereBinary(absolutePathSrc, targetfilename, key, encrypt)
    if retcode == 1:
        print("Cannot open source file or output file")
        exit(1)












def start_app():
    main_app = Mainscreen()
    main_app.master.title("Kripto")
    main_app.app_loop()

start_app()
