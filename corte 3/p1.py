# -*- coding: utf-8 -*-
"""
Created on Sat May 14 07:28:33 2022

@author: Tina
"""


class Persona:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname=lastname
        self.age=age
        self.id=0
        
    def info(self):
        print(self.name+" "+self.lastname+" , "+str(self.age))


class Integrante(Persona):
    def asignar_id(self,id):
        self.id=id
    def __str__(self):
        line = """
            Nombre:{0}
            Apellido:{1}
            Edad:{2}
            Identificación:{3}
    """.format(self.name,self.lastname,self.age,self.id)
        return  line
    def modif_Edad(self,n_age):
        self.age=n_age
    
class Grupo:
    def __init__(self,nombre,integrantes):
        self.nombre=nombre
        self.integrantes=integrantes
        self.listado=[]
    def agregar_integrante(self,integrante):
        if len(self.listado)<self.integrantes:
            self.listado.append(integrante)
        else:
            print("cupo no disponible")
    def buscar_mayor_menor(self,bus):
        elemento=self.listado[0]
        if(bus=="menor"):
            for a in self.listado:
                if(elemento.age>a.age):
                    elemento=a
        elif(bus=="mayor"):
            for a in self.listado:
                if(elemento.age<a.age):
                    elemento=a
        print(elemento.name+" "+elemento.lastname)
        
    def __str__(self):
        imp=" "
        for a in self.listado:
            line = """
                Nombre:{0}
                Apellido:{1}
                Edad:{2}
                Identificación:{3}
                """.format(a.name,a.lastname,a.age,a.id)
            imp=imp+line
        return imp
        
        


    
#__Pruba persona_______________
juan=Persona("Juan", "Perez", 26)
juan.info()

#____Prueba integrante_______________
pedro=Integrante("pedro","Arias",93)
pedro.asignar_id(233)
print(pedro)
pedro.modif_Edad(34)
print(pedro)

#_____________________Grupo

grp = Grupo("prueba", 2)
grp.agregar_integrante(pedro)
grp.agregar_integrante(juan)
grp.buscar_mayor_menor("mayor")
print(grp)