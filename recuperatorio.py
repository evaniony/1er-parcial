import random
import os

""" El centro de estudiantes de la UTN FRA realiza unas elecciones para definir a su próximo
presidente/a
Para ello requieren un sistema que logre contar los votos positivos de cada uno de los
alumnos.
Cada partido político va a guardar lo siguiente (Estructurar la matriz como crean
conveniente):
-Nro de lista (número positivo 3 cifras)
-Cantidad de votos (Turno mañana)
-Cantidad de votos (Turno tarde)
-Cantidad de votos (Turno noche)
De las 5 listas que se postularon se requiere lo siguiente: """
def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('clear')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    #validar
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))
    
    return numero    
def inicializar_matriz(fil, col):
    matriz = []
    for _ in range(fil):
        fila = [0] * col
        matriz += [fila]
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end = " ")
        print("")

partido_politico = inicializar_matriz(2, 4)
I_LISTA = 0
I_VOTO_MANANA = 1
I_VOTO_TARDE = 2
I_VOTO_NOCHE = 3


#1. Cargar Votos: Se realiza una carga secuencial de todos los votos de cada una de las cinco listas.
#NOTA: Validar todos los ingresos de datos, evitar votos negativos o nro de lista que no sean
#números de tres cifras.
def cargar_votos(lista: list, error: str) -> list:
    """
    En el bucle for, se toma el largo de de la lista como rango, y la variable 'voto' como iterador.
    Se ingresan los votos a traves de un input de entrada; se validan los valores que no pueden ser menones que 1.
    La tarea se repite con la misma lista y para los 3 turnos.
    Finalmente, guarda esos valores en la matriz lista.
    """
    for voto in range(len(lista)):
        numero_de_lista = random.randint(100, 999)
        votos_manana = int(input(f"PARTIDO {numero_de_lista}. INGRESO DE VOTOS DE LA MANANA: "))
        while votos_manana < 1:
            votos_manana = int(input(f"PARTIDO {numero_de_lista}. {error} LA MANANA:"))

        votos_tarde = int(input(f"PARTIDO {numero_de_lista}. INGRESO DE VOTOS DE LA TARDE: "))
        while votos_tarde < 1:
            votos_tarde = int(input(f"PARTIDO {numero_de_lista}. {error} LA TARDE:"))

        votos_noche = int(input(f"PARTIDO {numero_de_lista}. INGRESO DE VOTOS DE LA NOCHE: "))
        while votos_noche < 1:
            votos_noche = int(input(f"PARTIDO {numero_de_lista}. {error} LA NOCHE:"))

        lista[voto][I_LISTA] = numero_de_lista
        lista[voto][I_VOTO_MANANA] = votos_manana
        lista[voto][I_VOTO_TARDE] = votos_tarde
        lista[voto][I_VOTO_NOCHE] = votos_noche

#2. Mostrar Votos: Muestra en un lindo formato los siguientes datos:
#Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche,Porcentaje Voto:
def calcular_porcentaje(lista: list) -> list:
    total_general = 0
    for i in range(len(lista)):
        votos_manana = lista[i][I_VOTO_MANANA]
        votos_tarde = lista[i][I_VOTO_TARDE]
        votos_noche = lista[i][I_VOTO_NOCHE]
        total_general += votos_manana + votos_tarde + votos_noche

    if total_general == 0:
        return print("No hay votos registrados en ninguna lista.")
    else:
        return total_general
    
def mostar_votos(lista: list) -> list:
    for i in range(len(lista)):
        total_general = calcular_porcentaje(lista)
        suma = lista[i][I_VOTO_MANANA] + lista[i][I_VOTO_TARDE] + lista[i][I_VOTO_NOCHE]
        porcentaje = (suma / total_general) * 100 

        print(f"LISTA: {lista[i][I_LISTA]}\nCANTIDAD DE VOTOS TURNO MANANA: {lista[i][I_VOTO_MANANA]}\nCANTIDAD DE VOTOS TURNO TARDE: {lista[i][I_VOTO_TARDE]}\nCANTIDAD DE VOTOS TURNO NOCHE: {lista[i][I_VOTO_NOCHE]}\nPORCENTAJE: {round(porcentaje, 1)}%")
        print("")

#3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de votos que tuvieron en el turno mañana.
def orden_votos_turno_manana(lista: list) -> list:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][I_VOTO_MANANA] < lista[j][I_VOTO_MANANA]:
                aux = lista[i] 
                lista[i] = lista[j]
                lista[j] = aux 

def mostar_votos_turno_manana(lista: list) -> list:
    orden_votos_turno_manana(lista)
    for i in range(len(lista)):
        print(f"LISTA: {lista[i][I_LISTA]}\nCANTIDAD DE VOTOS TURNO MANANA: {lista[i][I_VOTO_MANANA]}")

#No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos los votos 
def listas_menor_votos(lista: list) -> list:
    total_general = calcular_porcentaje(lista)
    flag = False

    for i in range(len(lista)):
        suma = lista[i][I_VOTO_MANANA] + lista[i][I_VOTO_TARDE] + lista[i][I_VOTO_NOCHE]
        porcentaje = (suma / total_general) * 100

        if porcentaje < 5.0:
            print(f"LISTAS BAJO DEL 5% VOTADAS:\n{lista[i][I_LISTA]}\nCANTIDAD DE VOTOS TURNO MANANA: {lista[i][I_VOTO_MANANA]}\nCANTIDAD DE VOTOS TURNO TARDE: {lista[i][I_VOTO_TARDE]}\nCANTIDAD DE VOTOS TURNO NOCHE: {lista[i][I_VOTO_NOCHE]}")
            flag = True
            if flag == True:
                break

    if flag == False:
            print("No hay listas menores al 5% votadas.")

#5. Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos fueron a votar.
def turno_mas_votado(lista: list) -> list:
    total_manana = 0
    total_tarde = 0
    total_noche = 0

    for fila in lista:
        total_manana += fila[I_VOTO_MANANA]
        total_tarde += fila[I_VOTO_TARDE]
        total_noche += fila[I_VOTO_NOCHE]

    maximo = total_manana #inicio
    
    if total_tarde > maximo or total_tarde == maximo:
        maximo = total_tarde
    
    if total_noche > maximo or total_noche == maximo:
        maximo = total_noche
    
    print(f"TURNOS CON MAS VOTOS:\nTURNO MANANA: {total_manana} VOTOS. \nTURNO TARDE: {total_tarde} VOTOS. \nTURNO NOCHE: {total_noche} VOTOS. ")
            

#6. Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.
def ballotage(lista: list) -> list:
    total_general = calcular_porcentaje(lista)
    flag = False

    for i in range(len(lista)):
        suma = lista[i][I_VOTO_MANANA] + lista[i][I_VOTO_TARDE] + lista[i][I_VOTO_NOCHE]
        porcentaje = (suma / total_general) * 100

        if porcentaje > 50:
            print("No hay segunda vuelta")
            flag = True
            if flag == True:
                break
    if flag == False:
            print(f"Hay segunda vuelta; con {lista[i][I_LISTA]}")

#7. Realizar segunda vuelta:Se encarga de realizar la segunda vuelta electoral con los
""" dos candidatos más votados. Se le pide al usuario la cantidad de alumnos que fueron
a votar en cada turno en la segunda vuelta y de manera random se calculan los votos
del primer y segundo candidato en cada turno. Al final de ello se calcula el porcentaje
final de cada lista y se muestra al ganador de las elecciones.
NOTA: Solo se accede si hay la opción 6 verificó que hay segunda vuelta, sino indicar
que no hubo segunda vuelta.
La cantidad de votos por cada turno debe ser la misma que hubo en la primer vuelta. """


#cargar_votos(partido_politico, "EL VOTO NO PUEDE SER INFERIOR A 1; POR FAVOR, REINGRESE LOS VOTOS DE")
#mostar_votos(partido_politico)
#mostar_votos_turno_manana(partido_politico)
#listas_menor_votos(partido_politico)
#turno_mas_votado(partido_politico)
#ballotage(partido_politico)
