import mysql.connector as connector
from datetime import date

global conn, cursor

conn= connector.connect(host="localhost",database="pos",user="root",password="VChintu2611")
cursor = conn.cursor()

def clear():
    for _ in range(65):
        print()

def last_bill_no():
    cursor.execute('select max(bill_id) from bills')
    record = cursor.fetchone()
    return record

def find_item(no):
    cursor.execute('select * from items where id ={}'.format(no))
    record = cursor.fetchone()
    return record

def add_item():
    print('Add New Item - Screen')
    print('-'*100)
    item_name = input('Enter new Item Name :')
    item_price = input('Enter Item Price :')
    sql = 'select * from items where item_name like "%{}%"'.format(item_name)
    cursor.execute(sql)
    record=cursor.fetchone()
    if record==None:
        sql = 'insert into items(item_name,price) values("{}",{});'.format(item_name,item_price)
        cursor.execute(sql)
        print('\n\nNew Item added successfully.....\nPress any key to continue....')
    else:
        print('\n\nItem Name already Exist.....\nPress any key to continue....')
    conn.commit()
    wait= input()
#   function name       : modify_item
#   purpose             : change item details in items table

def modify_item():
    print('Modify Item Details - Screen')
    print('-'*100)
    item_id = input('Enter Item ID :')
    item_name = input('Enter new Item Name :')
    item_price = input('Enter Item Price :')
    sql = 'update items set item_name = "{}", price ={} where id={}'.format(item_id,item_name,item_price)
    cursor.execute(sql)
    conn.commit()
    print('\n\nRecord Updated Successfully............')
#   function name           : item_list
#   purpose                 : To display all the items in items tables

def item_list():
    sql="select * from items"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print('\nPress any key to continue.....')
    wait = input()
#   function name       : billing
#   purpose             : To generate bills 

def billing():
    items =[]
    bill_no = last_bill_no()
    if bill_no[0]==None:
        bill_no =1
    else:
        bill_no = bill_no[0]+1 
    name = input('Enter customer Name :')
    phone = input('Enter Phone No :')
    today = date.today()
    while True:
        no = int(input('Enter item No (0 to stop) :'))
        if no <=0:
            break
        else:
            item = find_item(no)
            if item==None:
                print('Item Not found  ')
            else:
                qty = int(input('Enter Item Qty :'))
                item = list(item)
                item.append(qty)
                items.append(item)
    print('                     Reliance Super Mart              ')
    print('                     Dimna Road, Mango, JSR    ')
    print('                     Phone: 7070056104, Email: vaibhav_sharm@outlook.com ')
    print('Bill No :{}        Date :{}'.format(bill_no,today))
    print('-'*100)
    print('Customer Name :{}          Phone No :{}'.format(name,phone))
    print('-'*100)
    print('Item Id     Item Name                Price            Qty         Amount ')
    print('-'*100)
    total =0
    for item in items:
        print('{:<10d} {:25s} {:.2f} {:>10d}          {:>.2f} \
            '.format(item[0],item[1],item[2],item[3],item[2]*item[3]))
        total = total +item[2]*item[3]
    print('-'*100)
    print('Total Payable amount : {}'.format(total))
    print('\nPress any key to continue........')
    #insert data into tables
    sql ='insert into bills(name,phone,bill_date) values("{}","{}","{}");'.format(name,phone,today)
    cursor.execute(sql)
    for item in items:
        sql='insert into transaction(item_id,qty,bill_id) values({},{},{});'.format(item[0],item[3],bill_no)
        cursor.execute(sql)
        conn.commit()
    wait= input()
#   function      : Date_wise_sell
#   purpose       : Create a report on date wise sell or sell between two dates 

def date_wise_sell():
    print('Sell Between Two Dates -- Screen')
    print('-'*100)
    start_date = input('Enter start Date (yyyy-mm-dd) :')
    end_date   = input('Enter End Date (yyyy-mm-dd) :')
    sql = 'select * from bills where bill_date between "{}" and "{}"'.format(start_date,end_date)
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Bill No       Customer Name         Phone No         Bill Date')
    print('-'*100)
    for row in records:
        print('{:10d} {:30s} {:20s} {}'.format(row[0],row[1],row[2],row[3]))
    print('-'*100)
    print('\n\nPress any key to continue....')
    wait= input()
# function name        : bill information
# purpose               : display details of any bill

def bill_information():
    bill_no = input('Enter Bill Number :')
    sql = 'select b.bill_id,b.name,b.phone,b.bill_date,t.item_id,t.qty,i.item_name,i.price from bills b,transaction t,items i \
           where b.bill_id = t.bill_id AND t.item_id= i.id AND \
           b.bill_id ={};'.format(bill_no)
    cursor.execute(sql)
    records = cursor.fetchall()
    n = cursor.rowcount
    print("Bill No :",bill_no)
    print('-'*100)
    if n<=0:
        print('Bill number {} does not exists'.format(bill_no))
    else:
        print('Customer Name : {}  Phone No :{}'.format(records[0][1],records[0][2]))
        print('Bill Date : {}'.format(records[0][3]))
        print('-'*100)
        print('{:10s} {:30s} {:20s} {:10s} {:30s}'.format('ID','Item Name','Qty','Price','Amount'))
        print('-'*100)
        for row in records:
            print('{:<10d} {:30s} {:<20d} {:.2f} {:>.2f}'.format(row[4],row[6],row[5],row[7],row[5]*row[7]))
        print('-'*100)
    print('\nPress any key to continue....')
    wait = input()   
#  function name    : amount_collected
#  purpose               : Function to display amount collected between two dates

def amount_collected():
    start_date = input('Enter start Date (yyyy-mm-dd) :')
    end_date   = input('Enter End   Date (yyyy-mm-dd) :')
    print('Amount collected between: {} and {}'.format(start_date,end_date))
    print('-'*100)
    sql = 'select sum(t.qty*i.price) from bills b,transaction t,items i \
           where b.bill_date between "{}" AND "{}" AND b.bill_id = t.bill_id AND \
           t.item_id = i.id;'.format(start_date,end_date)
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    print('\nPress any key to continue.....')
    wait= input()

def search_item():
    item_name =input('Enter Item Name :')
    sql ='select * from items where item_name like "%{}%";'.format(item_name)
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Item Names start with :',item_name)
    print('-'*100)
    print('{:10s} {:30s} {:20s}'.format('Item ID','Item Name','Item Price'))
    print('-'*100)
    for row in records:
        print('{:<10d} {:30s} {:.2f}'.format(row[0],row[1],row[2]))
    print('-'*100)
    print('\nPress any key to continue....')
    wait= input()

def search_customer():
    cust_name =input('Enter customer Name :')
    sql ='select * from bills where name like "%{}%";'.format(cust_name)
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Customer Names started with :',cust_name)
    print('-'*100)
    print('{:10s} {:30s} {:20s} {:20s}'.format('Bill No','Customer Name','Phone No','Bill Date'))
    print('-'*100)
    for row in records:
        print('{:<10d} {:30s} {:20s} {:20s}'.format(row[0],row[1],row[2],str(row[3])))
    print('-'*100)
    print('\nPress any key to continue....')
    wait= input()
# function name      : search_bill
# purpose            : function to find out bill information

def search_bill():
    bill_no = input('Enter Bill Number :')
    sql = 'select b.bill_id,b.name,b.phone,b.bill_date,t.item_id,t.qty,i.item_name,i.price from bills b,transaction t,items i \
           where b.bill_id = t.bill_id AND t.item_id= i.id AND \
           b.bill_id ={};'.format(bill_no)
    cursor.execute(sql) 
    records = cursor.fetchall()
    n = cursor.rowcount
    print("Bill No :",bill_no)
    print('-'*100)
    if n<=0:
        print('Bill number {} does not exists'.format(bill_no))
    else:
        print('Customer Name : {}  Phone No :{}'.format(records[0][1],records[0][2]))
        print('Bill Date : {}'.format(records[0][3]))
        print('-'*100)
        print('{:10s} {:30s} {:20s} {:10s} {:30s}'.format('ID','Item Name','Qty','Price','Amount'))
        print('-'*100)
        for row in records:
            print('{:<10d} {:30s} {:<20d} {:.2f} {:>.2f}'.format(row[4],row[6],row[5],row[7],row[5]*row[7]))
        print('-'*100)
    print('\nPress any key to continue....')
    wait = input()   
#  function name    : search_menu
#  purpose          : Display search menu on the screen

def search_menu():
    while True:
        print('      S E A R C H    M E N U ')
        print('-'*100)
        print('1.   Item Name')
        print('2.   Customer information')
        print('3.   Bill information')
        print('4.   Back to main Menu')
        choice = int(input('\n\nEnter your choice (1..4): '))
        if choice==1:
            search_item()
        if choice==2:
            search_customer()
        if choice==3:
            search_bill()
        if choice==4:
            break
#  function name    : report_menu
#  purpose          : Display report menu on the screen

def report_menu():
    while True:
        print('   R E P O R T   M E N U ')
        print('-'*100)
        print('1.   Item List')
        print('2.   Sell Between Dates')
        print('3.   Bill information')
        print('4.   Amount collected')
        print('5.   Back to main Menu')
        choice = int(input('\n\nEnter your choice (1..5): '))
        if choice==1:
            item_list()
        if choice==2:
            date_wise_sell()
        if choice==3:
            bill_information()
        if choice==4:
            amount_collected()
        if choice==5:
            break

def main_menu():
    while True:
        print('      M A I N   M E N U')
        print('-'*100)
        print('1.   Add New Item')
        print('2.   Modify Existing Item')
        print('3.   Billing')
        print('4.   Search Menu')
        print('5.   Report Menu')
        print('6.   Exit')
        choice = int(input('\n\nEnter your choice (1..6): '))
        if choice==1:
            add_item()
        if choice==2:
            modify_item()
        if choice==3:
            billing()
        if choice==4:
            search_menu()
        if choice==5:
            report_menu()
        if choice==6:
            break

if __name__=="__main__":
    main_menu()