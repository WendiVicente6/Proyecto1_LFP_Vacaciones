class Automata():
    def __init__(self, nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones # origen, valor y destino
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEstados: {self.estados}\nAlfabeto: {self.alfabeto}\nEstado inicial: {self.estado_inicial}\nEstados de aceptacion: {self.estados_aceptacion}\nTransiciones: {self.transiciones}"

class Node():
    def __init__ (self,dato=None,sig=None):
        self.dato=dato
        self.sig=sig

class Listar():
    def __init__(self):
        self.head=None
    def AgregarInicio(self,dato):
        self.head=Node(dato=dato,sig=self.head)

    def AgregarFinal(self,dato):
        if not self.head:
            self.head=Node(dato=dato)
            return
        actual=self.head
        while actual.sig:
            actual=actual.sig 
        actual.sig =Node(dato=dato)
           

    def getAutomata(self,afd):
        tmp=self.head
           
        while tmp is not None:
            if tmp.dato.nombre.strip()==afd:
                tmp2=tmp.dato
            tmp=tmp.sig
        return tmp2

class Transicion:
    def __init__(self, origen, entrada, destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino
    
    def __str__(self):
        return f"({self.origen}, {self.entrada}; {self.destino})"
    def __repr__(self):
        return str(self.__dict__)