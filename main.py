from Automata import *
from GR import *
from tkinter import END, Frame, Label, Menu, Scrollbar, Tk, filedialog, messagebox,Text, ttk

Lista_Automata=Listar()


'''def Menu_2():
    print("Desea ver un automata? (s/n)")
    opcion=input()
    if opcion=="s":
        Nombre_afd=input("Ingrese nombre del AFD: ")
        nomb=Lista_Automata.getAutomata(Nombre_afd)
        return f"Nombre: {nomb.nombre}\nEstados: {nomb.estados}\nAlfabeto: {nomb.alfabeto}\nEstado inicial: {nomb.estado_inicial}\nEstados de aceptacion: {nomb.estados_aceptacion}\nTransiciones: {nomb.transiciones}"'''

def AFD(nombre,estados,alfabeto,estado_inicial,estados_aceptacion,transiciones):
    lista_automatas = [] # Vacia inicialmente
    
    

    estados_ = estados.split(",") # "A,B,C" -> ["A", "B", "C"]
    alfabeto_ = alfabeto.split(",")
    estados_aceptacion_ = estados_aceptacion.split(",")
    transiciones_ = transiciones.split(";") # A,0,B ; A,1,B ; A,1,C -> ["A,0,B", "A,1,B", "A,1,C"]

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
            t = t.split(",") # ["A,0,B", "A,1,B", "A,1,C"] -> [ ["A", "0", "B"], ["A", "1", "B"], ["A", "1", "C"]
            if(not t[0] in estados_ or not t[2] in estados_):
                print("El origen o el destino de una transicion no esta en el conjunto de estados")
                break
            transiciones__.append(Transicion(t[0], t[1], t[2]))

        automata = Automata(nombre, estados_, alfabeto_, estado_inicial, estados_aceptacion_, transiciones__)
        Lista_Automata.AgregarInicio(automata)
        lista_automatas.append(automata)
        
        '''print("Desea agregar otro automata? (s/n)")
        opcion = input()
        if(opcion == "n"):
            print("Hola")
        else:
            Menu1

    print(Menu_2())'''



        print("Automatas ingresados: ")
        for automata in lista_automatas:
            print(automata)


        
def Cadena():
    estado=0
    tran=0
    destino=0
    origenes=[]
    cadena=input("Ingrese cadena: ")
    for caracter in cadena:

        if(caracter in alfabeto):
                if estado==0:
                #if transiciones_[tran][0] in estado_inicial: #["A,0,B", "A,1,B", "A,1,C"]
                    if caracter in transiciones_[tran]:                    
                        print("Caracter: "+caracter+" pasa por estado inicial "+estado_inicial+" y va a "+transiciones_[tran][4])
                        estado=+1
                        origenes.insert(0,tran)
                        tran=0
                        if transiciones_[tran][0] in estados_aceptacion_:
                            print("     tambien es acepetado")
                        continue   
                    else:
                        while caracter not in transiciones_[tran]:
                            tran+=1
                        print("Caracter: "+caracter+" pasa por estado inicial "+estado_inicial+" y va a "+transiciones_[tran][4])
                        estado=+1
                        origenes.insert(0,tran)
                        
                        if transiciones_[tran][0] in estados_aceptacion_:
                            print("     tambien es acepetado")
                        tran=0
                        continue  
                elif estado!=0:
                    while transiciones_[origenes[0]][4]!=transiciones_[tran][0] or not caracter in transiciones_[tran]:
                        tran+=1
                    if caracter in transiciones_[tran]:
                        destino=transiciones_[tran][4]
                        print("Caracter: "+caracter+" pasa por estado "+transiciones_[tran][0]+" y va a "+transiciones_[tran][4])
                        origenes.insert(0,tran)
                        tran=0
                else:
                    print("No puede ser aceptado")
                    break
        
                '''while caracter not in transiciones_[tran]:
                    tran+=1
                print("Caracter: "+caracter+" pasa por estado "+transiciones_[tran][0]+" y va a "+(transiciones_[tran][4]))
                tran=0    '''       



        
        
        




    