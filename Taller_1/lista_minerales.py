
import matplotlib.pyplot as plt
import numpy as np

#Clase Mineral
class Mineral:
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
        self.specific_gravity= self.specific_gravity*1000
        print(self.specific_gravity)
        
    def mostrar_color (self):
        rgb = tuple(int(self[i:i+2], 16) for i in (1, 3, 5))
        print(rgb)
        color = np.full((1, 1, 3), rgb)
    
        plt.imshow(color)
        plt.axis('off')
        plt.show()
        
    def imprimir_dureza (self):
        
        print(self.dureza)
        print(self.rompimiento_por_fractura)
        print(self.sistema_cristalino)



#Arreglo de minerales
def arreglo_minerales(archivo):
    with open(archivo,encoding="utf-8") as file:
        cont= file.read()

    minerales=[]
    
    renglones=cont.split("\n")[1:]
    
    for i in renglones:
        renglon= i.split("\t")
        minerales.append(Mineral(*renglon))

    return minerales
todos = arreglo_minerales('minerales.txt')


#Programa de Minerales
promedio_densidad= 0
silicatos=[]
for t in todos:
    promedio_densidad+= t.specific_gravity
    if t.silicato():
        silicatos.append(t)

promedio_densidad/=len(todos)
print("El promedio de la densidad de los silicatos es", str(promedio_densidad), "kg/m^3")

print("El número de minerales silicatos en la lista es", str(len(silicatos)), ".")
    