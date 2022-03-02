import mysql.connector
from datetime import date
from prettytable import PrettyTable

fine_per_day =1.0  #global variable

def clear():
  for _ in range(65):
     print()

def add_books():
  conn = mysql.connector.connect(
       host='localhost', database='library', user='root', password='VChintu2611')
  cursor = conn.cursor()

  title = input('Enter books Title :')
  author = input('Enter books Author : ')
  publisher = input('Enter books Publisher : ')
  pages = input('Enter books Pages : ')
  price = input('Enter books Price : ')
  edition = input('Enter books Edition : ')
  copies  = int(input('Enter copies : ')) 
  sql = 'insert into books(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
   #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  for _ in range(0,copies):
    cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\nNew books added successfully')
  wait = input('\n\n\n Press any key to continue....')


def add_member():
  conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='VChintu2611')
  cursor = conn.cursor()

  name = input('Enter Member Name :')
  clas = input('Enter Member Class & Section : ')
  address = input('Enter Member Address : ')
  phone = input('Enter Member Phone  : ')
  email = input('Enter Member Email  : ')
  
 
  sql = 'insert into member(name,class,address,phone,email) values ( "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'
  #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\nNew Member added successfully')
  wait = input('\n\n\n Press any key to continue....')


def modify_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('Modify books Details Screen ')
    print('-'*120)
    print('\n1. books Title')
    print('\n2. books Author')
    print('\n3. books Publisher')
    print('\n4. books Pages')
    print('\n5. books Price')
    print('\n6. books Edition')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'title'
    if choice == 2:
        field = 'author'
    if choice == 3:
        field = 'publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    books_id = input('Enter books ID :')
    value = input('Enter new value :')
    if field =='pages' or field == 'price':
        sql = 'update books set ' + field + ' = '+value+' where id = '+books_id+';'
    else:
        sql = 'update books set ' + field + ' = "'+value+'" where id = '+books_id+';'
    #print(sql)
    cursor.execute(sql)
    print('\n\n\nbooks details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def modify_member():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Emaile')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'phone'
    if choice == 5:
        field = 'email'
    mem_id =input('Enter member ID :')
    value = input('Enter new value :')
    sql = 'update member set '+ field +' = "'+value+'" where id = '+mem_id+';'
    #print(sql)
    cursor.execute(sql)
    print('Member details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def mem_issue_status(mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    sql ='select * from transaction where m_id ='+mem_id +' and dor is NULL;'
    #print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def books_status(books_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    sql = 'select * from book where id ='+books_id + ';'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[5]

def books_issue_status(books_id,mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    sql = 'select * from transaction where b_id ='+books_id + ' and m_id ='+ mem_id +' and dor is NULL;'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def issue_books():
    conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n books ISSUE SCREEN ')
    print('-'*120)
    books_id = input('Enter books  ID : ')
    mem_id  = input('Enter Member ID :')   
    result = books_status(books_id)
    result1 = mem_issue_status(mem_id)
    #print(result1)
    today = date.today()
    if len(result1) == 0:
      if result == 'available':
          sql = 'insert into transaction(b_id, m_id, doi) values('+books_id+','+mem_id+',"'+str(today)+'");'
          sql_books = 'update books set status="issue" where id ='+books_id + ';'
          cursor.execute(sql)
          cursor.execute(sql_books)
          print('\n\n\n books issued successfully')
      else:
          print('\n\nbooks is not available for ISSUE... Current status :',result1)
    else:
      if len(result1)<1:
        sql = 'insert into transaction(b_id, m_id, doi) values(' + \
             books_id+','+mem_id+',"'+str(today)+'");'
        sql_books = 'update books set status="issue" where id ='+books_id + ';'
        #print(len(result))
        cursor.execute(sql)
        cursor.execute(sql_books)
        print('\n\n\n books issued successfully')
      else:
        print('\n\nMember already have books from the Library')
      #print(result)
      conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def return_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    global fine_per_day
    print('\n books RETURN SCREEN ')
    print('-'*120)
    books_id = input('Enter books  ID : ')
    mem_id = input('Enter Member ID :')
    today =date.today()
    result = books_issue_status(books_id,mem_id)
    if result==None:
       print('books was not issued...Check books Id and Member ID again..')
    else:
       sql='update books set status ="available" where id ='+books_id +';'
       din = (today - result[3]).days
       fine = din * fine_per_day    #  fine per data
       sql1 = 'update transaction set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+books_id +' and m_id='+mem_id+' and dor is NULL;'       
       cursor.execute(sql)
       cursor.execute(sql1)
       print('\n\nbooks returned successfully')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_books(field):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n books SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' Value :'
    title = input(msg)
    sql ='select * from books where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Search Result for :',field,' :' ,title)
    print('-'*120)
    for record in records:
      print(record)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_menu():
    while True:
      print(' S E A R C H   M E N U ')
      print("\n1.  books Title")
      print('\n2.  books Author')
      print('\n3.  Publisher')
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field =''
      if choice == 1:
        field='title'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'publisher'
      if choice == 4:
        break
      search_books(field)


def reprot_books_list():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - books TITLES ')
    print('-'*120)
    sql ='select * from books'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')

def report_issued_bookss():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - books TITLES - Issued')
    print('-'*120)
    sql = 'select * from book where status = "issue";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.commit()
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_available_bookss():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - books TITLES - Available')
    print('-'*120)
    sql = 'select * from book where status = "available";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_weed_out_bookss():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - books TITLES - Weed Out')
    print('-'*120)
    sql = 'select * from book where status = "weed-out";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_stolen_bookss():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - books TITLES - Stolen')
    print('-'*120)
    sql = 'select * from book where status = "stolen";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_lost_bookss():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - books TITLES - lost')
    print('-'*120)
    sql = 'select * from book where status = "lost";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_member_list():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    print('\n REPORT - Members List ')
    print('-'*120)
    sql = 'select * from member'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_fine_collection():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    sql ='select sum(fine) from transaction where dor ="'+str(date.today())+'";'
    cursor.execute(sql)
    result = cursor.fetchone() #always return values in the form of tuple
    print('Fine collection')
    print('-'*120)
    print('Total fine collected Today :',result[0])
    print('\n\n\n')
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def report_menu():
    while True:
      print(' R E P O R T    M E N U ')
      print("\n1.  books List")
      print('\n2.  Member List')
      print('\n3.  Issued bookss')
      print('\n4.  Available bookss')
      print('\n5.  Weed out books')
      print('\n6.  Stolen books')
      print('\n7.  Lost books')
      print('\n8.  Fine Collection')
      print('\n9.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        reprot_books_list()
      if choice == 2:
        report_member_list()
      if choice == 3:
        report_issued_bookss()
      if choice == 4:
        report_available_bookss()
      if choice == 5:
        report_weed_out_bookss()
      if choice == 6:
        report_stolen_bookss()
      if choice == 7:
        report_lost_bookss()
      if choice == 8:
        report_fine_collection()
      if choice == 9:
        break


def change_books_status(status,books_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='VChintu2611')
    cursor = conn.cursor()
    sql = 'update books set status = "'+status +'" where id ='+books_id + ' and status ="available"'
    cursor.execute(sql)
    print('books status changed to ',status)
    print('\n\n\n')
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')

def special_menu():
    while True:
      print(' S P E C I A L     M E N U')
      print("\n1.  books Stolen")
      print('\n2.  books Lost')
      print('\n3.  books Weed out')
      print('\n4.  Return books')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      status=''
      if choice == 1:
         status ='stolen'
      if choice == 2:
         status = 'lost'
      if choice == 3:
         status = 'weed-out'
      if choice == 4:
         break
      books_id = input('Enter books id :')
      change_books_status(status,books_id)


def main_menu():
    while True:
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add bookss")
      print('\n2.  Add Member')
      print('\n3.  Modify books Information')
      print('\n4.  Modify Student Information')
      print('\n5.  Issue books')
      print('\n6.  Return books')
      print('\n7.  Search Meneu')
      print('\n8.  Report Menu')
      print('\n9.  Special Menu')
      print('\n0.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_books()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_books()
      if choice == 4:
        modify_member()
      if choice == 5:
        issue_books()
      if choice == 6:
        return_books()
      if choice == 7:
        search_menu()
      if choice == 8:
        report_menu()
      if choice == 9:
        special_menu()
      if choice == 0:
        break

if __name__ == "__main__":
    main_menu()
