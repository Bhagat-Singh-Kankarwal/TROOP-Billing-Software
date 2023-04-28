from graphics import *
import mysql.connector as sql
import matplotlib.pyplot as plt
import time
import pyautogui

# database connection
mycon = sql.connect(host='localhost', user='root', passwd='abcd')
cursor = mycon.cursor()

# create database
cursor.execute("create database if not exists app_data")
cursor.execute("use app_data")

# create companies & products table
cursor.execute("create table if not exists companies (company varchar(50), net_total integer,\
invoice integer,date Date)")

cursor.execute("create table if not exists products (product varchar(20),\
unit_price float, description varchar(20))")

# deleting empty tables
cursor.execute("show tables")

table_name_data = []
for t_name in cursor:
    if t_name[0] == 'products' or t_name[0] == 'companies':
        pass
    else:
        table_name_data.append(t_name[0])

for d_name in table_name_data:

    cursor.execute("select * from {}".format(d_name))
    d2 = cursor.fetchall()
    if d2 == []:
        cursor.execute("drop table {}".format(d_name))
    else:
        pass

mycon.commit()

# panes on screen
win = GraphWin("TROOP", 900, 600)
win.setBackground(color_rgb(255, 255, 255))

# documentation / user manual
b_img = Image(Point(450, 300), r"img\bg.png")
b_img.draw(win)

user_guide = Text(Point(565, 75), "USERS' GUIDE")
user_guide.setFace("Product Sans Medium")
user_guide.setSize(20)
user_guide.setTextColor(color_rgb(47, 47, 47))
user_guide.draw(win)

p1 = Text(Point(565, 160 - 40), "• Description of products is same as the brand/type.")
p2 = Text(Point(565, 200 - 40), "• Before making Invoice make sure there are Products\n \
available to add.")
p3 = Text(Point(565, 240 - 40), "• Default description is - 'no-description'")
p4 = Text(Point(565, 280 - 40), "• Default company name is - 'no-name'")
p5 = Text(Point(565, 320 - 40), "• After entering company's name click anywhere on screen once.")
p6 = Text(Point(565, 370 - 40), "• To add product in Invoice write its details then click\n\
anywhere on screen once.")
p7 = Text(Point(565, 410 - 40), "• 'Go Back' in settings menu takes you back to the previous screen.")
p8 = Text(Point(565, 460 - 40), "• To save a Invoice, click on Finalise when you want to stop adding Products\n\
then click on 'Save' button in Top-Right Corner.")
p9 = Text(Point(565, 500 - 40), "• Unauthorized access to Settings will block access to settings.")

p10 = Text(Point(565, 550 - 10),
           "Install fonts before running the program.\nWithout appropriate fonts some things may not look as intended.")
p10.setFace("Franklin Gothic Demi Cond")
p10.setSize(14)
p10.draw(win)

p1.setFace('Product Sans Light')
p2.setFace('Product Sans Light')
p3.setFace('Product Sans Light')
p4.setFace('Product Sans Light')
p5.setFace('Product Sans Light')
p6.setFace('Product Sans Light')
p7.setFace('Product Sans Light')
p8.setFace('Product Sans Light')
p9.setFace('Product Sans Light')

p1.setSize(14)
p2.setSize(14)
p3.setSize(14)
p4.setSize(14)
p5.setSize(14)
p6.setSize(14)
p7.setSize(14)
p8.setSize(14)
p9.setSize(14)

p1.draw(win)
p2.draw(win)
p3.draw(win)
p4.draw(win)
p5.draw(win)
p6.draw(win)
p7.draw(win)
p8.draw(win)
p9.draw(win)

end = Text(Point(565, 580), "Click anywhere to continue")
end.setSize(9)
end.draw(win)

win.getMouse()
b_img.undraw()
end.undraw()
user_guide.undraw()
p1.undraw()
p2.undraw()
p3.undraw()
p4.undraw()
p5.undraw()
p6.undraw()
p7.undraw()
p8.undraw()
p9.undraw()
p10.undraw()
# ------------------------------------------------

# Navbar
navbar = Rectangle(Point(0, 0), Point(230, 600))
navbar.setWidth(0)
navbar.setFill(color_rgb(58, 158, 229))

navbar.draw(win)

# app_title
app_title = Text(Point(115, 30), "TROOP")
app_title.setSize(28)
app_title.setStyle('bold italic')
app_title.setTextColor("white")
app_title.setFace("Consolas")

app_title.draw(win)

app_def = Text(Point(115, 55), "Billing Software")
app_def.setSize(10)
app_def.setStyle('bold italic')
app_def.setTextColor("white")
app_def.setFace("Calibri")

app_def.draw(win)

# app_tiles

invoice_Img = Image(Point(50, 130), r"img\green.png")
invoice_Img.draw(win)

tile_invoice = Text(Point(115, 130), "Invoice")
tile_invoice.setFace("Product Sans Light")
tile_invoice.setSize(15)
tile_invoice.setTextColor("white")

tile_invoice.draw(win)

# ------------------------------------------------

bill_Img = Image(Point(50, 190), r"img\red.png")
bill_Img.draw(win)

tile_bill = Text(Point(115, 190), "Sales   ")
tile_bill.setFace("Product Sans Light")
tile_bill.setSize(15)
tile_bill.setTextColor("white")

tile_bill.draw(win)

# ------------------------------------------------

sett_Img = Image(Point(50, 250), r"img\settings21.png")
sett_Img.draw(win)

tile_sett = Text(Point(115, 250), "  Settings")
tile_sett.setFace("Product Sans Light")
tile_sett.setSize(15)
tile_sett.setTextColor("white")

tile_sett.draw(win)

# ------------------------------------------------
dev_lop = Text(Point(115, 520), "Developer".upper())
dev_lop.setFace("Product Sans Medium")
dev_lop.setSize(12)
dev_lop.setTextColor("white")

dev_lop.draw(win)

# ------------------------------------------------
exodus = Text(Point(115, 570), "EXIT")
exodus.setFace("Product Sans Medium")
exodus.setSize(12)
exodus.setTextColor("white")

exodus.draw(win)

# ------------------------------------------------
chk_i = 0
chk_b = 0
chk_s = 0
chk_d = 0
add_let_dis = 'n'
let_dis = 'n'


# ------------------------------------------------

# ------------------------------------------------
def devo():
    global chk_i, chk_b, chk_s, chk_d

    rect_d = Rectangle(Point(55, 535), Point(175, 505))
    rect_d.setWidth(0)
    rect_d.setOutline(None)
    rect_d.draw(win)

    rect_d.undraw()
    rect_d.setWidth(2)
    rect_d.setOutline('ivory')
    rect_d.draw(win)
    time.sleep(0.1)
    rect_d.undraw()

    try:
        rect_b.undraw()
        b_Img.undraw()
        tile_b.undraw()
    except:
        pass

    try:
        rect_s.undraw()
        s_Img.undraw()
        tile_s.undraw()
    except:
        pass

    try:
        rect_i.undraw()
        i_Img.undraw()
        tile_i.undraw()
    except:
        pass

    chk_d = 1
    chk_i = 0
    chk_s = 0
    chk_b = 0

    dev_clear = Rectangle(Point(231, 0), Point(900, -600))
    dev_clear.setWidth(0)
    dev_clear.setFill('white')
    dev_clear.draw(win)

    for ufo in range(60):
        dev_clear.move(0, 10)
        time.sleep(0.001)

    cc = "Copyright © 2020 Bhagat Singh Kankarwal"
    cce = Text(Point(765, 580 + 40), cc)
    cce.setFace("Product Sans Medium")
    cce.setSize(9)
    cce.setTextColor("black")
    cce.draw(win)

    for cec in range(20):
        cce.move(0, -2)
        time.sleep(0.001)

    # developer

    time.sleep(0.2)

    cir = Circle(Point(565, -120), 110)
    cir.setFill("black")
    cir.draw(win)

    txt1 = Text(Point(565, -95), "DEVELOPED BY  ")
    txt1.setTextColor("black")
    txt1.setFace("Gill Sans MT Ext Condensed Bold")
    txt1.setStyle('italic')
    txt1.setSize(30)
    txt1.draw(win)

    txt = Text(Point(985, 300), "BHAGAT SINGH KANKARWAL ")
    txt.setTextColor("white")
    txt.setFace("Gill Sans MT Ext Condensed Bold")
    txt.setStyle('italic')
    txt.setSize(21 + 2)
    txt.draw(win)

    line = Line(Point(493, -72), Point(623, -72))
    line.setWidth(2)
    line.draw(win)

    for i in range(42):
        cir.move(0, 10)
        txt.move(-10, 0)
        txt1.move(0, 5)
        line.move(0, 5)
        time.sleep(0.01)

    time.sleep(0.6)

    for i in range(3):
        cir.undraw()
        txt.undraw()

        cir = Circle(Point(565, 300), 110)
        cir.setFill("white")
        cir.setOutline("white")
        cir.draw(win)

        txt = Text(Point(565, 300), "BHAGAT SINGH KANKARWAL ")
        txt.setTextColor("black")
        txt.setFace("Gill Sans MT Ext Condensed Bold")
        txt.setSize(21 + 2)
        txt.setStyle('italic')
        txt.draw(win)

        time.sleep(0.2)
        cir.undraw()
        txt.undraw()

        cir = Circle(Point(565, 300), 110)
        cir.setFill("black")
        cir.setOutline("black")
        cir.draw(win)

        txt = Text(Point(565, 300), "BHAGAT SINGH KANKARWAL ")
        txt.setTextColor("white")
        txt.setFace("Gill Sans MT Ext Condensed Bold")
        txt.setSize(21 + 2)
        txt.setStyle('italic')
        txt.draw(win)

        time.sleep(0.2)


# ------------------------------------------------
def invoice():
    global rect_i, i_Img, tile_i, chk_i, chk_b, chk_s

    if chk_b == 1:
        rect_b.undraw()
        b_Img.undraw()
        tile_b.undraw()

        if chk_i == 1:
            pass

        else:

            rect_i = Rectangle(Point(0, 100), Point(230, 160))
            rect_i.setWidth(0)
            rect_i.setFill(color_rgb(20, 120, 191))
            rect_i.draw(win)

            chk_i = 1
            chk_b = 0
            chk_s = 0

            i_Img = Image(Point(50, 130), r"img\green.png")
            i_Img.draw(win)

            tile_i = Text(Point(115, 130), "Invoice")
            tile_i.setFace("Product Sans Light")
            tile_i.setSize(15)
            tile_i.setTextColor("white")

            tile_i.draw(win)

    elif chk_s == 1:
        rect_s.undraw()
        s_Img.undraw()
        tile_s.undraw()

        if chk_i == 1:
            pass

        else:

            rect_i = Rectangle(Point(0, 100), Point(230, 160))
            rect_i.setWidth(0)
            rect_i.setFill(color_rgb(20, 120, 191))
            rect_i.draw(win)

            chk_i = 1
            chk_b = 0
            chk_s = 0

            i_Img = Image(Point(50, 130), r"img\green.png")
            i_Img.draw(win)

            tile_i = Text(Point(115, 130), "Invoice")
            tile_i.setFace("Product Sans Light")
            tile_i.setSize(15)
            tile_i.setTextColor("white")

            tile_i.draw(win)

    else:

        if chk_i == 1:
            pass

        else:

            rect_i = Rectangle(Point(0, 100), Point(230, 160))
            rect_i.setWidth(0)
            rect_i.setFill(color_rgb(20, 120, 191))
            rect_i.draw(win)

            chk_i = 1
            chk_b = 0
            chk_s = 0

            i_Img = Image(Point(50, 130), r"img\green.png")
            i_Img.draw(win)

            tile_i = Text(Point(115, 130), "Invoice")
            tile_i.setFace("Product Sans Light")
            tile_i.setSize(15)
            tile_i.setTextColor("white")

            tile_i.draw(win)


# ------------------------------------------------
def bill():
    global rect_b, b_Img, tile_b, chk_b, chk_i, chk_s

    if chk_i == 1:
        rect_i.undraw()
        i_Img.undraw()
        tile_i.undraw()

        if chk_b == 1:
            pass

        else:

            rect_b = Rectangle(Point(0, 160), Point(230, 220))
            rect_b.setWidth(0)
            rect_b.setFill(color_rgb(20, 120, 191))
            rect_b.draw(win)

            chk_b = 1
            chk_i = 0
            chk_s = 0

            b_Img = Image(Point(50, 190), r"img\red.png")
            b_Img.draw(win)

            tile_b = Text(Point(115, 190), "Sales   ")
            tile_b.setFace("Product Sans Light")
            tile_b.setSize(15)
            tile_b.setTextColor("white")

            tile_b.draw(win)

    elif chk_s == 1:
        rect_s.undraw()
        s_Img.undraw()
        tile_s.undraw()

        if chk_b == 1:
            pass

        else:

            rect_b = Rectangle(Point(0, 160), Point(230, 220))
            rect_b.setWidth(0)
            rect_b.setFill(color_rgb(20, 120, 191))
            rect_b.draw(win)

            chk_b = 1
            chk_s = 0
            chk_i = 0

            b_Img = Image(Point(50, 190), r"img\red.png")
            b_Img.draw(win)

            tile_b = Text(Point(115, 190), "Sales   ")
            tile_b.setFace("Product Sans Light")
            tile_b.setSize(15)
            tile_b.setTextColor("white")

            tile_b.draw(win)
    else:

        if chk_b == 1:
            pass

        else:

            rect_b = Rectangle(Point(0, 160), Point(230, 220))
            rect_b.setWidth(0)
            rect_b.setFill(color_rgb(20, 120, 191))
            rect_b.draw(win)

            chk_b = 1
            chk_s = 0
            chk_i = 0

            b_Img = Image(Point(50, 190), r"img\red.png")
            b_Img.draw(win)

            tile_b = Text(Point(115, 190), "Sales   ")
            tile_b.setFace("Product Sans Light")
            tile_b.setSize(15)
            tile_b.setTextColor("white")

            tile_b.draw(win)


# ------------------------------------------------
def settings():
    global rect_s, s_Img, tile_s, chk_b, chk_i, chk_s

    if chk_i == 1:
        rect_i.undraw()
        i_Img.undraw()
        tile_i.undraw()

        if chk_s == 1:
            pass

        else:
            # allow_entry()

            rect_s = Rectangle(Point(0, 220), Point(230, 280))
            rect_s.setWidth(0)
            rect_s.setFill(color_rgb(20, 120, 191))
            rect_s.draw(win)

            chk_s = 1
            chk_i = 0
            chk_b = 0

            s_Img = Image(Point(50, 250), r"img\settings22.png")
            s_Img.draw(win)

            tile_s = Text(Point(115, 250), "  Settings")
            tile_s.setFace("Product Sans Light")
            tile_s.setSize(15)
            tile_s.setTextColor("white")

            tile_s.draw(win)

    elif chk_b == 1:
        rect_b.undraw()
        b_Img.undraw()
        tile_b.undraw()

        if chk_s == 1:
            pass

        else:
            # allow_entry()

            rect_s = Rectangle(Point(0, 220), Point(230, 280))
            rect_s.setWidth(0)
            rect_s.setFill(color_rgb(20, 120, 191))
            rect_s.draw(win)

            chk_s = 1
            chk_i = 0
            chk_b = 0

            s_Img = Image(Point(50, 250), r"img\settings22.png")
            s_Img.draw(win)

            tile_s = Text(Point(115, 250), "  Settings")
            tile_s.setFace("Product Sans Light")
            tile_s.setSize(15)
            tile_s.setTextColor("white")

            tile_s.draw(win)

    else:

        if chk_s == 1:
            rect_s = Rectangle(Point(0, 220), Point(230, 280))
            rect_s.setWidth(0)
            rect_s.setFill(color_rgb(20, 120, 191))
            rect_s.draw(win)

            chk_s = 1
            chk_i = 0
            chk_b = 0

            s_Img = Image(Point(50, 250), r"img\settings22.png")
            s_Img.draw(win)

            tile_s = Text(Point(115, 250), "  Settings")
            tile_s.setFace("Product Sans Light")
            tile_s.setSize(15)
            tile_s.setTextColor("white")

            tile_s.draw(win)

        else:
            # allow_entry()

            rect_s = Rectangle(Point(0, 220), Point(230, 280))
            rect_s.setWidth(0)
            rect_s.setFill(color_rgb(20, 120, 191))
            rect_s.draw(win)

            chk_s = 1
            chk_i = 0
            chk_b = 0

            s_Img = Image(Point(50, 250), r"img\settings22.png")
            s_Img.draw(win)

            tile_s = Text(Point(115, 250), "  Settings")
            tile_s.setFace("Product Sans Light")
            tile_s.setSize(15)
            tile_s.setTextColor("white")

            tile_s.draw(win)

        # ------------------------------------------------


# ------------------------------------------------
def page_invoice():
    # page clear before invoice
    page_clear = Rectangle(Point(231, 0), Point(900, 600))
    page_clear.setWidth(0)
    page_clear.setFill("white")
    page_clear.draw(win)

    # div line
    div_line = Line(Point(230, 40), Point(900, 40))
    div_line.setFill("light gray")
    div_line.setWidth(1)
    div_line.draw(win)

    # create invoice text
    header = Text(Point(308, -20), "Create Invoice")
    header.setSize(16 + 3)
    header.setStyle("bold")
    header.setTextColor("Gray")
    header.setFace("Gill Sans MT Condensed")
    header.draw(win)

    # save button
    save_button_bg = Rectangle(Point(820, 30), Point(880, 10))
    save_button_bg.setFill(color_rgb(102, 206, 110))
    save_button_bg.setOutline(None)
    save_button_bg.setWidth(0)
    save_button_bg.draw(win)

    save_button_text = Text(Point(850, 20), "SAVE")
    save_button_text.setTextColor("ivory")
    save_button_text.setSize(11)
    save_button_text.setFace("Product Sans Medium")
    save_button_text.draw(win)

    save_button_bg.move(0, -40)
    save_button_text.move(0, -40)

    # loop for header and save button
    for save in range(20):
        save_button_bg.move(0, 2)
        save_button_text.move(0, 2)
        header.move(0, 2)
        time.sleep(0.001)

    # date defined
    global date

    cursor.execute("select curdate()")
    data = cursor.fetchall()
    for i in data:
        for j in i:
            date = j
            break

    date_field = Text(Point(720, 100), "Date: ")
    date_field.setTextColor(color_rgb(70, 70, 70))
    date_field.setFace("Product Sans Medium")
    date_field.setSize(15)
    date_field.draw(win)

    date_value = Text(Point(805, 100), date)
    date_value.setFace("Product Sans Medium")
    date_value.setTextColor(color_rgb(70, 70, 70))
    date_value.setSize(15)
    date_value.draw(win)

    # data titles
    prod_title = Text(Point(320, 160), "Product")
    prod_title.setTextColor(color_rgb(58, 158, 229))
    prod_title.setSize(15 + 3)
    prod_title.setFace("Gill Sans MT Condensed")
    prod_title.draw(win)

    des_title = Text(Point(480, 160), "Description")
    des_title.setTextColor(color_rgb(58, 158, 229))
    des_title.setSize(15 + 3)
    des_title.setFace("Gill Sans MT Condensed")
    des_title.draw(win)

    qty = Text(Point(640, 160), "Qty.")
    qty.setTextColor(color_rgb(58, 158, 229))
    qty.setSize(15 + 3)
    qty.setFace("Gill Sans MT Condensed")
    qty.draw(win)

    u_price = Text(Point(720, 160), "Unit price")
    u_price.setTextColor(color_rgb(58, 158, 229))
    u_price.setSize(15 + 3)
    u_price.setFace("Gill Sans MT Condensed")
    u_price.draw(win)

    tot_price = Text(Point(831, 160), "Total")
    tot_price.setTextColor(color_rgb(58, 158, 229))
    tot_price.setSize(15 + 3)
    tot_price.setFace("Gill Sans MT Condensed")
    tot_price.draw(win)

    # blue line
    blue_line = Line(Point(292, 178), Point(851, 178))
    blue_line.setFill(color_rgb(58, 158, 229))
    blue_line.setWidth(1)
    blue_line.draw(win)


# ------------------------------------------------
def products_drop():
    cursor.execute("select * from products order by product")
    produt = cursor.fetchall()
    
    prod_d = ''
    x = 0
    for lm in produt:
        prod_d += lm[0].title() + '\n'
        x += 1

    prod_d = prod_d[:-1]

    prod_de = ''
    for lm in produt:
        prod_de += lm[2] + '\n'

    prod_de = prod_de[:-1]
    
    if x <= 3:
        p1 = Point(270, 200 + 28 * ht + 20)
        p2 = Point(650, 200 + 28 * ht + (x * 45))
    else:
        p1 = Point(270, 200 + 28 * ht + 20)
        p2 = Point(650, 200 + 28 * ht + (x * 25))

    rect_drop = Rectangle(p1, p2)
    rect_drop.setFill(color_rgb(244, 252, 253))
    rect_drop.draw(win)

    if x <= 3:
        pr1 = Text(Point(365, 200 + 28 * ht + x * 28), prod_d)
    else:
        pr1 = Text(Point(365, 200 + 28 * ht + x * 14.7), prod_d)
    pr1.setFace('Product Sans Light')
    pr1.draw(win)

    if x <= 3:
        pr2 = Text(Point(522, 200 + 28 * ht + x * 28), prod_de)
    else:
        pr2 = Text(Point(522, 200 + 28 * ht + x * 14.7), prod_de)
    pr2.setFace('Product Sans Light')
    pr2.draw(win)

    time.sleep(1.3)
    pr1.undraw()
    pr2.undraw()
    rect_drop.undraw()


def ad_prod_drop():
    cursor.execute("select * from products order by product")
    produt = cursor.fetchall()

    prod_d = ''
    x = 0
    for lm in produt:
        prod_d += lm[0].title() + '\n'
        x += 1

    prod_d = prod_d[:-1]

    prod_de = ''
    for lm in produt:
        prod_de += lm[2] + '\n'

    prod_de = prod_de[:-1]

    if x <= 3:
        p1 = Point(270, 475 - 20)
        p2 = Point(650, 475 - (x * 44))
    else:
        p1 = Point(270, 475 - 20)
        p2 = Point(650, 475 - (x * 24.5))
    

    rect_drop = Rectangle(p1, p2)
    rect_drop.setFill(color_rgb(244, 252, 253))
    rect_drop.draw(win)

    if x <= 3:
        pr1 = Text(Point(365, 475 - x * 27.5), prod_d)
    else:
        pr1 = Text(Point(365, 475 - x * 14), prod_d)
    pr1.setFace('Product Sans Light')

    pr1.draw(win)

    if x <= 3:
        pr2 = Text(Point(522, 475 - x * 27.5), prod_de)
    else:
        pr2 = Text(Point(522, 475 - x * 14), prod_de)
    pr2.setFace('Product Sans Light')

    pr2.draw(win)

    time.sleep(1.5)
    pr1.undraw()
    pr2.undraw()
    rect_drop.undraw()


def motion(event):
    x, y = event.x, event.y

    if let_dis == 'y' and 290 <= x <= 620 and 200 + 28 * ht - 30 <= y <= 200 + 28 * ht + 25:
        products_drop()

    elif add_let_dis == 'y' and 290 <= x <= 620 and 475 - 30 <= y <= 475 + 30:
        ad_prod_drop()

    else:
        pass


# ------------------------------------------------
def items_invoice():
    global co_name, net_total, invoice_num, ht, let_dis

    net_total = 0
    # company name box
    company_title = Text(Point(350, 100), "Company's Name: ")
    company_title.setTextColor(color_rgb(70, 70, 70))
    company_title.setFace("Product Sans Medium")
    company_title.setSize(15)
    company_title.draw(win)

    company_name = Entry(Point(510, 100), 15)
    company_name.setFace("Product Sans Light")
    company_name.setTextColor(color_rgb(47, 47, 47))
    company_name.setSize(12)
    company_name.setFill("white")
    company_name.draw(win)

    # invoice number looper
    invoice_num = 1
    cursor.execute("select invoice from companies")
    invoice_list = cursor.fetchall()

    code_list = []
    for i in invoice_list:
        code_list.append(i[0])

    code_list.sort()

    for jk in range(len(code_list)):
        if invoice_num in code_list:
            try:
                if code_list[jk + 1] == code_list[jk] + 1:
                    pass
                else:
                    invoice_num = code_list[jk] + 1
                    break

            except:
                invoice_num = code_list[-1] + 1

        else:
            break

    invo_title = Text(Point(380, 70), "Invoice No: ")
    invo_title.setSize(15)
    invo_title.setTextColor(color_rgb(70, 70, 70))
    invo_title.setFace('Product Sans Medium')
    invo_title.draw(win)

    invo_name = Text(Point(460, 70), invoice_num)
    invo_name.setSize(15)
    invo_name.setTextColor(color_rgb(70, 70, 70))
    invo_name.setFace('Product Sans Light')
    invo_name.draw(win)

    # animation rectangle over data header tiles
    rec = Rectangle(Point(260, 300), Point(880, 50))
    rec.setFill('white')
    rec.setWidth(0)
    rec.draw(win)

    for x in range(40):
        rec.move(0, 5)
        time.sleep(0.01)

    rec.undraw()

    # company table defined
    win.getMouse()

    try:
        co_name = company_name.getText()
        co_name = co_name.strip()

        if co_name == '':
            co_name = "no_name"

        else:
            if ' ' in co_name:
                str_comp = ''
                letter = 0

                while letter < len(co_name):

                    while letter < len(co_name) and co_name[letter] == ' ':
                        str_comp += '_'
                        letter += 1

                    while letter < len(co_name) and co_name[letter] != ' ':
                        str_comp += co_name[letter]
                        letter += 1

                co_name = str_comp

    except:
        co_name = "no_name"

    try:
        cursor.execute("create table if not exists {}(product varchar(20),\
description varchar(20), quantity integer,unit_price float, total float)".format(co_name))
    except:
        pass

    # entries
    new_pr_chkr = 0
    ht = 0
    while new_pr_chkr == 0 and ht < 10:
        new_pr_chkr = 1
        let_dis = 'y'

        height = 200 + 28 * ht

        pr = Entry(Point(365, height), 14)
        pr.setSize(12)
        pr.setFill("white")
        pr.setFace("Product Sans Medium")
        pr.setTextColor(color_rgb(70, 70, 70))
        pr.draw(win)

        des = Entry(Point(522, height), 16)
        des.setSize(12)
        des.setFill("white")
        des.setFace("Product Sans Medium")
        des.setTextColor(color_rgb(70, 70, 70))
        des.draw(win)

        qt = Entry(Point(635, height), 5)
        qt.setSize(12)
        qt.setFill("white")
        qt.setFace("Product Sans Medium")
        qt.setTextColor(color_rgb(70, 70, 70))
        qt.draw(win)

        if ht < 9:
            plus1 = Line(Point(298, 224 + 28 * ht), Point(298, 238 + 28 * ht))
            plus1.setWidth(2)
            plus1.setFill(color_rgb(120, 120, 120))
            plus1.draw(win)

            plus2 = Line(Point(291, 231 + 28 * ht), Point(305, 231 + 28 * ht))
            plus2.setWidth(2)
            plus2.setFill(color_rgb(120, 120, 120))
            plus2.draw(win)

            add_icon = Text(Point(355, 231 + 28 * ht), "Add Product")
            add_icon.setFace('Product Sans Light')
            add_icon.setSize(12)
            add_icon.setTextColor(color_rgb(120, 120, 120))
            add_icon.draw(win)

            h11 = Line(Point(595, 224 + 28 * ht), Point(595, 238 + 28 * ht))
            h22 = Line(Point(600, 224 + 28 * ht), Point(600, 238 + 28 * ht))
            h33 = Line(Point(587, 224 + 28 * ht), Point(601, 224 + 28 * ht))
            h44 = Line(Point(594, 237 + 28 * ht), Point(608, 237 + 28 * ht))

            h11.setFill(color_rgb(120, 120, 120))
            h22.setFill(color_rgb(120, 120, 120))
            h33.setFill(color_rgb(120, 120, 120))
            h44.setFill(color_rgb(120, 120, 120))

            h11.setWidth(2)
            h22.setWidth(2)
            h33.setWidth(2)
            h44.setWidth(2)

            h11.draw(win)
            h22.draw(win)
            h33.draw(win)
            h44.draw(win)

            finalise = Text(Point(640, 231 + 28 * ht), "Finalise")
            finalise.setFace('Product Sans Light')
            finalise.setSize(13)
            finalise.setTextColor(color_rgb(120, 120, 120))
            finalise.draw(win)

        else:
            pass

        cursor.execute("select * from products order by product")
        product_data = cursor.fetchall()

        # binding mouse
        win.bind('<Motion>', motion)

        win.getMouse()

        # getting text from entry boxes
        try:
            product = pr.getText().strip()

            if product == '':
                product = 'no_name'

        except:
            product = ""

        try:
            qty = int(qt.getText())

        except:
            qty = 0

        try:
            descrip = des.getText().strip()

            if descrip == '':
                descrip = "no_description"

        except:
            descrip = "no_description"

        # getting unit price from products table
        unit_price = 0

        for i in product_data:
            if i[0].upper() == product.upper():
                if i[2].upper() == descrip.upper():
                    unit_price = i[1]
                    break

        unit_p = Text(Point(710, height), unit_price)
        unit_p.setSize(12)
        unit_p.setFace("Product Sans Medium")
        unit_p.setTextColor(color_rgb(70, 70, 70))
        unit_p.draw(win)

        total = Text(Point(825, height), qty * unit_price)
        total.setSize(12)
        total.setFace("Product Sans Medium")
        total.setTextColor(color_rgb(70, 70, 70))
        total.draw(win)

        # used at the end .... at the bottom of page
        net_total += qty * unit_price

        # win.getMouse()

        try:
            total = float(total.getText())
        except:
            total = 0

        try:
            cursor.execute("insert into {} values('{}','{}',{},{},{})".format(co_name, \
                                                                              product, descrip, qty, unit_price, total))
            let_dis = 'n'
        except:
            pass

        pr.undraw()
        des.undraw()
        qt.undraw()

        pr = Text(Point(335, height), product)
        pr.setSize(12)
        pr.setFace("Product Sans Medium")
        pr.setTextColor(color_rgb(70, 70, 70))
        pr.draw(win)

        des = Text(Point(502, height), descrip)
        des.setSize(12)
        des.setFace("Product Sans Medium")
        des.setTextColor(color_rgb(70, 70, 70))
        des.draw(win)

        qt = Text(Point(635, height), qty)
        qt.setSize(12)
        qt.setFace("Product Sans Medium")
        qt.setTextColor(color_rgb(70, 70, 70))
        qt.draw(win)

        if ht < 9:
            ch = 'y'
            while ch == 'y':
                chkr_click = win.getMouse()

                if 291 <= chkr_click.getX() <= 400 and (224 + 28 * ht) <= chkr_click.getY() <= (238 + 28 * ht):
                    new_pr_chkr = 0
                    ch = 'q'
                    plus1.undraw()
                    plus2.undraw()
                    add_icon.undraw()

                    h11.undraw()
                    h22.undraw()
                    h33.undraw()
                    h44.undraw()
                    finalise.undraw()

                elif 580 <= chkr_click.getX() <= 670 and (224 + 28 * ht) <= chkr_click.getY() <= (238 + 28 * ht):
                    ch = 'q'
                    new_pr_chkr = 1
                    let_dis = 'n'
                    h11.undraw()
                    h22.undraw()
                    h33.undraw()
                    h44.undraw()
                    finalise.undraw()

                    plus1.undraw()
                    plus2.undraw()
                    add_icon.undraw()
        ht += 1

    # inserting company names along with net total in money_dictionary

    try:
        cursor.execute("insert into companies values('{}',{},{},'{}')".format(co_name, net_total, invoice_num, date))
    except:
        pass

    mycon.commit()

    # entry loop ends
    company_name.undraw()

    company_name = Text(Point(510, 100), co_name)
    company_name.setFace("Product Sans Light")
    company_name.setTextColor(color_rgb(47, 47, 47))
    company_name.setSize(12)
    company_name.draw(win)

    line1 = Line(Point(700, 510), Point(855, 510))
    line1.setWidth(1)
    line1.setFill("light gray")
    line1.draw(win)

    line2 = Line(Point(700, 540), Point(855, 540))
    line2.setWidth(1)
    line2.setFill("light gray")
    line2.draw(win)

    tot_txt = Text(Point(735, 525), "Total ")
    tot_txt.setSize(12)
    tot_txt.setTextColor(color_rgb(50, 50, 50))
    tot_txt.setFace("Product Sans Medium")
    tot_txt.draw(win)

    net_amt = Text(Point(825, 525), net_total)
    net_amt.setSize(12)
    net_amt.setTextColor(color_rgb(50, 50, 50))
    net_amt.setFace("Product Sans Medium")
    net_amt.draw(win)

    # making inserted data permanent using save button
    while True:
        sv_clk = win.getMouse()

        if 820 <= sv_clk.getX() <= 880 and 10 <= sv_clk.getY() <= 30:
            # save button invert
            save_button_bg = Rectangle(Point(820, 30), Point(880, 10))
            save_button_bg.setFill('ivory')
            save_button_bg.setOutline(color_rgb(102, 206, 110))
            save_button_bg.setWidth(2)
            save_button_bg.draw(win)

            save_button_text = Text(Point(850, 20), "SAVE")
            save_button_text.setTextColor(color_rgb(102, 206, 110))
            save_button_text.setSize(11)
            save_button_text.setFace("Product Sans Medium")
            save_button_text.draw(win)

            time.sleep(0.1)
            save_button_bg.undraw()
            save_button_text.undraw()

            # save button revert
            save_button_bg = Rectangle(Point(820, 30), Point(880, 10))
            save_button_bg.setFill(color_rgb(102, 206, 110))
            save_button_bg.setOutline(None)
            save_button_bg.setWidth(0)
            save_button_bg.draw(win)

            save_button_text = Text(Point(850, 20), "SAVE")
            save_button_text.setTextColor("ivory")
            save_button_text.setSize(11)
            save_button_text.setFace("Product Sans Medium")
            save_button_text.draw(win)

            mycon.commit()
            break

        else:
            pass


# ------------------------------------------------
def bill_page():
    # page clear before invoice
    page_clear = Rectangle(Point(231, 0), Point(900, 600))
    page_clear.setWidth(0)
    page_clear.setFill("white")
    page_clear.draw(win)

    # div line
    div_line = Line(Point(230, 40), Point(900, 40))
    div_line.setFill("light gray")
    div_line.setWidth(1)
    div_line.draw(win)

    # create invoice text
    header = Text(Point(308, -20), "Sales Summary")
    header.setSize(16 + 3)
    header.setStyle("bold")
    header.setTextColor("Gray")
    header.setFace("Gill Sans MT Condensed")
    header.draw(win)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    bill_show = Image(Point(780, -20), r'img\show.png')
    bill_show.draw(win)

    for head in range(20):
        header.move(0, 2)
        bill_show.move(0, 2)
        time.sleep(0.001)

    # invoice header
    inv_head = Text(Point(290 + 600, 70), "Invoice")
    inv_head.setFace("Product Sans Medium")
    inv_head.setTextColor(color_rgb(47, 47, 47))
    inv_head.setSize(15)
    inv_head.setStyle("underline")
    inv_head.draw(win)

    # company header
    company = Text(Point(400 + 600, 70), "Company")
    company.setFace("Product Sans Medium")
    company.setTextColor(color_rgb(47, 47, 47))
    company.setSize(15)
    company.setStyle("underline")
    company.draw(win)

    # total_amount
    amt = Text(Point(780 + 600, 70), "Sales")
    amt.setFace("Product Sans Medium")
    amt.setTextColor(color_rgb(47, 47, 47))
    amt.setSize(15)
    amt.setStyle("underline")
    amt.draw(win)

    # break go back
    go_back = Text(Point(335 + 230 + 600, 550), "Go Back")
    go_back.setSize(13)
    go_back.setFace("Product Sans Light")
    go_back.setTextColor(color_rgb(80, 80, 80))
    go_back.draw(win)

    for l in range(60):
        company.move(-10, 0)
        amt.move(-10, 0)
        inv_head.move(-10, 0)
        go_back.move(-10, 0)
        time.sleep(0.001)

    time.sleep(0.1)

    # displaying sales summary
    cursor.execute("select * from companies order by invoice")
    company_names = cursor.fetchall()

    a = 20

    for i in company_names:
        i = list(i)

        iin = str(i[2])
        iin = ' ' * (3 - len(iin)) + iin

        inv_no = Text(Point(300, 100 + a), iin)
        inv_no.setSize(15)
        inv_no.setFace('Product Sans Light')
        inv_no.setTextColor(color_rgb(47, 47, 47))
        inv_no.draw(win)

        new_i = ''
        let = 0
        while let < len(i[0]):
            while let < len(i[0]) and i[0][let] == '_':
                new_i += ' '
                let += 1

            while let < len(i[0]) and i[0][let] != '_':
                new_i += i[0][let]
                let += 1

        new_i = new_i.lower()
        new_i += ' ' * (25 - len(new_i))

        company = Text(Point(547, 100 + a), new_i)
        company.setFace("Major Mono Display")
        company.setTextColor(color_rgb(47, 47, 47))
        company.setSize(15)
        company.draw(win)

        value = str(i[1])
        value = '  ' * (9 - len(value)) + value

        amt = Text(Point(760, 100 + a), value)
        amt.setFace("Product Sans Light")
        amt.setTextColor(color_rgb(47, 47, 47))
        amt.setSize(15)
        amt.draw(win)

        hr = Line(Point(260, 100 + a + 12), Point(817, 100 + a + 12))
        hr.setFill("gray")
        hr.setWidth(1)
        hr.draw(win)

        a += 22
        time.sleep(0.01)

    # loop ends


# ------------------------------------------------
def settings_page():
    # page clear before invoice
    page_clear = Rectangle(Point(231, 0), Point(900, 600))
    page_clear.setWidth(0)
    page_clear.setFill("white")
    page_clear.draw(win)

    # div line
    div_line = Line(Point(230, 40), Point(900, 40))
    div_line.setFill("light gray")
    div_line.setWidth(1)
    div_line.draw(win)

    # create invoice text
    header = Text(Point(308, -20), "Settings")
    header.setSize(16 + 3)
    header.setStyle("bold")
    header.setTextColor("Gray")
    header.setFace("Gill Sans MT Condensed")
    header.draw(win)

    for head in range(20):
        header.move(0, 2)
        time.sleep(0.001)

    # data tiles

    # add product
    add_pr = Text(Point(335 + 230 + 500, 200), "Edit Products")
    add_pr.setSize(16)
    add_pr.setFace("Product Sans Light")
    add_pr.setTextColor(color_rgb(80, 80, 80))
    add_pr.draw(win)

    # change companies in sales summary
    edit_sales = Text(Point(335 + 230 + 500, 300), "Edit Sales Summary")
    edit_sales.setSize(16)
    edit_sales.setFace("Product Sans Light")
    edit_sales.setTextColor(color_rgb(80, 80, 80))
    edit_sales.draw(win)

    # change companies in sales summary
    bill_data = Text(Point(335 + 230 + 500, 400), "Change Data in Bills")
    bill_data.setSize(16)
    bill_data.setFace("Product Sans Light")
    bill_data.setTextColor(color_rgb(80, 80, 80))
    bill_data.draw(win)

    # break go back
    go_back = Text(Point(335 + 230 + 500, 550), "Go Back")
    go_back.setSize(13)
    go_back.setFace("Product Sans Light")
    go_back.setTextColor(color_rgb(80, 80, 80))
    go_back.draw(win)

    rect_tt = Rectangle(Point(525, 565), Point(605, 535))
    rect_tt.setWidth(0)
    rect_tt.draw(win)

    # moving data tiles inside frame
    for a in range(50):
        add_pr.move(-10, 0)
        edit_sales.move(-10, 0)
        bill_data.move(-10, 0)
        go_back.move(-10, 0)
        time.sleep(0.001)

    # loop for clicks 
    while True:
        click_set = win.getMouse()

        if 490 <= click_set.getX() <= 640 and 180 <= click_set.getY() <= 220:
            img1 = Image(Point(565, 200), r"img\img1.png")
            img1.draw(win)

            time.sleep(0.2)
            img1.undraw()

            time.sleep(0.2)

            for var in range(50):
                add_pr.move(10, 0)
                edit_sales.move(10, 0)
                bill_data.move(10, 0)
                go_back.move(10, 0)
                header.move(0, -2)
                time.sleep(0.001)

            add_pr.undraw()
            edit_sales.undraw()
            bill_data.undraw()
            go_back.undraw()

            edit_products()
            break

        elif 465 <= click_set.getX() <= 665 and 280 <= click_set.getY() <= 320:
            img2 = Image(Point(565, 300), r"img\img2.png")
            img2.draw(win)

            time.sleep(0.2)
            img2.undraw()

            time.sleep(0.2)

            for var in range(50):
                add_pr.move(10, 0)
                edit_sales.move(10, 0)
                bill_data.move(10, 0)
                go_back.move(10, 0)
                header.move(0, -2)
                time.sleep(0.001)

            add_pr.undraw()
            edit_sales.undraw()
            bill_data.undraw()
            go_back.undraw()

            edit_sales_sum()
            break

        elif 465 <= click_set.getX() <= 665 and 380 <= click_set.getY() <= 420:
            img3 = Image(Point(565, 400), r"img\img3.png")
            img3.draw(win)

            time.sleep(0.2)
            img3.undraw()

            time.sleep(0.2)

            for var in range(50):
                add_pr.move(10, 0)
                edit_sales.move(10, 0)
                bill_data.move(10, 0)
                go_back.move(10, 0)
                header.move(0, -2)
                time.sleep(0.001)

            add_pr.undraw()
            edit_sales.undraw()
            bill_data.undraw()
            go_back.undraw()

            edit_invoice_data()
            break

        elif 525 <= click_set.getX() <= 605 and 535 <= click_set.getY() <= 565:
            for ai in range(2):
                rect_tt.setWidth(1)
                rect_tt.setOutline("gray")
                time.sleep(0.1)

                rect_tt.setWidth(0)
                rect_tt.setOutline(None)
                time.sleep(0.1)

            rect_tt.undraw()

            rect_tt = Rectangle(Point(231, -1), Point(900, -600))
            rect_tt.setWidth(0)
            rect_tt.setFill('white')
            rect_tt.draw(win)

            for l in range(60):
                rect_tt.move(0, 10)
                time.sleep(0.001)

            rect_s.undraw()
            s_Img.undraw()
            tile_s.undraw()

            break


# ------------------------------------------------

def edit_invoice_data():
    global product_s, product_i

    # page clear before invoice
    page_clear = Rectangle(Point(231, 0), Point(900, 600))
    page_clear.setWidth(0)
    page_clear.setFill("white")
    page_clear.draw(win)

    # div line
    div_line = Line(Point(230, 40), Point(900, 40))
    div_line.setFill("light gray")
    div_line.setWidth(1)
    div_line.draw(win)

    # create invoice text
    header = Text(Point(325, -20), "Edit Invoice Data")
    header.setSize(16 + 3)
    header.setStyle("bold")
    header.setTextColor("Gray")
    header.setFace("Gill Sans MT Condensed")
    header.draw(win)

    for var in range(20):
        header.move(0, 2)
        time.sleep(0.001)

    # title heads for company and sales
    title_1 = Text(Point(390, 80), "Company")
    title_1.setFace("Product Sans Medium")
    title_1.setTextColor(color_rgb(70, 70, 70))
    title_1.setSize(14)
    title_1.setStyle('underline')
    title_1.draw(win)

    # displaying sales summary
    cursor.execute("select * from companies order by invoice")
    company_names = cursor.fetchall()
    a = 15

    for i in company_names:
        i = list(i)

        new_i = ''
        let = 0
        while let < len(i[0]):
            while let < len(i[0]) and i[0][let] == '_':
                new_i += ' '
                let += 1

            while let < len(i[0]) and i[0][let] != '_':
                new_i += i[0][let]
                let += 1

        new_i = new_i.lower()

        company = Text(Point(390, 95 + a), new_i)
        company.setFace("Major Mono Display")
        company.setTextColor(color_rgb(47, 47, 47))
        company.setSize(12)
        company.draw(win)

        hr = Line(Point(240, 95 + a + 9), Point(540, 95 + a + 9))
        hr.setFill("gray")
        hr.setWidth(1)
        hr.draw(win)

        a += 20
        time.sleep(0.01)

    # vertical rule
    lineV = Line(Point(550, 40), Point(550, 600))
    lineV.setFill("light gray")
    lineV.setWidth(1)
    lineV.draw(win)

    # entry of name to be edited
    edit_entry = Text(Point(775 + 300, 200), "Enter Name of the Company to be Edited")
    edit_entry.setSize(14)
    edit_entry.setFace('Product Sans Light')
    edit_entry.setTextColor(color_rgb(80, 80, 80))
    edit_entry.draw(win)

    edit_entry_new_box = Entry(Point(775 + 300, 250), 17)
    edit_entry_new_box.setFace("Product Sans Light")
    edit_entry_new_box.setTextColor(color_rgb(50, 50, 50))
    edit_entry_new_box.setSize(12)
    edit_entry_new_box.setFill('ivory')
    edit_entry_new_box.draw(win)

    # exit
    exit_pr = Text(Point(775 + 300, 550), "Go Back")
    exit_pr.setSize(13)
    exit_pr.setFace('Product Sans Light')
    exit_pr.setTextColor(color_rgb(80, 80, 80))
    exit_pr.draw(win)

    # change invoice
    change_invoice_bg = Rectangle(Point(735 + 300, 380), Point(815 + 300, 420))
    change_invoice_bg.setFill(color_rgb(102, 206, 110))
    change_invoice_bg.setOutline(None)
    change_invoice_bg.setWidth(0)
    change_invoice_bg.draw(win)

    change_invoice = Text(Point(775 + 300, 400), "ENTER")
    change_invoice.setTextColor("ivory")
    change_invoice.setSize(13)
    change_invoice.setFace("Product Sans Medium")
    change_invoice.draw(win)

    for ex in range(35):
        edit_entry.move(-10, 0)
        edit_entry_new_box.move(-10, 0)
        change_invoice_bg.move(-10, 0)
        change_invoice.move(-10, 0)
        exit_pr.move(-10, 0)
        time.sleep(0.001)

    rect_m = Rectangle(Point(685, 565), Point(765, 535))
    rect_m.setWidth(0)
    rect_m.draw(win)

    while True:
        click_invo = win.getMouse()
        if 685 <= click_invo.getX() <= 765 and 380 <= click_invo.getY() <= 420:
            change_invoice_bg.undraw()
            change_invoice.undraw()

            # change invoice invert
            change_invoice_bg = Rectangle(Point(685, 380), Point(765, 420))
            change_invoice_bg.setFill('ivory')
            change_invoice_bg.setOutline(color_rgb(102, 206, 110))
            change_invoice_bg.setWidth(2)
            change_invoice_bg.draw(win)

            change_invoice = Text(Point(725, 400), "ENTER")
            change_invoice.setTextColor(color_rgb(102, 206, 110))
            change_invoice.setSize(13)
            change_invoice.setFace("Product Sans Medium")
            change_invoice.draw(win)

            time.sleep(0.1)
            change_invoice_bg.undraw()
            change_invoice.undraw()

            # change invoice revert
            change_invoice_bg = Rectangle(Point(685, 380), Point(765, 420))
            change_invoice_bg.setFill(color_rgb(102, 206, 110))
            change_invoice_bg.setOutline(None)
            change_invoice_bg.setWidth(0)
            change_invoice_bg.draw(win)

            change_invoice = Text(Point(725, 400), "ENTER")
            change_invoice.setTextColor("ivory")
            change_invoice.setSize(13)
            change_invoice.setFace("Product Sans Medium")
            change_invoice.draw(win)

            edi_name = edit_entry_new_box.getText().strip()

            time.sleep(0.2)

            chkr = 0
            global tab_edi_name

            tab_edi_name = ''

            while chkr < len(edi_name):
                while chkr < len(edi_name) and edi_name[chkr] == ' ':
                    tab_edi_name += '_'
                    chkr += 1
                while chkr < len(edi_name) and edi_name[chkr] != ' ':
                    tab_edi_name += edi_name[chkr]
                    chkr += 1

            # getting required data from all tables and databases
            try:
                cursor.execute("select * from {}".format(tab_edi_name))
                product_s = cursor.fetchall()

                cursor.execute("select * from companies where company = '{}'".format(tab_edi_name))
                product_i = cursor.fetchall()

                # removing elements from screen
                for clm in range(35):
                    edit_entry.move(10, 0)
                    edit_entry_new_box.move(10, 0)
                    change_invoice_bg.move(10, 0)
                    change_invoice.move(10, 0)
                    exit_pr.move(10, 0)
                    time.sleep(0.001)

                rect_cl = Rectangle(Point(231 + 320, 41), Point(900 + 320, 600))
                rect_cl.setWidth(0)
                rect_cl.setFill('white')
                rect_cl.draw(win)

                for clm in range(32):
                    rect_cl.move(-10, 0)
                    time.sleep(0.001)

                re_entering_invoice()
                break
            except:
                pass

        elif 685 <= click_invo.getX() <= 765 and 535 <= click_invo.getY() <= 565:
            for ani in range(2):
                rect_m.setWidth(1)
                rect_m.setOutline("gray")
                time.sleep(0.1)

                rect_m.setWidth(0)
                rect_m.setOutline(None)
                time.sleep(0.1)

            rect_m.undraw()

            rect_m = Rectangle(Point(231, -1), Point(900, -600))
            rect_m.setWidth(0)
            rect_m.setFill('white')
            rect_m.draw(win)

            edit_entry_new_box.undraw()

            for l in range(60):
                rect_m.move(0, 10)
                time.sleep(0.001)

            settings_page()
            break
        # ------------------------------------------------


def re_entering_invoice():
    global new_net_total, add_let_dis
    add_let_dis = 'n'
    # date display
    try:
        for cmw in product_i:
            if tab_edi_name.lower() == cmw[0].lower():
                invi_date = cmw[3]
                new_net_total = cmw[1]
    except:
        pass

    date_invo = Text(Point(295, 70), "Date: ")
    date_invo.setSize(13)
    date_invo.setFace('Product Sans Medium')
    date_invo.setTextColor(color_rgb(70, 70, 70))
    date_invo.draw(win)

    date_invo_data = Text(Point(390, 70), invi_date)
    date_invo_data.setSize(13)
    date_invo_data.setFace('Product Sans Medium')
    date_invo_data.setTextColor(color_rgb(70, 70, 70))
    date_invo_data.draw(win)

    comp_invo = Text(Point(650, 70), "Company: ")
    comp_invo.setSize(13)
    comp_invo.setFace('Product Sans Medium')
    comp_invo.setTextColor(color_rgb(70, 70, 70))
    comp_invo.draw(win)

    comp_edi_name = ''
    ari = 0
    while ari < len(tab_edi_name):
        while ari < len(tab_edi_name) and tab_edi_name[ari] == '_':
            comp_edi_name += ' '
            ari += 1
        while ari < len(tab_edi_name) and tab_edi_name[ari] != '_':
            comp_edi_name += tab_edi_name[ari]
            ari += 1

    comp_edi_name = comp_edi_name.title()

    comp_invo_data = Text(Point(810, 70), comp_edi_name)
    comp_invo_data.setSize(13)
    comp_invo_data.setFace('Product Sans Medium')
    comp_invo_data.setTextColor(color_rgb(70, 70, 70))
    comp_invo_data.draw(win)

    # print icon
    pr_ic = Image(Point(650, -20), r"img\print_icon.png")
    pr_ic.draw(win)

    # invoice head
    ti = Text(Point(730, -20), "Invoice No: ")
    ti.setFace('Product Sans Medium')
    ti.setSize(13)
    ti.setTextColor(color_rgb(70, 70, 70))
    ti.draw(win)

    try:
        for cmm in product_i:
            if tab_edi_name.lower() == cmm[0].lower():
                invi_num = cmm[2]
    except:
        pass

    ti_d = Text(Point(795, -20), invi_num)
    ti_d.setFace('Product Sans Light')
    ti_d.setSize(13)
    ti_d.setTextColor(color_rgb(70, 70, 70))
    ti_d.draw(win)

    for ti_ in range(20):
        ti.move(0, 2)
        ti_d.move(0, 2)
        pr_ic.move(0, 2)
        time.sleep(0.01)

    # product head
    t1 = Text(Point(320, 70 + 50), "Product")
    t1.setFace("Gill Sans MT Condensed")
    t1.setSize(13 + 3)
    t1.setStyle('bold')
    t1.setTextColor(color_rgb(70, 70, 70))
    t1.draw(win)

    # description head
    t2 = Text(Point(480, 70 + 50), "Description")
    t2.setFace("Gill Sans MT Condensed")
    t2.setSize(13 + 3)
    t2.setStyle('bold')
    t2.setTextColor(color_rgb(70, 70, 70))
    t2.draw(win)

    # quantity head
    t3 = Text(Point(640, 70 + 50), "Qty.")
    t3.setFace("Gill Sans MT Condensed")
    t3.setSize(13 + 3)
    t3.setStyle('bold')
    t3.setTextColor(color_rgb(70, 70, 70))
    t3.draw(win)

    # unit price head
    t4 = Text(Point(720, 70 + 50), "Unit Price")
    t4.setFace("Gill Sans MT Condensed")
    t4.setSize(13 + 3)
    t4.setStyle('bold')
    t4.setTextColor(color_rgb(70, 70, 70))
    t4.draw(win)

    # total head
    t5 = Text(Point(831, 70 + 50), "Total")
    t5.setFace('Gill Sans MT Condensed')
    t5.setSize(13 + 3)
    t5.setStyle('bold')
    t5.setTextColor(color_rgb(70, 70, 70))
    t5.draw(win)

    incr = 0
    for com in product_s:
        com = list(com)

        com[0] = com[0].title()
        pro_s = Text(Point(320, 95 + 50 + incr), com[0])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        com[1] = com[1].title()
        pro_s = Text(Point(480, 95 + 50 + incr), com[1])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(640, 95 + 50 + incr), com[2])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(720, 95 + 50 + incr), com[3])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(831, 95 + 50 + incr), com[4])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        incr += 20
        time.sleep(0.01)

    # total at the end of page
    line1 = Line(Point(700, 360), Point(855, 360))
    line1.setWidth(1)
    line1.setFill("light gray")
    line1.draw(win)

    line2 = Line(Point(700, 390), Point(855, 390))
    line2.setWidth(1)
    line2.setFill("light gray")
    line2.draw(win)

    tot_txt = Text(Point(735, 375), "Total ")
    tot_txt.setSize(12)
    tot_txt.setTextColor(color_rgb(50, 50, 50))
    tot_txt.setFace("Product Sans Medium")
    tot_txt.draw(win)

    net_amt = Text(Point(825, 375), new_net_total)
    net_amt.setSize(12)
    net_amt.setTextColor(color_rgb(50, 50, 50))
    net_amt.setFace("Product Sans Medium")
    net_amt.draw(win)

    # horizontal Line
    lineH = Line(Point(230, 400 + 300), Point(900, 400 + 300))
    lineH.setFill('light gray')
    lineH.setWidth(1)
    lineH.draw(win)

    # add item to invoice
    add_invo = Text(Point(350, 500 + 300), "Add Item")
    add_invo.setSize(15)
    add_invo.setFace('Product Sans Light')
    add_invo.setTextColor(color_rgb(80, 80, 80))
    add_invo.draw(win)

    # delete item from invoice
    del_invo = Text(Point(525, 500 + 300), "Delete Item")
    del_invo.setSize(15)
    del_invo.setFace('Product Sans Light')
    del_invo.setTextColor(color_rgb(80, 80, 80))
    del_invo.draw(win)

    # go back to invoice
    back_invo = Text(Point(850 - 100, 500 + 300), "Go Back")
    back_invo.setSize(13)
    back_invo.setFace('Product Sans Light')
    back_invo.setTextColor(color_rgb(80, 80, 80))
    back_invo.draw(win)

    for idk in range(30):
        lineH.move(0, -10)
        add_invo.move(0, -10)
        del_invo.move(0, -10)
        back_invo.move(0, -10)
        time.sleep(0.001)

    rect_go_back = Rectangle(Point(810 - 100, 515), Point(890 - 100, 485))
    rect_go_back.setWidth(0)
    rect_go_back.draw(win)

    # binding mouse
    win.bind('<Motion>', motion)

    while True:
        click_invo_edit = win.getMouse()

        if 300 <= click_invo_edit.getX() <= 400 and 480 <= click_invo_edit.getY() <= 520:

            bl1 = Rectangle(Point(300, 520), Point(296, 480))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(400, 520), Point(404, 480))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)

            #  add_invo_item()
            add_invo_item()

        elif 465 <= click_invo_edit.getX() <= 585 and 480 <= click_invo_edit.getY() <= 520:
            bl1 = Rectangle(Point(465, 520), Point(461, 480))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(585, 520), Point(589, 480))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)

            # delete_invo_item
            delete_invo_item()

        elif 630 <= click_invo_edit.getX() <= 670 and 0 <= click_invo_edit.getY() <= 40:

            pr_ic.undraw()

            time.sleep(0.5)

            loc = pyautogui.locateOnScreen(r'img\locator.png')
            left, top = loc[0], loc[1]
            width, height = 670, 400

            temp_rect = Rectangle(Point(231, 0), Point(675, 39))
            temp_rect.setWidth(0)
            temp_rect.setFill('white')
            temp_rect.draw(win)

            line_l = Line(Point(230, 0), Point(230, 400))
            line_r = Line(Point(899, 0), Point(899, 400))
            line_t = Line(Point(230, 1), Point(900, 1))

            line_l.setWidth(1)
            line_r.setWidth(1)
            line_t.setWidth(1)

            line_l.setFill('light gray')
            line_r.setFill('light gray')
            line_t.setFill('light gray')

            line_l.draw(win)
            line_r.draw(win)
            line_t.draw(win)

            time.sleep(0.5)

            scr = pyautogui.screenshot(region=(left, top, width, height))
            scr.save(r'Bills\Invoice_{}_{}.png'.format(invi_num, tab_edi_name.capitalize()))

            temp_rect.undraw()
            line_l.undraw()
            line_r.undraw()
            line_t.undraw()
            pr_ic.draw(win)

        elif 810 - 100 <= click_invo_edit.getX() <= 890 - 100 and 485 <= click_invo_edit.getY() <= 515:

            for ani in range(2):
                rect_go_back.setWidth(1)
                rect_go_back.setOutline("gray")
                time.sleep(0.1)

                rect_go_back.setWidth(0)
                rect_go_back.setOutline(None)
                time.sleep(0.1)

            rect_go_back.undraw()

            rect_go_back = Rectangle(Point(231, -1), Point(900, -600))
            rect_go_back.setWidth(0)
            rect_go_back.setFill('white')
            rect_go_back.draw(win)

            for l in range(60):
                rect_go_back.move(0, 10)
                time.sleep(0.001)

            edit_invoice_data()

            break


# ------------------------------------------------
# ------------------------------------------------
def add_invo_item():
    global add_let_dis, new_net_total

    # page moving in
    rect_mov = Rectangle(Point(231, 601 + 300), Point(900, 401 + 300))
    rect_mov.setWidth(0)
    rect_mov.setFill('white')
    rect_mov.draw(win)

    prod_title = Text(Point(320, 440 + 300), "Product")
    prod_title.setTextColor(color_rgb(90, 90, 90))
    prod_title.setSize(15 + 3)
    prod_title.setFace("Gill Sans MT Condensed")
    prod_title.draw(win)

    des_title = Text(Point(480, 440 + 300), "Description")
    des_title.setTextColor(color_rgb(90, 90, 90))
    des_title.setSize(15 + 3)
    des_title.setFace("Gill Sans MT Condensed")
    des_title.draw(win)

    qty = Text(Point(640, 440 + 300), "Qty.")
    qty.setTextColor(color_rgb(90, 90, 90))
    qty.setSize(15 + 3)
    qty.setFace("Gill Sans MT Condensed")
    qty.draw(win)

    u_price = Text(Point(720, 440 + 300), "Unit price")
    u_price.setTextColor(color_rgb(90, 90, 90))
    u_price.setSize(15 + 3)
    u_price.setFace("Gill Sans MT Condensed")
    u_price.draw(win)

    tot_price = Text(Point(831, 440 + 300), "Total")
    tot_price.setTextColor(color_rgb(90, 90, 90))
    tot_price.setSize(15 + 3)
    tot_price.setFace("Gill Sans MT Condensed")
    tot_price.draw(win)

    height = 475

    pr_invo = Entry(Point(365, height + 300), 14)
    pr_invo.setSize(12)
    pr_invo.setFill("white")
    pr_invo.setFace("Product Sans Medium")
    pr_invo.setTextColor(color_rgb(70, 70, 70))
    pr_invo.draw(win)

    des_invo = Entry(Point(522, height + 300), 16)
    des_invo.setSize(12)
    des_invo.setFill("white")
    des_invo.setFace("Product Sans Medium")
    des_invo.setTextColor(color_rgb(70, 70, 70))
    des_invo.draw(win)

    qt_invo = Entry(Point(635, height + 300), 5)
    qt_invo.setSize(12)
    qt_invo.setFill("white")
    qt_invo.setFace("Product Sans Medium")
    qt_invo.setTextColor(color_rgb(70, 70, 70))
    qt_invo.draw(win)

    # submit
    submit_bg = Rectangle(Point(525, 300 + 530), Point(605, 300 + 570))
    submit_bg.setFill(color_rgb(102, 206, 110))
    submit_bg.setOutline(None)
    submit_bg.setWidth(0)
    submit_bg.draw(win)

    submit = Text(Point(565, 300 + 550), "SUBMIT")
    submit.setTextColor("ivory")
    submit.setSize(13)
    submit.setFace("Product Sans Medium")
    submit.draw(win)

    for vevo in range(30):
        rect_mov.move(0, -10)
        prod_title.move(0, -10)
        des_title.move(0, -10)
        qty.move(0, -10)
        u_price.move(0, -10)
        tot_price.move(0, -10)
        pr_invo.move(0, -10)
        des_invo.move(0, -10)
        qt_invo.move(0, -10)
        submit_bg.move(0, -10)
        submit.move(0, -10)
        time.sleep(0.001)

    add_let_dis = 'y'

    while True:
        sub_item = win.getMouse()
        if 525 <= sub_item.getX() <= 605 and 530 <= sub_item.getY() <= 570:
            add_let_dis = 'n'

            submit_bg.undraw()
            submit.undraw()

            # submit invert
            submit_bg = Rectangle(Point(525, 530), Point(605, 570))
            submit_bg.setFill('ivory')
            submit_bg.setOutline(color_rgb(102, 206, 110))
            submit_bg.setWidth(2)
            submit_bg.draw(win)

            submit = Text(Point(565, 550), "SUBMIT")
            submit.setTextColor(color_rgb(102, 206, 110))
            submit.setSize(13)
            submit.setFace("Product Sans Medium")
            submit.draw(win)

            time.sleep(0.1)
            submit_bg.undraw()
            submit.undraw()

            # submit
            submit_bg = Rectangle(Point(525, 530), Point(605, 570))
            submit_bg.setFill(color_rgb(102, 206, 110))
            submit_bg.setOutline(None)
            submit_bg.setWidth(0)
            submit_bg.draw(win)

            submit = Text(Point(565, 550), "SUBMIT")
            submit.setTextColor("ivory")
            submit.setSize(13)
            submit.setFace("Product Sans Medium")
            submit.draw(win)

            try:
                insert_pr = pr_invo.getText().strip()
                insert_des = des_invo.getText().strip()
                insert_qt = int(qt_invo.getText())
            except:
                insert_pr = ''
                insert_des = ''
                insert_qt = 0

            cursor.execute("select * from products order by product")
            prd_data = cursor.fetchall()

            unit_price = 0

            for i in prd_data:
                if i[0].upper() == insert_pr.upper():
                    if i[2].upper() == insert_des.upper():
                        unit_price = i[1]
                        break

            if unit_price == 0:
                pass

            else:
                unit_pr = Text(Point(710, height), unit_price)
                unit_pr.setSize(12)
                unit_pr.setFace("Product Sans Medium")
                unit_pr.setTextColor(color_rgb(70, 70, 70))
                unit_pr.draw(win)

                total_s = Text(Point(825, height), insert_qt * unit_price)
                total_s.setSize(12)
                total_s.setFace("Product Sans Medium")
                total_s.setTextColor(color_rgb(70, 70, 70))
                total_s.draw(win)

            # getting total from total box
            try:
                total = float(insert_qt * unit_price)
            except:
                total = 0

            # inserting total and others in respective tables
            try:
                if insert_qt == 0 or unit_price == 0 or insert_pr == '':
                    pass
                else:
                    cursor.execute(
                        "insert into {} values('{}','{}',{},{},{})".format(tab_edi_name, insert_pr, insert_des,
                                                                           insert_qt, unit_price, total))
                    cursor.execute("update companies set net_total = net_total + {} where company = '{}'".format(total,
                                                                                                                 tab_edi_name.lower()))
            except:
                pass

            mycon.commit()

            # removing entry boxes
            pr_invo.undraw()
            des_invo.undraw()
            qt_invo.undraw()

            try:
                p_r = Text(Point(335, height), insert_pr)
                p_r.setSize(12)
                p_r.setFace("Product Sans Medium")
                p_r.setTextColor(color_rgb(70, 70, 70))
                p_r.draw(win)

                de_s = Text(Point(502, height), insert_des)
                de_s.setSize(12)
                de_s.setFace("Product Sans Medium")
                de_s.setTextColor(color_rgb(70, 70, 70))
                de_s.draw(win)

                q_t = Text(Point(635, height), insert_qt)
                q_t.setSize(12)
                q_t.setFace("Product Sans Medium")
                q_t.setTextColor(color_rgb(70, 70, 70))
                q_t.draw(win)
            except:
                pass

            time.sleep(0.5)
            break

    # taking back add item headers
    for vevo in range(30):
        rect_mov.move(0, 10)
        prod_title.move(0, 10)
        des_title.move(0, 10)
        qty.move(0, 10)
        u_price.move(0, 10)
        tot_price.move(0, 10)
        p_r.move(0, 10)
        de_s.move(0, 10)
        q_t.move(0, 10)

        if unit_price == 0:
            pass
        else:
            unit_pr.move(0, 10)
            total_s.move(0, 10)
        submit_bg.move(0, 10)
        submit.move(0, 10)
        time.sleep(0.001)

    # clearing screen to display new contents
    cls = Rectangle(Point(231, 110), Point(900, 399))
    cls.setFill('white')
    cls.setWidth(0)
    cls.draw(win)

    cursor.execute("select * from {}".format(tab_edi_name))
    product_ss = cursor.fetchall()
    # product head
    t1 = Text(Point(320, 70 + 50), "Product")
    t1.setFace("Gill Sans MT Condensed")
    t1.setSize(13 + 3)
    t1.setStyle('bold')
    t1.setTextColor(color_rgb(70, 70, 70))
    t1.draw(win)

    # description head
    t2 = Text(Point(480, 70 + 50), "Description")
    t2.setFace("Gill Sans MT Condensed")
    t2.setSize(13 + 3)
    t2.setStyle('bold')
    t2.setTextColor(color_rgb(70, 70, 70))
    t2.draw(win)

    # quantity head
    t3 = Text(Point(640, 70 + 50), "Qty.")
    t3.setFace("Gill Sans MT Condensed")
    t3.setSize(13 + 3)
    t3.setStyle('bold')
    t3.setTextColor(color_rgb(70, 70, 70))
    t3.draw(win)

    # unit price head
    t4 = Text(Point(720, 70 + 50), "Unit Price")
    t4.setFace("Gill Sans MT Condensed")
    t4.setSize(13 + 3)
    t4.setStyle('bold')
    t4.setTextColor(color_rgb(70, 70, 70))
    t4.draw(win)

    # total head
    t5 = Text(Point(831, 70 + 50), "Total")
    t5.setFace('Gill Sans MT Condensed')
    t5.setSize(13 + 3)
    t5.setStyle('bold')
    t5.setTextColor(color_rgb(70, 70, 70))
    t5.draw(win)

    incr = 0
    for com in product_ss:
        com = list(com)

        com[0] = com[0].title()
        pro_s = Text(Point(320, 95 + 50 + incr), com[0])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        com[1] = com[1].title()
        pro_s = Text(Point(480, 95 + 50 + incr), com[1])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(640, 95 + 50 + incr), com[2])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(720, 95 + 50 + incr), com[3])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(831, 95 + 50 + incr), com[4])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        incr += 20

    # total at the end of page
    line1 = Line(Point(700, 360), Point(855, 360))
    line1.setWidth(1)
    line1.setFill("light gray")
    line1.draw(win)

    line2 = Line(Point(700, 390), Point(855, 390))
    line2.setWidth(1)
    line2.setFill("light gray")
    line2.draw(win)

    tot_txt = Text(Point(735, 375), "Total ")
    tot_txt.setSize(12)
    tot_txt.setTextColor(color_rgb(50, 50, 50))
    tot_txt.setFace("Product Sans Medium")
    tot_txt.draw(win)

    new_net_total += total

    net_amt = Text(Point(825, 375), new_net_total)
    net_amt.setSize(12)
    net_amt.setTextColor(color_rgb(50, 50, 50))
    net_amt.setFace("Product Sans Medium")
    net_amt.draw(win)


# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
def delete_invo_item():
    global new_net_total

    # page moving in
    rect_mov = Rectangle(Point(231, 601 + 300), Point(900, 401 + 300))
    rect_mov.setWidth(0)
    rect_mov.setFill('white')
    rect_mov.draw(win)

    prod_title = Text(Point(465, 440 + 300), "Product")
    prod_title.setTextColor(color_rgb(90, 90, 90))
    prod_title.setSize(15 + 3)
    prod_title.setFace("Gill Sans MT Condensed")
    prod_title.draw(win)

    des_title = Text(Point(665, 440 + 300), "Description")
    des_title.setTextColor(color_rgb(90, 90, 90))
    des_title.setSize(15 + 3)
    des_title.setFace("Gill Sans MT Condensed")
    des_title.draw(win)

    height = 475

    pr_invo = Entry(Point(465, height + 300), 14)
    pr_invo.setSize(12)
    pr_invo.setFill("white")
    pr_invo.setFace("Product Sans Medium")
    pr_invo.setTextColor(color_rgb(70, 70, 70))
    pr_invo.draw(win)

    des_invo = Entry(Point(665, height + 300), 16)
    des_invo.setSize(12)
    des_invo.setFill("white")
    des_invo.setFace("Product Sans Medium")
    des_invo.setTextColor(color_rgb(70, 70, 70))
    des_invo.draw(win)

    # delete button defined
    del_bg = Rectangle(Point(525, 300 + 530), Point(605, 300 + 570))
    del_bg.setFill(color_rgb(102, 206, 110))
    del_bg.setOutline(None)
    del_bg.setWidth(0)
    del_bg.draw(win)

    del_txt = Text(Point(565, 300 + 550), "DELETE")
    del_txt.setTextColor("ivory")
    del_txt.setSize(13)
    del_txt.setFace("Product Sans Medium")
    del_txt.draw(win)

    for vevo in range(30):
        rect_mov.move(0, -10)
        prod_title.move(0, -10)
        des_title.move(0, -10)
        pr_invo.move(0, -10)
        des_invo.move(0, -10)
        del_bg.move(0, -10)
        del_txt.move(0, -10)
        time.sleep(0.001)

    while True:
        delete_item = win.getMouse()
        if 525 <= delete_item.getX() <= 605 and 530 <= delete_item.getY() <= 570:
            del_bg.undraw()
            del_txt.undraw()

            # delete button invert
            del_bg = Rectangle(Point(525, 530), Point(605, 570))
            del_bg.setFill('ivory')
            del_bg.setOutline(color_rgb(102, 206, 110))
            del_bg.setWidth(2)
            del_bg.draw(win)

            del_txt = Text(Point(565, 550), "DELETE")
            del_txt.setTextColor(color_rgb(102, 206, 110))
            del_txt.setSize(13)
            del_txt.setFace("Product Sans Medium")
            del_txt.draw(win)

            time.sleep(0.1)
            del_bg.undraw()
            del_txt.undraw()

            # delete button invert
            del_bg = Rectangle(Point(525, 530), Point(605, 570))
            del_bg.setFill(color_rgb(102, 206, 110))
            del_bg.setOutline(None)
            del_bg.setWidth(0)
            del_bg.draw(win)

            del_txt = Text(Point(565, 550), "DELETE")
            del_txt.setTextColor("ivory")
            del_txt.setSize(13)
            del_txt.setFace("Product Sans Medium")
            del_txt.draw(win)

            try:
                del_name = pr_invo.getText().strip()
                del_desc = des_invo.getText().strip()

                temp_del_name = ''
                for del_lett in del_name:
                    if del_lett == ' ':
                        temp_del_name += ' '
                    else:
                        temp_del_name += del_lett

                del_name = temp_del_name

                temp_del_desc = ''
                for del_lett in del_desc:
                    if del_lett == ' ':
                        temp_del_desc += ' '
                    else:
                        temp_del_desc += del_lett

                del_desc = temp_del_desc

            except:
                del_name = ''
                del_desc = ''

            cursor.execute("select * from {}".format(tab_edi_name))
            pr_data = cursor.fetchall()

            del_total = 0

            for demi in pr_data:
                demi = list(demi)
                if del_name.lower() == demi[0].lower() and del_desc.lower() == demi[1].lower():
                    del_total += demi[4]

            try:
                cursor.execute(
                    "delete from {} where product = '{}' and description = '{}'".format(tab_edi_name, del_name,
                                                                                        del_desc))
                cursor.execute("update companies set net_total = net_total - {} where company = '{}'".format(del_total,
                                                                                                             tab_edi_name.lower()))
            except:
                pass

            mycon.commit()

            # removing entry boxes
            pr_invo.undraw()
            des_invo.undraw()

            try:
                p_r = Text(Point(465, height), del_name)
                p_r.setSize(12)
                p_r.setFace("Product Sans Medium")
                p_r.setTextColor(color_rgb(70, 70, 70))
                p_r.draw(win)

                de_s = Text(Point(662, height), del_desc)
                de_s.setSize(12)
                de_s.setFace("Product Sans Medium")
                de_s.setTextColor(color_rgb(70, 70, 70))
                de_s.draw(win)
            except:
                pass

            time.sleep(0.5)
            break

    # taking back add item headers
    for vevo in range(30):
        rect_mov.move(0, 10)
        prod_title.move(0, 10)
        des_title.move(0, 10)
        p_r.move(0, 10)
        de_s.move(0, 10)
        del_bg.move(0, 10)
        del_txt.move(0, 10)
        time.sleep(0.001)

    # clearing screen to display new contents
    cls = Rectangle(Point(231, 110), Point(900, 399))
    cls.setFill('white')
    cls.setWidth(0)
    cls.draw(win)

    cursor.execute("select * from {}".format(tab_edi_name))
    product_ss = cursor.fetchall()
    # product head
    t1 = Text(Point(320, 70 + 50), "Product")
    t1.setFace("Gill Sans MT Condensed")
    t1.setSize(13 + 3)
    t1.setStyle('bold')
    t1.setTextColor(color_rgb(70, 70, 70))
    t1.draw(win)

    # description head
    t2 = Text(Point(480, 70 + 50), "Description")
    t2.setFace("Gill Sans MT Condensed")
    t2.setSize(13 + 3)
    t2.setStyle('bold')
    t2.setTextColor(color_rgb(70, 70, 70))
    t2.draw(win)

    # quantity head
    t3 = Text(Point(640, 70 + 50), "Qty.")
    t3.setFace("Gill Sans MT Condensed")
    t3.setSize(13 + 3)
    t3.setStyle('bold')
    t3.setTextColor(color_rgb(70, 70, 70))
    t3.draw(win)

    # unit price head
    t4 = Text(Point(720, 70 + 50), "Unit Price")
    t4.setFace("Gill Sans MT Condensed")
    t4.setSize(13 + 3)
    t4.setStyle('bold')
    t4.setTextColor(color_rgb(70, 70, 70))
    t4.draw(win)

    # total head
    t5 = Text(Point(831, 70 + 50), "Total")
    t5.setFace('Gill Sans MT Condensed')
    t5.setSize(13 + 3)
    t5.setStyle('bold')
    t5.setTextColor(color_rgb(70, 70, 70))
    t5.draw(win)

    incr = 0
    for com in product_ss:
        com = list(com)

        com[0] = com[0].title()
        pro_s = Text(Point(320, 95 + 50 + incr), com[0])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        com[1] = com[1].title()
        pro_s = Text(Point(480, 95 + 50 + incr), com[1])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(640, 95 + 50 + incr), com[2])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(720, 95 + 50 + incr), com[3])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        pro_s = Text(Point(831, 95 + 50 + incr), com[4])
        pro_s.setSize(12)
        pro_s.setTextColor(color_rgb(47, 47, 47))
        pro_s.setFace('Product Sans Light')
        pro_s.draw(win)

        incr += 20

    # total at the end of page
    line1 = Line(Point(700, 360), Point(855, 360))
    line1.setWidth(1)
    line1.setFill("light gray")
    line1.draw(win)

    line2 = Line(Point(700, 390), Point(855, 390))
    line2.setWidth(1)
    line2.setFill("light gray")
    line2.draw(win)

    tot_txt = Text(Point(735, 375), "Total ")
    tot_txt.setSize(12)
    tot_txt.setTextColor(color_rgb(50, 50, 50))
    tot_txt.setFace("Product Sans Medium")
    tot_txt.draw(win)

    new_net_total -= del_total

    net_amt = Text(Point(825, 375), new_net_total)
    net_amt.setSize(12)
    net_amt.setTextColor(color_rgb(50, 50, 50))
    net_amt.setFace("Product Sans Medium")
    net_amt.draw(win)


# ------------------------------------------------

def edit_sales_sum():
    # page clear before invoice
    page_clear = Rectangle(Point(231, 0), Point(900, 600))
    page_clear.setWidth(0)
    page_clear.setFill("white")
    page_clear.draw(win)

    # div line
    div_line = Line(Point(230, 40), Point(900, 40))
    div_line.setFill("light gray")
    div_line.setWidth(1)
    div_line.draw(win)

    # create invoice text
    header = Text(Point(325, -20), "Edit Sales Summary")
    header.setSize(16 + 3)
    header.setStyle("bold")
    header.setTextColor("Gray")
    header.setFace("Gill Sans MT Condensed")
    header.draw(win)

    for var in range(20):
        header.move(0, 2)
        time.sleep(0.001)

    # title heads for company and sales
    title_1 = Text(Point(350 - 70, 80), "Company")
    title_1.setFace("Product Sans Medium")
    title_1.setTextColor(color_rgb(70, 70, 70))
    title_1.setSize(14)
    title_1.setStyle('underline')
    title_1.draw(win)

    title_2 = Text(Point(750 - 130, 80), "Sales")
    title_2.setFace("Product Sans Medium")
    title_2.setTextColor(color_rgb(70, 70, 70))
    title_2.setSize(14)
    title_2.setStyle('underline')
    title_2.draw(win)

    # displaying sales summary
    cursor.execute("select * from companies order by invoice")
    company_names = cursor.fetchall()

    a = 15

    for i in company_names:
        i = list(i)

        new_i = ''
        let = 0
        while let < len(i[0]):
            while let < len(i[0]) and i[0][let] == '_':
                new_i += ' '
                let += 1

            while let < len(i[0]) and i[0][let] != '_':
                new_i += i[0][let]
                let += 1

        new_i = new_i.lower()
        new_i += ' ' * (25 - len(new_i))

        company = Text(Point(460 - 70, 95 + a), new_i)
        company.setFace("Major Mono Display")
        company.setTextColor(color_rgb(47, 47, 47))
        company.setSize(12)
        company.draw(win)

        value = str(i[1])
        value = '  ' * (10 - len(value)) + value

        amt = Text(Point(730 - 130, 95 + a), value)
        amt.setFace("Product Sans Light")
        amt.setTextColor(color_rgb(47, 47, 47))
        amt.setSize(12)
        amt.draw(win)

        hr = Line(Point(310 - 70, 95 + a + 9), Point(773 - 130, 95 + a + 9))
        hr.setFill("gray")
        hr.setWidth(1)
        hr.draw(win)

        a += 20
        time.sleep(0.01)

    # vertical rule
    lineV = Line(Point(660, 40), Point(660, 600))
    lineV.setFill("light gray")
    lineV.setWidth(1)
    lineV.draw(win)

    # edit entry
    edit_entry = Text(Point(780 + 200, 250), "Edit Name")
    edit_entry.setSize(15)
    edit_entry.setFace('Product Sans Light')
    edit_entry.setTextColor(color_rgb(80, 80, 80))
    edit_entry.draw(win)

    # delete entry
    del_entry = Text(Point(780 + 200, 350), "Delete Entry")
    del_entry.setSize(15)
    del_entry.setFace('Product Sans Light')
    del_entry.setTextColor(color_rgb(80, 80, 80))
    del_entry.draw(win)

    # exit
    exit_pr = Text(Point(780 + 200, 550), "Go Back")
    exit_pr.setSize(13)
    exit_pr.setFace('Product Sans Light')
    exit_pr.setTextColor(color_rgb(80, 80, 80))
    # exit_pr.setStyle('bold italic')
    exit_pr.draw(win)

    for ent in range(20):
        edit_entry.move(-10, 0)
        del_entry.move(-10, 0)
        exit_pr.move(-10, 0)
        time.sleep(0.001)

    rect_entry = Rectangle(Point(740, 565), Point(820, 535))
    rect_entry.setWidth(0)
    rect_entry.draw(win)

    while True:
        click_sett = win.getMouse()

        if 732 <= click_sett.getX() <= 828 and 230 <= click_sett.getY() <= 270:
            bl1 = Rectangle(Point(732, 230), Point(728, 270))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(828, 230), Point(832, 270))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)
            editing_entry()

        elif 720 <= click_sett.getX() <= 840 and 330 <= click_sett.getY() <= 370:
            bl1 = Rectangle(Point(720, 330), Point(716, 370))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(840, 330), Point(844, 370))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)
            deleting_entry()

        elif 740 <= click_sett.getX() <= 820 and 535 <= click_sett.getY() <= 565:
            for ani in range(2):
                rect_entry.setWidth(1)
                rect_entry.setOutline("gray")
                time.sleep(0.1)

                rect_entry.setWidth(0)
                rect_entry.setOutline(None)
                time.sleep(0.1)

            rect_entry.undraw()

            rect_entry = Rectangle(Point(231, -1), Point(900, -600))
            rect_entry.setWidth(0)
            rect_entry.setFill('white')
            rect_entry.draw(win)

            for l in range(60):
                rect_entry.move(0, 10)
                time.sleep(0.001)

            settings_page()
            break


# ------------------------------------------------
def editing_entry():
    # column clear
    column = Rectangle(Point(661 + 300, 41), Point(900 + 300, 600))
    column.setWidth(0)
    column.setFill('white')
    column.draw(win)

    # entry add tiles
    entry_name = Text(Point(780 + 300, 200), "Existing Name")
    entry_name.setSize(13)
    entry_name.setTextColor(color_rgb(70, 70, 70))
    entry_name.setFace("Product Sans Medium")
    entry_name.draw(win)

    entry_name_box = Entry(Point(780 + 300, 230), 17)
    entry_name_box.setFace("Product Sans Light")
    entry_name_box.setTextColor(color_rgb(50, 50, 50))
    entry_name_box.setSize(11)
    entry_name_box.setFill('ivory')
    entry_name_box.draw(win)

    entry_new = Text(Point(780 + 300, 330), "New Name")
    entry_new.setSize(13)
    entry_new.setTextColor(color_rgb(70, 70, 70))
    entry_new.setFace("Product Sans Medium")
    entry_new.draw(win)

    entry_new_box = Entry(Point(780 + 300, 360), 17)
    entry_new_box.setFace("Product Sans Light")
    entry_new_box.setTextColor(color_rgb(50, 50, 50))
    entry_new_box.setSize(11)
    entry_new_box.setFill('ivory')
    entry_new_box.draw(win)

    # change data
    change_entry_bg = Rectangle(Point(740 + 300, 480), Point(820 + 300, 520))
    change_entry_bg.setFill(color_rgb(102, 206, 110))
    change_entry_bg.setOutline(None)
    change_entry_bg.setWidth(0)
    change_entry_bg.draw(win)

    change_entry = Text(Point(780 + 300, 500), "UPDATE")
    change_entry.setTextColor("ivory")
    change_entry.setSize(13)
    change_entry.setFace("Product Sans Medium")
    change_entry.draw(win)

    for cl in range(30):
        column.move(-10, 0)
        entry_name.move(-10, 0)
        entry_name_box.move(-10, 0)
        entry_new.move(-10, 0)
        entry_new_box.move(-10, 0)
        change_entry_bg.move(-10, 0)
        change_entry.move(-10, 0)
        time.sleep(0.001)

    while True:
        entry_click = win.getMouse()

        if 740 <= entry_click.getX() <= 820 and 480 <= entry_click.getY() <= 520:
            change_entry_bg.undraw()
            change_entry.undraw()

            # change_entry button invert
            change_entry_bg = Rectangle(Point(740, 480), Point(820, 520))
            change_entry_bg.setFill('ivory')
            change_entry_bg.setOutline(color_rgb(102, 206, 110))
            change_entry_bg.setWidth(2)
            change_entry_bg.draw(win)

            change_entry = Text(Point(780, 500), "UPDATE")
            change_entry.setTextColor(color_rgb(102, 206, 110))
            change_entry.setSize(13)
            change_entry.setFace("Product Sans Medium")
            change_entry.draw(win)

            time.sleep(0.1)
            change_entry_bg.undraw()
            change_entry.undraw()

            # change_entry revert
            change_entry_bg = Rectangle(Point(740, 480), Point(820, 520))
            change_entry_bg.setFill(color_rgb(102, 206, 110))
            change_entry_bg.setOutline(None)
            change_entry_bg.setWidth(0)
            change_entry_bg.draw(win)

            change_entry = Text(Point(780, 500), "UPDATE")
            change_entry.setTextColor("ivory")
            change_entry.setSize(13)
            change_entry.setFace("Product Sans Medium")
            change_entry.draw(win)

            exi_name = entry_name_box.getText().strip()

            chkr = 0
            tab_exi_name = ''

            while chkr < len(exi_name):
                while chkr < len(exi_name) and exi_name[chkr] == ' ':
                    tab_exi_name += '_'
                    chkr += 1
                while chkr < len(exi_name) and exi_name[chkr] != ' ':
                    tab_exi_name += exi_name[chkr]
                    chkr += 1

            new_name = entry_new_box.getText().strip()

            chkr = 0
            tab_new_name = ''

            while chkr < len(new_name):
                while chkr < len(new_name) and new_name[chkr] == ' ':
                    tab_new_name += '_'
                    chkr += 1
                while chkr < len(new_name) and new_name[chkr] != ' ':
                    tab_new_name += new_name[chkr]
                    chkr += 1

            try:
                cursor.execute(
                    "update companies set company = '{}' where company = '{}'".format(tab_new_name, tab_exi_name))
                cursor.execute("ALTER TABLE {} RENAME TO {}".format(tab_exi_name, tab_new_name))
                mycon.commit()

            except:
                pass

            time.sleep(0.5)

            break

    for cl in range(30):
        column.move(10, 0)
        entry_name.move(10, 0)
        entry_name_box.move(10, 0)
        entry_new.move(10, 0)
        entry_new_box.move(10, 0)
        change_entry_bg.move(10, 0)
        change_entry.move(10, 0)
        time.sleep(0.001)

    # hiding previous data from products table
    rect_ = Rectangle(Point(231, 98), Point(659, 600))
    rect_.setFill('white')
    rect_.setWidth(0)
    rect_.draw(win)

    # displaying sales summary
    cursor.execute("select * from companies order by invoice")
    company_names = cursor.fetchall()

    a = 15

    for i in company_names:
        i = list(i)

        new_i = ''
        let = 0
        while let < len(i[0]):
            while let < len(i[0]) and i[0][let] == '_':
                new_i += ' '
                let += 1

            while let < len(i[0]) and i[0][let] != '_':
                new_i += i[0][let]
                let += 1

        new_i = new_i.lower()
        new_i += ' ' * (25 - len(new_i))

        company = Text(Point(460 - 70, 95 + a), new_i)
        company.setFace("Major Mono Display")
        company.setTextColor(color_rgb(47, 47, 47))
        company.setSize(12)
        company.draw(win)

        value = str(i[1])
        value = '  ' * (10 - len(value)) + value

        amt = Text(Point(730 - 130, 95 + a), value)
        amt.setFace("Product Sans Light")
        amt.setTextColor(color_rgb(47, 47, 47))
        amt.setSize(12)
        amt.draw(win)

        hr = Line(Point(310 - 70, 95 + a + 9), Point(773 - 130, 95 + a + 9))
        hr.setFill("gray")
        hr.setWidth(1)
        hr.draw(win)

        a += 20


# ------------------------------------------------
def deleting_entry():
    # column clear
    column = Rectangle(Point(661 + 300, 41), Point(900 + 300, 600))
    column.setWidth(0)
    column.setFill('white')
    column.draw(win)

    # entry del tiles
    del_entry_name = Text(Point(780 + 300, 200), "Company Name")
    del_entry_name.setSize(13)
    del_entry_name.setTextColor(color_rgb(70, 70, 70))
    del_entry_name.setFace("Product Sans Medium")
    del_entry_name.draw(win)

    del_entry_name_box = Entry(Point(780 + 300, 230), 17)
    del_entry_name_box.setFace("Product Sans Light")
    del_entry_name_box.setTextColor(color_rgb(50, 50, 50))
    del_entry_name_box.setSize(11)
    del_entry_name_box.setFill('ivory')
    del_entry_name_box.draw(win)

    # del data
    del_entry_bg = Rectangle(Point(740 + 300, 480), Point(820 + 300, 520))
    del_entry_bg.setFill(color_rgb(102, 206, 110))
    del_entry_bg.setOutline(None)
    del_entry_bg.setWidth(0)
    del_entry_bg.draw(win)

    del_entry = Text(Point(780 + 300, 500), "DELETE")
    del_entry.setTextColor("ivory")
    del_entry.setSize(13)
    del_entry.setFace("Product Sans Medium")
    del_entry.draw(win)

    for cl in range(30):
        column.move(-10, 0)
        del_entry_name.move(-10, 0)
        del_entry_name_box.move(-10, 0)
        del_entry_bg.move(-10, 0)
        del_entry.move(-10, 0)
        time.sleep(0.001)

    while True:
        del_entry_click = win.getMouse()

        if 740 <= del_entry_click.getX() <= 820 and 480 <= del_entry_click.getY() <= 520:
            del_entry_bg.undraw()
            del_entry.undraw()

            # del button invert
            del_entry_bg = Rectangle(Point(740, 480), Point(820, 520))
            del_entry_bg.setFill('ivory')
            del_entry_bg.setOutline(color_rgb(102, 206, 110))
            del_entry_bg.setWidth(2)
            del_entry_bg.draw(win)

            del_entry = Text(Point(780, 500), "DELETE")
            del_entry.setTextColor(color_rgb(102, 206, 110))
            del_entry.setSize(13)
            del_entry.setFace("Product Sans Medium")
            del_entry.draw(win)

            time.sleep(0.1)
            del_entry_bg.undraw()
            del_entry.undraw()

            # del data button revert
            del_entry_bg = Rectangle(Point(740, 480), Point(820, 520))
            del_entry_bg.setFill(color_rgb(102, 206, 110))
            del_entry_bg.setOutline(None)
            del_entry_bg.setWidth(0)
            del_entry_bg.draw(win)

            del_entry = Text(Point(780, 500), "DELETE")
            del_entry.setTextColor("ivory")
            del_entry.setSize(13)
            del_entry.setFace("Product Sans Medium")
            del_entry.draw(win)

            to_del_name = del_entry_name_box.getText().strip()

            chkr = 0
            tab_del_name = ''

            while chkr < len(to_del_name):
                while chkr < len(to_del_name) and to_del_name[chkr] == ' ':
                    tab_del_name += '_'
                    chkr += 1
                while chkr < len(to_del_name) and to_del_name[chkr] != ' ':
                    tab_del_name += to_del_name[chkr]
                    chkr += 1

            to_del_name = tab_del_name

            try:
                cursor.execute("delete from companies where company = '{}'".format(to_del_name))
                cursor.execute("drop table {}".format(to_del_name))
                mycon.commit()

            except:
                pass

            time.sleep(0.5)

            break

    for cl in range(30):
        column.move(10, 0)
        del_entry_name.move(10, 0)
        del_entry_name_box.move(10, 0)
        del_entry_bg.move(10, 0)
        del_entry.move(10, 0)
        time.sleep(0.001)

    # hiding previous data from products table
    rect_ = Rectangle(Point(231, 98), Point(659, 600))
    rect_.setFill('white')
    rect_.setWidth(0)
    rect_.draw(win)

    # displaying sales summary
    cursor.execute("select * from companies order by invoice")
    company_names = cursor.fetchall()

    a = 15

    for i in company_names:
        i = list(i)

        new_i = ''
        let = 0
        while let < len(i[0]):
            while let < len(i[0]) and i[0][let] == '_':
                new_i += ' '
                let += 1

            while let < len(i[0]) and i[0][let] != '_':
                new_i += i[0][let]
                let += 1

        new_i = new_i.lower()
        new_i += ' ' * (25 - len(new_i))

        company = Text(Point(460 - 70, 95 + a), new_i)
        company.setFace("Major Mono Display")
        company.setTextColor(color_rgb(47, 47, 47))
        company.setSize(12)
        company.draw(win)

        value = str(i[1])
        value = '  ' * (10 - len(value)) + value

        amt = Text(Point(730 - 130, 95 + a), value)
        amt.setFace("Product Sans Light")
        amt.setTextColor(color_rgb(47, 47, 47))
        amt.setSize(12)
        amt.draw(win)

        hr = Line(Point(310 - 70, 95 + a + 9), Point(773 - 130, 95 + a + 9))
        hr.setFill("gray")
        hr.setWidth(1)
        hr.draw(win)

        a += 20


# ------------------------------------------------
def edit_products():
    # page clear before invoice
    page_clear = Rectangle(Point(231, 0), Point(900, 600))
    page_clear.setWidth(0)
    page_clear.setFill("white")
    page_clear.draw(win)

    # div line
    div_line = Line(Point(230, 40), Point(900, 40))
    div_line.setFill("light gray")
    div_line.setWidth(1)
    div_line.draw(win)

    # create invoice text
    header = Text(Point(308, -20), "Edit Products")
    header.setSize(16 + 3)
    header.setStyle("bold")
    header.setTextColor("Gray")
    header.setFace("Gill Sans MT Condensed")
    header.draw(win)

    for var in range(20):
        header.move(0, 2)
        time.sleep(0.001)

    # title of data to be extracted
    title1 = Text(Point(300, 70), "Product Name")
    title1.setFace("Product Sans Medium")
    title1.setTextColor(color_rgb(70, 70, 70))
    title1.setSize(14)
    title1.setStyle('underline')
    title1.draw(win)

    title2 = Text(Point(440, 70), "Unit Price")
    title2.setFace("Product Sans Medium")
    title2.setTextColor(color_rgb(70, 70, 70))
    title2.setSize(14)
    title2.setStyle('underline')
    title2.draw(win)

    title3 = Text(Point(580, 70), "Description")
    title3.setFace("Product Sans Medium")
    title3.setTextColor(color_rgb(70, 70, 70))
    title3.setSize(14)
    title3.setStyle('underline')
    title3.draw(win)

    # taking data from products table
    cursor.execute("select * from products order by product")
    product_data = cursor.fetchall()

    b = 15
    for k in product_data:
        k = list(k)

        pr_name = Text(Point(300, 90 + b), k[0].capitalize())
        pr_name.setSize(13)
        pr_name.setTextColor(color_rgb(60, 60, 60))
        pr_name.setFace("Product Sans Light")
        pr_name.draw(win)

        pr_price = Text(Point(440, 90 + b), k[1])
        pr_price.setSize(13)
        pr_price.setTextColor(color_rgb(60, 60, 60))
        pr_price.setFace("Product Sans Light")
        pr_price.draw(win)

        pr_desc = Text(Point(580, 90 + b), k[2])
        pr_desc.setSize(13)
        pr_desc.setTextColor(color_rgb(60, 60, 60))
        pr_desc.setFace("Product Sans Light")
        pr_desc.draw(win)

        b += 20
        time.sleep(0.01)

    # vertical rule
    lineV = Line(Point(660, 40), Point(660, 600))
    lineV.setFill("light gray")
    lineV.setWidth(1)
    lineV.draw(win)

    # entry of commands
    ad_pr = Text(Point(780 + 200, 200), "Add Product ")
    ad_pr.setSize(15)
    ad_pr.setFace('Product Sans Light')
    ad_pr.setTextColor(color_rgb(80, 80, 80))
    ad_pr.draw(win)

    del_pr = Text(Point(780 + 200, 300), "Delete Product ")
    del_pr.setSize(15)
    del_pr.setFace('Product Sans Light')
    del_pr.setTextColor(color_rgb(80, 80, 80))
    del_pr.draw(win)

    edit_pr = Text(Point(780 + 200, 400), "Edit Product ")
    edit_pr.setSize(15)
    edit_pr.setFace('Product Sans Light')
    edit_pr.setTextColor(color_rgb(80, 80, 80))
    edit_pr.draw(win)

    exit_pr = Text(Point(780 + 200, 550), "Go Back")
    exit_pr.setSize(13)
    exit_pr.setFace('Product Sans Light')
    exit_pr.setTextColor(color_rgb(80, 80, 80))
    # exit_pr.setStyle('bold italic')
    exit_pr.draw(win)

    # loop to bring entry commands on screen
    for e in range(20):
        ad_pr.move(-10, 0)
        del_pr.move(-10, 0)
        edit_pr.move(-10, 0)
        exit_pr.move(-10, 0)
        time.sleep(0.001)

    rect_try = Rectangle(Point(740, 565), Point(820, 535))
    rect_try.setWidth(0)
    rect_try.draw(win)

    while True:
        click_sett = win.getMouse()

        if 720 <= click_sett.getX() <= 840 and 180 <= click_sett.getY() <= 220:
            bl1 = Rectangle(Point(720, 180), Point(716, 220))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(840, 180), Point(844, 220))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)
            add_product()

        elif 700 <= click_sett.getX() <= 860 and 280 <= click_sett.getY() <= 320:
            bl1 = Rectangle(Point(708, 280), Point(704, 320))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(848, 280), Point(852, 320))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)
            delete_product()

        elif 720 <= click_sett.getX() <= 840 and 380 <= click_sett.getY() <= 420:
            bl1 = Rectangle(Point(720, 380), Point(716, 420))
            bl1.setWidth(0)
            bl1.setFill('turquoise')
            bl1.draw(win)

            bl2 = Rectangle(Point(840, 380), Point(844, 420))
            bl2.setWidth(0)
            bl2.setFill('turquoise')
            bl2.draw(win)

            time.sleep(0.2)
            bl1.undraw()
            bl2.undraw()

            time.sleep(0.2)
            manipulate_product()

        elif 740 <= click_sett.getX() <= 820 and 535 <= click_sett.getY() <= 565:
            for ani in range(2):
                rect_try.setWidth(1)
                rect_try.setOutline("gray")
                time.sleep(0.1)

                rect_try.setWidth(0)
                rect_try.setOutline(None)
                time.sleep(0.1)

            rect_try.undraw()

            rect_try = Rectangle(Point(231, -1), Point(900, -600))
            rect_try.setWidth(0)
            rect_try.setFill('white')
            rect_try.draw(win)

            for l in range(60):
                rect_try.move(0, 10)
                time.sleep(0.001)

            settings_page()
            break


# ------------------------------------------------
def add_product():
    # column clear
    column = Rectangle(Point(661 + 300, 41), Point(900 + 300, 600))
    column.setWidth(0)
    column.setFill('white')
    column.draw(win)

    # product add tiles
    pro_name = Text(Point(780 + 300, 150), "Product Name")
    pro_name.setSize(13)
    pro_name.setTextColor(color_rgb(70, 70, 70))
    pro_name.setFace("Product Sans Medium")
    pro_name.draw(win)

    pro_name_box = Entry(Point(780 + 300, 180), 17)
    pro_name_box.setFace("Product Sans Light")
    pro_name_box.setTextColor(color_rgb(50, 50, 50))
    pro_name_box.setSize(11)
    pro_name_box.setFill('ivory')
    pro_name_box.draw(win)

    pro_price = Text(Point(780 + 300, 250), "Unit Price")
    pro_price.setSize(13)
    pro_price.setTextColor(color_rgb(70, 70, 70))
    pro_price.setFace("Product Sans Medium")
    pro_price.draw(win)

    pro_price_box = Entry(Point(780 + 300, 280), 17)
    pro_price_box.setFace("Product Sans Light")
    pro_price_box.setTextColor(color_rgb(50, 50, 50))
    pro_price_box.setSize(11)
    pro_price_box.setFill('ivory')
    pro_price_box.draw(win)

    pro_desc = Text(Point(780 + 300, 350), "Description")
    pro_desc.setSize(13)
    pro_desc.setTextColor(color_rgb(70, 70, 70))
    pro_desc.setFace("Product Sans Medium")
    pro_desc.draw(win)

    pro_desc_box = Entry(Point(780 + 300, 380), 17)
    pro_desc_box.setFace("Product Sans Light")
    pro_desc_box.setTextColor(color_rgb(50, 50, 50))
    pro_desc_box.setSize(11)
    pro_desc_box.setFill('ivory')
    pro_desc_box.draw(win)

    # submit data
    submit_bg = Rectangle(Point(740 + 300, 480), Point(820 + 300, 520))
    submit_bg.setFill(color_rgb(102, 206, 110))
    submit_bg.setOutline(None)
    submit_bg.setWidth(0)
    submit_bg.draw(win)

    submit = Text(Point(780 + 300, 500), "SUBMIT")
    submit.setTextColor("ivory")
    submit.setSize(13)
    submit.setFace("Product Sans Medium")
    submit.draw(win)

    for cl in range(30):
        column.move(-10, 0)
        pro_name.move(-10, 0)
        pro_name_box.move(-10, 0)
        pro_price.move(-10, 0)
        pro_price_box.move(-10, 0)
        pro_desc.move(-10, 0)
        pro_desc_box.move(-10, 0)
        submit_bg.move(-10, 0)
        submit.move(-10, 0)
        time.sleep(0.001)

    while True:
        sub_click = win.getMouse()

        if 740 <= sub_click.getX() <= 820 and 480 <= sub_click.getY() <= 520:
            submit_bg.undraw()
            submit.undraw()

            # submit button invert
            submit_bg = Rectangle(Point(740, 480), Point(820, 520))
            submit_bg.setFill('ivory')
            submit_bg.setOutline(color_rgb(102, 206, 110))
            submit_bg.setWidth(2)
            submit_bg.draw(win)

            submit = Text(Point(780, 500), "SUBMIT")
            submit.setTextColor(color_rgb(102, 206, 110))
            submit.setSize(13)
            submit.setFace("Product Sans Medium")
            submit.draw(win)

            time.sleep(0.1)
            submit_bg.undraw()
            submit.undraw()

            # submit revert
            submit_bg = Rectangle(Point(740, 480), Point(820, 520))
            submit_bg.setFill(color_rgb(102, 206, 110))
            submit_bg.setOutline(None)
            submit_bg.setWidth(0)
            submit_bg.draw(win)

            submit = Text(Point(780, 500), "SUBMIT")
            submit.setTextColor("ivory")
            submit.setSize(13)
            submit.setFace("Product Sans Medium")
            submit.draw(win)

            name = pro_name_box.getText()
            price = pro_price_box.getText()
            desc = pro_desc_box.getText()

            name = name.strip()
            desc = desc.strip()

            try:
                cursor.execute("insert into products values('{}',{},'{}')".format(name, price, desc))
                mycon.commit()

            except:
                pass

            time.sleep(0.5)

            break

    for cl in range(30):
        column.move(10, 0)
        pro_name.move(10, 0)
        pro_name_box.move(10, 0)
        pro_price.move(10, 0)
        pro_price_box.move(10, 0)
        pro_desc.move(10, 0)
        pro_desc_box.move(10, 0)
        submit_bg.move(10, 0)
        submit.move(10, 0)
        time.sleep(0.001)

    # hiding previous data from products table
    rect_ = Rectangle(Point(231, 90), Point(659, 600))
    rect_.setFill('white')
    rect_.setWidth(0)
    rect_.draw(win)

    # taking data from products table    
    cursor.execute("select * from products order by product")
    product_data = cursor.fetchall()

    b = 15
    for k in product_data:
        k = list(k)

        pr_name = Text(Point(300, 90 + b), k[0].capitalize())
        pr_name.setSize(13)
        pr_name.setTextColor(color_rgb(60, 60, 60))
        pr_name.setFace("Product Sans Light")
        pr_name.draw(win)

        pr_price = Text(Point(440, 90 + b), k[1])
        pr_price.setSize(13)
        pr_price.setTextColor(color_rgb(60, 60, 60))
        pr_price.setFace("Product Sans Light")
        pr_price.draw(win)

        pr_desc = Text(Point(580, 90 + b), k[2])
        pr_desc.setSize(13)
        pr_desc.setTextColor(color_rgb(60, 60, 60))
        pr_desc.setFace("Product Sans Light")
        pr_desc.draw(win)

        b += 20


# ------------------------------------------------
def delete_product():
    # column clear
    column = Rectangle(Point(661 + 300, 41), Point(900 + 300, 600))
    column.setWidth(0)
    column.setFill('white')
    column.draw(win)

    # product del tiles
    pro_name = Text(Point(780 + 300, 200), "Product Name")
    pro_name.setSize(13)
    pro_name.setTextColor(color_rgb(70, 70, 70))
    pro_name.setFace("Product Sans Medium")
    pro_name.draw(win)

    pro_name_box = Entry(Point(780 + 300, 230), 17)
    pro_name_box.setFace("Product Sans Light")
    pro_name_box.setTextColor(color_rgb(50, 50, 50))
    pro_name_box.setSize(11)
    pro_name_box.setFill('ivory')
    pro_name_box.draw(win)

    pro_desc = Text(Point(780 + 300, 300), "Description")
    pro_desc.setSize(13)
    pro_desc.setTextColor(color_rgb(70, 70, 70))
    pro_desc.setFace("Product Sans Medium")
    pro_desc.draw(win)

    pro_desc_box = Entry(Point(780 + 300, 330), 17)
    pro_desc_box.setFace("Product Sans Light")
    pro_desc_box.setTextColor(color_rgb(50, 50, 50))
    pro_desc_box.setSize(11)
    pro_desc_box.setFill('ivory')
    pro_desc_box.draw(win)

    # delete data
    delete_bg = Rectangle(Point(740 + 300, 480), Point(820 + 300, 520))
    delete_bg.setFill(color_rgb(102, 206, 110))
    delete_bg.setOutline(None)
    delete_bg.setWidth(0)
    delete_bg.draw(win)

    delete = Text(Point(780 + 300, 500), "DELETE")
    delete.setTextColor("ivory")
    delete.setSize(13)
    delete.setFace("Product Sans Medium")
    delete.draw(win)

    for cl in range(30):
        column.move(-10, 0)
        pro_name.move(-10, 0)
        pro_name_box.move(-10, 0)
        pro_desc.move(-10, 0)
        pro_desc_box.move(-10, 0)
        delete_bg.move(-10, 0)
        delete.move(-10, 0)
        time.sleep(0.001)

    while True:
        sub_click = win.getMouse()

        if 740 <= sub_click.getX() <= 820 and 480 <= sub_click.getY() <= 520:
            delete_bg.undraw()
            delete.undraw()

            # delete button invert
            delete_bg = Rectangle(Point(740, 480), Point(820, 520))
            delete_bg.setFill('ivory')
            delete_bg.setOutline(color_rgb(102, 206, 110))
            delete_bg.setWidth(2)
            delete_bg.draw(win)

            delete = Text(Point(780, 500), "DELETE")
            delete.setTextColor(color_rgb(102, 206, 110))
            delete.setSize(13)
            delete.setFace("Product Sans Medium")
            delete.draw(win)

            time.sleep(0.1)
            delete_bg.undraw()
            delete.undraw()

            # delete revert
            delete_bg = Rectangle(Point(740, 480), Point(820, 520))
            delete_bg.setFill(color_rgb(102, 206, 110))
            delete_bg.setOutline(None)
            delete_bg.setWidth(0)
            delete_bg.draw(win)

            delete = Text(Point(780, 500), "DELETE")
            delete.setTextColor("ivory")
            delete.setSize(13)
            delete.setFace("Product Sans Medium")
            delete.draw(win)

            name = pro_name_box.getText()
            desc = pro_desc_box.getText()

            name = name.strip()
            desc = desc.strip()

            try:
                cursor.execute("delete from products where product = '{}' and description = '{}'".format(name, desc))
                mycon.commit()

            except:
                pass

            time.sleep(0.5)

            break

    for cl in range(30):
        column.move(10, 0)
        pro_name.move(10, 0)
        pro_name_box.move(10, 0)
        pro_desc.move(10, 0)
        pro_desc_box.move(10, 0)
        delete_bg.move(10, 0)
        delete.move(10, 0)
        time.sleep(0.001)

    # hiding previous data from products table
    rect_ = Rectangle(Point(231, 90), Point(659, 600))
    rect_.setFill('white')
    rect_.setWidth(0)
    rect_.draw(win)

    # taking data from products table    
    cursor.execute("select * from products order by product")
    product_data = cursor.fetchall()

    b = 15
    for k in product_data:
        k = list(k)

        pr_name = Text(Point(300, 90 + b), k[0].capitalize())
        pr_name.setSize(13)
        pr_name.setTextColor(color_rgb(60, 60, 60))
        pr_name.setFace("Product Sans Light")
        pr_name.draw(win)

        pr_price = Text(Point(440, 90 + b), k[1])
        pr_price.setSize(13)
        pr_price.setTextColor(color_rgb(60, 60, 60))
        pr_price.setFace("Product Sans Light")
        pr_price.draw(win)

        pr_desc = Text(Point(580, 90 + b), k[2])
        pr_desc.setSize(13)
        pr_desc.setTextColor(color_rgb(60, 60, 60))
        pr_desc.setFace("Product Sans Light")
        pr_desc.draw(win)

        b += 20


# ------------------------------------------------
def manipulate_product():
    # column clear
    column = Rectangle(Point(661 + 300, 41), Point(900 + 300, 600))
    column.setWidth(0)
    column.setFill('white')
    column.draw(win)

    # product add tiles
    pro_name = Text(Point(780 + 300, 150), "Product Name")
    pro_name.setSize(13)
    pro_name.setTextColor(color_rgb(70, 70, 70))
    pro_name.setFace("Product Sans Medium")
    pro_name.draw(win)

    pro_name_box = Entry(Point(780 + 300, 180), 17)
    pro_name_box.setFace("Product Sans Light")
    pro_name_box.setTextColor(color_rgb(50, 50, 50))
    pro_name_box.setSize(11)
    pro_name_box.setFill('ivory')
    pro_name_box.draw(win)

    pro_price = Text(Point(780 + 300, 250), "Unit Price")
    pro_price.setSize(13)
    pro_price.setTextColor(color_rgb(70, 70, 70))
    pro_price.setFace("Product Sans Medium")
    pro_price.draw(win)

    pro_price_box = Entry(Point(780 + 300, 280), 17)
    pro_price_box.setFace("Product Sans Light")
    pro_price_box.setTextColor(color_rgb(50, 50, 50))
    pro_price_box.setSize(11)
    pro_price_box.setFill('ivory')
    pro_price_box.draw(win)

    pro_desc = Text(Point(780 + 300, 350), "Description")
    pro_desc.setSize(13)
    pro_desc.setTextColor(color_rgb(70, 70, 70))
    pro_desc.setFace("Product Sans Medium")
    pro_desc.draw(win)

    pro_desc_box = Entry(Point(780 + 300, 380), 17)
    pro_desc_box.setFace("Product Sans Light")
    pro_desc_box.setTextColor(color_rgb(50, 50, 50))
    pro_desc_box.setSize(11)
    pro_desc_box.setFill('ivory')
    pro_desc_box.draw(win)

    # change data
    change_bg = Rectangle(Point(740 + 300, 480), Point(820 + 300, 520))
    change_bg.setFill(color_rgb(102, 206, 110))
    change_bg.setOutline(None)
    change_bg.setWidth(0)
    change_bg.draw(win)

    change = Text(Point(780 + 300, 500), "CHANGE")
    change.setTextColor("ivory")
    change.setSize(13)
    change.setFace("Product Sans Medium")
    change.draw(win)

    for cl in range(30):
        column.move(-10, 0)
        pro_name.move(-10, 0)
        pro_name_box.move(-10, 0)
        pro_price.move(-10, 0)
        pro_price_box.move(-10, 0)
        pro_desc.move(-10, 0)
        pro_desc_box.move(-10, 0)
        change_bg.move(-10, 0)
        change.move(-10, 0)
        time.sleep(0.001)

    while True:
        sub_click = win.getMouse()

        if 740 <= sub_click.getX() <= 820 and 480 <= sub_click.getY() <= 520:
            change_bg.undraw()
            change.undraw()

            # change button invert
            change_bg = Rectangle(Point(740, 480), Point(820, 520))
            change_bg.setFill('ivory')
            change_bg.setOutline(color_rgb(102, 206, 110))
            change_bg.setWidth(2)
            change_bg.draw(win)

            change = Text(Point(780, 500), "CHANGE")
            change.setTextColor(color_rgb(102, 206, 110))
            change.setSize(13)
            change.setFace("Product Sans Medium")
            change.draw(win)

            time.sleep(0.1)
            change_bg.undraw()
            change.undraw()

            # change revert
            change_bg = Rectangle(Point(740, 480), Point(820, 520))
            change_bg.setFill(color_rgb(102, 206, 110))
            change_bg.setOutline(None)
            change_bg.setWidth(0)
            change_bg.draw(win)

            change = Text(Point(780, 500), "CHANGE")
            change.setTextColor("ivory")
            change.setSize(13)
            change.setFace("Product Sans Medium")
            change.draw(win)

            name = pro_name_box.getText()
            price = pro_price_box.getText()
            desc = pro_desc_box.getText()

            name = name.strip()
            desc = desc.strip()

            try:
                cursor.execute(
                    "update products set unit_price = {},description = '{}' where product = '{}'".format(price, desc,
                                                                                                         name))
                mycon.commit()

            except:
                pass

            time.sleep(0.5)

            break

    for cl in range(30):
        column.move(10, 0)
        pro_name.move(10, 0)
        pro_name_box.move(10, 0)
        pro_price.move(10, 0)
        pro_price_box.move(10, 0)
        pro_desc.move(10, 0)
        pro_desc_box.move(10, 0)
        change_bg.move(10, 0)
        change.move(10, 0)
        time.sleep(0.001)

    # hiding previous data from products table
    rect_ = Rectangle(Point(231, 90), Point(659, 600))
    rect_.setFill('white')
    rect_.setWidth(0)
    rect_.draw(win)

    # taking data from products table    
    cursor.execute("select * from products order by product")
    product_data = cursor.fetchall()

    b = 15
    for k in product_data:
        k = list(k)

        pr_name = Text(Point(300, 90 + b), k[0].capitalize())
        pr_name.setSize(13)
        pr_name.setTextColor(color_rgb(60, 60, 60))
        pr_name.setFace("Product Sans Light")
        pr_name.draw(win)

        pr_price = Text(Point(440, 90 + b), k[1])
        pr_price.setSize(13)
        pr_price.setTextColor(color_rgb(60, 60, 60))
        pr_price.setFace("Product Sans Light")
        pr_price.draw(win)

        pr_desc = Text(Point(580, 90 + b), k[2])
        pr_desc.setSize(13)
        pr_desc.setTextColor(color_rgb(60, 60, 60))
        pr_desc.setFace("Product Sans Light")
        pr_desc.draw(win)

        b += 20


# ------------------------------------------------
# ------------------------------------------------
def graph_build():
    cursor.execute("Select month(date), net_total from companies")
    graph_data = cursor.fetchall()

    dict_month = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                  7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

    sl = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
          'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}
    months = []

    for i_data in graph_data:
        i_data = list(i_data)

        if dict_month[i_data[0]] in months:
            a = dict_month[i_data[0]]
            sl[a] += i_data[1]

        else:
            months.append(dict_month[i_data[0]])
            a = dict_month[i_data[0]]
            sl[a] += i_data[1]

    # ---------------------------------------------------------------------

    plt.style.use("Solarize_Light2")

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    sales = sl.values()

    plt.bar(months, sales, width=0.7, color='tomato', label='Sales')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Sales Graph')

    plt.xticks(rotation=30)
    plt.ticklabel_format(style='plain', axis='y')
    plt.gcf().subplots_adjust(left=0.17, bottom=0.14)

    plt.title("Sales Summary", fontsize=14)
    plt.legend(bbox_to_anchor=(1, 1.1))
    plt.ylabel("Amount in \N{Indian rupee sign}")
    plt.xlabel('Months')

    plt.savefig(r"img\graph.png", dpi=110)
    plt.clf()

    gr = GraphWin("Sales Graph", 704, 528)
    gr.setBackground('white')

    gr_img = Image(Point(352, 256), r"img\graph.png")
    gr_img.draw(gr)


# ------------------------------------------------
# ------------------------------------------------
while True:
    click = win.getMouse()

    if 0 <= click.getX() <= 230 and 100 <= click.getY() <= 160:
        invoice()
        page_invoice()
        items_invoice()

    elif 0 <= click.getX() <= 230 and 161 <= click.getY() <= 220:
        bill()
        bill_page()

        while True:
            click2 = win.getMouse()
            if 772 <= click2.getX() <= 788 and 12 <= click2.getY() <= 28:
                try:
                    graph_build()
                except:
                    graph_build()

            elif 525 <= click2.getX() <= 605 and 535 <= click2.getY() <= 565:
                rect_tt = Rectangle(Point(525, 565), Point(605, 535))
                rect_tt.setWidth(0)
                rect_tt.draw(win)
                for ai in range(2):
                    rect_tt.setWidth(1)
                    rect_tt.setOutline("gray")
                    time.sleep(0.1)

                    rect_tt.setWidth(0)
                    rect_tt.setOutline(None)
                    time.sleep(0.1)

                rect_tt.undraw()
                rect_tt = Rectangle(Point(231, -1), Point(900, -600))
                rect_tt.setWidth(0)
                rect_tt.setFill('white')
                rect_tt.draw(win)

                for l in range(60):
                    rect_tt.move(0, 10)
                    time.sleep(0.001)

                chk_b = 0
                rect_b.undraw()
                b_Img.undraw()
                tile_b.undraw()

                break

    elif 0 <= click.getX() <= 230 and 221 <= click.getY() <= 280:
        allow_entry = 'no'
        try:
            from login import *
        except:
            pass

        if allow_entry == 'yes':
            settings()
            settings_page()

    elif 55 <= click.getX() <= 175 and 505 <= click.getY() <= 535:
        devo()

    elif 75 <= click.getX() <= 155 and 555 <= click.getY() <= 585:
        exit_rect = Rectangle(Point(75, 585), Point(155, 555))
        exit_rect.setWidth(2)
        exit_rect.setOutline('white')
        exit_rect.draw(win)
        time.sleep(0.2)
        exit_rect.undraw()
        time.sleep(0.2)

        break

    else:
        pass

# deleting empty tables
cursor.execute("show tables")
table_name_data = []
for t_name in cursor:
    if t_name[0] == 'products' or t_name[0] == 'companies':
        pass
    else:
        table_name_data.append(t_name[0])

for d_name in table_name_data:

    cursor.execute("select * from {}".format(d_name))
    d2 = cursor.fetchall()
    if d2 == []:
        cursor.execute("drop table {}".format(d_name))
    else:
        pass

mycon.commit()
mycon.close()
win.close()
