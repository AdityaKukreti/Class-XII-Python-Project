from project_module_installation_and_file_creation import *

if os.path.isfile(os.getcwd() + '/csv and text files/execution_value.txt') == False:
    make_folder()
    from project_mysql_execution import *
    execute_commands()
else:
    from project_objects import *
    cur.execute('USE project')

from tkinter import *
from project_login_and_signup import *
from project_restaurant_list import *
from project_cart import *
from project_order_history import *
from project_user_details import *
from project_sign_out import *
from send_email import smtp




label.place(relwidth = 1, relheight = 1)

canvas_1.place(relx = 0.1, rely = 0.1, relheight = 0.65, relwidth = 0.8)

if os.path.isfile(os.getcwd() + '/csv and text files/info.txt') == True:
    object_placement()
else:
    check_log_var()

restaurant_list_button.config(command = lambda : [welcome_label_1.place_forget(), welcome_label_2.place_forget(),restaurant_list()])
cart_button.config(command = lambda : [welcome_label_1.place_forget(), welcome_label_2.place_forget(),cart()])
order_history_button.config(command = lambda : [welcome_label_1.place_forget(), welcome_label_2.place_forget(),order_history()])
user_details_button.config(command = lambda : [welcome_label_1.place_forget(), welcome_label_2.place_forget(),user_details()])
sign_out_button.config(command = lambda : [welcome_label_1.place_forget(), welcome_label_2.place_forget(),sign_out()])


def on_closing_esc(event):
    global rem_info
    if os.path.isfile(os.getcwd() + '/csv and text files/info.txt') == True:
        with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
            for i in range(6):
                rem_info = pickle.load(f)
    ch = messagebox.askokcancel('Quit','Are you sure you want ot quit?')
    if ch == True:
        if smtp.quit() == False:
            smtp.quit()
        if rem_info == '0':
            try:
                os.remove(os.getcwd() + '/csv and text files/info.txt')
            except FileNotFoundError:
                pass

        root.destroy()

def on_closing():
    global rem_info
    if os.path.isfile(os.getcwd() + '/csv and text files/info.txt') == True:
        with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
            for i in range(6):
                rem_info = pickle.load(f)
    ch = messagebox.askokcancel('Quit','Are you sure you want ot quit?')
    if ch == True:
        if smtp.quit() == False:
            smtp.quit()
        if rem_info == '0':
            try:
                os.remove(os.getcwd() + '/csv and text files/info.txt')
            except FileNotFoundError:
                pass

        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.state('zoomed')
root.bind('<Escape>', on_closing_esc)
root.mainloop()
