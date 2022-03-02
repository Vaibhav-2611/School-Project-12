import mysql.connector 
import time
from datetime import date

global conn,cursor
conn = mysql.connector.connect(
    host='localhost', database=' parking_system', user='root', password='VChintu2611')
cursor = conn.cursor()

def clear():
  for _ in range(65):
     print()

def made_by():
    msg = ''' 
            Parking Management system made by  :Kumar Vaibhav, Pritam Raj & Shyam Kumar
            School Name                                               :BBEHS
            session                                                         :2020-21
            Thanks for evaluating my Project.
            \n\n\n'''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')

def display_parking_type_records():
    cursor.execute('select * from parking_type;')
    records = cursor.fetchall()
    for row in records:
        print(row)

def add_parking_type_record():
    name = input('Enter Parking Type( 1. Two wheelar 2. Car 3. Bus 4. Truck 5. Trolly ) : ')
    price =  input('Enter Parking Price per day : ')
    sql = 'insert into parking_type(name,price) values("{}",{});'.format(name,price)
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Parking Type added....')
    cursor.execute('select max(id) from parking_type')
    no = cursor.fetchone()
    print(' New Parking Type ID is : {} \n\n\n'.format(no[0]))
    wait= input('\n\n\nPress any key to continue............')

def add_parking_slot_record():
    parking_type_id = input(
        'Enter Parking Type( 1. Two wheelar 2. Car 3. Bus 4. Truck 5. Trolly ) :')
    status = input('Enter current Status ( Open/Full ) :')
    sql = 'insert into parking_space(type_id,status) values \
            ("{}","{}");'.format(parking_type_id,status) 
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Parking Space Record added....')
    cursor.execute('select max(id) from parking_space;')
    no = cursor.fetchone()
    print(' Your Parking ID is : {} \n\n\n'.format(no[0]))
    display_parking_type_records()
    wait = input('\n\n\nPress any key to continue............')

def modify_parking_type_record():
    print(' M O D I F Y   P A R K I N G   T Y P E  S C R E E N ')
    print('-'*100)
    print('1.  Parking Type Name \n')
    print('2.  Parking Price  \n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice==1:
        field='name'
    if choice==2:
        field='price'
    
    park_id = input('Enter Parking Type ID :')
    value = input('Enter new values :')
    sql = 'update parking_type set '+ field +' = "' + value +'" where id ='+ park_id +';'
    cursor.execute(sql)
    conn.commit()
    print('Record updated successfully................')
    display_parking_type_records()
    wait = input('\n\n\nPress any key to continue............')

def modify_parking_space_record():
    print(' M O D I F Y  P A R K I N G   S P A C E   R E C O R D ')
    print('-'*100)
    print('1.  Parking Type ID(1-Two Wheelar, 2: Car 3.Bus etc ):  ')
    print('2.  status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'type_id'
    if choice ==2:
        field = 'status'
    print('\n\n\n')
    crime_id = input('Enter Parking Space ID  :')
    value = input('Enter new values :')
    sql = 'update parking_space set ' + field + \
        ' = "' + value + '" where id =' + crime_id + ';'
    cursor.execute(sql)
    conn.cursor()
    conn.commit()
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')
def add_new_vehicle():
    print('Vehicle Login Screen ')
    print('-'*100)
    vehicle_id = input('Enter Vehicle Number :' )
    parking_id = input('Enter parking ID :')
    entry_date = date.today()
    sql = 'insert into transaction(vehicle_id,parking_id,entry_date) values \
           ("{}","{}","{}");'.format(vehicle_id,parking_id,entry_date)
    cursor.execute(sql)
    cursor.execute('update parking_space set status ="full" where id ={}'.format(parking_id))
    conn.commit()
    print('\n\n\n Record added successfully.................')
    wait= input('\n\n\nPress any key to continue.....')

def remove_vehicle():
    print('Vehicle Logout Screen')
    print('-'*100)
    vehicle_id = input('Enter vehicle No :')
    exit_date = date.today()
    sql = 'select parking_id,price,entry_date from transaction tr,parking_space ps, parking_type pt \
           where tr.parking_id = ps.id and ps.type_id = pt.id and \
           vehicle_id ="'+vehicle_id+'" and exit_date is NULL;'
    cursor.execute(sql)
    record = cursor.fetchone()
    days = (exit_date-record[2]).days
    if days ==0:
        days = days+1
    amount = record[1]*days
    print('Logout Details ')
    print('-'*100)
    print('Parking ID : {}'.format(record[0]))
    print('Vehicle ID : {}'.format(vehicle_id))
    print('Parking Date : {}'.format(record[2]))
    print('Current Date : {}'.format(exit_date))
    print('Amount Payable : {}'.format(amount))
    wait = input('press any key to continue......')
    #update transaction and parking space tables
    sql1 = 'update transaction set exit_date ="{}" , amount ={} where vehicle_id ="{}" \
            and exit_date is NULL;'.format(exit_date,amount, vehicle_id)
    sql2 =  'update parking_space set status ="open" where id = {}'.format(record[0])
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    wait = input('Vehicle Out from our System Successfully.......\n Press any key to continue....')

def search_menu():
    print(' S E A R C H  P A R K I N G  M E N U ')
    print('1.  Parking ID \n')
    print('2.  Vehicle Parked  \n')
    print('3.  Free Space \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'id'
    if choice == 2:
        field = 'vehicle No'
    if choice == 3:
        field = 'status'
    value = input('Enter value to search :')
    if choice == 1 or choice==3:
        sql = 'select ps.id,name,price, status \
          from parking_space ps , parking_type pt where ps.id = pt.id AND ps.id ={}'.format(value)
    else:
        sql = 'select id,vehicle_id,parking_id,entry_date from transaction where exit_date is NULL;'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
    for row in results:
        print(row)
    if records < 1:
        print('Record not found \n\n\n ')
    wait = input('\n\n\nPress any key to continue......')

def parking_status(status):
    print('Parking Status :',status)
    print('-'*100)
    sql ="select * from parking_space where status ='{}'".format(status)
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    wait =input('\n\n\nPress any key to continue.....')

def vehicle_status_report():
    print('Vehicle Status - Currently Parked')
    print('-'*100)
    sql='select * from transaction where exit_date is NULL;'
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    wait =input('\n\n\nPress any key to continue.....')

def money_collected():
    start_date = input('Enter start Date(yyyy-mm-dd): ')
    end_date = input('Enter End Date(yyyy-mm-dd): ')
    sql = "select sum(amount) from transaction where \
          entry_date ='{}' and exit_date ='{}'".format(start_date,end_date)
    cursor.execute(sql)
    result = cursor.fetchone()
    print('Total money Collected from {} to {}'.format(start_date,end_date))
    print('-'*100)
    print(result[0])
    wait =input('\n\n\nPress any key to continue.....')
def report_menu():
    while True:
        print(' P A R K I N G    R E P O R T S  ')
        print('-'*100)
        print('1.  Parking Types \n')
        print('2.  Free Space  \n')
        print('3.  Ocupied Space  \n')
        print('4.  Vehicle Status  \n')
        print('5.  Money Collected  \n')
        print('6.  Exit  \n')
        choice = int(input('Enter your choice :'))
        field = ''
        if choice == 1:
            display_parking_type_records()
        if choice == 2:
            parking_status("open")
        if choice == 3:
            parking_status("full")
        if choice == 4:
            vehicle_status_report()
        if choice == 5:
            money_collected()
        if choice ==6: 
            break
def main_menu():   
    while True:
      print(' P A R K I N G   M A N A G E M E N T    S Y S T E M')
      print('*'*100)
      print("\n1.  Add New Parking Type")
      print("\n2.  Add New Parking Slot")
      print('\n3.  Modify Parking Type Record')
      print('\n4.  Modify Parking Slot Record')
      print('\n5.  Vehicle Login ')
      print('\n6.  Vehicle Logout')
      print('\n7.  Search menu')
      print('\n8.  Report menu')
      print('\n9.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_parking_type_record()
      if choice == 2:
        add_parking_slot_record()
      if choice == 3:
        modify_parking_type_record()
      if choice == 4:
        modify_parking_space_record()
      if choice == 5:
        add_new_vehicle()      
      if choice == 6:
        remove_vehicle()
      if choice == 7:
        search_menu()
      if choice == 8:
        report_menu()    
      if choice == 9:
        break
    made_by()

if __name__ == "__main__":
    main_menu()
