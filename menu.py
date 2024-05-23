import tkinter as tk

def opcion1():
    print("Has seleccionado la opción 1")

def opcion2():
    print("Has seleccionado la opción 2")

def opcion3():
    print("Has seleccionado la opción 3")

root = tk.Tk()
root.title("Menú en Python")

menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu)
menu.add_cascade(label="Opciones", menu=submenu)
submenu.add_command(label="Opción 1", command=opcion1)
submenu.add_command(label="Opción 2", command=opcion2)
submenu.add_command(label="Opción 3", command=opcion3)

root.mainloop()