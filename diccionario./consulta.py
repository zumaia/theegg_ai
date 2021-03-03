# -*- coding: utf-8 -*-
import sqlite3 as db
import tkinter as tk
import tkinter.messagebox as mensaje


def sqlite(var):
    conexion = db.connect("db_diccionario.db")
    cursor = conexion.cursor()
    f = cursor.execute("SELECT * FROM diccionario WHERE palabra = '%s'" % (var))
    fila = f.fetchone()

    if (fila != None):

        # widgets
        titulo_ = tk.Label(w, text="Resultados:")
        contenedor1 = tk.Label(w, text="1. id: %s" % fila[0])
        contenedor2 = tk.Label(w, text="2. palabra: %s" % fila[1], bg="#EAEDF5")
        contenedor3 = tk.Label(w, text="3. descripcion: %s" % fila[2])
        contenedor4 = tk.Label(w, text="4. tarea: %s" % fila[3])
        contenedor5 = tk.Label(w, text="5. url: %s" % fila[4])
        contenedor6 = tk.Label(w, text="6. relaciones: %s" % fila[5])

        # distribución
        titulo_.grid(row=4, column=2, pady=5, sticky="W")
        contenedor1.grid(row=5, column=2, sticky="W")
        contenedor2.grid(row=6, column=2, sticky="W")
        contenedor3.grid(row=7, column=2, rowspan=3, sticky=tk.W)
        contenedor4.grid(row=10, column=2, sticky="W")
        contenedor5.grid(row=11, column=2, sticky="W")
        contenedor6.grid(row=12, column=2, sticky="W")
    else:
        mensaje.showerror("mensaje", "Esa palabra no está en el diccionario")


def consultar():
    valor = var1.get().upper()
    sqlite(valor)


# ventana principal
w = tk.Tk()

# propiedades de la ventana
w.title("Consultas Diccionario")
w.geometry("1000x300")
w.resizable(True, True)

# variables

var1 = tk.StringVar()

# wigets
titulo = tk.Label(w, text="Consulta Diccionario", anchor="n", font="verdana 10 bold")
etiqueta = tk.Label(w, text="Palabra:")
entrada = tk.Entry(w, width=20, textvariable=var1)
boton = tk.Button(w, text="Consultar", command=consultar, bg='green')

# distribución
titulo.grid(row=0, column=1, padx=10)
etiqueta.grid(row=1, column=1, padx=5)
entrada.grid(row=2, column=1, padx=5)
boton.grid(row=3, column=1, pady=10)
w.mainloop()