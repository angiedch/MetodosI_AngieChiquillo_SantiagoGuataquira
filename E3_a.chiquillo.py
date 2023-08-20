# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 06:27:44 2021

@author: angie
"""
#Punto 1
def encontrar_tesoro(instrucciones:list) -> dict:
    x= 0
    y= 0
    
    for instruccion in instrucciones:
        for i in instruccion:
            paso= instruccion[i]
            
            if i== "B": 
                y-= paso
                
            elif i== "A":
                y+= paso
                
            elif i== "I":
                x-= paso
                
            elif i== "D":
                x+= paso
    dic={}
    if x > 0:
        dic["D"]= x
    elif x < 0:
        dic["I"]= x - (2*x)
    
    if y > 0:
        dic["A"]= y
    elif y < 0:
        dic["B"]= y - (2*y)
              
    return dic


#Punto 2
def estadísticas_por_liga(dataset:list, liga:str) -> dict:
    dic={}   
    
    for jugador in dataset:
        liga_1= jugador["liga"].lower()
        if liga.lower() == liga_1:
            lista_clubes=[]
        
            dic= {"liga": liga_1, "cantidad_jugadores": 0, "promedio_edad": 0, "promedio_overall": 0, "cantidad_clubes": 0, "clubes": lista_clubes}
        
            dic["cantidad_jugadores"]+= 1
            dic["promedio_edad"]+= jugador["edad"]
            dic["promedio_overall"]+= jugador["overall"]
            
            if jugador["club"] not in lista_clubes:
                lista_clubes.append(jugador["club"])
                dic["cantidad_clubes"]+= 1
            
    dic["promedio_edad"]= dic["promedio_edad"]/dic["cantidad_jugadores"]
    dic["promedio_overall"]= dic["promedio_overall"] / dic["cantidad_jugadores"]
    del dic["clubes"]
    
    return dic


#Punto 3
def transaccion_mayor_en_bloque(blockchain:list, numero_bloque:int) -> dict:
    dic_transaccion= None
    mayor= ""
    
    for bloque in blockchain:
        if bloque["numero_bloque"] == numero_bloque:
            for i in range(0, bloque["cantidad_transacciones"]):
                transaccion= bloque[i] 
                valor= float(transaccion["valor"])
                
                if transaccion["operacion"] == "transferencia": 
                    if valor > mayor or dic_transaccion== None:
                        mayor= valor
                        dic_transaccion= transaccion
                        
    return dic_transaccion





