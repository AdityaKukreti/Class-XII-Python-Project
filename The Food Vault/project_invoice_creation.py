from fpdf import FPDF
from project_objects import *

def create_invoice(o_id,file_no):

    cur.execute('SELECT * FROM `user orders` WHERE `order id` = %s',(o_id,))
    for k in cur:
        order_id = 'Order id - ' + str(k[0])
        name = 'Customer Name - ' + k[2]
        number = 'Customer Number - ' + k[3]
        address = 'Customer Address - ' + k[4]
        rest = 'Restaurant Name - ' + k[5]
        rest_address = 'Restaurant Address - ' + k[-3]
        rest_number = 'Restaurant Number - ' + k[-2]
        ord_time = 'Order Time - ' + str(k[-1])
        item = k[6].split(',')
        item.pop()
        quantity = k[7].split(',')
        quantity.pop()
        price = k[8].split(',')
        price.pop()
        date = 'Order Date - ' + str(k[9])
        total_quantity = 0
        total_price = 0
        for i in range(len(item)):
            total_quantity += int(quantity[i])
            total_price += int(price[i]) * int(quantity[i])


    pdf = FPDF()

    pdf.add_page()


    pdf.set_font('Arial', size = 14)



    pdf.cell(200,10, txt = 'Python Project', ln = 1, align = 'C') 

    pdf.cell(200,5, txt = 'Food Ordering Program', ln = 1, align = 'C')

    pdf.dashed_line(34, 27, 185, 27, dash_length = 1)

    pdf.cell(200,12, txt = 'Invoice', ln = 1, align = 'C')

    pdf.dashed_line(34, 35, 185, 35, dash_length = 1)

    pdf.set_left_margin(33)

    pdf.cell(200,8, txt = order_id, ln = 1, align = 'L')
    pdf.cell(200,7, txt = date, ln = 1, align = 'L')
    pdf.cell(200,7, txt = ord_time, ln = 1, align = 'L')
    pdf.cell(200,7, txt = rest, ln = 1, align = 'L')
    pdf.cell(200,7, txt = rest_number, ln = 1, align = 'L')
    pdf.cell(200,7, txt = rest_address, ln = 1, align = 'L')
    pdf.cell(200,7, txt = name, ln = 1, align = 'L')
    pdf.cell(200,7, txt = number, ln = 1, align = 'L')
    pdf.cell(200,7, txt = address, ln = 1, align = 'L')

    pdf.dashed_line(34, 110, 185, 110, dash_length = 1)

    pdf.set_y(104)
    pdf.set_x(38)
    pdf.cell(200, 22, txt = 'Item', ln = 1)

    pdf.set_y(104)
    pdf.set_x(120)
    pdf.cell(200, 22, txt = 'Quantity', ln = 1)

    pdf.set_y(104)
    pdf.set_x(160)
    pdf.cell(200, 22, txt = 'Price', ln = 1)

    pdf.dashed_line(34, 120, 185, 120, dash_length = 1)

    

    for i in range(len(item)):
        pdf.set_x(38)
        y = pdf.get_y()
        pdf.cell(200, 10, txt = str(item[i]), ln = 1)



        pdf.set_y(y)
        pdf.set_x(125)
        pdf.cell(200, 10, txt = quantity[i], ln = 1)
        pdf.set_y(y)
        pdf.set_x(162)
        pdf.cell(200, 10, txt = price[i] + '.00', ln = 1)

    pdf.dashed_line(34, pdf.get_y() + 1.5, 185, pdf.get_y() + 1.5, dash_length = 1)

    

    pdf.set_x(38)
    y = pdf.get_y()
    pdf.cell(200, 17, txt = 'Total', ln = 1)
    pdf.set_y(y)
    pdf.set_x(125)
    pdf.cell(200, 17, txt = str(total_quantity), ln = 1)
    pdf.set_y(y)
    pdf.set_x(162)
    pdf.cell(200,17, txt = str(total_price) + '.00', ln = 1)

    y = pdf.get_y() - 10
    pdf.set_y(y)
    pdf.set_x(38)
    pdf.cell(200, 17, txt = 'GST(18%)', ln = 1)
    pdf.set_y(y)
    pdf.set_x(125)
    pdf.cell(200, 17, txt = str(total_quantity), ln = 1)
    pdf.set_y(y)
    pdf.set_x(162)
    tax = str(total_price * (18/100))
    fin_tax = ''
    cnt = 0
    for i in tax:
        if i == '.':
            fin_tax = fin_tax + tax[cnt:cnt + 3]
            break
        else:
            fin_tax = fin_tax + i
            cnt += 1

            
    pdf.cell(200, 17, txt = fin_tax, ln = 1)

    pdf.dashed_line(34, pdf.get_y() - 3, 185, pdf.get_y() - 3, dash_length = 1)

    y = pdf.get_y() - 5
    pdf.set_y(y)
    pdf.set_x(38)
    pdf.cell(200, 17, txt = 'Grand Total', ln = 1)
    pdf.set_y(y)
    pdf.set_x(125)
    pdf.cell(200, 17, txt = str(total_quantity), ln = 1)
    pdf.set_y(y)
    pdf.set_x(162)

    fin_tot_0 = str(total_price + float(fin_tax))
    fin_tot = ''
    cnt = 0
    for i in fin_tot_0:
        if i == '.':
            fin_tot = fin_tot + fin_tot_0[cnt:cnt + 3]
            break
        else:
            fin_tot = fin_tot + i
            cnt += 1


    pdf.cell(200,17, txt = fin_tot, ln = 1)

    pdf.dashed_line(34, pdf.get_y() - 3, 185, pdf.get_y() - 3, dash_length = 1)

    pdf.set_x(pdf.get_x() - 20)
    pdf.cell(200,17, txt = 'Thank you for ordering', ln = 1, align = 'C')
    pdf.set_y(pdf.get_y() - 8)
    pdf.set_x(pdf.get_x() - 20)
    pdf.cell(200,17, txt = 'We hope you have a great day!', ln = 1, align = 'C')

    file_name = os.getcwd() + '/Invoice/Invoice_' + str(file_no) + '.pdf'
    pdf.output(name = file_name)

    return file_name
