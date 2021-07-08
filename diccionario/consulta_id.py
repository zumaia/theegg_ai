import sqlite3
my_conn = sqlite3.connect('db_diccionario.db')
###### end of connection ####

##### tkinter window ######
import tkinter as tk
from tkinter import *
####### end of connection ####

my_w = tk.Tk()
my_w.geometry("600x400")

# add one Label
l1 = tk.Label(my_w,  text='Inserta la palabra', width= 25)
l1.grid(row=2,column=1)

# add one text box
t1 = tk.Text(my_w,  height=1, width=20, bg='white')
t1.grid(row=2,column=2)

b1 = tk.Button(my_w, text='Muestra los detalles', width=15, bg='green',
    command=lambda: my_details(t1.get('1.0', END)))
b1.grid(row=2,column=4)

my_str = tk.StringVar()
# add one Label
l2 = tk.Label(my_w, textvariable=my_str, height=4, width=60, fg='red')
l2.grid(row=6,column=1,columnspan=5)

my_str.set("Salida")

def my_details(palabra):
    try:
        val = int(palabra)
        try:
            q="SELECT * FROM diccionario WHERE mem_id = "+palabra
            my_cursor=my_conn.execute(q)
            data_row=my_cursor.fetchone()
            my_str.set(data_row)
        except sqlite3.Error as my_error:
            print("error: ", my_error)
    except:
        my_str.set("Revisa la entrada")
my_w.mainloop()