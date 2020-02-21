class No(): #NO
    def __init__(self, valor, prox):
        self.info = valor
        self.prox = prox

class FilaD(): #LISTA
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
        else:
            self.ult.prox = self.ult = No(valor,None)
        self.quant += 1

    def remover(self):
        if self.quant == 1:
            self.prim = self.ult= None
        else:
           self.prim = self.prim.prox
        self.quant-=1

    def getPrim(self):
        return self.prim

    def estahVazia(self):
        if self.quant == 0:
            return True
        return False

    def show(self):
        aux = self.prim # Aponta para o NO que contem A
        while aux != None:
            print(aux.info)
            aux = aux.prox