#Clase Minerales
import matplotlib.pyplot as plt
import numpy as np

class Minerales:
    def __init__ (self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = float(dureza)
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = float(specific_gravity)
        
    def silicato (self):
        
        return ("Si" in self.composicion) and ("O" in self.composicion)
            
    def densidad (self):
    #En unidades SI
        print(f'{self.specific_gravity} g/cm^3')
        
    def mostrar_color (self):
        rgb = tuple(int(self[i:i+2], 16) for i in (1, 3, 5))
        print(rgb)
        color = np.full((50, 50, 3), rgb)
    
        plt.imshow(color)
        plt.axis('off')
        plt.show()
        
    def imprimir_dureza (self):
        
        print(self.dureza)
        print(self.rompimiento_por_fractura)
        print(self.sistema_cristalino)

#Diccionario de minerales
def arreglo_minerales(archivo):
    with open(archivo,encoding="utf-8") as file:
        cont= file.read()

    mineral=[]
    
    renglones=cont.split("\n")[1:]
    
    for i in renglones:
        renglon= i.split("\t")
        mineral.append(Minerales(*renglon))
        
    #for i in mineral:
    #    if i != mineral[0]:
    #        for j in  i:
    #            if j==i[0]:
    #                arreglo[j] = []
    #                i.remove(j)
    #                min= j
    #            else:
    #                None
                
    #            arreglo[min]=i
                 
    return mineral
todos = arreglo_minerales('minerales.txt')

promedio_densidad= 0
silicatos=[]
for t in todos:
    promedio_densidad+= t.specific_gravity
    if t.silicato():
        silicatos.append(t)

promedio_densidad/= len(todos)
print(promedio_densidad)
print(len(silicatos))
#print(t.nombre, t.silicato())
    
#Programa Minerales

#Cantidad de silicatos
def cantidad_silicatos (lista):
    
    cant= 0
    for i in lista.values():
        for j in i:
            if j == i[3]:
                if "Si" and "O" in j:
                    cant+=1
                else:
                    None
            else:
                None
    return cant        

#Densidad promedio de los minerales   
def densidad_promedio(lista):
    
    suma= 0 
    cantidad= 0
    for i in lista.values():
        for j in i:
            if j == i[5]:
                suma+= float(j)
                cantidad+= 1
                
    media= suma/ cantidad
    return media 

#CONSOLA del programa
print()
