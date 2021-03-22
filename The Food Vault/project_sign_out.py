from project_objects import *
from project_login_and_signup import check_log_var


def sign_out():

    value = messagebox.askyesno('Confirm','Do you really want to sign out?')
    if value == True:
        os.remove(os.getcwd() + '/csv and text files/info.txt')
        if os.path.isfile(os.getcwd() + '/csv and text files/item.csv') == True:
            os.remove(os.getcwd() + '/csv and text files/item.csv')

        frame_1.place_forget()
        frame_2.place_forget()
        frame_5.place_forget()
        frame_8.place_forget()
        frame_10.place_forget()
        frame_12.place_forget()
        frame_14.place_forget()
        canvas_2.place_forget()

        rest_head.place_forget()
        menu_head.place_forget()
        user_head.place_forget()
        cart_head.place_forget()
        ord_head.place_forget()
        hist_head.place_forget()

        label_1.place_forget()
        order_placed_label_1.place_forget()

        restaurant_list_button.config(bg = 'white')
        cart_button.config(bg = 'white')
        order_history_button.config(bg = 'white')
        user_details_button.config(bg = 'white')
        sign_out_button.config(bg = 'white')

        check_log_var()
