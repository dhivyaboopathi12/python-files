import mysql.connector 
from tabulate import tabulate

con = mysql.connector.connect(host='localhost',user='root',password='',database='test_user')
res = con.cursor()
def insert(name,age,address):
    sql = "insert into user(name,age,address) values(%s,%s,%s)"
    u = (name,age,address)
    res.execute(sql,u)
    con.commit() 
    print("Added new users!!!")   
def update(name,age,address,id):
    sql = "update user set name=%s,age=%s,address=%s where id =%s"
    u = (name,age,address,id)
    res.execute(sql,u)
    con.commit()
    print("Data updated!!!")
def delete(id):
    res.execute("delete from user where id = %s",(id,))
    con.commit()
def select():            
   res.execute("select * from user;")
   r = res.fetchall()
   print(tabulate(r,headers=['ID','NAME','AGE','ADDRESS']))
while True:
    print("Enter 1 for Add new record" + "\n" +
          "Enter 2 for Updating records" + "\n" +
          "Enter 3 for Deleting Records" + "\n" +
           "Enter 4 to view all the records" +"\n"+
           "Enter 5 to exist")
    ch = int(input("enter your choice:")) 
    if ch == 1:
        print("Adding new entry..!!")
        name = input("Enter name")
        age = input("enter age:")
        address = input("enter addrss")
        insert(name,age,address)
    elif ch == 2:
        print("Updating value :")
        id = input("enter id :")
        name = input("Enter name")
        age = input("enter age:")
        address = input("enter addrss")
        update(name,age,address,id)
    elif ch == 3:
        print("Deleting record: ")
        id = input("Enter id")
        delete(id)
    elif ch == 4:
        print("Viewing all record..:")
        select()
    elif ch == 5:
        print("Thank you..!!! :)") 
        break   
    else:
        print("**Invalid message**")  
        
con.close()        
          
                   