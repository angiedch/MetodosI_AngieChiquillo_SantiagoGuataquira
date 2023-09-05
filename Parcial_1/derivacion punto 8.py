# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:11:53 2023

@author: santi
"""



import os
c='.Taller_1\Plasticos\French.yml'
o=open(c)
r=o.readlines()
o.close()
lineas='\n'.join(r)
datos=lineas.split('|')[1].split('-')[0].split('S')[0]
print(datos)  
# Directorio que contiene los archivos .yml
"""directorio = '.Taller_1\Plasticos\V


archivos = os.listdir(directorio)
# Iterar a través de los archivos y procesar los que tienen extensión .yml
for archivo in archivos:
    if archivo.endswith(".yml"):
        ruta_completa = os.path.join(directorio, archivo)

"""