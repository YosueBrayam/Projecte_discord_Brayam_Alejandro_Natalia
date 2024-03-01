
from login import login

# Códigos de formato ANSI para colores del texto
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'



#Nombre de jugadores


print(f"\033[95mHola jugadors! Benvingut al joc de Tic Tac Toe, on podran guanyar punts per competir.{RESET}")



jugador1 = input("Jugador 1. Quin és el teu nom?: ")
jugador2 = input("Jugador 2. Quin és el teu nom?: ") 

#############TAULA################



def print_taulell(partida):
    print("       0   1   2")
    print(f"   0 | {partida[0][0]} | {partida[0][1]} | {partida[0][2]} |")
    print(f"   1 | {partida[1][0]} | {partida[1][1]} | {partida[1][2]} |")
    print(f"   2 | {partida[2][0]} | {partida[2][1]} | {partida[2][2]} |")

def ha_guanyat(partida, jugador):
   
    for i in range(3):
        if partida[i][0] == partida[i][1] == partida[i][2] == jugador:
            return True 
        if partida[0][i] == partida[1][i] == partida[2][i] == jugador:
            return True 

    
    if partida[0][0] == partida[1][1] == partida[2][2] == jugador:
        return True 
    if partida[0][2] == partida[1][1] == partida[2][0] == jugador:
        return True 

    return False

def es_moviment_valid(partida, fila, col):
    # Comprovar si la casella està buida
    return partida[fila][col] == ' '
    

simbols = ['X', 'O']
noms = [jugador1 , jugador2]
jugador = 0

partida = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_taulell(partida)

moviments_realitzats = 0
max_moviments = 3 * 3  # 3x3 table
#Ubicar la fila 
while True:
    print(noms[jugador], "jugues tu")
    fila = ""
    while fila not in ['0','1','2']:
    
       fila = input("Quina fila (0,1,2)? ")
       if fila not in ['0','1','2']:
           print("El valor ha de ser 0,1,2!!!!")
       else: 
           fila = int(fila)
           break
    #Ubicar la cola
    col = ""
    while col not in ['0','1','2']:

        col = input ("Quina cola (0,1,2)? ")
        if col not in ['0','1','2']:
            print("El valor ha de ser 0,1,2!!!!")
        else:
            col = int(col)
            break
      
      #Detecció de casella ocupada
    if not es_moviment_valid(partida, fila, col):
        print("Moviment no vàlid. La casella ja està ocupada.")
        continue


    
    partida[fila][col] = simbols[jugador]
    moviments_realitzats += 1

    print_taulell(partida)

    if ha_guanyat(partida, simbols[jugador]):
        print(noms[jugador], "HAS GUANYAT!!!!")
        break

    if moviments_realitzats == max_moviments:
        print("Joc Empatat! No hi ha més moviments possibles.")
        break

    if jugador == 0:
        jugador = 1
    else:
        jugador = 0

