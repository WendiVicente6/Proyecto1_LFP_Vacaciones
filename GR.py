class Gramatica:
    def __init__(self, nombre, no_terminales, terminales, no_terminal_inicial, Aceptacion, producciones):
        self.nombre = nombre
        self.no_terminales = no_terminales
        self.terminales = terminales
        self.no_terminal_inicial = no_terminal_inicial
        self.producciones = producciones
        self.aceptacion=Aceptacion
    def retornarGR(self):
        return self.nombre,self.no_terminales,self.terminales,self.no_terminal_inicial,self.aceptacion,self.producciones
class Produccion:
    def __init__(self, origen, entrada, destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino

    def retorGR(self):
        return self.origen,self.entrada,self.destino

class NodeGR():
    def __init__ (self,dato=None,sig=None):
        self.dato=dato
        self.sig=sig

class ListarGR():
    def __init__(self):
        self.head=None

    def AgregarFinalGR(self,dato):
        if not self.head:
            self.head=NodeGR(dato=dato)
            return
        actual=self.head
        while actual.sig:
            actual=actual.sig 
        actual.sig =NodeGR(dato=dato)
           

    def getGR(self,afd):
        tmp=self.head
           
        while tmp is not None:
            if tmp.dato.nombre.strip()==afd:
                tmp2=tmp.dato
            tmp=tmp.sig
        return tmp2
    def MostrarGR(self):
        tmp=self.head
        tmp2=[]
        while tmp is not None:
            tmp2.append(tmp.dato[0])
            tmp=tmp.sig
        return tmp2
    
    def OperarGR(self,nombre):
        tmp=self.head
        while tmp is not None:
            if tmp.dato[0]==nombre:
                tmp2=tmp.dato
            tmp=tmp.sig
        return tmp2