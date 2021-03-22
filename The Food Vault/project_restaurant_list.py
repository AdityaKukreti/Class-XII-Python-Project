from tkinter import *
from project_objects import *
from tkinter import messagebox

def restaurant_list():

    rest_head.place(relx = 0.04, rely = 0.12)

    for i in rest_info_treeview.get_children():
        rest_info_treeview.delete(i)   

    def selected(event):

        def add_to_cart_list(event):
            global count_2
            nonlocal item_dict

            for i in cart_treeview.get_children():
                cart_treeview.delete(i)

            for i in range(1):
                if menu_treeview.item(menu_treeview.focus())['values'][0] not in ('Starters','MainCourse','Dessert'):
                    if menu_treeview.item(menu_treeview.focus())['values'][0] not in item_dict:
                        item_dict[menu_treeview.item(menu_treeview.focus())['values'][0]] = [menu_treeview.item(menu_treeview.focus())['values'][1],1]
                    elif menu_treeview.item(menu_treeview.focus())['values'][0] in item_dict:
                        item_dict.get(menu_treeview.item(menu_treeview.focus())['values'][0])[1] += 1

            for i in item_dict:
                value = [i]
                for j in item_dict.get(i):
                    value.append(j)
                cart_treeview.insert(parent = '', text = '', index = END, iid = count_2, values = value)
                count_2 += 1

        def remove_item_from_cart():
            nonlocal item_dict
            count_2 = 0
            
            
            if item_dict == {}:
                messagebox.showerror('Error','No item found in the list!')
            else:
                x = cart_treeview.item(cart_treeview.focus())['values'][0]
                item_dict.pop(x)

                for i in cart_treeview.get_children():
                    cart_treeview.delete(i)
                

                for i in item_dict:
                    value = [i]
                    for j in item_dict.get(i):
                        value.append(j)
                    cart_treeview.insert(parent = '', text = '', index = END, iid = count_2, values = value)
                    count_2 += 1


        def move_items_to_cart():
            nonlocal val
            nonlocal item_dict
            name = StringVar

            if item_dict == {}:
                messagebox.showerror('Error','No item found in the list!')
            
            elif os.path.isfile(os.getcwd() + '/csv and text files/item.csv') == False:
                with open(os.getcwd() + '/csv and text files/item.csv','w') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow([val])

                    for i in item_dict:
                        data = []
                        data.append(i)
                        for j in item_dict.get(i):
                            data.append(j)
                        csv_writer.writerow(data)

                    
                    messagebox.showinfo('Success','Items have been added to the cart successfully!')
                    frame_2.place_forget()
                    menu_head.place_forget()
                    
            else:
                if os.path.isfile(os.getcwd() + '/csv and text files/item.csv') == True:
                    with open(os.getcwd() + '/csv and text files/item.csv') as f:
                        csv_reader = csv.reader(f)
                        for i in csv_reader:
                            if len(i) == 1:
                                name = i[0]
                                StopIteration

                    
                    
                if name != val:
                    choice = messagebox.askyesno('Confirm',"You can't add items from 2 or more restaurants in the cart at the same time. Continuing will clear your previous selections. Do you want to continue?")
                    if choice == True:    
                        with open(os.getcwd() + '/csv and text files/item.csv','w') as f:
                            csv_writer = csv.writer(f)
                            csv_writer.writerow([val])

                            for i in item_dict:
                                data = []
                                data.append(i)
                                for j in item_dict.get(i):
                                    data.append(j)
                                csv_writer.writerow(data)
                        

                        
                        messagebox.showinfo('Success','Items have been added to the cart successfully!')
                        frame_2.place_forget()
                        menu_head.place_forget()

                elif name == val:
                    item_append_dict = {}
                    with open(os.getcwd() + '/csv and text files/item.csv','r') as f:
                        csv_reader = csv.reader(f)
                        for i in csv_reader:
                            if len(i) == 3:
                                item_append_dict[i[0]] = i[1:3]

                    for i in item_dict:
                        for j in item_append_dict:
                            if i == j:
                                item_append_dict.get(i)[1] = int(item_append_dict.get(i)[1]) + int(item_dict.get(j)[1])
                    
                    for i in item_dict:
                        if i not in item_append_dict:
                            item_append_dict[i] = item_dict.get(i)
                    
                    with open(os.getcwd() + '/csv and text files/item.csv','w') as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow([val])    
                        for i in item_append_dict:
                            data = []
                            data.append(i)
                            for j in item_append_dict.get(i):
                                data.append(j)
                            csv_writer.writerow(data)
                

                    
                    messagebox.showinfo('Success','Items have been added to the cart successfully!')
                    frame_2.place_forget()
                    menu_head.place_forget()


        item_dict = {}
        val = rest_info_treeview.item(rest_info_treeview.selection())['values'][0]

        menu_treeview_scrollbar = Scrollbar(frame_3)
        menu_treeview_scrollbar.pack(side = RIGHT, fill = Y)

        menu_treeview = ttk.Treeview(frame_3, yscrollcommand = menu_treeview_scrollbar.set)
        menu_treeview_scrollbar.config(command = menu_treeview.yview)

        menu_treeview['columns'] = ('Item', 'Price')

        menu_treeview.column('#0', width = 0, stretch = 0)
        menu_treeview.column('Item', width = 100, minwidth = 50, anchor = W)
        menu_treeview.column('Price', width = 40, minwidth = 40, anchor = W)

        menu_treeview.heading('#0', text = '', anchor = W)
        menu_treeview.heading('Item', text = 'Item', anchor = W)
        menu_treeview.heading('Price', text = 'Price', anchor = W)

        menu_treeview.insert(parent = '', index = END, iid = 0, text = '', values = 'Starters')
        menu_treeview.insert(parent = '', index = END, iid = 1, text = '', values = 'MainCourse')
        menu_treeview.insert(parent = '', index = END, iid = 2, text = '', values = 'Dessert')

        cur.execute('SELECT `starter items`,`prices` FROM `starters` where `rest name` = %s',(val,))
        count_1 = 3
        for i in cur:
            item_1 = i[0].split(',')
            price_1 =i[1].split(',')
            for j in range(len(item_1)):
                menu_treeview.insert(parent = '0', index = END, iid = count_1, text = '', values = (item_1[j], price_1[j])) 
                count_1 += 1

        cur.execute('SELECT `main course items`,`prices` FROM `main course` where `rest name` = %s',(val,))
        for i in cur:
            item_1 = i[0].split(',')
            price_1 =i[1].split(',')
            for j in range(len(item_1)):
                menu_treeview.insert(parent = '1', index = END, iid = count_1, text = '', values = (item_1[j], price_1[j])) 
                count_1 += 1

        cur.execute('SELECT `des items`,`prices` FROM `dessert` where `rest name` = %s',(val,))
        for i in cur:
            item_1 = i[0].split(',')
            price_1 =i[1].split(',')
            for j in range(len(item_1)):
                menu_treeview.insert(parent = '2', index = END, iid = count_1, text = '', values = (item_1[j], price_1[j])) 
                count_1 += 1

            

        menu_treeview.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.955)
        frame_3.place(relwidth = 1, relheight = 0.4)

        cart_treeview_scrollbar = Scrollbar(frame_4)
        cart_treeview_scrollbar.pack(side = RIGHT, fill = Y)

        cart_treeview = ttk.Treeview(frame_4, yscrollcommand = cart_treeview_scrollbar.set)
        cart_treeview_scrollbar.config(command = cart_treeview.yview)

        cart_treeview['columns'] = ('Item', 'Price', 'Quantity')

        cart_treeview.column('#0', width = 0, stretch = 0)
        cart_treeview.column('Item', width = 150, minwidth = 40, anchor = W)
        cart_treeview.column('Price', width = 30, minwidth = 40, anchor = W)
        cart_treeview.column('Quantity', width = 30, minwidth = 40, anchor = W)

        cart_treeview.heading('#0', text = '', anchor = W)
        cart_treeview.heading('Item', text = 'Item', anchor = W)
        cart_treeview.heading('Price', text = 'Price', anchor = W)
        cart_treeview.heading('Quantity', text = 'Quantity', anchor = W)

        cart_treeview.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.955)
        frame_4.place(rely = 0.45,relwidth = 1, relheight = 0.4)

            
        

        menu_treeview.bind('<Double-1>', add_to_cart_list)
        remove_button.config(command = remove_item_from_cart)
        remove_button.place(relx = 0.1, rely = 0.9, relwidth = 0.37, relheight = 0.08)
        add_button.config(command = move_items_to_cart)
        add_button.place(relx = 0.54, rely = 0.9, relwidth = 0.37, relheight = 0.08)

        menu_head.place(relx = 0.66, rely = 0.12)

        frame_2.place(relx = 0.66, rely = 0.22, relwidth = 0.3, relheight = 0.7)


    cart_head.place_forget()
    ord_head.place_forget()
    hist_head.place_forget()
    user_head.place_forget()

    frame_5.place_forget()
    frame_8.place_forget()
    frame_10.place_forget()
    frame_12.place_forget()
    frame_14.place_forget()

    welcome_label_1.place_forget()
    welcome_label_2.place_forget()
    label_1.place_forget()
    order_placed_label_1.place_forget()

    restaurant_list_button.config(bg = '#b3fff6')
    cart_button.config(bg = 'white')
    order_history_button.config(bg = 'white')
    user_details_button.config(bg = 'white')
    sign_out_button.config(bg = 'white')



    count = 0
    cur.execute('SELECT `rest name`,`establishment type`,`cuisines` FROM `rest info` ORDER BY `rest name` DESC')
    for i in cur:
        rest_info_treeview.insert(parent = '', index = 0, iid = count, text = '', values = i)
        count += 1



    frame_1.place(relx = 0.04, rely = 0.22, relwidth = 0.6, relheight = 0.5)
    rest_info_treeview.bind('<Double-1>', selected)

