import math
import random


def fahrenheit_a_celcius(t:float)->float:
    res = ((t-32)*5)/9
    return res

def imprimir_dos_veces(t:str)->str:
    t = t * 2
    return t 

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int)->int:
    res= (comensales * min_cant_de_porciones) / 8
    res= math.ceil(res)
    return res


def alguno_es_0(num1:int,num2:int)->bool:
    res = False
    if num1 == 0 or num2 == 0 :
        res=True
    return res


def ambos_son_0(num1:int, num2:int)->bool:
    res = False
    if num1 == 0 and num2 == 0:
        res = True
    return res

def es_bisiesto(año:int)->bool:
    res = False
    if  año % 4 == 0 and not (año%100 == 0):
        res = True
    elif año%400 == 0:
        res=True
    return res


def devolver_el_doble_si_es_par(n:int)->int:
    res = n 
    if n%2 == 0 :
        res =n*2
    return res

def devolver_valor_si_es_par_sino_el_que_sigue(n:int)->int:
    res=n
    if n%2 != 0 :
        res = n+1
    return res


def lindo_nombre(nombre:str)->str:
    if len(nombre) >= 5 :
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")



def jubilado(sexo:str,edad:int)->str:
    if sexo == "F" :
        if edad >= 60 :
            res = "Andá de vacaciones"
        else:
            res = "Te toca trabajar"
    else:
        if edad >= 65:
            res = "Andá de vaciones"
        else:
            res =  "Te toca trabajar"
    return res


def hasta_10()->str:
    i = 1
    while i < 11 :
        print(i)
        i +=1

def pares_10_40()->str:
    i=10
    while i >=10 and i <= 40 :
        print(i)
        i+=2

def despegue(n:int)-> str:
    i=n
    while i <= n and i >= 1:
        print(i)
        i= i-1
    print("Despegue!")


def viaje_al_pasado(partida:int,llegada:int)->str:
    i = partida - llegada
    while i >= 1 :
        print("Viajó un año al pasado, estamos en el año:"+str(llegada + i))
        i= i-1
    

def buscando_aristoteles(partida:int)->str:
    i = partida + 384
    while i >= 1:
        print("Viajó 20 años al pasado, estamos en el año:"+str(-384+i))
        i = i-20
    

def num_1_10_v2()->str:
    for i in range(1,11):
        print(i)
    


def num_10_40_v2()->str:
    for i in range(10,40,2):
        print(i)

def al_pasado_v2(partida:int,llegada:int)->int:
    for i in range(llegada,partida):
        print("Viajó un año al pasado, estamos en el año:"+str(partida-1))
        partida-=1


def buscando_aristoteles_v2(partida:int)->str:
    for i in range(0,partida+384,20):
        print("Viajó 20 años al pasado, estamos en el año:"+str(partida-20))
        partida-=20
        if (-384+partida)<(-384-partida):
            print("Viajo 20 años al pasado, estamos en el año:"+str(partida+20))



def pertenece(seq:list[int],n:int)->bool:
    res= False
    for i in range (0,len(seq)):
        if n==seq[i]:
            res=True
    return res


def divide_a_todos(seq:list[int], e:int)->bool:
    res=True
    for i in range (0,len(seq),1):
        if (seq[i])%e != 0:
            res=False
    return res

def divide_a_todos_v2(seq:list[int],e:int)->bool:
    res = True
    i = len(seq)-1 
    while i >= 0:
        if (seq[i])%e != 0 :
            res = False
        i-=1
    return res

def suma_total(seq:list[int])->int:
    acumulador = 0
    for i in range(0,len(seq),1):
        acumulador += seq[i]
    return acumulador    


def ordenados(seq:list[int])->bool:
    res=True
    long:int=len(seq)
    for i in range(long):
        if  (i <= (long-2)):
            if seq[i] >= seq[i+1]:
                res=False
    return res

def palabra_larga(seq:list[str])->bool:
    res=False
    for i in range(0,len(seq),1):
        if len(seq[i])>7:
            res=True
    return res

def es_palindromo(s:str)->bool:
    res=True
    a=1
    for i in range(len(s)):
        if s[i]!=s[-a]:
            res=False
        a+=1
    return res

def fortaleza_contrasena(s:str)->str:
    res = "AMARILLA"
    tiene_minusculas = False
    tiene_mayusculas = False
    tiene_digitos = False
    for i in s:
        if i >= 'a' and i <= 'z':
            tiene_minusculas=True
    for i in s:
        if i >= 'A' and i <= 'Z':
            tiene_mayusculas=True
    for i in s:
        if i >='0' and i <= '9':
            tiene_digitos = True
    
    if (len(s)>8) and tiene_minusculas==True and tiene_mayusculas==True and tiene_digitos == True:
        res = "VERDE"

    if len(s) < 5 :
        res = "ROJA"
    return res


def contador_saldo(seq:list[(str,int)])->int:
    saldo_tot = 0
    for i in range(0,len(seq),1):
        if seq[i] [0] == "I":
            saldo_tot += seq[i] [1] 
        if seq[i] [0] == "R":
            saldo_tot -= seq [i] [1]
    return saldo_tot          

def borrarPosicionesPares (lista:list[int]) -> [int]:
    for i in range (0,len(lista)):
        if(i%2==0):
            lista[i]=0
    return lista


def borrarPosicionesPares_v2 (lista:list[int]) -> [int]:
    
    lista_out:list[int] = lista
    for i in range (0,len(lista)):
        if(i%2==0):
            lista_out[i]=0
    return lista_out


def saca_vocales(seq:list[chr])->list[chr]:
    nueva_lista = [] 
    for i in range(0,len(seq),1):
        if not (seq[i]== 'a' or seq[i]== 'e' or seq[i]== 'i' or seq[i]== 'u' or seq[i]== 'o'):
            nueva_lista += seq[i]
    return nueva_lista




def reemplaza_vocales(seq:list[chr])->list[chr]: #si aparece una vocal, la reemplaza con un espacio
    
    for i in range(len(seq)):
        if (seq[i]== 'a' or seq[i]== 'e' or seq[i]== 'i' or seq[i]== 'u' or seq[i]== 'o'):
            seq[i]=" "
    return seq


def da_vuelta_str(seq:list[chr])->list[chr]:
    nueva_palabra:list[chr] = []
    for i in range(len(seq)):
        nueva_palabra+=seq[len(seq)-i-1]
    return nueva_palabra

def eliminar_repetidos(seq:list[chr])->list[chr]:
    sin_repetidos:list[chr]= []
    long:int=len(seq)
    for i in range(0,long,1):
        if not(pertenece_v2(sin_repetidos,seq[i])):
            sin_repetidos.append(seq[i])
    return sin_repetidos


def pertenece_v2(seq:list[chr],n:chr)->bool:
    res= False
    long:int = len(seq)
    for i in range (0,long,1):
        if n==seq[i]:
            res=True
    return res

def aprobado(seq:list[int])->int:
    long:int=len(seq)
    sumatoria_notas=0
    res = 2
    for i in range(long):
        if seq[i] < 4:
            res = 3
    for i in range(long):
        sumatoria_notas+=seq[i]
    if (sumatoria_notas / long) > 7:
        res = 1 
    return res


def ingresar_nombres()->list[str]:
    res:list[str]=[]
    nombre=""
    while (nombre!="listo"):
        nombre=input("ingrese un nombre: ")
        if nombre!="listo":
            res.append(nombre)
    return res

def tracking_sube()->list[(str,int)]:
    res:list[(str,int)]=[]
    operacion=""
    carga=""
    monto_total:int=0
    while operacion!="X":
        operacion=input("¿Que operacion desea realizar? C para cargar, D para descontar, X para terminar la operacion: ")
        if operacion !="X":
            carga=input("Ingrese un monto: ")
            res.append((operacion,carga))
            if operacion == "C":
                monto_total+=int(carga)
            if operacion == "D":
                monto_total-=int(carga)

    print("Su carga final es: " +str(monto_total))
    return res


def siete_y_medio()->list[int]:
    print("Las reglas del juego son las siguientes: Se reparte una carta. Si esa carta vale mas de 7.5, perdió. Ud puede plantarse diciendo 'Me planto' y esperar a que su valor sea el mas proximo a 7,5 de todos los jugadores o continuar.")
    print("El puntaje de las cartas es el que indica el numero expecto 10, 11 y 12 que valen 0,5")
    print("Si desea continuar, se le repartirá otra carta, que se suma al puntaje anterior, y asi continua el juego, hasta que se pase o gane.")
    print("Gana si la sumatoria de sus cartas es exactamente 7,5.")
    comenzar:str=input("¿Comenzamos? ")
    cartas_posibles:list[int]=[0,1,2,3,4,5,6,7,10,11,12]
    historial_cartas:list[int]=[]
    sumatoria_numeros:float=0
    otra_carta="Seguir"
    carta:int=random.choice(cartas_posibles)
    print("Su carta es " +str(carta)+ "!")
    sumatoria_numeros+=carta
    historial_cartas.append(carta)
    while sumatoria_numeros < 7.5 and otra_carta != "Me planto":
        nueva_carta:int=random.choice(cartas_posibles)
        otra_carta=input("¿Desea pedir otra carta o prefiere Plantarse? ")
        if otra_carta != "Me planto":
            if nueva_carta != 10 and nueva_carta != 11 and nueva_carta != 12:
                sumatoria_numeros+=nueva_carta 
                print("Su nueva carta es " +str(nueva_carta)+". Puntaje hasta ahora: "+str(sumatoria_numeros))
            else:
                sumatoria_numeros+=0.5
                print("Su nueva carta es " +str(nueva_carta)+". Puntaje hasta ahora: "+str(sumatoria_numeros))
            historial_cartas.append(nueva_carta)
    if sumatoria_numeros == 7.5:
        print("Ganaste!")
    if sumatoria_numeros > 7.5:
        print("Pasaste los 7.5, perdiste!")
    return historial_cartas


def pertenece_a_cada_uno_V1(seq:list[list[int]],e:int)->list[bool]: #dado un elemento, chequeo si esta en cada una de las listas que conforman seq.
    res:list[bool]=[]
    long:int=len(seq)
    for i in range(long):
            if pertenece(seq[i],e):
                res.append(True)
            else:
                res.append(False)
    return res


def es_matriz(seq:list[list[int]])->bool:
    long:int=len(seq)
    long_fila_0:int=len(seq[0])
    res=True
    for i in range(long):
        long_i:int=len(seq[i])
        if long_i != long_fila_0:
            res=False
    return res


def filas_ordenadas(seq:list[list[int]])->list[bool]:
    res:list[bool]=[]
    long:int=len(seq)
    for i in range(long):
        if not(ordenados(seq[i])):
            res.append(False)
        else:
            res.append(True)
    return res


def sumatoria_rara(d:int,p:int)->list[list[int]]:
    matriz_aleatoria = np.random.randint(0,10, (d,d))
    while p >= 0:
        matriz_aleatoria=(matriz_aleatoria)*(matriz_aleatoria)
        p-=1
    return matriz_aleatoria    

