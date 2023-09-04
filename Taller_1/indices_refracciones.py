import numpy as np 
import matplotlib.pyplot as mp 
import pandas as po


def  lectura (archivo):
    o=open(archivo)
    r=o.readlines()
    o.close()
    lineas='\n'.join(r)
    datos=lineas.split('|')[1].split('-')[0].split('S')[0]
    valores = datos.split()  
    if "tabulated k" in lineas:
        datos1=lineas.split("tabulated k")[1].split("|")[1].split('S')[0]
        valores1=datos1.split()
        return valores,valores1
    else:
            return valores

def refraccion (archivo):
    lista_tuplas=[]
    x=lectura(archivo)
    a=len(x)
    if a>2:
    
        for i in range(0, a, 2):
            if i + 1 < a:
                tupla = (x[i], x[i + 1])
                lista_tuplas.append(tupla)
    
    elif a<=2:
        for j in x:
            
            z= [(j[i], j[i + 1]) for i in range(0, len(j), 2)]
            lista_tuplas.append(z)
    
    
    return lista_tuplas


"""
kapton=refraccion('.\Plasticos\French.yml')
NOA138=refraccion('.\Adhesivos_Ópticos\Iezzi.yml')
longitudes_de_ondakn=[]
longitudes_de_ondakk=[]
longitudes_de_ondan=[]
for i in kapton[0]:
    longitud=(i[0])
    longitudes_de_ondakn.append(longitud)
for i in kapton[1]:
        longitud=(i[0])
        longitudes_de_ondakk.append(longitud)
for i in NOA138:
    longitud=(i[0])
    longitudes_de_ondan.append(longitud)

indices_refracciónkn=[]
indices_refracciónkk=[]
indices_refracciónn=[]
for i in kapton[0]:
    indices=(i[1])
    indices_refracciónkn.append(indices) 
for i in kapton[1]:
    indices=(i[1])
    indices_refracciónkk.append(indices) 
for i in NOA138:
    indices=(i[1])
    indices_refracciónn.append(indices)

indices_refracciónk1=np.array(indices_refracciónkn,dtype=(float))
indices_refracciónk2=np.array(indices_refracciónkk,dtype=(float))
indices_refracciónna=np.array(indices_refracciónn,dtype=(float))
longitudes_de_ondak1=np.array(longitudes_de_ondakn,dtype=(float))
longitudes_de_ondak2=np.array(longitudes_de_ondakk,dtype=(float))
longitudes_de_ondana=np.array(longitudes_de_ondan,dtype=(float))
"""
def promedio(x):
    y=np.mean(x)
    return np.round(y,5)
def desviacion_estandar(x):
    y=np.std(x)
    return np.round(y,5)
"""
k=promedio(indices_refracciónk1)
kd=desviacion_estandar(indices_refracciónk1)
n=promedio(indices_refracciónk1)
nd=desviacion_estandar(indices_refracciónna)
k1=promedio(indices_refracciónk2)
kd1=desviacion_estandar(indices_refracciónk2)


fig,axs=mp.subplots(1,3,figsize=(20,5))
axs[0].plot(longitudes_de_ondak1,indices_refracciónk1,color="#d61ca8")
axs[0].set_ylabel('indices refraccion')
axs[0].set_xlabel('longitud de onda')
axs[0].set_title('Kapton n prom=' +str(k)+" error="+str(kd)) 

axs[1].plot(longitudes_de_ondak2,indices_refracciónk2,color="#d61ca8")
axs[1].set_ylabel('indices refraccion')
axs[1].set_xlabel('longitud de onda')
axs[1].set_title('Kapton k prom='+str(k1)+" error="+str(kd1)) 


axs[2].plot(longitudes_de_ondana,indices_refracciónna,color="#14e330")
axs[2].set_ylabel('indices refraccion')
axs[2].set_xlabel('longitud de onda')
axs[2].set_title('NOA1038 prom='+str(n)+" error="+str(nd))           

"""
def graficas(archivo):
    y=refraccion(archivo)
    t=len(y)
    if t>2:
        indicesrefraccion=[]
        longitudesondas=[]
        for i in y:
            indicesrefraccion.append(i[1])
            longitudesondas.append(i[0])
        indicesrefracciona=np.array(indicesrefraccion,dtype=(float))
        longitudesondasa=np.array(longitudesondas,dtype=(float))
        nombre=archivo.split(".")[1].split('\\')[-1].split("\\")[0] 
        r=promedio(indicesrefracciona)
        l=desviacion_estandar(indicesrefracciona)
        mp.plot(longitudesondasa,indicesrefracciona)
        mp.ylabel('indices refraccion')
        mp.xlabel('longitud de onda')
        mp.title(str(nombre)+" Prom " +str(r)+" Dev. est. "+str(l))
    elif t<=2:
        indicesrefraccion=[]
        longitudesondas=[]
        indicesrefraccion2=[]
        longitudesondas2=[]
        for i in y[0]:
            indicesrefraccion.append(i[1])
            longitudesondas.append(i[0])
        for i in y[1]:
            indicesrefraccion2.append(i[1])
            longitudesondas2.append(i[0])
        nombre=archivo.split(".")[0].split('\\')[-1].split("\\")[0] 
        indicesrefracciona=np.array(indicesrefraccion,dtype=(float))
        longitudesondasa=np.array(longitudesondas,dtype=(float))
        indicesrefraccion2a=np.array(indicesrefraccion2,dtype=(float))
        longitudesondas2a=np.array(longitudesondas2,dtype=(float))
        r=promedio(indicesrefracciona)
        l=desviacion_estandar(indicesrefracciona)
        r2=promedio(indicesrefraccion2a)
        l2=desviacion_estandar(indicesrefraccion2a)
        fig,axs=mp.subplots(1,2,figsize=(15,5))
        axs[0].plot(longitudesondasa,indicesrefracciona,color="#0ee8b9")
        axs[0].set_ylabel('indices refraccion')
        axs[0].set_xlabel('longitud de onda')
        axs[0].set_title(str(nombre)+ " n"+" Prom " +str(r)+" Dev. est. "+str(l))
        
        axs[1].plot(longitudesondas2a,indicesrefraccion2a,color="#0ee8b9")
        axs[1].set_ylabel('indices refraccion')
        axs[1].set_xlabel('longitud de onda')
        axs[1].set_title(str(nombre)+ " n"+" Prom " +str(r2)+" Dev. est. "+str(l2))
        
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
    return "gráficas guardadas con exito :D"
lista_elementos = po.read_csv('./indices_refraccion.csv')
lista_rutas_yml = './'+lista_elementos['Categoría']+'/'+lista_elementos['Material']+'.yml'

for f in lista_rutas_yml.values:
    graficas(f)
    

