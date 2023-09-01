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

def promedio(x):
    y=np.mean(x)
    return np.round(y,2)
def desviacion_estandar(x):
    y=np.std(x)
    return np.round(y,2)
k=promedio(indices_refracciónka)
kd=desviacion_estandar(indices_refracciónka)
n=promedio(indices_refracciónka)
fig,axs=mp.subplots(1,3)
axs[0].plot(longitudes_de_ondak,indices_refracciónk)
axs[0].set_ylabel('indices refraccion')
axs[0].set_xlabel('longitud de onda')
axs[0].set_xticks([])
axs[0].set_yticks([])
axs[0].set_title('Krapton'+ " promedio"+ str(kd))

axs[1].plot(longitudes_de_ondan,indices_refracciónn)
axs[1].set_ylabel('indices refraccion')
axs[1].set_xlabel('longitud de onda')
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].set_title('NOA1038')            


def graficas(archivo):
    y=refraccion(archivo)
    indicesrefraccion=[]
    longitudesondas=[]
    for i in y:
        indicesrefraccion.append(i[1])
        longitudesondas.append(i[0])
    indicesrefracciona=np.array(indicesrefraccion,dtype=(float))
    longitudesondasa=np.array(longitudesondas,dtype=(float))
    nombre=archivo.split('\\')[-1].split("\\")[0] 
    #r=promedio(indicesrefracciona)
    #l=desviacion_estandar(indicesrefracciona)
    axs[2].plot(longitudesondasa,indicesrefracciona)
    axs[2].set_ylabel('indices refraccion')
    axs[2].set_xlabel('longitud de onda')
    axs[2].set_xticks([])
    axs[2].set_yticks([])
    axs[2].set_title(str(nombre))
    if "Vidrio" in archivo:
        guardargrafica=(".\Vidrio"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Plasticos" in archivo:
        guardargrafica=(".\plasticos"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Mezclas" in archivo:
        guardargrafica=(".\Mezclas"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Materia_Orgánica" in archivo:
        guardargrafica=(".\Materia_Orgánica"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Materia_Inorgánica" in archivo:
        guardargrafica=(".\Materia_Inorgánica"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Exotico" in archivo:
        guardargrafica=(".\Exotico"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Combustible" in archivo:
        guardargrafica=(".\Combustible"+"\\"+"grafica" + str(nombre)+".jpg")
    elif "Adhesivos_Ópticos" in archivo:
        guardargrafica=(".\Adhesivos_Ópticos"+"\\"+"grafica" + str(nombre)+".jpg")
        
    
    mp.savefig(guardargrafica)
    mp.show()
    return "gráficas guardadas con exito :D"

print(graficas('.\Plasticos\French.yml'))