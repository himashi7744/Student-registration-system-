from tkinter import *
from tkinter import messagebox
import mysql.connector


def Ok():
    studname = e1.get()
    coursename = e2.get()
    feee = e3.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="smschool")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO record (id,stname,course,fee) VALUES (%s, %s, %s, %s)"
        val = ("", studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("information", "Record inserted successfully...")


    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


root = Tk()
root.title("Student Registation")
root.geometry("300x200")
global e1
global e2
global e3

Label(root, text="Student Name").place(x=10, y=10)
Label(root, text="Course").place(x=10, y=40)
Label(root, text="Fee").place(x=10, y=80)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=80)

Button(root, text="Add", command=Ok, height=3, width=13).place(x=10, y=120)

root.mainloop()