# Clase tablero
import numpy as np
import random

class tablero:

    def __init__(self, player, board=np.full((10,10), " ")):
        self.player = player
        self.board=board
    
    def vidas(self):
        lives = np.count_nonzero(np.char.count(self.board, 'O')) # contador de vidas, cuando uno llegue a 0 se acaba el juego
        return lives

    def disparo(self, radar): # diparos sobre el tablero de los barcos (self) y pintamos el resultado en radar, que será otro mapa
        print('Selecciona las coordenadas donde quieres disparar.')
        self.eleccoords()

        if self.board[x:x+1,y:y+1] == "O":
            self.board[x:x+1,y:y+1] = 'X'
            radar.board[x:x+1,y:y+1] = 'X' # pintamos en el tablero de disparos
            k = 0
            for i in [x-1, x, x+1]:
                for j in [y-1, y, y+1]:
                    if self.board[i:i+1, j:j+1].size == 0: #comprobamos que no se salga del mapa a buscar
                        continue
                    elif self.board[i:i+1,j:j+1] == 'O': # comprobamos si sigue habiendo algún trozo de barco en los alrededores, porque no puede haber barcos pegados
                        k += 1
                    elif self.board[i:i+1,j:j+1] == 'X':
                        for a in [i-1, i, i+1]:
                            for b in [j-1, j, j+1]:
                                if self.board[i:i+1, j:j+1].size == 0: #comprobamos que no se salga del mapa a buscar
                                    continue
                                elif self.board[a:a+1,b:b+1] == 'O':
                                    k += 1
            if k > 0: # si hay algún trozo de barco que solo sea tocado
                print('Tocado')
                return self.disparo(radar)
            elif k == 0:
                print('Tocado y hundido.') # si no hay nada alrededor que sea tocado y hundido
                if self.vidas() == 0:
                    return
                return self.disparo(radar)
        elif self.board[x:x+1,y:y+1] == ' ':
            self.board[x:x+1,y:y+1] = '+'
            radar.board[x:x+1,y:y+1] = '+'
            print('Agua')
        elif self.board[x:x+1,y:y+1] == 'X' or self.board[x:x+1,y:y+1] == '+':
            print("Ya has disparado aquí, prueba en otro sitio.")
            return(self.disparo(radar))

    def dispmaquina(self, radar): # lo mismo de arriba pero para la máquina, que dispare aleatoriamente
        self.coords()

        if self.board[x:x+1,y:y+1] == "O":
            self.board[x:x+1,y:y+1] = 'X'
            radar[x:x+1,y:y+1] = 'X' # pintamos en el mapa de disparon también
            k = 0
            for i in [x-1, x, x+1]:
                for j in [y-1, y, y+1]:
                    if self.board[i:i+1, j:j+1].size == 0: #comprobamos que no se salga del mapa a buscar
                        continue
                    if self.board[i:i+1,j:j+1] == 'O': # comprobamos si sigue habiendo algún trozo de barco en los alrededores, porque no puede haber barcos pegados
                        k += 1
            if k > 0: # si hay algún trozo de barco que solo sea tocado
                print('Turno de la máquina.\nTocado')
                return self.dispmaquina(radar)
            elif k == 0:
                print('Turno de la máquina.\nTocado y hundido.') # si no hay nada alrededor que sea tocado y hundido
                if self.vidas() == 0:
                    return
                return self.dispmaquina(radar)
        elif self.board[x:x+1,y:y+1] == ' ':
            self.board[x:x+1,y:y+1] = '+'
            radar.board[x:x+1,y:y+1] = '+'
            print('Turno de la máquina.\nAgua')
        elif self.board[x:x+1,y:y+1] == 'X' or self.board[x:x+1,y:y+1] == '+':
            return(self.dispmaquina(radar))
        
    def genbarcos(self):
        global manauto
        if self.player == 'Jugador':
            manauto = input('Introduce 1 para colocar los barcos manualmente o 2 para hacerlo automáticamente:')
        elif self.player == 'Máquina':
            manauto = '2'
        listab = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4] # esloras de los barcos
        while len(listab) > 0:
            try:
                global lbarco
                if manauto == '1':
                    print('Te quedan', listab.count(1), 'barcos de 1 eslora.')
                    print('Te quedan', listab.count(2), 'barcos de 2 esloras.')
                    print('Te quedan', listab.count(3), 'barcos de 3 esloras.')
                    print('Te quedan', listab.count(4), 'barcos de 4 esloras.')
                    print(self.board)
                    lbarco = int(input("Introduce la eslora del barco (entre 1 y 4 casillas). Introduce 0 para volver al modo automático."))
                    if lbarco == 0:
                        break
                    self.eleccoords()
                elif manauto == '2':
                    lbarco = np.random.choice(listab)
                    self.coords()
                
                else:
                    print('Escoge una de las 2 opciones.')
                    continue
                self.orien()
            except:
                print("Introduce un número del 1 al 4.")
                continue
            if lbarco in listab:
                listab.remove(lbarco)
        if lbarco == 0:
            return self.genbarcos()

    def coords(self):
        global x
        global y
        global contador
        contador = [] # vamosa crear una lista que almacene las 4 orientaciones futuras por cada coordenada
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    
        #print(x, y)
        if  self.board[x:x+1,y:y+1] == "X" or self.board[x:x+1,y:y+1] == '+':
            return self.coords()

    def eleccoords(self): # elegir coordenadas por un input
        global x
        global y
        letrax = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9} # cambiamos de letra a número
        try:
            a=input('Introduce una letra de la A a la J para la coordenada x:')
            if a not in letrax: # lo mismo pero con las letras
                print('Una letra de la A a la J.')
                return self.eleccoords()
            x=letrax[a]
            b = int(input('Introduce un número del 1 al 10 para la coordenada y:'))
            if b < 1 or b > 10: # comprobamos que sea una corrdenada dentro del tablero
                print('Un número del 1 al 10.')
                return self.eleccoords()
            y=b-1

            if self.board[x:x+1,y:y+1] == "X" or self.board[x:x+1,y:y+1] == '+':
                print('Ya has disparado aquí.')
                return self.eleccoords()

        except:
            print('Introduce un número del 1 al 10.')
            return self.eleccoords()
    
    def norte(self):
        if x < lbarco-1: # si la longitud del barco es mayor que lo que resta de tablero por arriba, que nos de otra
            return self.orien()
        for i in range(x-lbarco,x+2):
            for j in range(y-1,y+2): #buscamos alrededor de toda la zona del barco para comprobar que no haya otros
                if self.board[i:i+1,j:j+1].size == 0: #si detecta una casilla fuera del borde nos da un array vacío, lo que no cuenta como barco
                    continue
                if self.board[i:i+1,j:j+1] == "O" or self.board[i:i+1,j:j+1] == "X": # si detecta barco o sale del tablero que empiece de nuevo
                    return self.orien()
        self.board[x-lbarco+1:x+1,y:y+1] = "O" # subimos posiciones en la columna igual a la longitud del barco
    
    def sur(self):
        if x > 10-lbarco: # si la longitud del barco es mayor que lo que resta de tablero por abajo, que nos de otra
            return self.orien()
        for i in range(x-1,x+lbarco+1):
            for j in range(y-1,y+2):
                if self.board[i:i+1,j:j+1].size == 0:
                    continue
                if self.board[i:i+1,j:j+1] == "O" or self.board[i:i+1,j:j+1] == "X": # si detecta barco o sale del tablero que empiece de nuevo
                    return self.orien()
        self.board[x:x+lbarco,y:y+1] = "O" # bajamos posiciones en la columna igual a la longitud del barco

    def este(self):
        if y > 10-lbarco: # si la longitud del barco es mayor que lo que resta de tablero por la derecha, que nos de otra
            return self.orien()
        for j in range(y-1,y+lbarco+1):
            for i in range(x-1,x+2):
                if self.board[i:i+1,j:j+1].size == 0:
                    continue
                if self.board[i:i+1,j:j+1] == "O" or self.board[i:i+1,j:j+1] == "X": # si detecta barco o sale del tablero que empiece de nuevo
                    return self.orien()
        self.board[x:x+1,y:y+lbarco] = "O" # lbarco posiciones a la derecha

    def oeste(self):
        if y < lbarco-1: # si la longitud del barco es mayor que lo que resta de tablero por la izquierda, que nos de otra
            return self.orien()
        for j in range(y-lbarco,y+2):
            for i in range(x-1,x+2):
                if self.board[i:i+1,j:j+1].size == 0:
                    continue
                if self.board[i:i+1,j:j+1] == "O" or self.board[i:i+1,j:j+1] == "X": # si detecta barco o sale del tablero que empiece de nuevo
                    return self.orien()
        self.board[x:x+1,y-lbarco+1:y+1] = "O" # 4 posiciones a la izquierda

    def orien(self):
        if np.count_nonzero(self.board == 'O') > 60: #para que no entre en un bucle infinito si hay poco sitio y no encuentra
            return print("Hay demasiados barcos ya.")
    
        if len(contador) == 4: # si todas las coordenadas han sido almacenadas es porque esa coordenada no sirve, que nos de otra
            #print("Estas coordenadas no sirven.")
            self.coords()
            return self.orien()
    
        # orientación NSEO -> 1234
        if manauto == '2':
            ori = random.randint(1,4)
        elif manauto == '1':
            try:
                ori = int(input('Introduce un número del 1 al 4 para la orientación:\n1 --> N\n2 -- S\n3 --> E\n4 --> O'))
                if ori > 4 or ori < 1:
                    print('Un número del 1 al 4.')
                    return self.orien()
            except:
                print('Un número del 1 al 4.')
                return self.orien()

        if ori in contador: # si la orientación ha sido almacenada en la lista es que ya se ha probado con ella
            return self.orien()
        contador.append(ori) # metemos la orientación una vez hemos comprobado que no está

        # poner barco en la orientación que salga
        try:
            if ori == 1: # norte
                self.norte()

            elif ori == 2: # sur
                self.sur()

            elif ori == 3: # este
                self.este()

            elif ori == 4: # oeste
                self.oeste()
        except RecursionError: # para que no se quede dando vueltas sin parar
            return print("No encuentra sitio.")