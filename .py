
import pywhatkit
from tkinter import Tk
from tkinter.filedialog import askopenfilename

numPhone = str(input('Ingrese el número: '))
horas = int(input('Ingresa la Hora (formato de 24 horas): '))
minutos = int(input('Ingresa los Minutos: '))

# Abre una ventana de diálogo para que el usuario seleccione un archivo .txt
Tk().withdraw()
filename = askopenfilename(filetypes=[('Archivos de texto', '*.txt')])

with open(filename, 'r') as file:
    mensaje = file.read()

pywhatkit.sendwhatmsg(f"+52{numPhone}", mensaje, horas, minutos)
