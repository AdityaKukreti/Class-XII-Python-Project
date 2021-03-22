from project_objects import *
from tkinter import *
from project_invoice_creation import *


def download_all_invoice():

    global placed_orders_treeview

    for z in placed_orders_treeview.get_children():
        o_id = placed_orders_treeview.item(z)['values'][0]


        file_no = 1

        while True:
            if os.path.isfile(os.getcwd() + '/Invoice/Invoice_' + str(file_no) + '.pdf') is True:
                file_no += 1
            else:
                break

        t = threading.Thread(target = create_invoice, args = (o_id,file_no))
        t.start()            

    messagebox.showinfo('Success','Your invoices have been downloaded successfully!')

def download_invoice():
    
    global placed_orders_treeview

    d = placed_orders_treeview.focus()

    try:
        o_id = placed_orders_treeview.item(d)['values'][0]
        file_no = 1

        while True:
            if os.path.isfile(os.getcwd() + '/Invoice/Invoice_' + str(file_no) + '.pdf') is True:
                file_no += 1
            else:
                break

        t = threading.Thread(target = create_invoice, args = (o_id,file_no))
        t.start()
        
        messagebox.showinfo('Success','Your invoice has been downloaded successfully!')
    except IndexError:
        messagebox.showerror('Error','Select an Invoice')

    
        

def order_history():

    rest_head.place_forget()
    menu_head.place_forget()
    cart_head.place_forget()
    ord_head.place_forget()
    user_head.place_forget()

    hist_head.place(relx = 0.04, rely = 0.12)

    frame_1.place_forget()
    frame_2.place_forget()
    frame_5.place_forget()
    frame_8.place_forget()
    frame_14.place_forget()

    welcome_label_1.place_forget()
    welcome_label_2.place_forget()

    restaurant_list_button.config(bg = 'white')
    cart_button.config(bg = 'white')
    order_history_button.config(bg = '#b3fff6')
    user_details_button.config(bg = 'white')
    sign_out_button.config(bg = 'white')

    for i in placed_orders_treeview.get_children():
        placed_orders_treeview.delete(i)

    for i in details_treeview.get_children():
        details_treeview.delete(i)

    

    def open_details(event):
        
        ord_head.place(relx = 0.6, rely = 0.12)
        
        def close_frame():
            ord_head.place_forget()
            frame_12.place_forget()

        for i in details_treeview.get_children():
            details_treeview.delete(i)
        
        try:
            order_id = placed_orders_treeview.item(placed_orders_treeview.focus())['values'][0]
        except IndexError:
            pass

        try:    
            cur.execute('SELECT * FROM `user orders` WHERE `order id` = %s',(order_id,))
        except UnboundLocalError:
            pass
        
        for i in cur:
            name = i[2]
            phone_number = i[3]
            address = i[4]
            rest_name_ord = i[5]
            order_date = i[9]
            amt = 'Rs ' + i[10]

            ord_item = i[6].split(',')
            ord_item.pop()

            ord_quantity = i[7].split(',')
            ord_quantity.pop()

            ord_price = i[8].split(',')
            ord_price.pop()

        for i in range (len(ord_item)):
            details_treeview.insert(parent = '', text = '', iid = i, index = END, values = (ord_item[i],ord_quantity[i],ord_price[i]))
    
        ord_name_entry = Entry(frame_12, width = 24, font = '1')
        ord_name_entry.insert(END, name)
        ord_name_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        ord_name_entry.place(relx = 0.35, rely = 0, relheight = 0.06)

        ord_number_entry = Entry(frame_12, width = 24, font = '1')
        ord_number_entry.insert(END, phone_number)
        ord_number_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        ord_number_entry.place(relx = 0.35, rely = 0.06, relheight = 0.06)

        ord_address_entry = Entry(frame_12, width = 24, font = '1')
        ord_address_entry.insert(END, address)
        ord_address_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        ord_address_entry.place(relx = 0.35, rely = 0.12, relheight = 0.06)    
        
        ord_rest_entry = Entry(frame_12, width = 24, font = '1')
        ord_rest_entry.insert(END, rest_name_ord)
        ord_rest_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        ord_rest_entry.place(relx = 0.35, rely = 0.18, relheight = 0.06)

        ord_date_entry = Entry(frame_12, width = 24, font = '1')
        ord_date_entry.insert(END, order_date)
        ord_date_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        ord_date_entry.place(relx = 0.35, rely = 0.24, relheight = 0.06)


        ord_amt_entry = Entry(frame_12, width = 24, font = '1')
        ord_amt_entry.insert(END, amt)
        ord_amt_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        ord_amt_entry.place(relx = 0.35, rely = 0.64, relheight = 0.06)




        details_treeview.place(relheight = 1, relwidth = 0.96)
        frame_12.place(relx = 0.6, rely = 0.22, relheight = 0.8, relwidth = 0.4)
        frame_13.place(rely = 0.32, relheight = 0.3, relwidth = 0.9)

        Button(frame_12, text = 'Close', bg = 'white', activebackground = '#b3fff6', command = close_frame, border = 0, cursor = 'hand2').place(relx = 0.3, rely = 0.8, relheight = 0.07, relwidth = 0.3)


    placed_orders_treeview.place(relheight = 1, relwidth = 0.97)

    email = ''
    with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
            for i in range(2):
                pickle.load(f)
            email = decrypt(pickle.load(f))

    cur.execute('SELECT `order id`,`restaurant name`,`date`,`status` FROM `user orders` where `email` = %s',(email,))
    count = 0
    for i in cur:
        placed_orders_treeview.insert(parent = '', index = 0, iid = count, text = '', values = (i[0],i[1],i[2],i[3]))
        count += 1

    placed_orders_treeview.bind('<Double-1>', open_details)

    frame_11.place(relx = 0, rely = 0, relheight = 0.4, relwidth = 1)
    frame_10.place(relx = 0.04, rely = 0.22, relwidth = 0.5, relheight = 0.8)

    Button(frame_10, text = 'Download Selected Invoice', bg = 'white', activebackground = '#b3fff6', border = 0, command = download_invoice, cursor = 'hand2').place(relx = 0.15, rely = 0.7, relheight = 0.07, relwidth = 0.3)
    Button(frame_10, text = 'Download All Invoice', bg = 'white', activebackground = '#b3fff6', border = 0, command = download_all_invoice, cursor = 'hand2').place(relx = 0.55, rely = 0.7, relheight = 0.07, relwidth = 0.3)
    
   
