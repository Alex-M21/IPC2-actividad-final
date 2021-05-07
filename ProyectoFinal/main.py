import tkinter

import numpy as np

tablero = np.zeros((3,3))

a = tablero[0][0] == 1
print(a)

def turno(entrada):
    turnoactual = entrada
    if turnoactual == 0:
        turnosiguiente = 1
        return turnosiguiente
    elif turnoactual == 1:
        turnosiguiente = 0
        return turnosiguiente



def reset():
    text1.set('')

    text2.set('')

    text3.set('')

    text4.set('')

    text5.set('')

    text6.set('')

    text7.set('')

    text8.set('')

    text9.set('')


def cambiartexto1():
    turno = 0
    if turno == 0:
        text1.set('X')
    elif turno == 1:
        text1.set('O')
def cambiartexto2():
    turno = 0
    if turno == 0:
        text2.set('X')
    elif turno == 1:
        text2.set('O')
def cambiartexto3():
    turno = 0
    if turno == 0:
        text3.set('X')
    elif turno == 1:
        text3.set('O')
def cambiartexto4():
    turno = 0
    if turno == 0:
        text4.set('X')
    elif turno == 1:
        text4.set('O')
def cambiartexto5():
    turno = 0
    if turno == 0:
        text5.set('X')
    elif turno == 1:
        text5.set('O')
def cambiartexto6():
    turno = 0
    if turno == 0:
        text6.set('X')
    elif turno == 1:
        text6.set('O')
def cambiartexto7():
    turno = 0
    if turno == 0:
        text7.set('X')
    elif turno == 1:
        text7.set('O')
def cambiartexto8():
    turno = 0
    if turno == 0:
        text8.set('X')
    elif turno == 1:
        text8.set('O')
def cambiartexto9():
    turno = 0
    if turno == 0:
        text9.set('X')
    elif turno == 1:
        text9.set('O')


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




    tkinter.mainloop()



