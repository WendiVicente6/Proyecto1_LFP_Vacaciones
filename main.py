from Automata import *
from GR import *

lista_automatas = [] # Vacia inicialmente
while(True):
    print("Creacion de un automata")
    nombre = input("Ingrese el nombre del automata: ")
    estados = input("Ingrese los estados del automata separados por una coma: ")
    alfabeto = input("Ingrese el alfabeto del automata separados por una coma: ")
    estado_inicial = input("Ingrese el estado inicial del automata: ")
    estados_aceptacion = input("Ingrese los estados de aceptacion del automata separados por una coma: ")
    transiciones = input("Ingrese las transiciones del automata separados por una coma: ") # origen,valor,destino ; origen,valor,destino ; origen,valor,destino

    estados_ = estados.split(",") # "A,B,C" -> ["A", "B", "C"]
    alfabeto_ = alfabeto.split(",")
    estados_aceptacion_ = estados_aceptacion.split(",")
    transiciones_ = transiciones.split(";") # A,0,B ; A,1,B ; A,1,C -> ["A,0,B", "A,1,B", "A,1,C"]

    if(not estado_inicial in estados_ and not estados_aceptacion_ in estados_):
        print("El estado inicial o los estados de aceptacion no estan en el conjunto de estados")
        continue
    
    # verificar que el alfabeto no sea parte de los estados
    salir = False
    for estado in estados:
        if(estado in alfabeto_):
            print("El alfabeto no puede ser parte de los estados")
            salir = True
            break
    if(salir):
        continue
    
    # creacion de transiciones por separado
    transiciones__ = []
    for t in transiciones_:
        t = t.split(",") # ["A,0,B", "A,1,B", "A,1,C"] -> [ ["A", "0", "B"], ["A", "1", "B"], ["A", "1", "C"]
        if(not t[0] in estados_ or not t[2] in estados_):
            print("El origen o el destino de una transicion no esta en el conjunto de estados")
            salir = True
            break
        transiciones__.append(Transicion(t[0], t[1], t[2]))
        # FORMA DE INGRESO DE TRANSICIONES
        # Manual
        # origen, alfabeto, destino ; origen, alfabeto, destino ; origen, alfabeto, destino

        # Archivo de entrada
        # origen, alfabeto; destino
        # origen, alfabeto; destino
        # origen, alfabeto; destino
    
    if(salir):
        continue

    # Creacion del automata
    automata = Automata(nombre, estados_, alfabeto_, estado_inicial, estados_aceptacion_, transiciones__)
    lista_automatas.append(automata)

    # Preguntar si desea agregar otro automata
    print("Desea agregar otro automata? (s/n)")
    opcion = input()
    if(opcion == "n"):
        break

print("Automatas ingresados: ")
for automata in lista_automatas:
    print(automata)

estado=0
tran=0
cadena=input("Ingrese cadena: ")
for caracter in cadena:

    if(caracter in alfabeto):
        if caracter in transiciones_[tran]:
                if transiciones_[tran][0] in estado_inicial:
                    destino=transiciones_[tran][4]
                    print("Caracter: "+caracter+" pasa por estado inicial "+estado_inicial+" y va a "+destino)
                    if transiciones_[tran][0] in estados_aceptacion_:
                        print("     tambien es acepetado")
                    continue
        while caracter not in transiciones_[tran]:
            tran+=1
        print("Caracter: "+caracter+" pasa por estado "+transiciones_[tran][0]+" y va a "+(transiciones_[tran][4]))
        tran=0
            


        
        
        




    