# r recargar, v pagar viaje, s balance, x salir
from queue import Queue as cola

def verificar_transacciones(seq:str)->int:

    saldo_final:int=0
    los_que_restan:int=len(seq)
    long:int=len(seq)
    j:int=0
    for i in range(long):
        j+=1
        if seq[i]=="x" and los_que_restan==long:
            los_que_restan=-(j-long)


    for i in range(long-(los_que_restan)):
        if seq[i] == "v" and saldo_final>=56:
            saldo_final-=56

        if seq[i] == "r":
            saldo_final+=350


    return saldo_final

def valor_minimo(seq:list[(float,float)])->float:
    minimo:float=seq[0][0]
    for i in seq:
        if i[0]<minimo:
            minimo=i[0]
    return minimo

def minimo(seq:list[int,float])->float:
    minimo:float=seq[0][1]
    for tupla in seq:
        if tupla[1]<minimo:
            minimo=tupla[1]
    return minimo

def maximo(seq:list[(int,float)])->float:
    maximo:float=seq[0][1]
    for tupla in seq:
        if tupla[1]>maximo:
            maximo=tupla[1]
    return maximo

def valores_extremos(portafolio:dict[str,(int,float)])->dict[str,(float,float)]:
    diccionario:dict[str,(float,float)]={}
    for empresa,valor_diario in portafolio.items():
        diccionario[empresa]=(minimo((valor_diario)),maximo((valor_diario)))
    return diccionario
  

def hay_repetidos(lista:list[int])->bool:
    nueva_lista:list[int]=[]
    res:bool=False
    for elemento in lista:
        if elemento in nueva_lista and elemento != 0:
            res=True
        nueva_lista.append(elemento)
    return res

def es_sudoku_valido(sudoku:list[list[int]])->bool:
    res:bool=True
    i:int=0

    for fila in sudoku:
        if hay_repetidos(fila)==True:
            res=False
    
    while i < 9:
        lista_nueva:list[int]=[]
        for fila in sudoku:
            lista_nueva.append(fila[i])
        if hay_repetidos(lista_nueva)==True:
            res=False
        i+=1
    return res      

    

#OTRO PARCIAL

# ej1
def reordenar_fila_priorizando_vips(fila_clientes: cola[(str,str)]) -> cola[str]:
    vips_adelante = cola()
    no_vips = cola()

    # Procesar cada elemento en la cola original
    while not fila_clientes.empty():
        cliente = fila_clientes.get()
        if cliente[1].lower() == "vip":
            vips_adelante.put(cliente[0])
        else:
            no_vips.put(cliente[0])
    
    # Añadir los no VIPs a la cola vips_adelante
    while not no_vips.empty():
        vips_adelante.put(no_vips.get())
    
    return vips_adelante
    

    return vips_adelante

def imprimir_cola(cola):
    while not cola.empty():
        print(cola.get())

# Testear la función
def test_reordenar_fila_priorizando_vips():
    # Crear una instancia de Queue y llenarla con datos de prueba
    fila_clientes = cola()
    fila_clientes.put(("Alice", "vip"))
    fila_clientes.put(("Bob", "normal"))
    fila_clientes.put(("Charlie", "vip"))
    fila_clientes.put(("David", "normal"))
    
    # Llamar a la función y obtener la cola reordenada
    cola_reordenada = reordenar_fila_priorizando_vips(fila_clientes)
    
    # Imprimir la cola reordenada
    imprimir_cola(cola_reordenada)

# Ejecutar el test


# ej 2


def comparar(estrategia_1:str,estrategia_2:str)->str:
    res:str=""
    if estrategia_1 == "me la banco y no me desvio" and estrategia_2 == "me la banco y no me desvio":
        res="chocaron"
    if estrategia_1 == "me desvio siempre" and estrategia_2 == "me desvio siempre":
        res="ambos desvian"
    if estrategia_1 == "me desvio siempre" and estrategia_2 == "me la banco y no me desvio":
        res="gano estrategia_2"
    if estrategia_2 == "me desvio siempre" and estrategia_1 == "me la banco y no me desvio":
        res="gano estrategia_1"
    return res

def torneo_de_gallinas(estrategias:dict[str,str])->dict[str,int]:
    diccionario:dict[str,int]={}
    long_d:int=len(diccionario)
    i:int=0
    lista_estrategias:list[str]=[]
    lista_nombres:list[str]=[]

    for nombre in estrategias.keys():
        diccionario[nombre]=0 #adjudico 0 ptos y luego veo si sumo o resto
        lista_nombres.append(nombre)

    for value in estrategias.values():
        lista_estrategias.append(value)

    for nombre, estrategia in estrategias.items():
        if len(lista_estrategias)==1:
            break
        for j in range(1,len(lista_estrategias)):
                
                if comparar(estrategia,lista_estrategias[j]) == "chocaron":
                    diccionario[nombre]-=5
                    diccionario[lista_nombres[j]]-=5   

                if comparar(estrategia,lista_estrategias[j]) == "ambos desvian":
                    diccionario[nombre]-=10
                    diccionario[lista_nombres[j]]-=10
                
                if comparar(estrategia,lista_estrategias[j]) == "gano estrategia_1":
                    diccionario[nombre]+=10
                    diccionario[lista_nombres[j]]-=15

                if comparar(estrategia,lista_estrategias[j]) == "gano estrategia_2":
                    diccionario[nombre]-=15
                    diccionario[lista_nombres[j]]+=10
        lista_estrategias.pop(0)
        lista_nombres.pop(0)
    return diccionario

    
def quien_gano_el_tateti_facilito(tablero:list[list[chr]])->int:
    ganador:int=0
    res:list[int]=[]
    j:int=0
    while j < len(tablero[0]):
        columna_temporal:list[chr]=[]

        for i in range(len(tablero[0])):
            columna_temporal.append((tablero[i])[j])
        if hay_3_seguidos(columna_temporal) == "si, hay 3 X":
                res.append(1)
        if hay_3_seguidos(columna_temporal) == "si, hay 3 O":
                res.append(2)
        if hay_3_seguidos(columna_temporal) == "si, hay 3 O y tambien 3 X":
                res.append(3)
        j+=1

    if 1 in res and 2 in res:
        ganador = 3
    elif 1 in res:
        ganador = 1
    elif 2 in res:
        ganador = 2
    else:
        ganador = 0

    return ganador


def hay_3_seguidos(columna_temporal:list[chr])->"str":
    res:str=""
    for i in range(2,(len(columna_temporal))):
        if res == "si, hay 3 O":
            if (columna_temporal[i] == 'X') and ('X' == columna_temporal[i-1]) and ('X' == columna_temporal[i-2]):
                res="si, hay 3 O y tambien 3 X"
                
        if res == "si, hay 3 X":
            if columna_temporal[i] == "O"  and "O" == columna_temporal[i-1] and "O" == columna_temporal[i-2]:
                res="si, hay 3 O y tambien 3 X"
        
        if res != "si, hay 3 O y tambien 3 X":       
            if (columna_temporal[i] == 'X') and ('X' == columna_temporal[i-1]) and ('X' == columna_temporal[i-2]):
                res="si, hay 3 X"
            if columna_temporal[i] == "O"  and "O" == columna_temporal[i-1] and "O" == columna_temporal[i-2]:
                    res="si, hay 3 O"
            
    return res