import time
from pynput import keyboard as kb_input
import os
import winsound

def print_mapa(mapa,color_square):
    global points
    lista = []
    lista.append([color_square+"╔"+("═"*75)+"╗"])
    for j in range(len(mapa)):  
        
        for iii in range(5):
            fila="║"
            for h in range(len(mapa[j])):
                for g in range(len(mapa[j][h][iii])):
                    fila+=mapa[j][h][iii][g]
            fila+= color_square + "║"
            lista.append([fila])

    lista.append(["╚"+("═"*75)+"╝"])
    
    return lista  

def atack_f(mapa,bomba_pos):
    import random

    global atack
    if atack > 1 :
        
        for x in range(1,random.randrange(2,8)):
            num_random = random.randrange(1,14)
            mapa[0][num_random] = bomba
        atack = 0
    else:
        for i in range(len(mapa)):
            for c in range(len(mapa[i])):
                if mapa[i][c] == bomba:
                    if [i,c] not in bomba_pos:
                        bomba_pos.append([i,c])
                    

def move_atack(mapa,bomba_pos):

    global close

    for i in range(len(bomba_pos)):
        if(bomba_pos[i][0] == 2)and(mapa[(bomba_pos[i][0])+1][bomba_pos[i][1]] != bloquePersonaje):
            mapa[bomba_pos[i][0]][bomba_pos[i][1]] = bloqueUp
            mapa[(bomba_pos[i][0])+1][bomba_pos[i][1]] = bomba
            bomba_pos[i] = [(bomba_pos[i][0])+1,bomba_pos[i][1]]

        elif(bomba_pos[i][0] == 4):
            for d in range(len(bomba_pos)):
                if(bomba_pos[i][0] == 4):
                    mapa[(bomba_pos[i][0])][bomba_pos[i][1]] = bloqueDown
                    bomba_pos.remove(bomba_pos[i])
            break

        elif(mapa[(bomba_pos[i][0])+1][bomba_pos[i][1]] == bloquePersonaje):
            mapa[(bomba_pos[i][0])+1][bomba_pos[i][1]] = [[f"{color_piernasPersj}█   █"],[f"{color_piernasPersj} █ █ "],[f"{color_piernasPersj}█████"],[f"{color_piernasPersj} █ █ "],[f"{color_piernasPersj}█ █ █"]]
            close = True
            keyboardInput.stop()
            return
        else:
            mapa[(bomba_pos[i][0])+1][bomba_pos[i][1]],mapa[bomba_pos[i][0]][bomba_pos[i][1]] = mapa[bomba_pos[i][0]][bomba_pos[i][1]],mapa[(bomba_pos[i][0])+1][bomba_pos[i][1]]
            bomba_pos[i] = [(bomba_pos[i][0])+1,bomba_pos[i][1]]
            

def check_key(key):
    global close
    global mapa
    global up

    key = str(key).replace("'", "")
    for m in range(len(mapa)):
        for n in range(len(mapa[m])):
            if(mapa[m][n] == bloquePersonaje):
                current_pos = [m,n]
                new_pos = [m,n]

    if key == "Key.up":
        if(current_pos[0]>2):
            new_pos[0] -= 1 
            up = True
            if(mapa[new_pos[0]][new_pos[1]] != bloqueDown)and(mapa[new_pos[0]][new_pos[1]] != bloqueUp):
                new_pos[0] += 1
                
        
    elif key == "Key.left":
        if(current_pos[1]>1):
            new_pos[1] -= 1  
            if(mapa[new_pos[0]][new_pos[1]] != bloqueDown)and(mapa[new_pos[0]][new_pos[1]] != bloqueUp):
                new_pos[1] += 1 

    elif key == "Key.right":
        if(current_pos[1]<13):
            new_pos[1] += 1
            if(mapa[new_pos[0]][new_pos[1]] != bloqueDown)and(mapa[new_pos[0]][new_pos[1]] != bloqueUp):
                new_pos[1] -= 1

    elif key == "Key.down":
        if(current_pos[0]<4):
            new_pos[0] += 1
            up = False
            if(mapa[new_pos[0]][new_pos[1]] != bloqueDown)and(mapa[new_pos[0]][new_pos[1]] != bloqueUp):
                new_pos[0] -= 1

    elif key == "q":
        close = True

    else:
        None
                          
    mapa[new_pos[0]][new_pos[1]], mapa[current_pos[0]][current_pos[1]] = mapa[current_pos[0]][current_pos[1]], mapa[new_pos[0]][new_pos[1]]

    if(current_pos[0] == 2):
        newList = []
        for t in range(len(mapa[current_pos[0]][current_pos[1]])):
            newLine = []
            for z in range(len(mapa[current_pos[0]][current_pos[1]][t])):
                qw = str(mapa[current_pos[0]][current_pos[1]][t][z]).replace(color_fondo,color_suelo)
                newLine.append(qw)
            newList.append(newLine)
    else:
        newList = []
        for sd in range(len(mapa[current_pos[0]][current_pos[1]])):
            newLine = []
            for af in range(len(mapa[current_pos[0]][current_pos[1]][sd])):
                cc = str(mapa[current_pos[0]][current_pos[1]][sd][af]).replace(color_suelo,color_fondo)
                newLine.append(cc)
            newList.append(newLine)

    mapa[current_pos[0]][current_pos[1]] = newList

color_cabezaPersj = "\x1b[35m"
color_cuerpoPersj = "\x1b[93m"
color_piernasPersj = "\x1b[31m"

color_fondo = "\x1b[104m"
color_suelo = "\x1b[100m"
color_square = "\x1b[0m"


bloqueVacio = [[" " for z in range(5)] for x in range(5)]    
bloqueUp = [[" " for l in range(5)]for b in range(5)]
bloqueDown = [[" " for n in range(5)] for m in range(5)]

bloquePersonaje = [[f" {color_cabezaPersj}███ "],[f"{color_cuerpoPersj}█████"],[f"{color_cuerpoPersj}█████"],[f"{color_cuerpoPersj}█{color_piernasPersj}███{color_cuerpoPersj}█"],[f" {color_piernasPersj}█ █ "]]
mapa = [[bloqueVacio for c in range(15)] for v in range(5)]

bomba = [[f"{color_piernasPersj}█████"],[f"{color_piernasPersj} ███ "],[f"{color_piernasPersj} ███ "],[f"{color_piernasPersj}  █  "],[f"{color_piernasPersj}  █  "]]
bomba_pos = []

for f in range(3):
    for d in range(15):
        mapa[f][d] = bloqueUp

for s in range(3,5):
    for a in range(15):
        mapa[s][a] = bloqueDown

for ff in range(5):
    bloqueUp[ff][0] = color_suelo + " "
    bloqueDown[ff][0] = color_fondo + " "

for f in range(3):
    mapa[f][0] = bloqueUp

for s in range(3,5):
    mapa[s][0] = bloqueDown

mapa[4][10] = bloquePersonaje

mapa[0][3] = bomba

global up
global close
global atack
global points
points = 0
close = False
up = True
firstTime = True
atack = 0
bomba_pos = []
goback = ("\033[F") * 27
clear = lambda: os.system('cls')


winsound.PlaySound("Droplex.wav",winsound.SND_ASYNC)
print("""
        ¿ ? ------------------------- ¿ ?
            A R E   Y O U   R E A D Y
                F U C K I N G
                 P L A Y E R
        ¿ ? ------------------------- ¿ ?
""")
time.sleep(8)
while True:
    if(close == True):
        break
    keyboardInput = kb_input.Listener(check_key)
    keyboardInput.start()

    while keyboardInput.is_alive():
        if(close == True):
            break
        outputs = ["",[["A"] for gh in range(27)]]
        clear()
        while True:       
            if(close == True):
                break  
            time.sleep(.2)   
            atack +=1
            points += 1
            atack_f(mapa,bomba_pos)
            move_atack(mapa,bomba_pos)
            outputs.pop(0)
            output_text = print_mapa(mapa,color_square)
            outputs.append(output_text)

            if(points%1100 == 0):
                winsound.PlaySound("Droplex.wav",winsound.SND_ASYNC)

            if(firstTime == True):
                firstTime = False
                for p in range(27):
                    print(outputs[1][p][0])
            else:
                for b in range(27):
                    if(b == 0):
                        print(goback+outputs[1][b][0])
                    else:
                        print(outputs[1][b][0])



winsound.PlaySound("risa.wav",winsound.SND_ASYNC)
time.sleep(2)
print(f"HAS PERDIDO PRINGADOO !!!! -- {points}")