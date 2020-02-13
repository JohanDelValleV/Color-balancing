import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog

pathIn = ''
interface = Tk()


def openFile():
    global pathIn
    imagenPath = filedialog.askopenfilename(
        title="Seleccionar archivo de video")
    pathIn = imagenPath
    interface.mainloop()


def processImageWithMin():
    minimo = []
    image = cv2.imread(pathIn)
    cv2.imshow('Original', image)
    SB = np.sum(image[:, :, 0])
    SG = np.sum(image[:, :, 1])
    SR = np.sum(image[:, :, 2])

    print(f'SB:{SB}, SG:{SG}, SR:{SR}')

    minimo.append(SB)
    minimo.append(SG)
    minimo.append(SR)

    Smin = np.amin(minimo)
    print(f'Min: {Smin}')
    KB = Smin/SB
    KG = Smin/SG
    KR = Smin/SR

    print(f'KB:{KB}, KG:{KG}, KR:{KR}')

    image[:, :, 0] = image[:, :, 0] * KB
    image[:, :, 1] = image[:, :, 1] * KG
    image[:, :, 2] = image[:, :, 2] * KR

    cv2.imshow('New image', image)
    cv2.waitKey()


def processImageWithMax():
    maximo = []
    image = cv2.imread(pathIn)
    cv2.imshow('Original', image)
    SB = np.amax(image[:, :, 0])
    SG = np.amax(image[:, :, 1])
    SR = np.amax(image[:, :, 2])

    print(f'SB:{SB}, SG:{SG}, SR:{SR}')

    maximo.append(SB)
    maximo.append(SG)
    maximo.append(SR)

    Smax = np.amin(maximo)
    print(f'Max {Smax}')

    KB = Smax/SB
    KG = Smax/SG
    KR = Smax/SR

    print(f'KB:{KB}, KG:{KG}, KR:{KR}')

    image[:, :, 0] = image[:, :, 0] * KB
    image[:, :, 1] = image[:, :, 1] * KG
    image[:, :, 2] = image[:, :, 2] * KR

    cv2.imshow('New image', image)


def processImageWithShades():
    minimo = []
    p = 5.5
    image = cv2.imread(pathIn)
    cv2.imshow('Original', image)
    SB = np.sum(image[:, :, 0]**p)**(1/p)
    SG = np.sum(image[:, :, 1]**p)**(1/p)
    SR = np.sum(image[:, :, 2]**p)**(1/p)

    print(f'SB:{SB}, SG:{SG}, SR:{SR}')

    minimo.append(SB)
    minimo.append(SG)
    minimo.append(SR)

    Smin = np.amin(minimo)
    print(f'Min: {Smin}')
    KB = Smin/SB
    KG = Smin/SG
    KR = Smin/SR

    print(f'KB:{KB}, KG:{KG}, KR:{KR}')

    image[:, :, 0] = image[:, :, 0] * KB
    image[:, :, 1] = image[:, :, 1] * KG
    image[:, :, 2] = image[:, :, 2] * KR

    cv2.imshow('New image', image)
    cv2.waitKey()


Button(interface, text='Seleccionar imagen',
       command=openFile).grid(row=1, column=1)
Button(interface, text='Procesar imagen min',
       command=processImageWithMin).grid(row=1, column=2)
Button(interface, text='Procesar imagen max',
       command=processImageWithMax).grid(row=1, column=3)
Button(interface, text='Procesar imagen escala de grises',
       command=processImageWithShades).grid(row=1, column=4)
interface.mainloop()
