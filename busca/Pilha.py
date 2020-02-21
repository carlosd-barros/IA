class No():
    def __init__(self, value=None, next=None):
        self.info= value
        self.prox= next

class PilhaD():
    def __init__(self):
        self.prim= self.ult= None
        self.quant= 0

    def push(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor)
        else:
            self.prim = No(valor,self.prim)
        self.quant += 1

    def pop(self):
        if self.quant == 1:
            self.prim= self.ult= None
        else:
            self.prim= self.prim.prox
        self.quant -= 1

    def getTopo(self):
        return self.prim.info

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox
        print("\n")

    def estahVazia(self):
        return self.quant==0