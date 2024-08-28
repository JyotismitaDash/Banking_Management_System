import cx_Oracle
from tkinter import messagebox

# Connecting to oracle database
con=cx_Oracle.connect("system/MAMA") # Enter your "userid/password" to connect with database
cursor=con.cursor()
def Insert(a,b,c,d,e):
    try:
        # First create a database for your data then insert into them
        bank_table = "create table bank_info(Name varchar2(15) not null,Pancard_no number(10) unique not null,Amount number(10) not null,Account_no number(15) primary key not null,Mobile_no number(11) not null)"
        cursor.execute(bank_table)

    except cx_Oracle.DatabaseError: 
        # if table is already exists then it come here and data inserted
        if(con):
            cursor.execute("insert into bank_info(Name,Pancard_no,Amount,Account_no,Mobile_no)values('"+a+"','"+b+"',"+c+",'"+d+"',"+e+")")
            con.commit()
            messagebox.showinfo("info","Your Account has been created successfully")
        else:
            print("Error in Connection")
            
    else:
        # if table first time created successfully then it come here and data inserted
        if(con):
            cursor.execute("insert into bank_info(Name,Pancard_no,Amount,Account_no,Mobile_no)values('"+a+"','"+b+"',"+c+",'"+d+"',"+e+")")
            con.commit()
            messagebox.showinfo("info","Your Account has been created successfully")
        else:
            print("Error in Connection")

def Credit(id,b):
    if(con):
        cursor=con.cursor()
        cursor.execute("select Amount from bank_info where Account_no='"+id+"'")
        result=cursor.fetchall()
        amount=result[0]
        print(amount[0])
        amount=int(amount[0])+int(b)
        print(amount)
        cursor.execute("update bank_info set Amount="+str(amount)+" where Account_no='"+id+"'")
        con.commit()
        return True
def Debit(id,b):
    if(con):
        cursor=con.cursor()
        cursor.execute("select Amount from bank_info where Account_no='"+id+"'")
        result=cursor.fetchall()
        amount=result[0]
        print(amount[0])
        amount=int(amount[0])-int(b)
        print(amount)
        cursor.execute("update bank_info set Amount="+str(amount)+" where Account_no='"+id+"'")
        con.commit()
        return True
def Show(id):
    if(con):
        cursor=con.cursor()
        cursor.execute("select *from bank_info  where Account_no='"+id+"'")
        data=cursor.fetchall()
        return data
