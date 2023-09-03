#Clase Minerales
import matplotlib.pyplot as plt
import numpy as np

class Minerales:
    def __init__ (self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = float(dureza)
        self.lustre = float(lustre)
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = float(specific_gravity)
        
    def silicato (self):
        
        if "Si" and "O" in self.composicion:
            print("El mineral es un silicato")    
        else:
            print("El mineral no es un silicato")
            
    def densidad (self):
        
        print(f'{self.specific_gravity} g/cm^3')
        
    def mostrar_color (self):
        rgb = tuple(int(self[i:i+2], 16) for i in (1, 3, 5))
        print(rgb)
        color = np.full((50, 50, 3), rgb)
    
        plt.imshow(color)
        plt.axis('off')
        plt.show()
        
    def imprimir_datos (self):
        
        print(f'La dureza del mineral es {self.dureza}.')
        print(f'El rompimiento del mineral es {self.rompimiento_por_fractura}.')
        print(f'El sistema cristalino del mineral es {self.sistema_cristalino}.')