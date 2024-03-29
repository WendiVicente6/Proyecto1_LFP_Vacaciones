from tkinter import END, Entry, Label, Menu, Text, Tk, filedialog, messagebox, ttk,Button,Toplevel,Frame,StringVar
from main import *
from GramaticasRegulares import *




class VentanaAFD(Toplevel):
    
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("CREACION AFD")
        self.geometry("500x500")
        inicio=Label(self,text="INGRESE DATOS")
        inicio.pack()
        self.Contenido()
        
    
    def Contenido(self):
        Frame_AFD=Frame(self)
        Frame_AFD.pack()

        Nombre=StringVar()
        Nombre_AFD=Label(Frame_AFD,text="Nombre: ")
        Nombre_AFD.grid(row=1,column=1)
        txtNombre=Entry(Frame_AFD, textvariable=Nombre)
        txtNombre.grid(row=1,column=2)

        Estados=StringVar()
        Estados_AFD=Label(Frame_AFD,text="Estados: ")
        Estados_AFD.grid(row=2,column=1)
        txtEstados=Entry(Frame_AFD, textvariable=Estados)
        txtEstados.grid(row=2,column=2)

        Alfabeto=StringVar()
        Alfabeto_AFD=Label(Frame_AFD,text="Alfabeto: ")
        Alfabeto_AFD.grid(row=3,column=1)
        txtAlfabeto=Entry(Frame_AFD,textvariable=Alfabeto)
        txtAlfabeto.grid(row=3,column=2)

        Inicial=StringVar()
        Inicial_AFD=Label(Frame_AFD,text="Estado Inicial: ")
        Inicial_AFD.grid(row=4,column=1)
        txtInicial=Entry(Frame_AFD,textvariable=Inicial)
        txtInicial.grid(row=4,column=2)

        Aceptacion=StringVar()
        Aceptacion_AFD=Label(Frame_AFD,text="Estado Aceptacion: ")
        Aceptacion_AFD.grid(row=5,column=1)
        txtAceptacion=Entry(Frame_AFD,textvariable=Aceptacion)
        txtAceptacion.grid(row=5,column=2)

        Trans=StringVar()
        Trans_AFD=Label(Frame_AFD,text="Transiciones: ")
        Trans_AFD.grid(row=6,column=1)
        txtTrans=Entry(Frame_AFD,textvariable=Trans)
        txtTrans.grid(row=6,column=2)

        Boton_AFD=Button(Frame_AFD,text="Guardar AFD",command=lambda:AFD(Nombre.get(),Estados.get(),Alfabeto.get(),Inicial.get(),Aceptacion.get(),Trans.get()))
        Boton_AFD.grid(row=7,column=2)



class VentanaAFD_Cadena(Toplevel):
    Lista_Automata=Listar()
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.title("VALIDACIÓN CADENA")
        self.geometry("500x500")
        inicio=Label(self,text="INGRESE CADENA")
        inicio.pack()
        self.Contenido()
        
    
    def Contenido(self):
        Frame_AFD2=Frame(self)
        Frame_AFD2.pack()   

        disponible=Label(Frame_AFD2,text="AFD Disponibles")
        disponible.grid(row=5,column=1)
        

        combo = ttk.Combobox(Frame_AFD2,state="readonly",values=Lista_Automata.Mostrar())
        combo.grid(row=6,column=2)

        Lbcadena=Label(Frame_AFD2,text="Ingrese Cadena: ")
        Lbcadena.grid(row=7,column=1)
        
        cadena=StringVar()
        txtcadena=Entry(Frame_AFD2,textvariable=cadena)
        txtcadena.grid(row=8,column=2)

        Boton_AFD_Ayuda=Button(Frame_AFD2,text="Ayuda(Ver Grafo)",command=lambda:GrafoAFD(combo.get()))
        Boton_AFD_Ayuda.grid(row=9,column=2)

        Boton_AFD=Button(Frame_AFD2,text="Validar Cadena",command=lambda:Cadena(cadena.get(),combo.get()))
        Boton_AFD.grid(row=10,column=2) 

        Boton_AFD=Button(Frame_AFD2,text="Mostrar Ruta",command=lambda:CadenaRuta(cadena.get(),combo.get()))
        Boton_AFD.grid(row=11,column=2) 

class VentanaAFD_Reporte(Toplevel):
    Lista_Automata=Listar()
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.title("Generar Reporte")
        self.geometry("500x500")
        self.Contenido()
        
    
    def Contenido(self):
        Frame_AFD2=Frame(self)
        Frame_AFD2.pack()   

        combo = ttk.Combobox(Frame_AFD2,state="readonly",values=Lista_Automata.Mostrar())
        combo.grid(row=6,column=2)

        Boton_AFD=Button(Frame_AFD2,text="Generar Reporte",command=lambda:GrafoAFD(combo.get()))
        Boton_AFD.grid(row=10,column=2)

#------------------GR--------------------------------------------------------
        
class VentanaGR(Toplevel):
    
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("CREACION GR")
        self.geometry("500x500")
        inicio=Label(self,text="INGRESE DATOS")
        inicio.pack()
        self.Contenido()
        
    
    def Contenido(self):
        Frame_AFD=Frame(self)
        Frame_AFD.pack()

        Nombre=StringVar()
        Nombre_AFD=Label(Frame_AFD,text="Nombre: ")
        Nombre_AFD.grid(row=1,column=1)
        txtNombre=Entry(Frame_AFD, textvariable=Nombre)
        txtNombre.grid(row=1,column=2)

        Estados=StringVar()
        Estados_AFD=Label(Frame_AFD,text="No Terminales: ")
        Estados_AFD.grid(row=2,column=1)
        txtEstados=Entry(Frame_AFD, textvariable=Estados)
        txtEstados.grid(row=2,column=2)

        Alfabeto=StringVar()
        Alfabeto_AFD=Label(Frame_AFD,text="Terminales: ")
        Alfabeto_AFD.grid(row=3,column=1)
        txtAlfabeto=Entry(Frame_AFD,textvariable=Alfabeto)
        txtAlfabeto.grid(row=3,column=2)

        Inicial=StringVar()
        Inicial_AFD=Label(Frame_AFD,text="No terminal Inicial ")
        Inicial_AFD.grid(row=4,column=1)
        txtInicial=Entry(Frame_AFD,textvariable=Inicial)
        txtInicial.grid(row=4,column=2)


        Trans=StringVar()
        Trans_AFD=Label(Frame_AFD,text="Producciones: ")
        Trans_AFD.grid(row=6,column=1)
        txtTrans=Entry(Frame_AFD,textvariable=Trans)
        txtTrans.grid(row=6,column=2)

        Boton_AFD=Button(Frame_AFD,text="Guardar AFD",command=lambda:GR(Nombre.get(),Estados.get(),Alfabeto.get(),Inicial.get(),Trans.get()))
        Boton_AFD.grid(row=7,column=2)



class VentanaGR_Cadena(Toplevel):
    Lista_AutomataGR=ListarGR()
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.title("VALIDACIÓN CADENA")
        self.geometry("500x500")
        inicio=Label(self,text="INGRESE CADENA")
        inicio.pack()
        self.Contenido()
        
    
    def Contenido(self):
        Frame_AFD2=Frame(self)
        Frame_AFD2.pack()   

        disponible=Label(Frame_AFD2,text="GR Disponibles")
        disponible.grid(row=5,column=1)
        

        combo = ttk.Combobox(Frame_AFD2,state="readonly",values=Lista_AutomataGR.MostrarGR())
        combo.grid(row=6,column=2)

        Lbcadena=Label(Frame_AFD2,text="Ingrese Cadena: ")
        Lbcadena.grid(row=7,column=1)
        
        cadena=StringVar()
        txtcadena=Entry(Frame_AFD2,textvariable=cadena)
        txtcadena.grid(row=8,column=2)

        Boton_GR_AYUDA=Button(Frame_AFD2,text="Ayuda (Ver Grafo)",command=lambda:GrafoGR(combo.get()))
        Boton_GR_AYUDA.grid(row=9,column=2)

        Boton_AFD=Button(Frame_AFD2,text="Validar Cadena",command=lambda:CadenaGR(cadena.get(),combo.get()))
        Boton_AFD.grid(row=10,column=2) 

        Boton_AFD=Button(Frame_AFD2,text="Mostrar Ruta",command=lambda:CadenaRutaGR(cadena.get(),combo.get()))
        Boton_AFD.grid(row=11,column=2) 

class VentanaGR_Reporte(Toplevel):
    Lista_AutomataGR=ListarGR()
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.title("Generar Reporte")
        self.geometry("500x500")
        self.Contenido()
        
    
    def Contenido(self):
        Frame_AFD2=Frame(self)
        Frame_AFD2.pack()   

        combo = ttk.Combobox(Frame_AFD2,state="readonly",values=Lista_AutomataGR.MostrarGR())
        combo.grid(row=6,column=2)

        Boton_AFD=Button(Frame_AFD2,text="Generar Reporte",command=lambda:GrafoGR(combo.get()))
        Boton_AFD.grid(row=10,column=2)

#--------------------CARGAS MASIVAS-------------------------------------------------

class VentanaArchivoAFD(Toplevel):
    Lista_Automata=Listar()
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.title("CARGAR ARCHIVO AFD")
        self.geometry("500x500")
        inicio=Label(self,text="CARGAR ARCHIVO AFD")
        inicio.pack()
        Frame_AFD2=Frame(self)
        Frame_AFD2.pack()  

        Boton_Cargar_AFD=Button(Frame_AFD2,text="Buscar Archivo",command=lambda:self.AbrirArchivo())
        Boton_Cargar_AFD.pack()
        self.label_file_explorer = Label(Frame_AFD2, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue") 
        self.label_file_explorer.pack() 

    def AbrirArchivo(self):
        
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files",  "*.afd*"), ("all files", "*.*"))) 
        self.label_file_explorer.configure(text="File Opened:\n "+filename) 
        Datos=[]
        with open(filename) as archivo:
            No_Linea=0
            Transi=""
            for linea in archivo:
                No_Linea+=1
                
                if No_Linea<=5:
                    Nueva=linea.replace("\n","")
                    Datos.append(Nueva)
                    continue
                else:
                    
                    if linea!="%\n" and linea!="\n":
                        Transi=Transi+linea.replace(";",",")

                    else:
                        Datos.append(Transi.replace("\n",";"))
                        Tran=Datos[5]
                        

                        AFDArchivo(Datos[0],Datos[1],Datos[2],Datos[3],Datos[4],Tran.rstrip(Tran[-1]))
                        Datos.clear()
                        No_Linea=0
                        Transi=""

class VentanaArchivoGR(Toplevel):
    Lista_AutomataGR=ListarGR()
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.title("CARGAR ARCHIVO GR")
        self.geometry("500x500")
        inicio=Label(self,text="CARGAR ARCHIVO GR")
        inicio.pack()
        Frame_AFD2=Frame(self)
        Frame_AFD2.pack()  

        Boton_Cargar_AFD=Button(Frame_AFD2,text="Buscar Archivo",command=lambda:self.AbrirArchivo())
        Boton_Cargar_AFD.pack()
        self.label_file_explorer = Label(Frame_AFD2, text = "GRAMATICAS REGULARES", width = 100, height = 4, fg = "blue") 
        self.label_file_explorer.pack() 

    def AbrirArchivo(self):
        
        filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.gre*"), 
                                                       ("all files", 
                                                        "*.*"))) 
        self.label_file_explorer.configure(text="File Opened:\n "+filename) 
        Datos=[]
        with open(filename) as archivo:
            No_Linea=0
            Transi=""
            for linea in archivo:
                No_Linea+=1
                
                if No_Linea<=4:
                    Nueva=linea.replace("\n","")
                    Datos.append(Nueva)
                    continue
                else:
                    
                    if linea!="%\n" and linea!="\n":
                        Transi=Transi+linea.replace("\n",";")

                    else:
                        Datos.append(Transi)
                        Tran=Datos[4]
                        GR_Archivo(Datos[0],Datos[1],Datos[2],Datos[3],Tran.rstrip(Tran[-1]))
                        Datos.clear()
                        No_Linea=0
                        Transi=""

        

                     


    
    



ventana=Tk()

ventana.title("Proyecto 1")
ventana.geometry("700x200")
Datos=Label(text="Wendi Paulina Vicente Pérez"+"\n"+" Carnet: 202106484")
Datos.pack()

notebook=ttk.Notebook(ventana)
notebook.pack(fill="both",expand="yes")

pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
pes2=ttk.Frame(notebook)
notebook.add(pes0,text="Modulo AFD")
notebook.add(pes1,text="Modulo GR")
notebook.add(pes2,text="Modulo Cargar Archivo")
Label(pes0,text="PROYECTO 1 LFP")

Boton=Button(pes0,text="CREAR AFD",bg="white",width=15,height=5,font="Poppins")
Boton.bind("<Button>",lambda e:VentanaAFD(pes0))
Boton.grid(row=2,column=0,padx=5,pady=10)
Boton2=Button(pes0,text="EVALUAR CADENA",bg="white",width=25,height=5,font="Poppins")
Boton2.bind("<Button>",lambda i:VentanaAFD_Cadena(pes0))
Boton2.grid(row=2,column=1,padx=5,pady=10)
Boton3=Button(pes0,text="GENERAR REPORTE AFD",bg="white",width=25,height=5,font="Poppins",command=lambda:VentanaAFD_Reporte(pes0))
Boton3.grid(row=2,column=3,padx=5,pady=10)

Boton4=Button(pes1,text="CREAR GR",bg="white",width=15,height=5,font="Poppins")
Boton4.bind("<Button>",lambda e:VentanaGR(pes1))
Boton4.grid(row=2,column=0,padx=5,pady=10)
Boton5=Button(pes1,text="EVALUDAR CADENA",bg="white",width=25,height=5,font="Poppins")
Boton5.bind("<Button>",lambda i:VentanaGR_Cadena(pes1))
Boton5.grid(row=2,column=1,padx=5,pady=10)
Boton6=Button(pes1,text="GENERAR REPORTE GR",bg="white",width=25,height=5,font="Poppins",command=lambda:VentanaGR_Reporte(pes1))
Boton6.grid(row=2,column=3,padx=5,pady=10)

Boton7=Button(pes2,text="CARGAR AFD",bg="white",width=15,height=5,font="Poppins")
Boton7.bind("<Button>",lambda e:VentanaArchivoAFD(pes1))
Boton7.grid(row=2,column=0,padx=5,pady=10)

Boton8=Button(pes2,text="CARGAR GR",bg="white",width=15,height=5,font="Poppins")
Boton8.bind("<Button>",lambda e:VentanaArchivoGR(pes1))
Boton8.grid(row=2,column=1,padx=5,pady=10)

ventana.mainloop()

    
