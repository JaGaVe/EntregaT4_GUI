#IMPORTANTE: En tk se utilizan bucles recurrentes con "ventanax.after", especificando función a ejecutar y tiempo de refresco en ms.
#NO se usan bucles while o for, o congelarán la interfaz
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb
from sense_emu import SenseHat
from sense_emu import SenseStick
import time
import datetime

class Aplicacion():
    def __init__(self):
        self.sense=SenseHat()
        self.ventana1=tk.Tk()
        self.ventana1.title("Monitorización SenseHAT")
        self.ventana1.geometry("960x540")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        #Estas listas servirán para graficar
        self.listaT=[]
        self.listaP=[]
        self.listaH=[]

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

        #Añadir gráfica en el notebook 2

        self.ventana1.mainloop()
    
    def control(self):
        
        self.label1=tk.Label(self.labelframe1,text="Periodo (ms): 1000")
        self.label1.grid(column=0,row=1, sticky='NW')

        self.txtboton1=tk.StringVar()
        self.txtboton1.set('Iniciar')
        self.boton1=tk.Button(self.labelframe1,text=self.txtboton1.get(),command=self.ChangeB,bg='green')
        self.boton1.grid(column=0,row=0, pady=10,columnspan=2)    

    def medidas(self):

        self.entry3=tk.Entry(self.labelframe2,width=15)
        self.entry3.insert(0,str(self.sense.temperature))
        self.entry3.grid(row=0,column=1)

        self.seleccion1=tk.IntVar()
        self.seleccion1.set(1)

        self.radio1=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion1, value=1,command=self.MostrarDatos)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Presión", variable=self.seleccion1, value=2,command=self.MostrarDatos)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion1, value=3,command=self.MostrarDatos)
        self.radio3.grid(column=2, row=1)

    def arbol(self):
        self.scroll1 = tk.Scrollbar(self.labelframe3, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(self.labelframe3, yscrollcommand=self.scroll1.set)
        self.tree.grid(column=0,row=0,columnspan=3)

        self.scroll1.configure(command=self.tree.yview)         
        self.scroll1.grid(column=4, row=0, sticky='NS')

        self.tree['columns'] = ('valor', 'tipo', 'fecha')
        self.tree.heading('#0', text='Num')
        self.tree.heading('valor', text='Valor')
        self.tree.heading('tipo', text='Tipo')
        self.tree.heading('fecha', text='Fecha/Hora')

        self.boton2=tk.Button(self.labelframe3,text='Limpiar',command=self.ClearTree)
        self.boton2.grid(column=2,row=1)
        self.boton3=tk.Button(self.labelframe3,text="Calcular media",command=self.Average)
        self.boton3.grid(column=0,row=1)

        self.seleccion2=tk.IntVar()
        self.checkbutton1=tk.Checkbutton(self.labelframe3,text='Añadir a la lista',variable=self.seleccion2)
        self.checkbutton1.grid(column=1,row=1)

    def MostrarDatos(self): #Defino self.a y self.tipo para pasarlo al tree, y añado a la lista los elementos para la media e imprimirlos
        if self.seleccion1.get()==1:
            self.listaH,self.listaP,self.listaH=[],[],[]    #REINICIAMOS LAS LISTAS PARA QUE OCURRA LO MISMO EN LA GRÁFICA
            self.a=self.sense.temp
            self.tipo="Temperatura"
            self.listaT.append(self.a)
        
        if self.seleccion1.get()==2:
            self.listaH,self.listaP,self.listaH=[],[],[]
            self.a=self.sense.pressure
            self.tipo="Presión"
            self.listaP.append(self.a)

        if self.seleccion1.get()==3:
            self.listaH,self.listaP,self.listaH=[],[],[]
            self.a=self.sense.humidity
            self.tipo="Humedad"
            self.listaH.append(self.a)

        self.entry3.delete(0,tk.END)
        self.entry3.insert(0,str(self.a))

    def ChangeB(self):         #Para cambiar botón e iniciar toma de datos
        if self.txtboton1.get()=="Iniciar":
            self.txtboton1.set('Parar')
            self.boton1.config(bg='red',text=self.txtboton1.get())
        else:
            self.txtboton1.set("Iniciar")
            self.boton1.config(bg='green',text=self.txtboton1.get())
        self.TomarDatos()

    def TomarDatos(self):
        if self.txtboton1.get()=="Parar":
            self.MostrarDatos()
        cont=1
        if self.seleccion2.get()==1 and self.txtboton1.get()=="Parar":
            fyh=datetime.datetime.now()     #Fecha y hora
            self.tree.insert('', 0, text='Muestra '+str(cont), values=(self.a,self.tipo,fyh.strftime("%Y-%m-%d %H:%M:%S")))
            cont=+1

        self.ventana1.after(1000,self.TomarDatos)   #Bucle recurrente

    def ClearTree (self):   #También vacía las listas
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    def Average (self):
        t,p,h=[],[],[]
        x=self.tree.get_children()       #Recupera los id's del tree
        for item in x:
            dicc=self.tree.set(item)    #Recupera el diccionario de una línea del tree
            if dicc['tipo']=='Temperatura':
                t.append(float(dicc['valor']))
            if dicc['tipo']=='Presión':
                p.append(float(dicc['valor']))
            if dicc['tipo']=='Humedad':
                h.append(float(dicc['valor']))
        if t==[]:
            mostrarT="No se han tomado valores de temperatura\n"
        else:
            avgT=round(sum(t)/len(t),2)
            mostrarT="La media de la temperatura de la tabla es: "+str(avgT)+' C\n'
        if p==[]:
            mostrarP="\nNo se han tomado valores de presión\n"
        else:
            avgP=round(sum(p)/len(p),2)
            mostrarP="\nLa media de la presión de la tabla es: "+str(avgP)+' mbar\n'
        if h==[]:
            mostrarH="\nNo se han tomado valores de humedad"
        else:
            avgH=round(sum(h)/len(h),2)
            mostrarH="\nLa media de la humedad de la tabla es: "+str(avgH)+'%'
        mb.showinfo('Media',mostrarT+mostrarP+mostrarH)
        

    def VentanaPeq(self):
        self.ventana1.geometry("854x480")

    def VentanaMed(self):
        self.ventana1.geometry("960x540")

    def VentanaGrand(self):
        self.ventana1.geometry("1280x720")

    def mostrarInfo(self):
        mb.showinfo("Info","Programa creado para monitorizar valores de entrada de la placa SenseHAT")


app=Aplicacion()
