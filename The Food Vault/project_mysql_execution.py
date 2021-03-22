import mysql.connector
import os
from project_objects import db,cur


def execute_commands():
    cur.execute('CREATE DATABASE project')

    cur.execute('USE project')

    cur.execute("""CREATE TABLE `rest info`(`rest code` INTEGER NOT NULL PRIMARY KEY,`rest name` VARCHAR(50) NOT NULL,`establishment type` VARCHAR(200) NOT NULL,`address` VARCHAR(200) NOT NULL,`facilities` VARCHAR(500) NOT NULL,`cuisines` VARCHAR(200) NOT NULL,`city` VARCHAR(20) NOT NULL,`phone no.` VARCHAR(50) NOT NULL)""")
    cur.execute("""INSERT INTO `rest info` VALUES(001,'Chaayos - Meri Wali Chai',' Cafe ','MAT 2-KSK 05 & KSK 04, Lower Ground Floor, Shipra Mall, Indirapuram',' Breakfast, Wifi, Home Delivery, Indoor Seating ',' Tea, Beverages, Fast Food, Street Food, Desserts ','Ghaziabad','0120-2580657')""")
    cur.execute("""INSERT INTO `rest info` VALUES(002,'Rolls Mania',' Quick Bites ','Harichand Complex, Sarafabad, Sector 73',' Indoor Seating, Home Delivery ',' Rolls, Fast Food ','Noida','0120-4652364')""")
    cur.execute("""INSERT INTO `rest info` VALUES(003,"Nathu's Sweets",' Sweet Shop, Quick Bites ','GC- 08, Ground Floor, Dubai Mall, RDC, Raj Nagar',' Breakfast, Indoor Seating, Home Delivery, Vegetarian Only ',' Mithai, North Indian, Street Food, South Indian, Continental ','Ghaziabad','+911204880471')""")
    cur.execute("""INSERT INTO `rest info` VALUES(004,'Barista Diner',' Cafe ','Unit UG 02, Starling Mall, Sector 104',' Breakfast, Desserts and Bakes, Home Delivery, Indoor Seating ',' Cafe, Desserts, Beverages, Sandwich, Biryani ','Noida','+917277788876')""")
    cur.execute("""INSERT INTO `rest info` VALUES(005,"Nawab's Biryani",' Casual Dining ','C-16, Market, Gautam Budh Nagar, Sector 18',' Home Deliver, Indoor Seating, Table Booking Recommended ',' Mughlai, Biryani, North Indian ', 'Noida', '+918287344501')""")
    cur.execute("""INSERT INTO `rest info` VALUES(006,"Chili's Grill & Bar",' Casual Dining ','3rd Floor, DLF Mall Of India, Sector 18',' Home Delivery, Indoor Seating, Mall Parking, Table Booking Recommended, Wheelchair Accessible, Live Sports Screening '," Mexican, Italian, American, Tex-Mex, Bar Food, Beverages ",'Noida','+919650082466')""")
    cur.execute("""INSERT INTO `rest info` VALUES(007,'Dasaprakash',' Casual Dining ','HA 106, Sector 104, Opposite Pathway School, Hajipur',' Home Delivery, Indoor Seating, Breakfast ',' North Indian, South Indian, Chinese, Beverages ','Noida','+919693969371')""")
    cur.execute("""INSERT INTO `rest info` VALUES(008,'The Brew Room',' Cafe, Casual Dining ','C16, 1st Floor, Opposite IIT Gate, SDA',' Home Delivery, Indoor Seating, Breakfast, Wifi, Table Booking Recommended ',' Cafe, Italian, American, Pizza, Continental ','New Delhi','+919958366347')""")
    cur.execute("""INSERT INTO `rest info` VALUES(009,"The Culinary Court - Park Ascent",' Casual Dining ','Park Ascent, Plot 126, Noida Khoda Road, Sector 62',' Home Delivery, Indoor Seating, Wifi, Buffet, Table Booking Recommended, Wheelchair Accessible, Full Bar Available ',' North Indian, Chinese, Continental ','Noida', '+911206780012')""")
    cur.execute("""INSERT INTO `rest info` VALUES(010,'The Feast Box',' Casual Dining ','Shop 32, Assotech Business Cresterra, Sector 135',' Home Delivery, Indoor Seating, Wifi ',' North Indian, Mughlai, Continental, Rolls, Fast Food ','Noida','+919830094049')""")
    cur.execute("""INSERT INTO `rest info` VALUES(011,'Maestro',' Cafe ','B-14, Deep Cinema Complex, Ashok Vihar Phase 1',' Home Delivery, Indoor Seating, Live Sports Screening, Wifi ',' Cafe, North Indian, Chinese, Italian ','New Delhi','+919811624971')""")
    cur.execute("""INSERT INTO `rest info` VALUES(012,"Haldiram's",' Quick Bites, Sweet Shop ','Ground Floor, Block 3, Vatika Business Park, Sector 49',' Home Delivery, Indoor Seating, Breakfast, Vegetarian Only, Mall Parking, Desserts and Bakes ',' North Indian, Chinese, South Indian, Street Food, Mithai ','Gurugram','+919212764630')""")
    cur.execute("""INSERT INTO `rest info` VALUES(013,'Taco Bell',' Quick Bites ','Shop GF-03A & GF-04, BG-1 & BG-2, Gourmet Hub, Paschim Puri, Paschim Vihar',' Home Delivery, Indoor Seating, Wheelchair Accessible, Wifi, Mall Parking ',' Mexican, Fast Food, Wraps ','New Delhi','+917428535738')""")
    cur.execute("""INSERT INTO `rest info` VALUES(014,'KFC',' Quick Bites ','Shop 25 & 26, Plot 1, Ground Floor, Gourmet Hub, Paschim Puri, Near Punjabi Bagh',' Home Delivery, Indoor Seating ',' Burger, Fast Food, Finger Food, Beverages ','New Delhi','+911133994444')""")
    cur.execute("""INSERT INTO `rest info` VALUES(015,'Ah So Yum',' Quick Bites ','Parsvnath Exotica, DLF Phase 5, Sector 53, Gurugram, Haryana 122003', ' Home Delivery Only ',' Chinese, Thai, Malaysian, Japanese, Asian ','Gurugram','+917303200824')""")

    cur.execute("""CREATE TABLE `starters`(`rest code` INTEGER NOT NULL PRIMARY KEY,`rest name` VARCHAR(999) NOT NULL,`starter items` VARCHAR(999) NOT NULL,`prices` VARCHAR(999) NOT NULL)""")
    cur.execute("""INSERT INTO `starters` VALUES('001','Chaayos - Meri Wali Chai','Cheese Balls,Dumplings,Cheese Toast,Vada Pav,Bhelpuri','250,178,167,100,114')""")
    cur.execute("""INSERT INTO `starters` VALUES('002','Rolls Mania','French Fries,Chilli Garlic Poppers,Cheese Poppers,Nachos,Chicken Cheese Popcorn','60,70,80,80,90')""")
    cur.execute("""INSERT INTO `starters` VALUES('003',"Nathu's Sweets",'Paneer Tikka,Chilly Paneer,Spring Rolls,Chilly Potato','240,250,170,180')""")
    cur.execute("""INSERT INTO `starters` VALUES('004','Barista Diner','Smoked Chicken Sandwich,Spinach and Corn Club Sandwich,Garlic Toasties,Cheese Garlic Bruschetta','250,289,129,169')""")
    cur.execute("""INSERT INTO `starters` VALUES('005',"Nawab's Biryani",'Baby Corn Fry,Honey Chilly Potato,Crispy Veg,Chilly Chicken,Pepper Chicken','269,269,260,329,319')""")
    cur.execute("""INSERT INTO `starters` VALUES('006',"Chili's Grill & Bar",'Texas Cheese Poppers,Potato Wedges,Onion Rings,Chicken Crispers,Country Fried Chicken','10,20,30,40,50')""")
    cur.execute("""INSERT INTO `starters` VALUES('007','Dasaprakash','Veg Cutlets,Potato Bonda,Paneer Pakoda','85,75,100')""")
    cur.execute("""INSERT INTO `starters` VALUES('008','The Brew Room','Cream of Mushroom,Cream of Chicken,Roasted Bell Pepper and Tomato','200,250,200')""")
    cur.execute("""INSERT INTO `starters` VALUES('009','The Culinary Court - Park Ascent','Sialkot Murgh Tikka,Murgh Nafees,Tandoori Chicken','425,425,425')""")
    cur.execute("""INSERT INTO `starters` VALUES('0010','The Feast Box','Spring Rolls,Cheese Corn Rolls,Chilly Potato','169,209,99')""")
    cur.execute("""INSERT INTO `starters` VALUES('0011','Maestro','Mexican Nacho Corn Chaat,Mexican Quesadillas,Garlic Bread with Cheese','219,239,169')""")
    cur.execute("""INSERT INTO `starters` VALUES('0012',"Haldiram's",'Bhelpuri,Aloo Tikki,Pav Bhaji','48,62,97')""")
    cur.execute("""INSERT INTO `starters` VALUES('0013','Taco Bell','Quesadilla,Cheese Pockets,Cheese Nuggets','159,99,149')""")
    cur.execute("""INSERT INTO `starters` VALUES('0014','KFC','French Fries,Chicken Strips,Veggie Strips','95,215,140')""")
    cur.execute("""INSERT INTO `starters` VALUES('0015','Ah So Yum','Honey Chilly Potato,Mushroom Pakoda Pav,Vietnnamese Rolls','295,379,370')""")

    cur.execute("""CREATE TABLE `main course`(`rest code` integer NOT NULL PRIMARY KEY,`rest name` VARCHAR(999) NOT NULL,`main course items` VARCHAR(999) NOT NULL,`prices` varchar(999) NOT NULL)""")
    cur.execute("""INSERT INTO `main course` VALUES('001','Chaayos - Meri Wali Chai','Pav Bhaaji,Rajma Rice Bowl,Paneer Rice Bowl','150,180,240')""")
    cur.execute("""INSERT INTO `main course` VALUES('002','Rolls Mania','Soya Chaap Roll,Paneer Roll,Paneer Tikka Roll','180,150,170')""")
    cur.execute("""INSERT INTO `main course` VALUES('003',"Nathu's Sweets",'Kadhai Paneer,Mix Vegetable,Pindi Chholey','320,230,280')""")
    cur.execute("""INSERT INTO `main course` VALUES('004','Barista Diner','Arabiata Sauce Pasta, Cheesy White Sauce Pasta, Five Cheese Pizza','230,230,450')""")
    cur.execute("""INSERT INTO `main course` VALUES('005',"Nawab's Biryani",'Hyderabadi Biryani,Keema Biryani,Dum Biryani','240,280,190')""")
    cur.execute("""INSERT INTO `main course` VALUES('006',"Chili's Grill & Bar",'Chipotle Chicken Flatbread,Margherita Flat Bread,Pepperoni Pizza','525,415,580')""")
    cur.execute("""INSERT INTO `main course` VALUES('007','Dasaprakash','Masala Dosa,Rawa Plain Dosa, Vegetable Utappam','159,99,120')""")
    cur.execute("""INSERT INTO `main course` VALUES('008','The Brew Room','Cajun Chicken Pasta Alfredo,Cajun Shrimp Pasta Alfredo,Cajun Veg Pasta Alfredo','540,600,395')""")
    cur.execute("""INSERT INTO `main course` VALUES('009','The Culinary Court - Park Ascent','Chicken Rice Bowl,Roasted Veggie Rice Bowl,takoyaki','210,185,325')""")
    cur.execute("""INSERT INTO `main course` VALUES('010','The Feast Box','Parmesan Crusted Cottage Cheese Quesadilla,Santa Fe Chicken Quesadilla,Veg Cheese Quesadilla','535,325,450')""")
    cur.execute("""INSERT INTO `main course` VALUES('011','Maestro','Parmesan Crusted Cottage Cheese Quesadilla,Santa Fe Chicken Quesadilla,Smoked Chicken Quesadilla','415,450,550')""")
    cur.execute("""INSERT INTO `main course` VALUES('012',"Haldiram's",'Chholey Bhature,Palak Paneer,Shahi Paneer','215,310,420')""")
    cur.execute("""INSERT INTO `main course` VALUES('013','Taco Bell','Crispy Chicken Taco,Crispy Paneer,Cottage Cheese Taco','525,375,415')""")
    cur.execute("""INSERT INTO `main course` VALUES('014','KFC','Veg Zinger Burger,Classic Chicken Zinger Burger,Dream Team Bucket','89,142,522')""")
    cur.execute("""INSERT INTO `main course` VALUES('015','Ah So Yum','Blackened Salmon,Shrimp Fajita,Santa fe Paneer Salad','550,780,600')""")

    cur.execute("""CREATE TABLE `dessert`(`rest code` integer NOT NULL PRIMARY KEY,`rest name` varchar(999) NOT NULL,`des items` varchar(999) NOT NULL,`prices` varchar(999) NOT NULL)""")
    cur.execute("""INSERT INTO `dessert` VALUES('001','Chaayos - Meri Wali Chai','Buttery Raspberry Crumble Bars,Mint Oreo Cake,Ultimate Gooey Brownies','120,159,200')""")
    cur.execute("""INSERT INTO `dessert` VALUES('002','Rolls Mania','Chocolate And Strawberry Cake,Old Fashioned Sour Cream Doughnuts,Coconut Cream Crepe Cake','230,320,415')""")
    cur.execute("""INSERT INTO `dessert` VALUES('003',"Nathu's Sweets",'Cookie Dough Cheesecake Bars,Meyer Lemon Bars,Pomegranate Mousse Cake','125,260,175')""")
    cur.execute("""INSERT INTO `dessert` VALUES('004','Barista Diner','Chocolate Chip Cookies With Nutella,Pavlova With Blueberry Jam,Roasted Pears With Espresso Mascarpone Cream','115,215,100')""")
    cur.execute("""INSERT INTO `dessert` VALUES('005',"Nawab's Biryani",'Salted Caramel Chocolate Tart,Banana Pudding Parfaits,Browned Butter Toffee cookies','315,24,110')""")
    cur.execute("""INSERT INTO `dessert` VALUES('006',"Chili's Grill & Bar",'Nutella Brownies,Coconut Tres Leches,Tiramisu','150,220,175')""")
    cur.execute("""INSERT INTO `dessert` VALUES('007','Dasaprakash','Blueberry-Streusel Bars,Lavender Ruffle,Rum Cannoli','215,415,615')""")
    cur.execute("""INSERT INTO `dessert` VALUES('008','The Brew Room','Chocolate Mousse Cake,Cherry Squares,Snickers Cake','220,115,310')""")
    cur.execute("""INSERT INTO `dessert` VALUES('009','The Culinary Court - Park Ascent','Passionfruit Bars,Peach Pie,Velvety Dark Chocolate Pudding','125,145,180')""")
    cur.execute("""INSERT INTO `dessert` VALUES('010','The Feast Box','Lemon Sandwich Cookies,Meringue Tartlets,Blueberry Cardamom Buckle','315,245,175')""")
    cur.execute("""INSERT INTO `dessert` VALUES('011','Maestro',"Butterscotch Pie,S'mores Cupcakes,Dark Chocolate Frosted Yellow Cake",'120,130,500')""")
    cur.execute("""INSERT INTO `dessert` VALUES('012',"Haldiram's",'Cream Cheese Swirl Bars,Alfajores,Mixed Berry Slab Pie','99,175,315')""")
    cur.execute("""INSERT INTO `dessert` VALUES('013','Taco Bell','Pistachio Pavlova,Cannoli Tart,Caramel Pecan Blondies','249,329,139')""")
    cur.execute("""INSERT INTO `dessert` VALUES('014','KFC','Toasted Coconut Toffee,Skillet Cookie,Brownie Cookies','315,210,139')""")
    cur.execute("""INSERT INTO `dessert` VALUES('015','Ah So Yum','Cheesecake,Banana Cream Pie With Hot Fudge,Caramel Mousse Pie','285,310,415')""")

    cur.execute("""CREATE TABLE `user details`(`first name` VARCHAR(20) NOT NULL,`last name` VARCHAR(20) NOT NULL,`email` VARCHAR(100) NOT NULL, `password` VARCHAR(20) NOT NULL, `mobile no.` varchar(15) NOT NULL)""")

    cur.execute("""CREATE TABLE `user addresses`(`email` VARCHAR(100) NOT NULL, `address` varchar(999) NOT NULL)""")

    cur.execute("""CREATE TABLE `user orders`(`order id` int auto_increment NOT NULL PRIMARY KEY,`email` VARCHAR(100) NOT NULL,`customer name` VARCHAR(99) NOT NULL,`mobile number` varchar(15) NOT NULL,`delivery address` varchar(999) NOT NULL,`restaurant name` VARCHAR(99) NOT NULL, `items` VARCHAR(999) NOT NULL, `quantity` VARCHAR(999) NOT NULL, `prices` VARCHAR(999) NOT NULL, `date` DATE NOT NULL,`amount payable` varchar(20) NOT NULL, `status` VARCHAR(20) NOT NULL, `address` VARCHAR(999) NOT NULL, `number` VARCHAR(15) NOT NULL, `time` TIME NOT NULL)""")
    
    db.commit()


