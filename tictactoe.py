def print_taulell(partida):
    print("       0   1   2")
    print(f"   0 | {partida[0][0]} | {partida[0][1]} | {partida[0][2]} |")
    print(f"   1 | {partida[1][0]} | {partida[1][1]} | {partida[1][2]} |")
    print(f"   2 | {partida[2][0]} | {partida[2][1]} | {partida[2][2]} |")

def ha_guanyat(partida):
    # Comprovar files i columnes
    for i in range(3):
        if partida[i][0] == partida[i][1] == partida[i][2] == ' X ':
            return True  
        if partida[0][i] == partida[1][i] == partida[2][i] == ' X ':
            return True 

    # Comprovar diagonals
    if partida[0][0] == partida[1][1] == partida[2][2] == ' X ':
        return True
    if partida[0][2] == partida[1][1] == partida[2][0] == ' X ':
        return True  

    return False


# simbol1 = "X"
# simbol2 = "O"
# j1 = "Yosue"
# j2 = "Alejandro"
# jugador = j1

simbols = ['X','O']
noms = ['Yosue','Alejandro']
jugador = 0

partida = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print_taulell(partida)

while True:
    print(noms[jugador], "jugues tu")
    fila = int(input("Quina fila (0,1,2)? "))
    col = int(input("Quina col (0,1,2)? "))

    partida[fila][col]=simbols[jugador]

    print_taulell(partida)

    

    if ha_guanyat(partida):
        print(noms[jugador], "HAS GUANYAAAAT!!!!")
        break
    if jugador == 0:
        jugador = 1
    else:
        jugador = 0
    


'''

fitxers

def guarda_historial(j1,j2)
    open file 
    genera timestamp (202402161827)
    write(202402161827-j1-j2-qui guanya)
    
def llista_historial()
    open file()
    for.... read
        PRINT 1-    202402161827 ...
        2.202402161827....
        3.202402161827
def recupera_punts(nom)
    return punts 

def guarda_punts(nom, punts)

def compra_punts(nom)
    input(targeta)
    input(caducitat)
    input(punts) 5
    if    API---> openurl
        saldo = recupera_punts(nom)
        saddo = saldo + punts

        guarda_punts(nom,saldo)
    else    
        error







***************************************

3 EN RALLA

mostra menu
   def print_menu()


1-nova partida
input demana nom j1
input jug2

recupera saldo
print saldo
    nova partida x=yosue (11p) vs O=alejandro (17p)
       A   B   C
   1 |   |   |   |
   2 |   |   |   |
   3 |   |   |   |

    yosue, jugues tu. Posicio? B2

       A   B   C
   1 |   |   |   |
   2 |   | X |   |
   3 |   |   |   |

   alejandro, jugues tu. Posicio?


   def print_taulell(partida)






'''