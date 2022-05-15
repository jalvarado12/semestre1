#=============================================================================================================================================================
#                                                                          Modulos                                                                           #
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
#                                                               Caracteristicas de la ventana                                                                #
#=============================================================================================================================================================
ventana=t.Tk()#Crear ventana de tkinter
ventana.title("Fun Graphic")#Titulo de la ventana
ventana.geometry("900x800")#Tamaño de la ventana
style.use("fivethirtyeight")#Agregar un estilo a la grafica
fg=Figure()#Crea el recuadro de la grafica
ax=fg.add_subplot(111)#Contraer o alargar el recuadro(primer digito en el eje y, segundo digito en el eje x) del 1 al 9, desplazar con el tercer digito (de 1 a 6)
cv=FigureCanvasTkAgg(fg, ventana)#Crea contenedor donde va a estar la grafica
cv.get_tk_widget().pack(side=t.TOP, fill=t.BOTH, expand=1)#Expansión del contenedor
cv.draw() #Para que aparezcan las modificaciones al contenedor
tlb=NavigationToolbar2Tk(cv, ventana)#Importar iconos de navegación #toolbar
tlb.update()#Actualizar los iconos

#=============================================================================================================================================================
#                                                          Rangos y Funciones especiales a graficar                                                          #
#=============================================================================================================================================================
r1=False #Rango 1
r2=""#Rango 2
r3=""#Rango 3
function_np={"sin":"np.sin","cos":"np.cos", "sqrt":"np.sqrt", "exp":"np.exp", "log":"np.log", "abs":"np.abs"} #guardar las funciones especiales en un diccionario
#=============================================================================================================================================================
#                                                                       Graficadora                                                                          #
#=============================================================================================================================================================
def reemplazar(p): #Reemplaza la abreviación que usamos en las funciones especiales por su metodo para que funcionen al graficarlas
    for i in function_np:
        if i in p:
            p=p.replace(i, function_np[i])
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
            e_var.delete(0, len(e_var.get()))#Devuelve lo que esta dentro de la variable y la borra
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
#                                                                        Botones Y Barras                                                                    #
#=============================================================================================================================================================
ani=anim.FuncAnimation(fg, animate, interval=1000)
bo1=t.Button(ventana, text="graficar", command=represent)#Crear boton
e_func=t.Entry(ventana, width=60)#Crear espacio de entrada
e_var=t.Entry(ventana, width=20)#Crear entrada de variación
bo1.pack(side=t.BOTTOM)
e_var.pack(side=t.RIGHT)#Ubicar entrada de variación
e_func.pack(side=t.BOTTOM)#Ubicar el espacio

show()#Muestra la función ingresada sin necesidad de dar el rango de x
ventana.mainloop()#Hacer visible la ventana
