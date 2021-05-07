import tkinter

import numpy as np

tablero = np.zeros((3,3)).astype(int)


print(tablero)

listaT=['0']

def revisarGanador():

    ganador = ''
    salida = np.sum(tablero, axis=1)
    nuevoarray = []
    for r in range(0,2):
        if int(salida[r]) == 9:
            ganador = 'Gano el jugador 1 "X"'
        elif int(salida[r]) == 12:
            ganador = 'Gano el jugador 2 "O"'
    diagonalSum = int(tablero[0, 0]) + int(tablero[1, 1]) + int(tablero[2, 2])
    diagonalSumInv = int(tablero[2,0]) + int(tablero[1, 1]) + int(tablero[0,2])

    if diagonalSum == 9 or diagonalSumInv == 9:
        ganador = 'Gano el jugador 1 "X"'
    elif diagonalSum == 12 or diagonalSumInv == 12:
        ganador = 'Gano el juagador 2 "O"'

    for x in range(0,3):
        sumaColumna = 0
        for y in range(0,3):
            sumaColumna = sumaColumna + tablero[y, x]
        nuevoarray.append(sumaColumna)

    for a in range(0,2):
        if nuevoarray[a] == 9:
            ganador = 'Gano el jugador 1 "X"'
        elif nuevoarray[a] == 12:
            ganador = 'Gano el jugador 2 "O"'

    print (ganador)
    txtresult.set(ganador)




def ResetGame():
    text1.set('')
    text2.set('')
    text3.set('')
    text4.set('')
    text5.set('')
    text6.set('')
    text7.set('')
    text8.set('')
    text9.set('')
    for i in range(0,2):
        for j in range(0,2):
            tablero[i,j] = 0

    print(tablero)

def cambiartexto1():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text1.set('X')
        tablero[0,0] = 3
        listaT[0]=1
    elif int(listaT[0]) == 1:
        text1.set('O')
        tablero[0,0] = 4
        listaT[0]=0
    revisarGanador()
    print(tablero)
def cambiartexto2():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text2.set('X')
        tablero[0, 1] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text2.set('O')
        tablero[0, 1] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)
def cambiartexto3():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text3.set('X')
        tablero[0, 2] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text3.set('O')
        tablero[0, 2] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)
def cambiartexto4():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text4.set('X')
        tablero[1, 0] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text4.set('O')
        tablero[1, 0] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)

def cambiartexto5():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text5.set('X')
        tablero[1, 1] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text5.set('O')
        tablero[1, 1] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)
def cambiartexto6():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text6.set('X')
        tablero[1, 2] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text6.set('O')
        tablero[1, 2] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)
def cambiartexto7():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text7.set('X')
        tablero[2, 0] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text7.set('O')
        tablero[2, 0] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)
def cambiartexto8():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text8.set('X')
        tablero[2, 1] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text8.set('O')
        tablero[2, 1] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)
def cambiartexto9():
    print(listaT[0])
    if int(listaT[0]) == 0:
        text9.set('X')
        tablero[2, 2] = 3
        listaT[0] = 1
    elif int(listaT[0]) == 1:
        text9.set('O')
        tablero[2, 2] = 4
        listaT[0] = 0
    revisarGanador()
    print(tablero)


if __name__ == '__main__':

    ventana = tkinter.Tk()
    ventana.title("TOTITO")

    ventana.geometry('500x500')



    text1 = tkinter.StringVar()
    text1.set('')
    text2 = tkinter.StringVar()
    text2.set('')
    text3 = tkinter.StringVar()
    text3.set('')
    text4 = tkinter.StringVar()
    text4.set('')
    text5 = tkinter.StringVar()
    text5.set('')
    text6 = tkinter.StringVar()
    text6.set('')
    text7 = tkinter.StringVar()
    text7.set('')
    text8 = tkinter.StringVar()
    text8.set('')
    text9 = tkinter.StringVar()
    text9.set('')



    button_1 = tkinter.Button(ventana, textvariable=text1,command=cambiartexto1)
    button_1.place(x=60, y=40, width=100, height=30)

    button_2 = tkinter.Button(ventana, textvariable=text2,command=cambiartexto2)
    button_2.place(x=180, y=40, width=100, height=30)

    button_3 = tkinter.Button(ventana, textvariable=text3,command=cambiartexto3)
    button_3.place(x=300, y=40, width=100, height=30)

    button_4 = tkinter.Button(ventana, textvariable=text4,command=cambiartexto4)
    button_4.place(x=60, y=90, width=100, height=30)

    button_5 = tkinter.Button(ventana, textvariable=text5,command=cambiartexto5)
    button_5.place(x=180, y=90, width=100, height=30)

    button_6 = tkinter.Button(ventana, textvariable=text6,command=cambiartexto6)
    button_6.place(x=300, y=90, width=100, height=30)

    button_7 = tkinter.Button(ventana, textvariable=text7,command=cambiartexto7)
    button_7.place(x=60, y=140, width=100, height=30)

    button_8 = tkinter.Button(ventana, textvariable=text8,command=cambiartexto8)
    button_8.place(x=180, y=140, width=100, height=30)


    button_9 = tkinter.Button(ventana, textvariable=text9,command=cambiartexto9)
    button_9.place(x=300, y=140, width=100, height=30)

    button_r = tkinter.Button(ventana, text='Reset Game' ,command=ResetGame)
    button_r.place(x=200, y=190, width=100, height=30)

    txtresult = tkinter.StringVar()
    txtresult.set('¡EL ganador es!...........')
    result = tkinter.Label(ventana, textvariable = txtresult)
    result.place(x=175, y=250, width=125, height=50)




    tkinter.mainloop()



