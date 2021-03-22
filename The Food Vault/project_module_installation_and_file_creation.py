import os
import subprocess
from tkinter import *
import pickle
from project_encryption_and_decryption import *


def make_folder():
    subprocess.call([os.getcwd() + '/bat file/module installation.bat'])
    os.makedirs(os.getcwd() + '/Invoice')

    def pass_file():
        with open(os.getcwd() + '/csv and text files/pass file.txt','wb') as f:
            pickle.dump(encrypt(user_entry.get()), f)
            pickle.dump(encrypt(host_entry.get()), f)
            pickle.dump(encrypt(pass_entry.get()), f)
        my_pass.destroy()

    my_pass = Tk()
    my_pass.title('Enter your MySQL password')
    my_pass.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
    my_pass.geometry('600x200')
    my_pass.transient()

    canvas = Canvas(my_pass, bg = '#b2d9ed')
    canvas.place(relheight = 1, relwidth = 1)

    Label(canvas, text = 'Enter your MySQL username:', font = 'Arial 13 bold', bg = '#b2d9ed').place(relx = 0.05, rely = 0.2)

    user_entry = Entry(canvas, width = 25, font = 'Arial 13')
    user_entry.place(relx = 0.5, rely = 0.2, relheight = 0.1)

    Label(canvas, text = 'Enter your MySQL host:', font = 'Arial 13 bold', bg = '#b2d9ed').place(relx = 0.05, rely = 0.4)

    host_entry = Entry(canvas, width = 25, font = 'Arial 13')
    host_entry.place(relx = 0.5, rely = 0.4, relheight = 0.1)

    Label(canvas, text = 'Enter your MySQL password:', font = 'Arial 13 bold', bg = '#b2d9ed').place(relx = 0.05, rely = 0.6)

    pass_entry = Entry(canvas, width = 25, show = '*', font = 'Arial 13')
    pass_entry.place(relx = 0.5, rely = 0.6, relheight = 0.1)


    pass_button = Button(canvas, text = 'Submit', border = 0, bg = 'white', activebackground = '#cfd1d1', command = pass_file)
    pass_button.place(relx = 0.35, rely = 0.8, relwidth = 0.3, relheight = 0.15)

    my_pass.mainloop()

    with open(os.getcwd() + '/csv and text files/execution_value.txt','w') as f:
        f.write('!!!!!THIS FILE IS CREATED ON THE FIRST EXECUTION OF THE PROGRAM!!!!!\n')
        f.write('!!!!!DO NOT DELETE THIS OR ANY FILE!!!!!!\n')
        f.write('!!!!!IF DELETED THEN THE PROGRAM WILL NOT WORK!!!!!!')
