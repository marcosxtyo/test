from classtabl import tablero
import numpy as np

tablero1_1 = tablero('Jugador', board=np.full((10,10), " ")) #tablero del jugador con barcos
tablero1_2 = tablero('Disparos jugador', board=np.full((10,10), " ")) #tablero donde el jugador ver los disparos efectuados
tablero2_1 = tablero('Máquina', board=np.full((10,10), " ")) #tablero de la máquina con barcos
tablero2_2 = tablero('Disparos máquina', board=np.full((10,10), " ")) #tablero donde la máquina ve sus disparos

tablero1_1.genbarcos()
tablero2_1.genbarcos()


while True:
    opciones = input('''
Introduce 1 para disparar.
Introduce 2 para ver el mapa.
Introduce 3 para salir
''')

    if opciones == '1':
        tablero2_1.disparo(tablero1_2)
        tablero1_1.dispmaquina(tablero2_2)
        if tablero1_1.vidas() == 0 or tablero2_1.vidas() == 0:
            break

    elif opciones == '2':
        print(f'Tablero de barcos:\n{tablero1_1.board}')
        print(f'Tablero de disparos:\n{tablero1_2.board}')

    elif opciones == '3':
        break

if tablero1_1.vidas() == 0:
    print('La máquina gana.')

elif tablero2_1.vidas() == 0:
    print('Ganaste.')

elif tablero1_1.vidas() > 0 or tablero2_1.vidas() > 0:
    print('Saliste del juego.')