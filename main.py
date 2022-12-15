from Automata import *
from GR import *
from tkinter import END, Frame, Label, Menu, Scrollbar, Tk, filedialog, messagebox,Text, ttk
from graphviz import Digraph

Lista_Automata=Listar()

estados_ = ""
alfabeto_ = ""
estados_aceptacion_ =""
transiciones_ =""
alfabeto=""
estado_inicial=""

def AFD(nombre,estados,alfa,estado_ini,estados_aceptacion,transiciones):
    lista_automatas = [] 
    alfabeto=alfa
    estado_inicial=estado_ini
    

    estados_ = estados.split(",") 
    alfabeto_ = alfabeto.split(",")
    estados_aceptacion_ = estados_aceptacion.split(",")
    transiciones_ = transiciones.split(";") 

    if(not estado_inicial in estados_ and not estados_aceptacion_ in estados_):
        messagebox.showinfo("Error de archivo","VERIFICAR QUE EL ESTADO INICIAL O ESTADO DE ACEPTACION ESTÉ EN EL CONJUNTO DE ESTADOS");
    
    else:

        for estado in estados:
            if(estado in alfabeto_):
                print("El alfabeto no puede ser parte de los estados")
                break
        
        # creacion de transiciones por separado
        transiciones__ = []
        for t in transiciones_:
            t = t.split(",")
            if(not t[0] in estados_ or not t[2] in estados_):
                print("El origen o el destino de una transicion no esta en el conjunto de estados")
                break
            Clase_Transiciones=Transicion(t[0], t[1], t[2])
            transiciones__.append(Clase_Transiciones.retor())

        Clase_automata = Automata(nombre, estados_, alfabeto_, estado_inicial, estados_aceptacion_, transiciones__)
        automata=Clase_automata.retornar()
        Lista_Automata.AgregarFinal(automata)
        lista_automatas.append(automata)
        
        print("Automatas ingresados: ")
        for automata in lista_automatas:
            print(automata)

def AFDArchivo(nombre,estados,alfa,estado_ini,estados_aceptacion,transiciones):
    lista_automatas = [] 
    alfabeto=alfa
    estado_inicial=estado_ini
    

    estados_ = estados.split(",") 
    alfabeto_ = alfabeto.split(",")
    estados_aceptacion_ = estados_aceptacion.split(",")
    transiciones_ = transiciones.split(";") 

    if(not estado_inicial in estados_ and not estados_aceptacion_ in estados_):
        messagebox.showinfo("Error de archivo","VERIFICAR QUE EL ESTADO INICIAL O ESTADO DE ACEPTACION ESTÉ EN EL CONJUNTO DE ESTADOS");
    
    else:

        for estado in estados:
            if(estado in alfabeto_):
                messagebox.showinfo("Advertencia"+"El alfabeto no puede ser parte de los estados")
                break
        
        # creacion de transiciones por separado
        transiciones__ = []
        for t in transiciones_:
            t = t.split(",")
            if(not t[0] in estados_ or not t[2] in estados_):
                messagebox.showinfo("Advertencia","El origen o el destino de una transicion no esta en el conjunto de estados")
                break
            Clase_Transiciones=Transicion(t[0], t[1], t[2])
            transiciones__.append(Clase_Transiciones.retor())

        Clase_automata = Automata(nombre, estados_, alfabeto_, estado_inicial, estados_aceptacion_, transiciones__)
        automata=Clase_automata.retornar()
        Lista_Automata.AgregarFinal(automata)
        lista_automatas.append(automata)
        
        print("Automatas ingresados: ")
        for automata in lista_automatas:
            print(automata)
        
def Cadena(cadena,seleccion):
    Automata=Lista_Automata.Operar(seleccion)
    estado=0
    tran=0
    origenes=[]
    contar_cadena=0
    for caracter in cadena:
        contar_cadena+=1

        if(caracter in Automata[2]):
                if estado==0:

                    if caracter in Automata[5][tran]:                    
                        estado=+1
                        origenes.insert(0,tran)
                        tran=0
                        
                        if len(cadena)==contar_cadena:
                                if Automata[5][tran][2] in Automata[4]:
                                    messagebox.showinfo("Respuesta","Aceptado")
                        continue   
                    else:
                        while caracter not in Automata[5][tran] or tran>=len(Automata[5]):
                            tran+=1
                        if Automata[5][tran][0] in Automata[3]:
                            estado=+1
                            origenes.insert(0,tran)
                            if len(cadena)==contar_cadena:
                                if Automata[5][tran][2] in Automata[4]:
                                    messagebox.showinfo("Respuesta","Aceptado")
                            tran=0
                            continue  
                        else:
                            messagebox.showinfo("Repuesta","No es aceptado")
                elif estado!=0:
                    if len(cadena)==contar_cadena:
                        while Automata[5][origenes[0]][2]!=Automata[5][tran][0] or not caracter in Automata[5][tran]:
                            tran+=1
                        if Automata[5][tran][2] in Automata[4]:
                            destino=Automata[5][tran][2]
                            origenes.insert(0,tran)
                            tran=0
                            messagebox.showinfo("Respuesta","Aceptado")
                        else:
                            messagebox.showinfo("Respuesta","No es aceptado")
                    else:
                        while Automata[5][origenes[0]][2]!=Automata[5][tran][0] or not caracter in Automata[5][tran]:
                            tran+=1
                        if caracter in Automata[5][tran]:
                            destino=Automata[5][tran][2]
                            origenes.insert(0,tran)
                            tran=0
                            
                else:
                    print("No puede ser aceptado")
                    break
        else:
            messagebox.showinfo("Información","Revisar entrada... un caracter no pertenece al alfabeto")
def CadenaRuta(cadena,seleccion):
    Automata=Lista_Automata.Operar(seleccion)
    estado=0
    tran=0
    Ruta=[]
    origenes=[]
    contar_cadena=0
    for caracter in cadena:
        contar_cadena+=1

        if(caracter in Automata[2]):
                if estado==0:
                    if caracter in Automata[5][tran]:                    
                        Ruta.append("Caracter "+caracter+" pasa por estado inicial "+Automata[3]+" y va a "+Automata[5][tran][2])
                        estado=+1
                        origenes.insert(0,tran)
                        tran=0
                        
                        if len(cadena)==contar_cadena:
                                if Automata[5][tran][2] in Automata[4]:
                                    MensajeRuta="\n".join(Ruta)
                                    messagebox.showinfo("Ruta",MensajeRuta)

                        continue   
                    else:
                        while caracter not in Automata[5][tran] or tran>=len(Automata[5]):
                            tran+=1
                        if Automata[5][tran][0] in Automata[3]:
                            Ruta.append("Caracter "+caracter+" pasa por estado inicial "+Automata[3]+" y va a "+Automata[5][tran][2])
                            estado=+1
                            origenes.insert(0,tran)
   
                            if len(cadena)==contar_cadena:
                                if Automata[5][tran][2] in Automata[4]:
                                    MensajeRuta="\n".join(Ruta)
                                    messagebox.showinfo("Ruta",MensajeRuta)
                            tran=0
                            continue  
                        else:
                            print("No es aceptado")
                elif estado!=0:
                    if len(cadena)==contar_cadena:
                        while Automata[5][origenes[0]][2]!=Automata[5][tran][0] or not caracter in Automata[5][tran]:
                            tran+=1
                        if Automata[5][tran][2] in Automata[4]:
                            destino=Automata[5][tran][2]
                            Ruta.append("Caracter: "+caracter+" pasa por estado "+Automata[5][tran][0]+" y va a "+Automata[5][tran][2]+" y termina")
                            origenes.insert(0,tran)
                            tran=0
                            MensajeRuta="\n".join(Ruta)
                            messagebox.showinfo("Ruta",MensajeRuta)
                        else:
                            print("No es aceptado")
                    else:
                        while Automata[5][origenes[0]][2]!=Automata[5][tran][0] or not caracter in Automata[5][tran]:
                            tran+=1
                        if caracter in Automata[5][tran]:
                            destino=Automata[5][tran][2]
                            Ruta.append("Caracter: "+caracter+" pasa por estado "+Automata[5][tran][0]+" y va a "+Automata[5][tran][2])
                            origenes.insert(0,tran)
                            tran=0
                            
                else:
                    print("No puede ser aceptado")
                    break
def GrafoAFD(seleccion):
    Automata=Lista_Automata.Operar(seleccion)
    dot=Digraph(name="Gramatica",encoding='UTF-8',format='pdf',filename='Gramaticas')
    dot.attr(rankdir='LR',layout='dot',shape='circle')
    for ea in Automata[1]:
        if ea in Automata[4]:
            dot.node(name=ea,shape='doublecircle')
        else:
            dot.node(name=ea,shape='circle')
    dot.node('Inicio',shape='plaintext')

    dot.edge('Inicio',''+Automata[3])
    Tran=""
    for es in Automata[5]:
        dot.edge(''+es[0],''+es[2],label=es[1])
        Tran=Tran+"\n"+es[0]+","+es[1]+";"+es[2]


    Datos="Nombre: "+Automata[0]+"\n"+"Estados: "+",".join(Automata[1])+"\n"+"Alfabeto: "+",".join(Automata[2])+"\n"+"Estado Inicial: "+Automata[3]+"\n"+"Estados de aceptación: "+",".join(Automata[4])+"\n"+"Transiciones:"+Tran

    dot.node(Datos,shape='box')
    dot.render(Automata[0],format='pdf',view=True)

    


        
        
        




    