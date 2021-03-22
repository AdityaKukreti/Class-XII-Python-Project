from tkinter import *
from tkinter import messagebox
from project_objects import *
from send_email import verification_code_mail, forgot_password_mail
import pickle


def check_log_var():
    global event_val
    global log_var

    frame_1.place_forget()
    frame_2.place_forget()
    frame_5.place_forget()
    frame_8.place_forget()
    frame_10.place_forget()
    frame_12.place_forget()
    frame_14.place_forget()
    canvas_2.place_forget()

    
    c = 1

    def f_p(event):
        nonlocal c
        if c == 1:
            forgot_password_button.config(font = 'Arial 13 underline', fg = '#0553f0', activeforeground = '#0553f0')
            c *= -1
        elif c == -1:
            forgot_password_button.config(font = 'Arial 13', fg = 'black', activeforeground = 'black')
            c *= -1

    def set_log_var_1():
        global log_var
        log_var = 0

    def set_log_var_2():
        global log_var
        log_var = 1


    def signup():

        email_login_label.place_forget()
        email_login_entry.place_forget()

        password_login_label.place_forget()
        password_login_entry.place_forget()

        rem_info_checkbox.place_forget()
        forgot_password_button.place_forget()

        login_button.place_forget()
        signup_button.place_forget()

        label_0.place_forget()
        login_label.place_forget()
        

        def check_signup():
            code = random.randint(111111,999999)

            def check_code():
                nonlocal code
                nonlocal code_entry
            
                if str(code) == code_entry.get():
                    new.destroy()
                    messagebox.showinfo('Success!','Your account has been verified!')
                    cur.execute('INSERT INTO `user details` VALUES(%s,%s,%s,%s,%s)',(first_name_signup_entry.get(), last_name_signup_entry.get(), email_signup_entry.get(), password_signup_entry.get(), '+91 ' + number_signup_entry.get(),))
                    cur.execute('INSERT INTO `user addresses` VALUES(%s,%s)',(email_signup_entry.get(),address_signup_entry.get(),))
                    fn = first_name_signup_entry.get()
                    ln = last_name_signup_entry.get()
                    e = email_signup_entry.get()
                    p = password_signup_entry.get()
                    pn = '+91 ' + number_signup_entry.get()
                    with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                        pickle.dump(encrypt(fn),info)
                        pickle.dump(encrypt(ln),info)
                        pickle.dump(encrypt(e),info)
                        pickle.dump(encrypt(p),info)
                        pickle.dump(encrypt(pn),info)
                        pickle.dump('0',info)
                    db.commit()

                    first_name_signup_label.place_forget()
                    first_name_signup_entry.place_forget()

                    last_name_signup_label.place_forget()
                    last_name_signup_entry.place_forget()

                    email_signup_label.place_forget()
                    email_signup_entry.place_forget()

                    reenter_email_signup_label.place_forget()
                    reenter_email_signup_entry.place_forget()
                    
                    password_signup_label.place_forget()
                    password_signup_entry.place_forget()

                    reenter_password_signup_label.place_forget()
                    reenter_password_signup_entry.place_forget()
                    
                    address_signup_label.place_forget()
                    address_signup_entry.place_forget()

                    number_signup_label.place_forget()
                    number_signup_entry.place_forget()

                    register_screen_button.place_forget()
                    login_screen_button.place_forget()

                    label_2.place_forget()
                    signup_label.place_forget()

                    set_log_var_1()
                    object_placement()

                else:
                    messagebox.showerror('Error','Invalid code entered!')

            cur.execute("SELECT * FROM `user details`")
            email_id = []
            for i in cur:
                email_id.append(i[2])

            if (first_name_signup_entry.get() == '' or last_name_signup_entry.get() == '' or email_signup_entry.get() == '' or reenter_email_signup_entry.get() == '' or password_signup_entry.get() == '' or reenter_password_signup_entry.get() == '' or address_signup_entry.get() == '' or number_signup_entry.get() == ''):
                messagebox.showerror('Error','No field can be left blank!')
            elif email_signup_entry.get() != reenter_email_signup_entry.get():
                messagebox.showerror('Error',"Entered email id doesn't match")
            elif len(number_signup_entry.get()) > 10 or len(number_signup_entry.get()) <10:
                messagebox.showerror('Error',"Entered number is invalid")
            elif email_signup_entry.get() in email_id:
                messagebox.showerror('Error','Account with this email already exists!')
            elif password_signup_entry.get() != reenter_password_signup_entry.get():
                messagebox.showerror('Error',"Entered password doesn't match")
            elif len(password_signup_entry.get()) <= 7:
                messagebox.showwarning('Warning','Choose a longer password')
            else:
                ver_code_thread = threading.Thread(target = verification_code_mail, args=(first_name_signup_entry.get(),email_signup_entry.get(),code))
                ver_code_thread.start()
                messagebox.showinfo('Verify','Verification code has been sent to your email!')
                new = Toplevel()
                new.geometry('350x150')
                new.title('Verify')
                new.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
                new.focus()
                new.transient(root)

                canvas = Canvas(new, bg = '#c2eaff')
                canvas.place(relheight = 1, relwidth = 1)

                Label(canvas, text = 'Enter your verification code :', font = 'Arial 13 bold', bg = '#c2eaff').place(relx = 0.15, rely = 0.2)
                code_entry = Entry(canvas, width = 28, font = 'Arial 13')
                code_entry.place(relx = 0.125, rely = 0.4)

                Button(canvas, text = 'Submit', bg = 'white', activebackground = '#cfd1d1', border = 0, command = check_code).place(relx = 0.3, rely = 0.7, relwidth = 0.4, relheight = 0.2)
            

                
        

        first_name_signup_label.place(relx = 0.15, rely = 0.3)
        first_name_signup_entry.place(relx = 0.27, rely = 0.3, relheight =  0.05, relwidth = 0.2)

        last_name_signup_label.place(relx = 0.5, rely = 0.3)
        last_name_signup_entry.place(relx = 0.69, rely = 0.3, relheight =  0.05, relwidth = 0.2)

        email_signup_label.place(relx = 0.15, rely = 0.4)
        email_signup_entry.place(relx = 0.27, rely = 0.4, relheight =  0.05, relwidth = 0.2)

        reenter_email_signup_label.place(relx = 0.5, rely = 0.4)
        reenter_email_signup_entry.place(relx = 0.69, rely = 0.4, relheight =  0.05, relwidth = 0.2)
        
        password_signup_label.place(relx = 0.15, rely = 0.5)
        password_signup_entry.place(relx = 0.27, rely = 0.5, relheight =  0.05, relwidth = 0.2)

        reenter_password_signup_label.place(relx = 0.5, rely = 0.5)
        reenter_password_signup_entry.place(relx = 0.69, rely = 0.5, relheight =  0.05, relwidth = 0.2)
        
        address_signup_label.place(relx = 0.15, rely = 0.6)
        address_signup_entry.place(relx = 0.27, rely = 0.6, relheight = 0.05, relwidth = 0.2)

        number_signup_label.place(relx = 0.5, rely = 0.6)
        number_signup_entry.place(relx = 0.69, rely = 0.6, relheight =  0.05, relwidth = 0.2)

        register_screen_button.place(relx = 0.45, rely = 0.73, relheight = 0.05, relwidth = 0.1)
        register_screen_button.config(command = check_signup)

        login_screen_button.place(relx = 0.45, rely = 0.88, relheight = 0.05, relwidth = 0.1)
        login_screen_button.config(command = lambda : [set_log_var_1(), check_log_var()])

        label_2.place(relx = 0.422, rely = 0.805)
        signup_label.place(relx = 0.45, rely = 0.1)



    def login():

        first_name_signup_label.place_forget()
        first_name_signup_entry.place_forget()

        last_name_signup_label.place_forget()
        last_name_signup_entry.place_forget()

        email_signup_label.place_forget()
        email_signup_entry.place_forget()

        reenter_email_signup_label.place_forget()
        reenter_email_signup_entry.place_forget()
        
        password_signup_label.place_forget()
        password_signup_entry.place_forget()

        reenter_password_signup_label.place_forget()
        reenter_password_signup_entry.place_forget()
        
        address_signup_label.place_forget()
        address_signup_entry.place_forget()

        number_signup_label.place_forget()
        number_signup_entry.place_forget()

        label_2.place_forget()
        signup_label.place_forget()

        register_screen_button.place_forget()
        login_screen_button.place_forget()

        def f_p_window():
            x = Toplevel()
            x.title('Forgot Password')
            x.geometry('350x200')
            x.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
            x.focus()
            x.transient(root)

            canvas = Canvas(x, bg = '#c2eaff')
            canvas.place(relheight = 1, relwidth = 1)

            e_label = Label(canvas, text = 'Enter your email id:', font = 'Arial 14', bg= '#c2eaff')
            e_label.place(relx = 0.075, rely = 0.25, relwidth = 0.85, relheight = 0.1)

            e_entry = Entry(canvas, width = 20, font = 'Arial 13')
            e_entry.place(relx = 0.125, rely = 0.4, relheight = 0.125, relwidth = 0.75)

            def s_m():
                cur.execute('SELECT `first name` FROM `user details` WHERE `email` = %s',(e_entry.get(),))
                for i in cur:
                    n = i[0]
                code = random.randint(111111,999999)
                try:
                    f_p_thread = threading.Thread(target=forgot_password_mail, args=(n,e_entry.get(),code))
                    f_p_thread.start()
                    messagebox.showinfo('Success','A verification code has been sent to your email id.')
                    x.deiconify()

                    e_label.place_forget()
                    e_entry.place_forget()
                    e_button.place_forget()

                    c_label = Label(canvas, text = 'Enter your code:', font = 'Arial 14', bg = '#c3eaff')
                    c_label.place(relx = 0.075, rely = 0.25, relwidth = 0.85, relheight = 0.1)

                    c_entry = Entry(canvas, width = 20, font = 'Arial 13')
                    c_entry.place(relx = 0.125, rely = 0.4, relheight = 0.125, relwidth = 0.75)

                    def c_code():
                        nonlocal code

                        if str(code) == c_entry.get():

                            c_label.place_forget()
                            c_entry.place_forget()
                            c_button.place_forget()

                            c_p_label = Label(canvas, text = 'Enter your new password:', font = 'Arial 14', bg = '#c2eaff')
                            c_p_label.place(relx = 0.075, rely = 0.12, relwidth = 0.85, relheight = 0.1)

                            c_p_entry = Entry(canvas, width = 20, font = 'Arial 13', show = '*')
                            c_p_entry.place(relx = 0.125, rely = 0.27, relheight = 0.125, relwidth = 0.75)

                            c_p_rlabel = Label(canvas, text = 'Re-enter your new password:', font = 'Arial 14', bg = '#c2eaff')
                            c_p_rlabel.place(relx = 0.075, rely = 0.42, relwidth = 0.85, relheight = 0.1)

                            c_p_rentry = Entry(canvas, width = 20, font = 'Arial 13', show = '*')
                            c_p_rentry.place(relx = 0.125, rely = 0.57, relheight = 0.125, relwidth = 0.75)

                            def up_code():
                                if len(c_p_entry.get()) <= 7:
                                    messagebox.showwarning('Warning','Choose a longer password')
                                    x.deiconify()
                                elif c_p_entry.get() == c_p_rentry.get():
                                    cur.execute('UPDATE `user details` SET `password` = %s WHERE `email` = %s',(c_p_rentry.get(),e_entry.get()))
                                    db.commit()
                                    messagebox.showinfo('Success','Your password has been changed successfully!')
                                    x.destroy()
                                else:
                                    messagebox.showerror('Error','Entered passwords do not match')
                                    x.deiconify()

                            c_p_button = Button(canvas, text = 'Submit', font = 'Arial 13', bg = 'white', border = 0, activebackground = '#cfd1d1', command = up_code)
                            c_p_button.place(relx = 0.3, rely = 0.75, relwidth = 0.4, relheight = 0.15)
                        
                        else:
                            messagebox.showerror('Invalid','Entered code is invalid')
                            x.deiconify()


                    c_button = Button(canvas, text = 'Submit', font = 'Arial 13', bg = 'white', border = 0, activebackground = '#cfd1d1', command = c_code)
                    c_button.place(relx = 0.3, rely = 0.65, relwidth = 0.4, relheight = 0.15)

                    
                except UnboundLocalError:
                    messagebox.showerror('Error','No account exists with this email id')
                    x.deiconify()

                

            e_button = Button(canvas, text = 'Submit', font = 'Arial 13', bg = 'white', border = 0, activebackground = '#cfd1d1', command = s_m)
            e_button.place(relx = 0.3, rely  = 0.65, relwidth = 0.4, relheight = 0.15)

        def check_login(event):

            email_id = []
            passwords = []
            first_names = []
            last_names = []
            phone_number = []

            cur.execute('SELECT * FROM `user details`')

            for i in cur:
                first_names.append(i[0])
                last_names.append(i[1])
                email_id.append(i[2])
                passwords.append(i[3])
                phone_number.append(i[4])
            
            count = 0
            if email_login_entry.get() in email_id and password_login_entry.get() in passwords:
                for i in range(len(email_id)):
                    if email_login_entry.get() != email_id[i]:
                        count += 1
                    else:
                        fn = first_names[count]
                        ln = last_names[count]
                        e = email_id[count]
                        p = passwords[count]
                        pn = phone_number[count]
                with open(os.getcwd() + '/csv and text files/info.txt','wb') as info:
                    pickle.dump(encrypt(fn),info)
                    pickle.dump(encrypt(ln),info)
                    pickle.dump(encrypt(e),info)
                    pickle.dump(encrypt(p),info)
                    pickle.dump(encrypt(pn),info)
                    pickle.dump(str(rem_info.get()),info)
                
                email_login_label.place_forget()
                email_login_entry.place_forget()

                password_login_entry.place_forget()
                password_login_label.place_forget()

                rem_info_checkbox.place_forget()
                forgot_password_button.place_forget()

                login_button.place_forget()
                signup_button.place_forget()

                label_0.place_forget()
                login_label.place_forget()

                set_log_var_1()
                object_placement()

            elif email_login_entry.get() == '':
                messagebox.showerror('Error','Enter your email.')
            elif  password_login_entry.get() == '':
                messagebox.showerror('Error','Enter your password.')
            else :
                messagebox.showerror ("Error","No id exists!")

        login_label.place(relx = 0.45, rely = 0.1)

        email_login_label.place(relx = 0.25, rely = 0.3, relheight =  0.1, relwidth = 0.11)
        email_login_entry.place(relx = 0.37, rely = 0.32, relheight =  0.05, relwidth = 0.3)

        password_login_label.place(relx = 0.25, rely = 0.4, relheight =  0.1, relwidth = 0.11)
        password_login_entry.place(relx = 0.37, rely = 0.42, relheight =  0.05, relwidth = 0.3)

        rem_info_checkbox.place(relx = 0.37, rely = 0.5, relheight = 0.05)
        forgot_password_button.place(relx = 0.565, rely = 0.5, relheight = 0.05)
        forgot_password_button.config(command = f_p_window)
        forgot_password_button.bind('<Enter>', f_p)
        forgot_password_button.bind('<Leave>', f_p)

        login_button.place(relx = 0.45, rely = 0.67, relheight = 0.05, relwidth = 0.1)
        login_button.config(command = lambda : [check_login(event_val)])

        signup_button.place(relx = 0.45, rely = 0.825, relheight = 0.05, relwidth = 0.1)
        signup_button.config(command = lambda : [set_log_var_2(), check_log_var()])

        label_0.place(relx = 0.422, rely = 0.75)

    if log_var == 0:
        login()
    elif log_var == 1:
        signup()