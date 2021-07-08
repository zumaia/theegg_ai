from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkmessagebox
import connection

root = Tk()
root.title("Añadimos datos al Diccionario")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(True, True)


# ==================================METHODS============================================

def insertardata():
    if (
        PALABRA.get() == ""
        or DESCRIPCION.get() == ""
        or TAREA.get() == ""
        or URL.get() == ""
        or RELACIONES.get() == ""
    ):
        txt_result.config(text="Por favor, completa los datos requeridos!", fg="red")
    else:
        connection.database()
        connection.cursor.execute(
            "INSERT INTO `diccionario` (palabra, descripcion, tarea, url, relaciones) VALUES(?, ?, ?, ?, ?)",
            (
                str(PALABRA.get()).upper(),
                str(DESCRIPCION.get()).title(),
                str(TAREA.get()).lower(),
                str(URL.get()).lower(),
                str(RELACIONES.get()).lower(),
            ),
        )
        connection.conn.commit()
        PALABRA.set("")
        DESCRIPCION.set("")
        TAREA.set("")
        URL.set("")
        RELACIONES.set("")
        connection.cursor.close()
        connection.conn.close()
        txt_result.config(text="Introduce los datos!", fg="blue")

        displaydata()


def displaydata():
    """
    Función que muestra ordenado de manera alfabetica los datos introducidos por palabra
    """
    tree.delete(*tree.get_children())
    connection.database()
    connection.cursor.execute("SELECT * FROM `diccionario` ORDER BY `palabra` ASC")
    fetch = connection.cursor.fetchall()
    for data in fetch:
        tree.insert("", "end", values=(data[1], data[2], data[3], data[4], data[5]))
    connection.cursor.close()
    connection.conn.close()


def salida():
    """
    Función destinada a salirse de la aplicación y advertir de la salida de la misma
    """
    result = tkmessagebox.askquestion(
        "Introduce los datos", "Estas seguro que quieres salir?", icon="warning"
    )
    if result == "yes":
        root.destroy()
        exit()


# ==================================VARIABLES==========================================
PALABRA = StringVar()
DESCRIPCION = StringVar()
TAREA = StringVar()
URL = StringVar()
RELACIONES = StringVar()

# ==================================FRAME==============================================
Top = Frame(root, width=1000, height=50, bd=8, relief="raise", bg='white')
Top.pack(side=TOP)
Left = Frame(root, width=600, height=500, bd=8, relief="raise", bg='white')
Left.pack(side=LEFT)
Right = Frame(root, width=400, height=500, bd=8, relief="raise", bg='white')
Right.pack(side=RIGHT)
Forms = Frame(Right, width=400, height=450, bg='white')
Forms.pack(side=TOP)
Buttons = Frame(Right, width=300, height=80, bd=8, relief="raise", bg='white')
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)

# ==================================LABEL WIDGET=======================================
txt_title = Label(
    Top, width=1200, font=("arial", 24), text="Diccionario - Introducción de datos.", bg='white'
)
txt_title.pack()
txt_palabra = Label(Forms, text="Palabra:", font=("arial", 16), bd=15, bg='white')
txt_palabra.grid(row=0, stick="e")
txt_descripcion = Label(Forms, text="Descripcion:", font=("arial", 16), bd=15, bg='white')
txt_descripcion.grid(row=1, stick="e")
txt_tarea = Label(Forms, text="Tarea:", font=("arial", 16), bd=15, bg='white')
txt_tarea.grid(row=2, stick="e")
txt_url = Label(Forms, text="Url:", font=("arial", 16), bd=15, bg='white')
txt_url.grid(row=3, stick="e")
txt_relaciones = Label(Forms, text="Relaciones:", font=("arial", 16), bd=15, bg='white')
txt_relaciones.grid(row=4, stick="e")
txt_result = Label(Buttons, bg='white')
txt_result.pack(side=TOP)

# ==================================ENTRY WIDGET=======================================
palabra = Entry(Forms, textvariable=PALABRA, width=60, justify=LEFT)
palabra.grid(row=0, column=1)
descripcion = Entry(Forms, textvariable=DESCRIPCION, width=60)
descripcion.grid(row=1, column=1)
tarea = Entry(Forms, textvariable=TAREA, width=60)
tarea.grid(row=2, column=1)
url = Entry(Forms, textvariable=URL, width=60)
url.grid(row=3, column=1)
relaciones = Entry(Forms, textvariable=RELACIONES, width=60)
relaciones.grid(row=4, column=1)

# ==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Insertar", command=insertardata, bg='green')
btn_create.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Salir", command=salida, bg='red')
btn_exit.pack(side=LEFT)

# ==================================LIST WIDGET========================================
scrollbary = Scrollbar(Left, orient=VERTICAL)
scrollbarx = Scrollbar(Left, orient=HORIZONTAL)
tree = ttk.Treeview(
    Left,
    columns=("palabra", "descripcion", "tarea", "url", "relaciones"),
    selectmode="extended",
    height=500,
    yscrollcommand=scrollbary.set,
    xscrollcommand=scrollbarx.set,
)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading("palabra", text="palabra", anchor=E)
tree.heading("descripcion", text="descripcion", anchor=W)
tree.heading("tarea", text="tarea", anchor=W)
tree.heading("url", text="url", anchor=W)
tree.heading("relaciones", text="relaciones", anchor=W)
tree.column("#0", stretch=NO, minwidth=0, width=0)
tree.column("#1", stretch=NO, minwidth=0, width=60)
tree.column("#2", stretch=NO, minwidth=0, width=200)
tree.column("#3", stretch=NO, minwidth=0, width=30)
tree.column("#4", stretch=NO, minwidth=0, width=150)
tree.column("#5", stretch=NO, minwidth=0, width=80)
tree.pack()

# ==================================INITIALIZATION=====================================
displaydata()

if __name__ == "__main__":
    root.mainloop()
