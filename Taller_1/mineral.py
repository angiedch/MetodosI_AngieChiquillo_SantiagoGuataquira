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