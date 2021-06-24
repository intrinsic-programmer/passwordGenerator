from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator")

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()

length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 15).pack()
pass_str = StringVar()

def Generator():
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    possibilities = []
    possibilities.extend(list(letters))
    possibilities.extend(list(digits))
    possibilities.extend(list(special_char))
    random.shuffle(possibilities)
    password = "".join(possibilities[0:pass_len.get()])
    pass_str.set(password)

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

root.mainloop()