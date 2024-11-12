from recuperatorio import *

def menu():
    while True:
        print("ELECCIONES\n1. CARGAR VOTOS\n2. MOSTRAR VOTOS \n3. MOSTRAR VOTOS DE LA MAÑANA\n4. MENORES VOTOS\n5. TURNO MAS VOTADO\n6. BALLOTAGE \n7. SEGUNDA VUELTA\n8. salir")
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-8\nSu opcion:",1,8)

        if opcion == 1:
            cargar_votos(partido_politico, "EL VOTO NO PUEDE SER INFERIOR A 1; POR FAVOR, REINGRESE LOS VOTOS DE")
        elif opcion == 2:
            mostar_votos(partido_politico)
        elif opcion == 3:
            mostar_votos_turno_manana(partido_politico)
        elif opcion == 4:
            listas_menor_votos(partido_politico)
        elif opcion == 5:
            turno_mas_votado(partido_politico)
        elif opcion == 6:
            ballotage(partido_politico)
        elif opcion == 7:
            print("NO FOUND")
        elif opcion == 8:
            print("fin.")
            break
        limpiar_consola()

menu()
