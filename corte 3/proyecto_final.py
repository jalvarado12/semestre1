#=============================================================================================================================================================
#                                       modulos
#=============================================================================================================================================================
import tkinter as t
from tkinter import messagebox
from matplotlib.pyplot import *
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from math import*
import math
#=============================================================================================================================================================
#                                       caracteristicas de la ventana
#=============================================================================================================================================================
ventana=t.Tk()#crear ventana de tkinter
ventana.title("Fun Graphic")#titulo de la ventana
ventana.geometry("900x800")#tamaño de la ventana
style.use("fivethirtyeight")#agregar un estilo al contenedor
fg=Figure()#crear una figura
ax=fg.add_subplot(111)#crear eje x
cv=FigureCanvasTkAgg(fg, ventana)#crea contenedor donde va a estar la grafica
cv.draw()
cv.get_tk_widget().pack(side=t.TOP, fill=t.BOTH, expand=1)#expansión del contenedor
tlb=NavigationToolbar2Tk(cv, ventana)#importar iconos de navegación #toolbar
tlb.update()
cv.get_tk_widget().pack(side=t.TOP, fill=t.BOTH, expand=1)
#=============================================================================================================================================================
#                                       rangos y funciones a graficar
#=============================================================================================================================================================
r1=False #rango1
r2=""#rango2
r3=""#rango3
fun={"sin":"np.sin","cos":"np.cos", "sqrt":"np.sqrt", "exp":"np.exp", "log":"np.log"} #guardar las funciones en un diccionario
#=============================================================================================================================================================
#                                       funciones
#=============================================================================================================================================================
def reemplazar(p):
    for i in fun:
        if i in p:
            p=p.replace(i, fun[i])
    return p
    
def animate(i):
    global r1
    global r2
    if r1==True:
        try:
            min=float(r3[0]);max=float(r3[1])
            if min<max:
                x=np.arange(min, max, 0.01)
                r2=[min, max]
            else:
                r1=False
        except:
            messagebox.showwarning("el rango es incorrecto")
            r1=False
            e_var.delete(0, len(e_var.get()))#devuelve lo que esta dentro de la variable y la borra
    else:
        if r2!="":
         x=np.arange(r2[0], r2[1], 0.01)   
        else:
          x=np.arange(0,10,0.01)
    try:
        sl=eval(graf_dt)#evaluar los datos ingresados
        ax.clear()
        ax.plot(x, sl)
    except:
        ax.plot()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")
    ani.event_source.stop()#detener el evento
def represent():
    global graf_dt
    global r3
    global r1
    t_ori=e_func.get()
    if e_var.get()!="":
        rann=e_var.get()
        r3=rann.split(",")#separar el rango
        r1=True
    graf_dt=reemplazar(t_ori)
    ani.event_source.start()
#=============================================================================================================================================================
#                                       ventanas
#=============================================================================================================================================================
ani=anim.FuncAnimation(fg, animate, interval=1000)
show()
bo1=t.Button(ventana, text="graficar", command=represent)#crear boton
e_func=t.Entry(ventana, width=60)#crear espacio de entrada
e_var=t.Entry(ventana, width=20)#crear entrada de variación
bo1.pack(side=t.BOTTOM)
e_var.pack(side=t.RIGHT)#ubicar entrada de variación
e_func.pack(side=t.BOTTOM)#ubicar el espacio


ventana.mainloop()#Hacer que la ventana cierre bien
