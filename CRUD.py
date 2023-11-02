import tkinter
# CRUD:CREATE, RETRIEVE,UPDATE,DELETE

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listbox.selection()[0]
    select = listbox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['empname'])
    e3.insert(0, select['mobile'])
    e4.insert(0, select['salary'])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="samiksha_pyt70")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO registration (id,empname,mobile,salary) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="samiksha_pyt70")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update registration set empname= $s, mobile= %s, salary=%s where id=%s"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record updated successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    try:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="samiksha_pyt70")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,empname,mobile,salary FROM registration")
        record = mycursor.fetchall()
        print(record)

        for i, (id, stname, course, fee) in enumerate(record, start=1):
            listbox.insert("", "end", values=(id, stname, course, fee))

        mysqldb.close()
    except Exception as e:
        print(e)


root = tk.Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4


def delete():
    studid = e1.get()

    try:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="samiksha_pyt70")
        mycursor = mysqldb.cursor()
        sql = "DELETE FROM registration WHERE id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record deleted successfully...")
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def search():
    studid = e1.get()

    try:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="samiksha_pyt70")
        mycursor = mysqldb.cursor()
        sql = "Select * from WHERE id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record searched successfully...")
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


tk.Label(root, text="Employee Registration", fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Employee ID").place(x=10, y=10)
Label(root, text="Employee Name").place(x=10, y=40)
Label(root, text="Mobile").place(x=10, y=70)
Label(root, text="Salary").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="Update", command=update, height=3, width=13).place(x=160, y=130)
Button(root, text="Delete", command=delete, height=3, width=13).place(x=280, y=130)
Button(root, text="Search", command=search, height=3, width=13).place(x=400, y=130)

cols = ('id', 'empname', 'mobile', 'salary')
listbox = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=2)
    listbox.place(x=10, y=200)
show()
listbox.bind('<Double-Button-1>', GetValue)  # double click on blue line highlight for getting value
root.mainloop()