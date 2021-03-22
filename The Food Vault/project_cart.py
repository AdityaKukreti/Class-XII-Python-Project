from tkinter import *
import pickle
from project_objects import *
from send_email import order_placed_email
from datetime import datetime


def cart():

    for i in menu_treeview.get_children():
        menu_treeview.delete(i)

    for i in place_order_treeview.get_children():
        place_order_treeview.delete(i)


    def cancel():
        ord_head.place_forget()
        frame_8.place_forget()

    
    def clear_cart():

        choice = messagebox.askyesno('Confirm','Are you sure you want to clear the cart?')
        if choice == True:

            cart_head.place_forget()
            ord_head.place_forget()

            for i in menu_treeview.get_children():
                menu_treeview.delete(i)

            for i in place_order_treeview.get_children():
                place_order_treeview.delete(i)


            if os.path.isfile(os.getcwd() + '/csv and text files/item.csv') == True:
                os.remove(os.getcwd() + '/csv and text files/item.csv')

            frame_5.place_forget()
            frame_6.place_forget()
            frame_7.place_forget()
            frame_8.place_forget()

            place_order_button.place_forget()
            clear_cart_button.place_forget()

            no_item_label_1.place(relx = 0.3, rely = 0.4)
            no_item_label_2.place(relx = 0.27, rely = 0.5)

            frame_5.place(relheight = 1, relwidth = 1)


    def place_order():
        ord_head.place(relx = 0.6, rely = 0.12)

        def confirm_and_place_order():
            def move_items_to_db():
                items = ''
                prices = ''
                quantities = ''
                email = StringVar
                rest_name = rest_entry.get()
                status = 'Pending'
                order_date = str(date.today())

                with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
                    for i in range(2):
                        pickle.load(f)
                    email = decrypt(pickle.load(f))

                for i in place_order_treeview.get_children():
                    items = items + str(place_order_treeview.item(i, 'values')[0]) + ','
                    quantities = quantities + str(place_order_treeview.item(i, 'values')[1]) + ','
                    prices = prices + str(place_order_treeview.item(i, 'values')[2]) + ','

                cur.execute('SELECT `address`,`phone no.` FROM `rest info` WHERE `rest name` = %s',(rest_name,))
                for i in cur:
                    address = i[0]
                    number = i[1]
                cur.execute('INSERT INTO `user orders` (`email`,`customer name`,`mobile number`,`delivery address`,`restaurant name`,`items`,`quantity`,`prices`,`date`,`amount payable`,`status`,`address`,`number`,`time`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (email,name_entry.get(),number_entry.get(),combobox.get(),rest_name,items,quantities,prices,order_date,(price + (price * 0.18)),status,address,number,str(datetime.now().strftime("%H:%M:%S"))))
                db.commit()

            confirm = messagebox.askyesno('Confirmation','Are you sure you want to place order?')
            if confirm == True:
                if combobox.get() == 'Select Address':
                    messagebox.showerror('Invalid','Select an address first.')
                else:
                    cart_head.place_forget()
                    ord_head.place_forget()
                    move_items_to_db()
                    frame_8.place_forget()
                    for i in place_order_treeview.get_children():
                        place_order_treeview.delete(i)

                    
                    os.remove(os.getcwd() + '/csv and text files/item.csv')
                    frame_5.place_forget()
                    frame_6.place_forget()
                    frame_7.place_forget()
                    frame_8.place_forget()
                    place_order_button.place_forget()
                    clear_cart_button.place_forget()
                    
                    order_placed_label_1.place(relx = 0.2, rely = 0.4)    
                    label_1.place(relx = 0.45, rely = 0.47)


                    frame_5.place(relheight = 1, relwidth = 1)
                    
                    cur.execute('SELECT `order id` FROM `user orders` WHERE `email` = %s',(email,))
                    
                    id = ''

                    for i in cur:
                        id = i[0]

                    with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
                        name = decrypt(pickle.load(f))
                    
                    t = threading.Thread(target = order_placed_email, args = (id,name,email))
                    t.start()



        place_order_treeview.place(relheight = 1, relwidth = 0.96)
        frame_9.place(relx = 0, rely = 0.275, relwidth = 1, relheight = 0.3)
        frame_8.place(relx = 0.6, rely = 0.22, relheight = 0.9, relwidth = 0.35)

        count_0 = 0
        for i in cart_items_dict:
            value = [i]
            for j in cart_items_dict.get(i):
                value.append(int(j))
            place_order_treeview.insert(parent = '', text = '', iid = count_0, index = 0, values = [value[0],value[2],value[1]])
            count_0 += 1

        with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
            first_name = decrypt(pickle.load(f))
            last_name = decrypt(pickle.load(f))
            email = decrypt(pickle.load(f))
            pickle.load(f)
            phone_number = decrypt(pickle.load(f))

        name_entry = Entry(frame_8, width = 30, font = '1')
        name_entry.insert(END, first_name + ' ' + last_name)
        name_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        name_entry.place(relx = 0.4, rely = 0, relheight = 0.05)

        number_entry = Entry(frame_8, width = 30, font = '1')
        number_entry.insert(END, phone_number)
        number_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        number_entry.place(relx = 0.4, rely = 0.05, relheight = 0.05)

        cur.execute('SELECT `address` FROM `user addresses` WHERE `email` = %s',(email,))
        options = ['Select Address']
        for i in cur:
            options.append(i[0])

        combobox = ttk.Combobox(frame_8, value = options, font = '1')        
        combobox.current(0)
        combobox.place(relx = 0.4, rely = 0.1, relwidth = 0.6, relheight = 0.05)

        
        rest_entry = Entry(frame_8, width = 30, font = '1')
        rest_entry.insert(END, rest_name)
        rest_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        rest_entry.place(relx = 0.4, rely = 0.15, relheight = 0.05)

        date_entry = Entry(frame_8, width = 30, font = '1')
        date_entry.insert(END, date.today())
        date_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        date_entry.place(relx = 0.4, rely = 0.2, relheight = 0.05)


        amt_entry = Entry(frame_8, width = 30, font = '1')
        amt_entry.insert(END, 'Rs ' + str(grand_total_calc_entry.get()))
        amt_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        amt_entry.place(relx = 0.4, rely = 0.6, relheight = 0.05)

        confirm_and_proceed_button.place(relx = 0.15, rely = 0.7, relheight = 0.07, relwidth = 0.35)
        cancel_button.place(relx = 0.55, rely = 0.7, relheight = 0.07, relwidth = 0.35)

        confirm_and_proceed_button.config(command = confirm_and_place_order)
        cancel_button.config(command = cancel)


    rest_head.place_forget()
    menu_head.place_forget()
    ord_head.place_forget()
    hist_head.place_forget()
    user_head.place_forget()

    frame_1.place_forget()
    frame_2.place_forget()
    frame_5.place_forget()
    frame_10.place_forget()
    frame_12.place_forget()
    frame_14.place_forget()

    welcome_label_1.place_forget()
    welcome_label_2.place_forget()

    no_item_label_1.place_forget()
    no_item_label_2.place_forget()



    restaurant_list_button.config(bg = 'white')
    cart_button.config(bg = '#b3fff6')
    order_history_button.config(bg = 'white')
    user_details_button.config(bg = 'white')
    sign_out_button.config(bg = 'white')


    cart_items_dict = {}
    rest_name = StringVar

    if os.path.isfile(os.getcwd() + '/csv and text files/item.csv') == True:
        with open(os.getcwd() + '/csv and text files/item.csv','r') as f:
            csv_reader = csv.reader(f)
            for i in csv_reader:
                if len(i) == 1:
                    rest_name = i[0]
                elif len(i) == 3:
                    cart_items_dict[i[0]] = i[1:3]

        cart_head.place(relx = 0.04, rely = 0.12)


        count_0 = 0
        for i in cart_items_dict:
            value = [i]
            for j in cart_items_dict.get(i):
                value.append(int(j))
            menu_treeview.insert(parent = '', text = '', iid = count_0, index = 0, values = [value[0],value[2],value[1]])
            count_0 += 1

        Label(frame_7, text = '__________________________________________________', font = 'Arial 15 bold', bg = 'white').place(relx = 0.05, rely = 0.4, relheight = 0.3)


        Label(frame_7, text = 'Sub Total', font = 'Arial 11', bg = 'white').place(relx = 0.1, rely = 0.1)

        price = 0
        quantity = 0
        for i in cart_items_dict:
            price += int(cart_items_dict.get(i)[0]) * int(cart_items_dict.get(i)[1])
            quantity += int(cart_items_dict.get(i)[1])


        sub_total_entry = Entry(frame_7, font = 'Arial 11', border = 0)
        sub_total_entry.insert(END, str(price) + '.00')
        sub_total_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        sub_total_entry.place(relx = 0.75, rely = 0.1)

        Label(frame_7, text = 'Tax(18%)', font = 'Arial 11', bg = 'white').place(relx = 0.1, rely = 0.3)

        tax = str(price * 18/100)
        fin_tax = ''

        for i in range (len(tax)):
            if tax[i] == '.':
                fin_tax = fin_tax + tax[i:i+2]
                break
            else:
                fin_tax = fin_tax + tax[i]

        tax_calc_entry = Entry(frame_7, font = 'Arial 11', border = 0)
        tax_calc_entry.insert(END, fin_tax)
        tax_calc_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        tax_calc_entry.place(relx = 0.76, rely = 0.3)

        Label(frame_7, text = 'Grand Total', font = 'Arial 11 bold', bg = 'white').place(relx = 0.1, rely = 0.7)

        grand_total_calc_entry = Entry(frame_7, font = 'Arial 11 bold', border = 0)
        grand_total_calc_entry.insert(END, price + float(fin_tax))
        grand_total_calc_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        grand_total_calc_entry.place(relx = 0.755, rely = 0.7)

        place_order_button.config(command = place_order)
        place_order_button.place(relx = 0.25, rely = 0.8, relheight = 0.08, relwidth = 0.25)

        clear_cart_button.config(command = clear_cart)
        clear_cart_button.place(relx = 0.55, rely = 0.8, relheight = 0.08, relwidth = 0.25)


        frame_5.place(relx = 0.04, rely = 0.22, relwidth = 0.5, relheight = 0.8)
        frame_6.place(relheight = 0.4, relwidth = 1)
        frame_7.place(rely = 0.45, relheight = 0.25, relwidth = 1)
    
    else:
        frame_1.place_forget()
        frame_2.place_forget()
        frame_5.place_forget()
        frame_10.place_forget()
        frame_12.place_forget()
        frame_14.place_forget()

        welcome_label_1.place_forget()
        welcome_label_2.place_forget()

        no_item_label_1.place(relx = 0.3, rely = 0.4)
        no_item_label_2.place(relx = 0.27, rely = 0.5)

        label_1.place_forget()
        order_placed_label_1.place_forget()
        
        frame_5.place(relheight = 1, relwidth = 1)
