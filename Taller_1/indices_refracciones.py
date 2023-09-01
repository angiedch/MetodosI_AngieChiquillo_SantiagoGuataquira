import numpy as np 
import matplotlib.pyplot as mp 


c=open('.\Plasticos\French.yml')
x= c.readlines()
c.close()

def refraccion (archivo):
    o=open(archivo)
    r=o.readlines()
    o.close()
    lineas='\n'.join(r)
    datos=lineas.split('|')[1].split('-')[0].split('S')[0]
    lista_tuplas=[]
    valores = datos.split()  
    a = len(valores)

    for i in range(0, a, 2):
        if i + 1 < a:
            tupla = (valores[i], valores[i + 1])
            lista_tuplas.append(tupla)

    return lista_tuplas

kapton=refraccion('.\Plasticos\French.yml')
NOA138=refraccion('.\Adhesivos_Ópticos\Iezzi.yml')
longitudes_de_ondak=[]
longitudes_de_ondan=[]
for i in kapton:
    longitud=(i[0])
    longitudes_de_ondak.append(longitud)
for i in NOA138:
    longitud=(i[0])
    longitudes_de_ondan.append(longitud)
indices_refracciónk=[]
indices_refracciónn=[]
for i in kapton:
    indices=(i[1])
    indices_refracciónk.append(indices) 
for i in NOA138:
    indices=(i[1])
    indices_refracciónn.append(indices) 
indices_refracciónka=np.array(indices_refracciónk,dtype=(np.float))
indices_refracciónna=np.array(indices_refracciónn,dtype=(np.float))
print(indices_refracciónka)
def promedio(x):
    return np.mean(x)
def desviacion_estandar(x):
    return np.std(x)

  
fig,axs=mp.subplots(1,2)

axs[0].plot(longitudes_de_ondak,indices_refracciónk)
axs[0].set_ylabel('indices refraccion')
axs[0].set_xlabel('longitud de onda')
axs[0].set_xticks([])
axs[0].set_yticks([])
axs[0].set_title('Krapton')

axs[1].plot(longitudes_de_ondan,indices_refracciónn)
axs[1].set_ylabel('indices refraccion')
axs[1].set_xlabel('longitud de onda')
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].set_title('NOA1038')            



