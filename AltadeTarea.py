import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar

Tareas = []

global ventana
ventana = tk.Tk()
ventana.title("Ingresar Descripción")
# Crear una variable para almacenar la opción seleccionada
def RegistroDescripción():
    global Descripción
    Descripción = EntradaDescripción.get()
    if not Descripción.isalpha():
        # Mostrar mensaje de error
        messagebox.showerror(message="Error al subir. La descripción debe contener letras")
    else:
        global opcion
        opcion = variable_opcion.get()
        if opcion == "Pendiente":
            mensaje = "Has ingresado una Tarea Pendiente"
            VentanaCalendario()
            
            
        elif opcion == "En Progreso":
            mensaje = "Has ingresado una Tarea en Progreso"
            VentanaCalendario()
        else:
            mensaje = "No has seleccionado ninguna opción"
        messagebox.showinfo("Opción Seleccionada", mensaje)
    

def VentanaCalendario():
        global ventana2
        ventana2 = tk.Tk()
        ventana.destroy()
        ventana2.focus()
        ventana2.title("Calendario")
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        global calendario
        calendario = Calendar(ventana2, 
                              selectmode='day', 
                              year=2024, 
                              month=5, 
                              day=18,
                              locale='es',  # Configurar la localización a español
                            date_pattern='dd/mm/yyyy',  # Formato de fecha
                            monthnames=meses, 
                            daynames=dias)
        calendario.pack(pady=20)

# Crear el botón para seleccionar la fecha
        boton_seleccionar = tk.Button(ventana2, text="Seleccionar Fecha", command=mostrar_fecha)
        boton_seleccionar.pack(pady=20)
    

LabelDescripción = Label(ventana,text="Descripción")
LabelDescripción.pack()
EntradaDescripción = Entry(ventana)
EntradaDescripción.pack()

# Crear la ventana principal

variable_opcion = tk.StringVar(value="ninguna")
# Crear los botones de opción (radio buttons)
tk.Radiobutton(ventana, text="Pendiente", variable=variable_opcion, value="Pendiente").pack(anchor=tk.W)
tk.Radiobutton(ventana, text="En Progreso", variable=variable_opcion, value="En Progreso").pack(anchor=tk.W)
BotónVentana = tk.Button(ventana,text="Añadir Descripción",command = RegistroDescripción)
BotónVentana.pack()



fecha_seleccionada = None
def RegistroTarea():
    
    
    Tarea = ({"Descripción": Descripción,"Fecha de Vencimiento":fecha_seleccionada, "Estado": opcion})
    
    Tareas.append(Tarea)
    with open("Tareas.json", "w")as Archivo:
        json.dump(Tareas, Archivo, indent=6)
            
    ventana2.destroy()
def mostrar_fecha():
    global fecha_seleccionada
    fecha_seleccionada = calendario.get_date()
    messagebox.showinfo("Fecha Seleccionada", f"Has seleccionado: {fecha_seleccionada}")
    RegistroTarea()
    

# Crear la ventana principal

# Iniciar el bucle principal de la aplicación
ventana.mainloop()


    
