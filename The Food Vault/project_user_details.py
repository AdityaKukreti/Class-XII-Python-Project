from tkinter import *
from project_objects import *
from project_login_and_signup import *
from send_email import email_change_alert_email,account_deletion_mail



def user_details():
    global count_3
    count_3 += 1

    with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
        for i in range(5):
            pickle.load(f)
        rem_info = pickle.load(f)

    rest_head.place_forget()
    menu_head.place_forget()
    cart_head.place_forget()
    ord_head.place_forget()
    hist_head.place_forget()

    user_head.place(relx = 0.075, rely = 0.12)

    frame_1.place_forget()
    frame_2.place_forget()
    frame_5.place_forget()
    frame_8.place_forget()
    frame_10.place_forget()
    frame_12.place_forget()

    welcome_label_1.place_forget()
    welcome_label_2.place_forget()

    rest_head.place_forget()
    menu_head.place_forget()



    restaurant_list_button.config(bg = 'white')
    cart_button.config(bg = 'white')
    order_history_button.config(bg = 'white')
    user_details_button.config(bg = '#b3fff6')
    sign_out_button.config(bg = 'white')

    for i in address_treeview.get_children():
        address_treeview.delete(i)
    

    def delete_account_confirm():
        nonlocal password
        global log_var
        value = messagebox.askyesno('Confirm','Do you really want to delete your account?')
        if value == True:
            new = Toplevel()
            new.title('Confirm')
            new.geometry('300x140')
            new.resizable(0,0)
            new.focus()
            new.transient(root)
            new.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')

            canvas = Canvas(new, bg = '#b2d9ed')
            canvas.place(relheight = 1, relwidth = 1)

            Label(canvas, text = 'Enter your password to confirm :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0.1, rely = 0.1, relheight = 0.3)
            confirm_entry = Entry(canvas, width = 30, show = '*', font = 'Arial 13')
            confirm_entry.place(relx = 0.1,  rely = 0.42, relheight  = 0.175, relwidth = 0.8)
    
            def del_confirm():
                if password == confirm_entry.get():
                    cur.execute("DELETE FROM `user details` where `email` = %s",(email,))
                    cur.execute("DELETE FROM `user addresses` where `email` = %s",(email,))
                    cur.execute("DELETE FROM `user orders` where `email` = %s",(email,))
                    db.commit()

                    messagebox.showinfo('Message','Account has been deleted successfully!')
                    os.remove(os.getcwd() + '/csv and text files/info.txt')
                    user_head.place_forget()
                    user_details_button.config(bg = 'white')
                    check_log_var()
                    new.destroy()

                    a_d_thread = threading.Thread(target = account_deletion_mail, args=(first_name_account_entry.get(),email_account_entry.get()))
                    a_d_thread.start()
                else:
                    messagebox.showerror('Error','Entered password is invalid!')
                    new.deiconify()

            Button(canvas, text = 'Confirm', border = 0, bg = 'white', activebackground = '#cfd1d1', command = del_confirm, cursor = 'hand2').place(relx = 0.3, rely =  0.72, relwidth = 0.4, relheight = 0.2)

    def phone_number_change():
        x = Toplevel()
        x.title('Confirm')
        x.geometry('300x170')
        x.resizable(0,0)
        x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
        x.focus()
        x.transient(root)

        canvas = Canvas(x, bg = '#b2d9ed')
        canvas.place(relheight = 1, relwidth = 1)
            
        Label(canvas, text  = 'Enter your new mobile number :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.075, relheight  = 0.1, relwidth = 1 )
        change_mobile_number_entry = Entry(canvas, width = 30, font = 'Arial 13')
        change_mobile_number_entry.insert(END, '+91 ')
        change_mobile_number_entry.place(relx = 0.1,  rely = 0.22, relheight  = 0.15, relwidth = 0.8)

        Label(canvas, text  = 'Re-enter your new mobile number :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.455, relheight  = 0.1, relwidth = 1 )
        change_mobile_number_reentry = Entry(canvas, width = 30, font = 'Arial 13')
        change_mobile_number_reentry.insert(END, '+91 ')
        change_mobile_number_reentry.place(relx = 0.1,  rely = 0.6, relheight  = 0.15, relwidth = 0.8)


        
        def check_phone_number():
            email_txt = email_account_entry.get()
            password_txt = password_account_entry.get()
            first_name_txt = first_name_account_entry.get()
            last_name_txt = last_name_account_entry.get()
            phone_number_txt = change_mobile_number_entry.get()

            if change_mobile_number_entry.get() == change_mobile_number_reentry.get():
                cur.execute("UPDATE `user details` SET `mobile no.` = %s where `email` = %s",(change_mobile_number_entry.get(),email))
                db.commit()

                phone_number_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')
                phone_number_account_entry.insert(END, change_mobile_number_entry.get())
                phone_number_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
                phone_number_account_entry.place(relx = 0.17, rely = 0.49, relheight = 0.065, relwidth = 0.25)

                with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                    pickle.dump(encrypt(first_name_txt),info)
                    pickle.dump(encrypt(last_name_txt),info)
                    pickle.dump(encrypt(email_txt),info)
                    pickle.dump(encrypt(password_txt),info)
                    pickle.dump(encrypt(phone_number_txt),info)
                    pickle.dump(rem_info, info)
                messagebox.showinfo("Success",'Mobile number has been changed!')
                x.destroy()
            else:
                messagebox.showerror('Error',"Entered numbers don't match!")
                x.deiconify()
                
        Button(canvas, text = 'Submit', border = 0, command = check_phone_number, bg = 'white', activebackground = '#cfd1d1', cursor = 'hand2').place(relx = 0.3, rely =  0.8, relwidth = 0.4, relheight = 0.16)

    def last_name_change():
        x = Toplevel()
        x.title('Confirm')
        x.geometry('300x170')
        x.resizable(0,0)
        x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
        x.transient(root)
        x.focus()

        canvas = Canvas(x, bg = '#b2d9ed')
        canvas.place(relheight = 1, relwidth = 1)

        Label(canvas, text  = 'Enter your new last name :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.075, relheight  = 0.1, relwidth = 1)
        change_last_name_entry = Entry(canvas, width = 30, font = 'Arial 13')
        change_last_name_entry.place(relx = 0.1,  rely = 0.22, relheight  = 0.15, relwidth = 0.8)

        Label(canvas, text  = 'Re-enter your new last name :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.455, relheight  = 0.1, relwidth = 1)
        change_last_name_reentry = Entry(canvas, width = 30, font = 'Arial 13')
        change_last_name_reentry.place(relx = 0.1,  rely = 0.6, relheight  = 0.15, relwidth = 0.8)


        def check_last_name():
            email_txt = email_account_entry.get()
            password_txt = password_account_entry.get()
            first_name_txt = first_name_account_entry.get()
            last_name_txt = change_last_name_entry.get()
            phone_number_txt = phone_number_account_entry.get()

            if change_last_name_entry.get() == change_last_name_reentry.get():
                cur.execute("UPDATE `user details` SET `last name` = %s where `email` = %s",(change_last_name_entry.get(),email))
                db.commit()

                last_name_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')
                last_name_account_entry.insert(END, change_last_name_entry.get())
                last_name_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
                last_name_account_entry.place(relx = 0.17, rely = 0.38, relheight = 0.065, relwidth = 0.25)

                with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                    pickle.dump(encrypt(first_name_txt),info)
                    pickle.dump(encrypt(last_name_txt),info)
                    pickle.dump(encrypt(email_txt),info)
                    pickle.dump(encrypt(password_txt),info)
                    pickle.dump(encrypt(phone_number_txt),info)
                    pickle.dump(rem_info, info)
                messagebox.showinfo("Success",'Last name has been changed!')
                x.destroy()

            else:
                messagebox.showerror('Error',"Entered names don't match")
                x.deiconify()

        Button(canvas, text = 'Submit', border = 0, bg = 'white', command = check_last_name, activebackground = '#cfd1d1', cursor = 'hand2').place(relx = 0.3, rely =  0.8, relwidth = 0.4, relheight = 0.16)


    def first_name_change():

        x = Toplevel()
        x.title('Confirm')
        x.geometry('300x170')
        x.resizable(0,0)
        x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
        x.focus()
        x.transient(root)

        canvas = Canvas(x, bg = '#b2d9ed')
        canvas.place(relheight = 1, relwidth = 1)
        
        Label(canvas, text  = 'Enter your new first name :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.075, relheight  = 0.1, relwidth = 1)
        change_first_name_entry = Entry(canvas, width = 30, font = 'Arial 13')
        change_first_name_entry.place(relx = 0.1,  rely = 0.22, relheight  = 0.15, relwidth = 0.8)

        Label(canvas, text  = 'Re-enter your new first name :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.455, relheight  = 0.1, relwidth = 1 )
        change_first_name_reentry = Entry(canvas, width = 30, font = 'Arial 13')
        change_first_name_reentry.place(relx = 0.1,  rely = 0.6, relheight  = 0.15, relwidth = 0.8)


        def check_first_name():
            email_txt = email_account_entry.get()
            password_txt = password_account_entry.get()
            first_name_txt = change_first_name_entry.get()
            last_name_txt = last_name_account_entry.get()
            phone_number_txt = phone_number_account_entry.get()

            if change_first_name_entry.get() == change_first_name_reentry.get():
                cur.execute("UPDATE `user details` SET `first name` = %s where `email` = %s",(change_first_name_entry.get(),email))
                db.commit()

                first_name_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')
                first_name_account_entry.insert(END, change_first_name_entry.get())
                first_name_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
                first_name_account_entry.place(relx = 0.17, rely = 0.27, relheight = 0.065, relwidth = 0.25)

                
                with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                    pickle.dump(encrypt(first_name_txt),info)
                    pickle.dump(encrypt(last_name_txt),info)
                    pickle.dump(encrypt(email_txt),info)
                    pickle.dump(encrypt(password_txt),info)
                    pickle.dump(encrypt(phone_number_txt),info)
                    pickle.dump(rem_info, info)
                messagebox.showinfo("Success",'First name has been changed!')
                x.destroy()
            else:
                messagebox.showerror('Error',"Entered names don't match!")
                x.deiconify()

        Button(canvas, text = 'Submit', border = 0,bg = 'white', command = check_first_name, activebackground = '#cfd1d1', cursor = 'hand2').place(relx = 0.3, rely =  0.8, relwidth = 0.4, relheight = 0.16)



    def password_change():
        x = Toplevel()
        x.title('Confirm')
        x.geometry('300x170')
        x.resizable(0,0)
        x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
        x.focus()
        x.transient(root)

        canvas = Canvas(x, bg = '#b2d9ed')
        canvas.place(relheight = 1, relwidth = 1)
        
        Label(canvas, text  = 'Enter your new password :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.075, relheight  = 0.1, relwidth = 1 )
        change_password_entry = Entry(canvas, width = 30, show = '*', font = 'Arial 13')
        change_password_entry.place(relx = 0.1,  rely = 0.22, relheight  = 0.15, relwidth = 0.8)

        Label(canvas, text  = 'Re-enter your new password :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.455, relheight  = 0.1, relwidth = 1 )
        change_password_reentry = Entry(canvas, width = 30, show = '*', font = 'Arial 13')
        change_password_reentry.place(relx = 0.1,  rely = 0.6, relheight  = 0.15, relwidth = 0.8)


        
        def check_password():
            email_txt = email_account_entry.get()
            password_txt = change_password_entry.get()
            first_name_txt = first_name_account_entry.get()
            last_name_txt = last_name_account_entry.get()
            phone_number_txt = phone_number_account_entry.get()


            if len(change_password_entry.get()) <= 7:
                messagebox.showwarning('Warning','Choose a longer password')
            elif change_password_entry.get() == change_password_reentry.get():
                cur.execute("UPDATE `user details` SET `password` = %s where `email` = %s",(change_password_entry.get(),email))
                db.commit()

                password_account_entry = Entry(frame_14, width = 50, show = '*', font = 'Arial 15 bold')
                password_account_entry.insert(END, change_password_entry.get())
                password_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
                password_account_entry.place(relx = 0.17, rely = 0.16, relheight =  0.065, relwidth = 0.25)

                with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                    pickle.dump(encrypt(first_name_txt),info)
                    pickle.dump(encrypt(last_name_txt),info)
                    pickle.dump(encrypt(email_txt),info)
                    pickle.dump(encrypt(password_txt),info)
                    pickle.dump(encrypt(phone_number_txt),info)
                    pickle.dump(rem_info, info)
                messagebox.showinfo("Success",'Password has been changed!')
                x.destroy()
            else:
                messagebox.showerror('Error',"Entered passwords don't match")
                x.deiconify()
                
        Button(canvas, text = 'Submit', border = 0,bg = 'white', command = check_password, activebackground = '#cfd1d1', cursor = 'hand2').place(relx = 0.3, rely =  0.8, relwidth = 0.4, relheight = 0.16)


    def email_change():
        x = Toplevel()
        x.title('Confirm email')
        x.geometry('300x170')
        x.resizable(0,0)
        x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
        x.focus()
        x.transient(root)

        canvas = Canvas(x, bg = '#b2d9ed')
        canvas.place(relheight = 1, relwidth = 1)
        
        Label(canvas, text  = 'Enter your new email id :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.075, relheight  = 0.1, relwidth = 1)
        change_email_entry = Entry(canvas, width = 30, font = 'Arial 13')
        change_email_entry.place(relx = 0.1,  rely = 0.22, relheight  = 0.15, relwidth = 0.8)

        Label(canvas, text  = 'Re-enter your new email id :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.455, relheight  = 0.1, relwidth = 1  )
        change_email_reentry = Entry(canvas, width = 30, font = 'Arial 13')
        change_email_reentry.place(relx = 0.1,  rely = 0.6, relheight  = 0.15, relwidth = 0.8)


        def check_email():
            global email_account_entry
            global first_name_account_entry
            email_txt = change_email_entry.get()
            password_txt = password_account_entry.get()
            first_name_txt = first_name_account_entry.get()
            last_name_txt = last_name_account_entry.get()
            phone_number_txt = phone_number_account_entry.get()

            if change_email_entry.get() == change_email_reentry.get():
                code = random.randint(111111,999999)

                e_c_thread = threading.Thread(target = email_change_alert_email, args=(first_name_account_entry.get(),email_account_entry.get(),code))
                e_c_thread.start()
                messagebox.showinfo('Message','A verification code has been sent to your registerd email id')

                canvas.place_forget()

                canvas_0 = Canvas(x, bg = '#b2d9ed')
                canvas_0.place(relheight = 1, relwidth = 1)



                Label(canvas_0, text = 'Enter your verification code :', font = 'Arial 13 bold', bg = '#b2d9ed').place(relx = 0.1, rely = 0.2)
                code_entry = Entry(canvas_0, width = 28, font = 'Arial 13')
                code_entry.place(relx = 0.1, rely = 0.4)

                def change_email():
                    nonlocal code
                    if code_entry.get() == str(code):

                        cur.execute("UPDATE `user details` SET `email` = %s where `email` = %s",(change_email_entry.get(),email))
                        cur.execute("UPDATE `user addresses` SET `email` = %s where `email` = %s",(change_email_entry.get(),email))
                        cur.execute("UPDATE `user orders` SET `email` = %s where `email` = %s",(change_email_entry.get(),email))    
                        db.commit()
                        email_account_entry = Entry(frame_14, width = 50, font = 'Arial 15')
                        email_account_entry.insert(END, change_email_entry.get())
                        email_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
                        email_account_entry.place(relx = 0.17, rely = 0.05, relheight =  0.065, relwidth = 0.25)

                        with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                            pickle.dump(encrypt(first_name_txt),info)
                            pickle.dump(encrypt(last_name_txt),info)
                            pickle.dump(encrypt(email_txt),info)
                            pickle.dump(encrypt(password_txt),info)
                            pickle.dump(encrypt(phone_number_txt),info)
                            pickle.dump(rem_info, info)
                        
                        messagebox.showinfo("Success",'Email id has been changed!')
                        x.destroy()
                    
                    else:
                        messagebox.showerror('Error','Entered code is invalid.')
                        x.deiconify()


                b = Button(canvas_0, text = 'Submit', border = 0, command = change_email, bg = 'white', activebackground = '#cfd1d1', cursor = 'hand2')
                b.place(relx = 0.3, rely =  0.8, relwidth = 0.4, relheight = 0.16)
        

            
            else:
                messagebox.showerror('Error',"Entered email ids don't match")
                x.deiconify()


        b = Button(canvas, text = 'Submit', border = 0, command = check_email, bg = 'white', activebackground = '#cfd1d1', cursor = 'hand2')
        b.place(relx = 0.3, rely =  0.8, relwidth = 0.4, relheight = 0.16)



    def add_address():
        nonlocal email
        x = Toplevel()
        x.title('Enter new address')
        x.geometry('300x140')
        x.resizable(0,0)
        x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
        x.focus()
        x.transient(root)

        canvas = Canvas(x, bg = '#b2d9ed')
        canvas.place(relheight = 1, relwidth = 1)
            
        Label(canvas, text  = 'Enter your new address :', font = 'Arial 13', bg = '#b2d9ed').place(relx = 0, rely = 0.15, relheight  = 0.15, relwidth = 1 )
        new_address_entry = Entry(canvas, width = 30, font = 'Arial 13')
        new_address_entry.place(relx = 0.1,  rely = 0.42, relheight  = 0.175, relwidth = 0.8)

        def add_address_to_db():
            nonlocal email
    
            if new_address_entry.get() == '':
                messagebox.showerror('Error','The field is blank!')
                x.deiconify()
            else:
                cur.execute('INSERT INTO `user addresses` VALUES(%s,%s)',(email, new_address_entry.get()))
                db.commit()

                for i in address_treeview.get_children():
                    address_treeview.delete(i)
                
                cur.execute('SELECT `address` FROM `user addresses` WHERE `email` = %s',(email,))
                count = 0
                for i in cur:
                    address_treeview.insert(parent = '', text = '', index = END, iid = count, values = (count + 1,i[0]))
                    count += 1

                x.destroy()

        Button(canvas, text = 'Submit', border = 0, command = add_address_to_db, bg = 'white', activebackground = '#cfd1d1', cursor = 'hand2').place(relx = 0.3, rely =  0.72, relwidth = 0.4, relheight = 0.2)



    def remove_address():
        nonlocal email

        def remove_address_from_db():
            cur.execute('DELETE FROM `user addresses` WHERE `email` = %s AND `address` = %s',(email, address_treeview.item(address_treeview.focus())['values'][1]))
            db.commit()

        if len(address_treeview.get_children()) <= 1:
            messagebox.showerror('Error','Minimum one address is required!')
        else:
            remove_address_from_db()
            address_treeview.delete(address_treeview.focus())
            cur.execute('SELECT `address` FROM `user addresses` WHERE `email` = %s',(email,))
            
            for i in address_treeview.get_children():
                address_treeview.delete(i)
            
            count = 0
            for i in cur:
                address_treeview.insert(parent = '', text = '', index = END, iid = count, values = (count + 1,i[0]))
                count += 1


    if os.path.isfile(os.getcwd() + '/csv and text files/info.txt'):
        with open(os.getcwd() + '/csv and text files/info.txt','rb') as f:
            first_name = decrypt(pickle.load(f))
            last_name = decrypt(pickle.load(f))
            email = decrypt(pickle.load(f))
            password = decrypt(pickle.load(f))
            phone_number = decrypt(pickle.load(f))

    if count_3 == 1:

        email_account_label.place(relx = 0.03, rely = 0.05, relheight = 0.065)
        email_account_entry.insert(END, email)
        email_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        Button(frame_14, text = 'Change', border = 0, bg = 'white', activebackground = '#b3fff6', command = email_change, cursor = 'hand2').place(relx = 0.45, rely = 0.05, relheight = 0.065, relwidth = 0.1)
        email_account_entry.place(relx = 0.17, rely = 0.05, relheight =  0.065, relwidth = 0.25)


        password_account_label.place(relx = 0.03, rely = 0.16, relheight = 0.065)
        password_account_entry.insert(END, password)
        password_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        Button(frame_14, text = 'Change', border = 0, bg = 'white', activebackground = '#b3fff6', command = password_change, cursor = 'hand2').place(relx = 0.45, rely = 0.16, relheight = 0.065, relwidth = 0.1)
        password_account_entry.place(relx = 0.17, rely = 0.16, relheight =  0.065, relwidth = 0.25)


        first_name_account_label.place(relx = 0.03, rely = 0.27, relheight = 0.065)
        first_name_account_entry.insert(END, first_name)
        first_name_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        Button(frame_14, text = 'Change', border = 0, bg = 'white', activebackground = '#b3fff6', command = first_name_change, cursor = 'hand2').place(relx = 0.45, rely = 0.27, relheight = 0.065, relwidth = 0.1)
        first_name_account_entry.place(relx = 0.17, rely = 0.27, relheight = 0.065, relwidth = 0.25)


        last_name_account_label.place(relx = 0.03, rely = 0.38, relheight = 0.065)
        last_name_account_entry.insert(END, last_name)
        last_name_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        Button(frame_14, text = 'Change', border = 0, bg = 'white', activebackground = '#b3fff6', command = last_name_change, cursor = 'hand2').place(relx = 0.45, rely = 0.38, relheight = 0.065, relwidth = 0.1)
        last_name_account_entry.place(relx = 0.17, rely = 0.38, relheight = 0.065, relwidth = 0.25)


        phone_number_account_label.place(relx = 0.03, rely = 0.49, relheight = 0.065)
        phone_number_account_entry.insert(END, phone_number)
        phone_number_account_entry.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        Button(frame_14, text = 'Change', border = 0, bg = 'white', activebackground = '#b3fff6', command = phone_number_change, cursor = 'hand2').place(relx = 0.45, rely = 0.49, relheight = 0.065, relwidth = 0.1)
        phone_number_account_entry.place(relx = 0.17, rely = 0.49, relheight = 0.065, relwidth = 0.25)


    add_address_button = Button(frame_14, text = 'Add Address', border = 0, bg = 'white', activebackground = '#b3fff6', command = add_address, cursor = 'hand2')
    add_address_button.place(relx = 0.7, rely = 0.49, relheight = 0.065, relwidth = 0.1)

    remove_address_button = Button(frame_14, text = 'Remove Address', border = 0, bg = 'white', activebackground = '#b3fff6', command = remove_address, cursor = 'hand2')
    remove_address_button.place(relx = 0.81, rely = 0.49, relheight = 0.065, relwidth = 0.1)

    delete_account_button = Button(frame_14, text = 'Delete Account', border = 0, bg = 'white', activebackground = '#b3fff6', command = delete_account_confirm, cursor = 'hand2')
    delete_account_button.place(relx = 0.425, rely = 0.75, relheight = 0.07, relwidth = 0.15)


    cur.execute('SELECT `address` FROM `user addresses` WHERE `email` = %s',(email,))
    count = 0
    for i in cur:
        address_treeview.insert(parent = '', text = '', index = END, iid = count, values = (count + 1,i[0]))
        count += 1


    address_treeview.place(relheight = 1,  relwidth = 1)


    frame_14.place(relx = 0.05, rely = 0.22, relheight = 0.8, relwidth = 0.9)
    frame_15.place(relx = 0.65, rely = 0.05, relheight = 0.4, relwidth = 0.3)
