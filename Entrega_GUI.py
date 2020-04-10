import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb
#from sense_emu import SenseHat
#from sense_emu import SenseStick

"""sense=SenseHat()
print(sense.temp)"""

class Aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Monitorización SenseHAT")
        self.ventana1.geometry("480x320")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        #Añadimos un menú para ajustar resolución y otro de información
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1,tearoff=0)
        opciones1.add_command(label="Ventana pequeña",command=self.VentanaPeq)
        opciones1.add_command(label="Ventana mediana",command=self.VentanaMed)
        opciones1.add_command(label="Ventana grande",command=self.VentanaGrand)
        menubar1.add_cascade(label="Tamaño",menu=opciones1)
        
        opciones2=tk.Menu(menubar1,tearoff=0)
        opciones2.add_command(label="Info",command=self.mostrarInfo)
        menubar1.add_cascade(label="Información",menu=opciones2)

        #Ahora añadimos las páginas
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Monitorización")

        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text='Gráfica')

        self.cuaderno1.grid(column=0, row=0)    #Si no añades esto, no aparece el notebook

        #Añadir labelframes
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Control")        
        self.labelframe1.grid(column=0, row=1,pady=10)
        self.control()

        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Medidas")        
        self.labelframe2.grid(column=0, row=2, padx=5, pady=10)
        self.medidas()

        self.labelframe3=ttk.LabelFrame(self.pagina1,text="Lista")
        self.labelframe3.grid(column=0, row=3, padx=5, pady=10)
        self.arbol()    

        self.ventana1.mainloop()
    
    def control(self):
        self.boton1=tk.Button(self.labelframe1,text="Iniciar")
        self.boton1.grid(column=0,row=0, pady=10,columnspan=2)
        self.label1=tk.Label(self.labelframe1,text="Tiempo de simulación:")
        self.label1.grid(column=0,row=1, sticky='NW')
        self.label2=tk.Label(self.labelframe1,text="Intervalo:")
        self.label2.grid(column=0,row=2, sticky='NW')
        
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.labelframe1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=1)

        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.labelframe1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=2)

        self.labelxx=tk.Label(self.pagina1,text="Aquí ira un CANVAS", bg='red')
        self.labelxx.grid(column=2,row=0,rowspan=2,sticky='NSEW',padx=5)

    
    def medidas(self):

        self.dato3=tk.StringVar()
        self.entry3=tk.Entry(self.labelframe2,width=15,textvariable=self.dato3,state='readonly')
        self.entry3.grid(row=0,column=1)
        #self.dato3.set('HolaMundo') Así se modifica el entry

        #Los radiobutton, PONERLE COMMAND PARA QUE CAMBIE EL ENTRY                                      !!!!
        self.seleccion1=tk.IntVar()
        self.seleccion1.set(1)

        self.radio1=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion1, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Presión", variable=self.seleccion1, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion1, value=3)
        self.radio3.grid(column=2, row=1)

    def arbol(self):
        self.scroll1 = tk.Scrollbar(self.labelframe3, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(self.labelframe3, yscrollcommand=self.scroll1.set)
        self.tree.grid(column=0,row=0,columnspan=3)

        self.scroll1.configure(command=self.tree.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')

        self.tree['columns'] = ('valor', 'tipo', 'fecha')
        self.tree.heading('#0', text='Num')
        self.tree.heading('valor', text='Valor')
        self.tree.heading('tipo', text='Tipo')
        self.tree.heading('fecha', text='Fecha/Hora')

        self.boton2=tk.Button(self.labelframe3,text='Limpiar')
        self.boton2.grid(column=0,row=1,sticky='E')
        self.boton3=tk.Button(self.labelframe3,text="Calcular media")
        self.boton3.grid(column=1,row=1)
        self.boton4=tk.Button(self.labelframe3,text="Exportar")
        self.boton4.grid(column=2,row=1,sticky='W')


        self.seleccion2=tk.IntVar()
        self.checkbutton1=tk.Checkbutton(self.labelframe3,text='Añadir a la lista',variable=self.seleccion2)
        self.checkbutton1.grid(column=1,row=2,pady=5)
        

    def VentanaPeq(self):
        self.ventana1.geometry("480x320")

    def VentanaMed(self):
        self.ventana1.geometry("640x480")

    def VentanaGrand(self):
        self.ventana1.geometry("1024x768")

    def mostrarInfo(self):
        mb.showinfo("Info","Programa creado para monitorizar entradas de la placa SenseHAT")


app=Aplicacion()