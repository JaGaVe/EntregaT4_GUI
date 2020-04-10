import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb
#from sense_emu import SenseHat

#sense=SenseHat()
#print(sense.temp)

class Aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title('Monitorización SenseHAT')
        self.ventana1.geometry('480x320')

        #Añadimos un menú para ajustar resolución y otro de información
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1,tearoff=0)
        opciones1.add_command(label='Ventana pequeña',command=self.VentanaPeq)
        opciones1.add_command(label='Ventana mediana',command=self.VentanaMed)
        opciones1.add_command(label='Ventana grande',command=self.VentanaGrand)
        menubar1.add_cascade(label='Tamaño',menu=opciones1)
        opciones2=tk.Menu(menubar1,tearoff=0)
        opciones2.add_command(label='Info',command=self.mostrarInfo)
        menubar1.add_cascade(label='Información',menu=opciones2)

        self.ventana1.mainloop()

    def VentanaPeq(self):
        self.ventana1.geometry('480x320')

    def VentanaMed(self):
        self.ventana1.geometry('640x480')

    def VentanaGrand(self):
        self.ventana1.geometry('1024x768')

    def mostrarInfo(self):
        mb.showinfo('Info','Programa creado para monitorizar entradas de la placa SenseHAT')




app=Aplicacion()