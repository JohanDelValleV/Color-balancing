import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

pathIn = ''
interface = Tk()


combo = ttk.Combobox(interface, values=("Gray-world", "Scale-by-max", "Shades-of-gray"),
                     state="readonly")
combo.current(0)
entry = ttk.Entry(interface)
entry.insert(0, 5.5)
separador = ttk.Separator(interface, orient=tk.HORIZONTAL)


def openFile():
    global pathIn
    imagenPath = filedialog.askopenfilename(
        title="Seleccionar archivo de video", filetypes=[("Image File", '.jpg'), ("Image File", '.png'), ("Image File", '.jpeg')])
    pathIn = imagenPath
    if pathIn == "":
        messagebox.showinfo("¡ERROR!", "Debes seleccionar una imagen")

    interface.mainloop()


def grayWorld():
    minimo = []
    if pathIn == "":
        messagebox.showinfo("¡ERROR!", "Debes seleccionar una imagen")
    else:
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


def scaleByMax():
    maximo = []
    if pathIn == "":
        messagebox.showinfo("¡ERROR!", "Debes seleccionar una imagen")
    else:
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


def shadesOfGray():
    minimo = []
    p = float(entry.get())
    if pathIn == "":
        messagebox.showinfo("¡ERROR!", "Debes seleccionar una imagen")
    else:
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


def checkCombo():
    if combo.get() == "Gray-world":
        grayWorld()
    elif combo.get() == "Scale-by-max":
        scaleByMax()
    elif combo.get() == "Shades-of-gray":
        shadesOfGray()
    elif combo.get() == "":
        messagebox.showinfo("¡ERROR!")


photo = PhotoImage(file=r"btn.png")

Button(interface, text='Seleccionar imagen', image=photo, compound=LEFT,
       command=openFile).grid(row=1, column=1)
Label(interface, text="P").grid(row=1, column=2)
entry.grid(row=1, column=3)
separador.grid(row=1, column=4, sticky=tk.W)
combo.grid(row=1, column=5)
Button(interface, text='Processar imagen',
       command=checkCombo).grid(row=2, column=3)
interface.mainloop()
