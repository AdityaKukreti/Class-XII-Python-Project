from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import os
import csv
import pickle
import random
from datetime import date
from project_encryption_and_decryption import *
import threading

# MySql Variables

with open(os.getcwd() + '/csv and text files/pass file.txt','rb') as f:
    my_user = decrypt(pickle.load(f))
    my_host = decrypt(pickle.load(f))
    my_pass = decrypt(pickle.load(f))


db = mysql.connector.connect(user = '{username}'.format(username = my_user), host = '{host}'.format(host = my_host), passwd = '{password}'.format(password = my_pass))
cur = db.cursor()


log_var = 0
first_name = ''

# MAIN SCREEN

# Main Screen Declaration
root = Tk()
root.geometry('1920x1080')
root.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
root.title('The Food Vault')
style = ttk.Style()
style.theme_use('clam')

background = PhotoImage(file = os.getcwd() + '/Background and Icon/629222.png') 
label = Label(root, image = background)

event_val = ''

# Main Screen Canvas
canvas_1 = Canvas(root, bg = '#34aeeb')
canvas_2 = Canvas(root, bg = '#34aeeb')


# Main Function

def object_placement():
    global log_var
    global first_name
    global rem_info

    canvas_2.place(relx = 0.1, rely = 0.8, relheight = 0.07, relwidth = 0.8)

    with open(os.getcwd() + '/csv and text files/info.txt','rb') as f: 
        first_name = decrypt(pickle.load(f))
        for i in range(4):
            pickle.load(f)
        rem_info = pickle.load(f)

    welcome_label_1.config(text = 'Welcome ' + first_name + '!')
    welcome_label_1.place(relx = 0.4, rely = 0.4)
    welcome_label_2.place(relx = 0.285, rely = 0.5)

    restaurant_list_button.place(relx = 0.025, rely = 0.2, relheight = 0.6, relwidth = 0.15)

    cart_button.place(relx = 0.225, rely = 0.2, relheight = 0.6, relwidth = 0.15)

    order_history_button.place(relx = 0.425, rely = 0.2, relheight = 0.6, relwidth = 0.15)

    user_details_button.place(relx = 0.625, rely = 0.2, relheight = 0.6, relwidth = 0.15)

    sign_out_button.place(relx = 0.825, rely = 0.2, relheight = 0.6, relwidth = 0.15)


# Main Screen Label
welcome_label_1 = Label(canvas_1, text = 'Welcome ' + first_name + '!', font = 'Sans 20 bold', bg = '#34aeeb')
welcome_label_2 = Label(canvas_1, text = ' Select one of the options from below!', font = 'Arial 20 bold', bg = '#34aeeb')


# Main Screen Buttons
restaurant_list_button = Button(canvas_2, text = 'Restaurant List', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
cart_button = Button(canvas_2, text = 'Cart', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
order_history_button = Button(canvas_2, text = 'Order History', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
user_details_button = Button(canvas_2, text = 'User Details', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
sign_out_button = Button(canvas_2, text = 'Sign Out', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')


# LOGIN 

# Login Variable
rem_info = IntVar()
# Login Labels
login_label = Label(canvas_1, text = 'Login', font = 'Arial 35 bold', bg = '#34aeeb')
forgot_password_button = Button(canvas_1, text = 'Forgot password?', font = 'Arial 13', bg = '#34aeeb',border = 0, activebackground = '#34aeeb', cursor = 'hand2')

email_login_label = Label(canvas_1, text = 'Email :        ',font = 'Arial 15 bold', bg = '#34aeeb')
password_login_label = Label(canvas_1, text = 'Password :  ', font = 'Arial 15 bold', bg = '#34aeeb')

label_0 = Label(canvas_1, text = "Don't have an account?", font = 'Arial 12 bold', bg = '#34aeeb')

# Login Entry Fields
email_login_entry = Entry(canvas_1, width = 200, font = 'Arial 13')
password_login_entry = Entry(canvas_1, width = 200,show = '*', font = 'Arial 13')

# Login Checkbox
rem_info_checkbox = Checkbutton(canvas_1, text = 'Keep me signed in',font = 'Arial 13', variable = rem_info, activebackground = '#34aeeb', bg = '#34aeeb', cursor = 'hand2')

# Login Buttons
login_button = Button(canvas_1, text = 'Login', border = 0, font = 'Arial 10', bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
signup_button = Button(canvas_1, text = 'Sign up', border = 0, font = 'Arial 10', bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')


# SIGNUP

# Signup Labels
signup_label = Label(canvas_1, text = 'Sign up', font = 'Arial 35 bold', bg = '#34aeeb')

first_name_signup_label = Label(canvas_1 ,text = 'First Name :',font = 'Arial 15 bold', bg = '#34aeeb')
last_name_signup_label = Label(canvas_1 ,text = 'Last Name :',font = 'Arial 15 bold', bg = '#34aeeb')

email_signup_label = Label(canvas_1 , text = 'Email :', font = 'Arial 15 bold', bg = '#34aeeb')
reenter_email_signup_label = Label(canvas_1 ,text = 'Re-enter email :',font = 'Arial 15 bold', bg = '#34aeeb')

password_signup_label = Label(canvas_1 ,text = 'Password :',font = 'Arial 15 bold', bg = '#34aeeb')
reenter_password_signup_label = Label(canvas_1 , text = 'Re-enter password :', font = 'Arial 15 bold', bg = '#34aeeb')

address_signup_label = Label(canvas_1 , text = 'Address :', font = 'Arial 15 bold', bg = '#34aeeb')
number_signup_label = Label(canvas_1 , text = 'Mobile no. :', font = 'Arial 15 bold', bg = '#34aeeb')

label_2 = Label(canvas_1, text = "Already have an account?", font = 'Arial 12 bold', bg = '#34aeeb')

# Signup Entry Fields

first_name_signup_entry = Entry(canvas_1 , width = 50, font = 'Arial 13')
last_name_signup_entry = Entry(canvas_1 , width = 50, font = 'Arial 13')

email_signup_entry = Entry(canvas_1 , width = 50, font = 'Arial 13')
reenter_email_signup_entry = Entry(canvas_1 , width = 50, font = 'Arial 13')

password_signup_entry = Entry(canvas_1 , width = 50, show = '*', font = 'Arial 13')
reenter_password_signup_entry = Entry(canvas_1 , width = 50, show = '*', font = 'Arial 13')

address_signup_entry = Entry(canvas_1 , width = 50, font = 'Arial 13')
number_signup_entry = Entry(canvas_1 , width = 50, font = 'Arial 13')

# Signup Buttons
register_screen_button = Button(canvas_1 , text = 'Register', border = 0, font = 'Arial 10', bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
login_screen_button = Button(canvas_1 , text = 'Login', border = 0, font = 'Arial 10', bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')




# RESTAURANT LIST PAGE

# Restaurant List Variables
count_2 = 0

# Heading

rest_head = Label(canvas_1, text = 'Restaurant List', font = 'Arial 20 bold', bg = '#34aeeb')
menu_head = Label(canvas_1, text = 'Menu', font = 'Arial 20 bold', bg = '#34aeeb')

# Restaurant List Frames
frame_1 = Frame(canvas_1, bg = '#34aeeb')
frame_2 = Frame(canvas_1, bg = '#34aeeb')
frame_3 = Frame(frame_2)
frame_4 = Frame(frame_2)


# Restaurant List Treeview
treeview_scrollbar = Scrollbar(frame_1)
treeview_scrollbar.pack(side = RIGHT, fill = Y)

rest_info_treeview = ttk.Treeview(frame_1, yscrollcommand = treeview_scrollbar.set)
treeview_scrollbar.config(command = rest_info_treeview.yview)


rest_info_treeview['columns'] = ('Name', 'Establishment Type', 'Cuisines')

rest_info_treeview.column('#0', width = 0, stretch = 0)
rest_info_treeview.column('Name',  width = 0, minwidth= 190, anchor = W)
rest_info_treeview.column('Establishment Type', width = 0, minwidth = 100, anchor = W)
rest_info_treeview.column('Cuisines', width = 150, minwidth = 50, anchor = W)

rest_info_treeview.heading('#0', text = '', anchor = W)
rest_info_treeview.heading('Name', text = 'Name', anchor = W)
rest_info_treeview.heading('Establishment Type', text = 'Establishment Type', anchor = W)
rest_info_treeview.heading('Cuisines', text = 'Cuisines', anchor = W)

rest_info_treeview.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.977)



# Restaurant List Buttons
remove_button = Button(frame_2, text = 'Remove Item', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')
add_button = Button(frame_2, text = 'Add Items to cart', border = 0, bg = 'white', activebackground = '#b3fff6', cursor = 'hand2')



# Cart Frames
frame_5 = Frame(canvas_1, bg = '#34aeeb')
frame_6 = Frame(frame_5)
frame_7 = Frame(frame_5, bg = 'white')
frame_8 = Frame(canvas_1, bg = '#34aeeb')
frame_9 = Frame(frame_8)

# Heading

cart_head = Label(canvas_1, text = 'Cart', font = 'Arial 20 bold', bg = '#34aeeb')
ord_head = Label(canvas_1, text = 'Order Details', font = 'Arial 20 bold', bg = '#34aeeb')

# Cart Emoji
emoji = PhotoImage(file = os.getcwd() + '/Background and Icon/grinning.png') 
label_1 = Label(frame_5, image = emoji, border = 0)

order_placed_label_1 = Label(frame_5, text = 'Your Order has been placed successfully!', font = 'Arial 30 bold', bg = '#34aeeb')



# Cart Variable
count_0 = 0

# Cart Buttons
place_order_button = Button(frame_5, text = 'Place Order', border = 0, activebackground = '#b3fff6', bg = 'white', cursor = 'hand2')
clear_cart_button = Button(frame_5, text = 'Clear Cart', border = 0, activebackground = '#b3fff6', bg = 'white', cursor = 'hand2')

# Cart Labels
no_item_label_1 = Label(frame_5, text = 'Oops! It seems your cart is empty!', font = 'Arial 20 bold', bg = '#34aeeb')
no_item_label_2 = Label(frame_5, text = 'Please add some items to your cart first!', font = 'Arial 20 bold', bg = '#34aeeb')


# Cart Treeview
menu_treeview_scrollbar = Scrollbar(frame_6)
menu_treeview_scrollbar.pack(side = RIGHT, fill = Y)

menu_treeview = ttk.Treeview(frame_6, yscrollcommand = menu_treeview_scrollbar.set, selectmode = NONE)
menu_treeview_scrollbar.config(command = menu_treeview.yview)

menu_treeview['columns'] = ('Item', 'Quantity', 'Price')

menu_treeview.column('#0', width = 0, stretch = 0)
menu_treeview.column('Item', width = 50, minwidth = 50, anchor = W)
menu_treeview.column('Quantity', width = 50, minwidth = 0, anchor = W)
menu_treeview.column('Price', width = 40, minwidth = 40, anchor = W)

menu_treeview.heading('#0', text = '', anchor = W)
menu_treeview.heading('Item', text = 'Item', anchor = W)
menu_treeview.heading('Quantity', text = 'Quantity', anchor = W)
menu_treeview.heading('Price', text = 'Price', anchor = W)

menu_treeview.place(relheight = 1, relwidth = 0.972)

# Place Order Treeview

place_order_treeview_scrollbar = Scrollbar(frame_9)
place_order_treeview_scrollbar.pack(side = RIGHT, fill = Y)

place_order_treeview = ttk.Treeview(frame_9, yscrollcommand = place_order_treeview_scrollbar.set)
place_order_treeview_scrollbar.config(command = place_order_treeview.yview)
place_order_treeview['columns'] = ('Item', 'Quantity', 'Price')

place_order_treeview.column('#0', width = 0, stretch = 0)
place_order_treeview.column('Item', width = 150, minwidth = 40, anchor = W)
place_order_treeview.column('Quantity', width = 60, minwidth = 40, anchor = W)
place_order_treeview.column('Price', width = 60, minwidth = 40, anchor = W)


place_order_treeview.heading('#0', text = '', anchor = W)
place_order_treeview.heading('Item', text = 'Item', anchor = W)
place_order_treeview.heading('Quantity', text = 'Quantity', anchor = W)
place_order_treeview.heading('Price', text = 'Price', anchor = W)



# Place Order Labels
Label(frame_8, text = 'Customer Name :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0, relheight = 0.05)

Label(frame_8, text = 'Mobile Number :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.05, relheight = 0.05)

Label(frame_8, text = 'Delivery Address :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.1, relheight = 0.05)

Label(frame_8, text = 'Restaurant Name :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.15, relheight = 0.05)

Label(frame_8, text = 'Order Date :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.2, relheight = 0.05)

Label(frame_8, text = 'Amount Payable :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.6 , relheight = 0.05)

# Place Order Buttons

confirm_and_proceed_button = Button(frame_8, text = 'Confirm and Proceed', border = 0, activebackground = '#b3fff6', bg = 'white', cursor = 'hand2')
cancel_button = Button(frame_8, text = 'Cancel', border = 0, activebackground = '#b3fff6', bg = 'white', cursor = 'hand2')


# Order History Frames
frame_10 = Frame(canvas_1, bg = '#34aeeb')
frame_11 = Frame(frame_10)
frame_12 = Frame(canvas_1, bg = '#34aeeb')
frame_13 = Frame(frame_12)

# Heading
hist_head = Label(canvas_1, text = 'Order History', font = 'Arial 20 bold', bg = '#34aeeb')

# Order History Main Treeview
placed_order_treeview_scrollbar = Scrollbar(frame_11)
placed_order_treeview_scrollbar.pack(side = RIGHT, fill = Y)


placed_orders_treeview = ttk.Treeview(frame_11, yscrollcommand = placed_order_treeview_scrollbar.set)
placed_order_treeview_scrollbar.config(command = placed_orders_treeview.yview)

placed_orders_treeview['columns'] = ('Order id','Restaurant Name', 'Date', 'Status')

placed_orders_treeview.column('#0', width = 0, stretch = 0)
placed_orders_treeview.column('Order id', width = 50, minwidth = 50, anchor = W)
placed_orders_treeview.column('Restaurant Name', width = 140, minwidth = 50, anchor = W)
placed_orders_treeview.column('Date', width = 40, minwidth = 40, anchor = W)
placed_orders_treeview.column('Status', width = 50, minwidth = 50, anchor = W)

placed_orders_treeview.heading('#0', text = '', anchor = W)
placed_orders_treeview.heading('Order id', text = 'Order id', anchor = W)
placed_orders_treeview.heading('Restaurant Name', text = 'Restaurant Name', anchor = W)
placed_orders_treeview.heading('Date', text = 'Date', anchor = W)
placed_orders_treeview.heading('Status', text = 'Status', anchor = W)


# Order History Details Treeview

details_treeview_scrollbar = Scrollbar(frame_13)
details_treeview_scrollbar.pack(side = RIGHT, fill = Y)

details_treeview = ttk.Treeview(frame_13, yscrollcommand = details_treeview_scrollbar.set)
details_treeview_scrollbar.config(command = details_treeview.yview)
details_treeview['columns'] = ('Item', 'Quantity', 'Price')

details_treeview.column('#0', width = 0, stretch = 0)
details_treeview.column('Item', width = 150, minwidth = 40, anchor = W)
details_treeview.column('Price', width = 60, minwidth = 40, anchor = W)
details_treeview.column('Quantity', width = 60, minwidth = 40, anchor = W)

details_treeview.heading('#0', text = '', anchor = W)
details_treeview.heading('Item', text = 'Item', anchor = W)
details_treeview.heading('Price', text = 'Price', anchor = W)
details_treeview.heading('Quantity', text = 'Quantity', anchor = W)


# Order History Details Labels

Label(frame_12, text = 'Customer Name :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0, relheight = 0.05)

Label(frame_12, text = 'Mobile Number :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.06, relheight = 0.05)

Label(frame_12, text = 'Delivery Address :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.12, relheight = 0.05)

Label(frame_12, text = 'Restaurant Name :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.18, relheight = 0.05)

Label(frame_12, text = 'Order Date :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.24, relheight = 0.05)

Label(frame_12, text = 'Amount Payable :', font = 'Arial 13 bold', bg = '#34aeeb').place(relx = 0, rely = 0.64 , relheight = 0.05)


# USER DETAILS PAGE

# Heading

user_head = Label(canvas_1, text = 'User Details', font = 'Arial 20 bold', bg = '#34aeeb')

# User Details Frames
frame_14 = Frame(canvas_1, bg = '#34aeeb')
frame_15 = Frame(frame_14)

# User Details Labels and Entries
email_account_label = Label(frame_14, text = 'Email :', font = 'Arial 15 bold', bg = '#34aeeb')
email_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')

password_account_label = Label(frame_14,text = 'Password :',font = 'Arial 15 bold', bg = '#34aeeb')
password_account_entry = Entry(frame_14, width = 50, show = '*', font = 'Arial 15')
    
first_name_account_label = Label(frame_14, text = 'First Name :', font = 'Arial 15 bold', bg = '#34aeeb')
first_name_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')

last_name_account_label = Label(frame_14, text = 'Last Name :', font = 'Arial 15 bold', bg = '#34aeeb')
last_name_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')

phone_number_account_label = Label(frame_14, text = 'Mobile no :', font = 'Arial 15 bold', bg = '#34aeeb')
phone_number_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')
    
# User Details Address Treeview
address_treeview_scrollbar = Scrollbar(frame_15)
address_treeview_scrollbar.pack(side = RIGHT, fill = Y)


address_treeview = ttk.Treeview(frame_15, yscrollcommand = address_treeview_scrollbar.set)
address_treeview_scrollbar.config(command = address_treeview.yview)

address_treeview['columns'] = ('Sno', 'Address')

address_treeview.column('#0', width = 0, stretch = 0)
address_treeview.column('Sno', width = 2, minwidth = 0, anchor = W)
address_treeview.column('Address', width = 200, minwidth = 40, anchor = W)

address_treeview.heading('#0', text = '', anchor = W)
address_treeview.heading('Sno', text = 'Sno', anchor = W)
address_treeview.heading('Address', text = 'Address', anchor = W)

    
# User Details Variables
count_1 = 0
count_3 = 0