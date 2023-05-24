class Triangulo:
    lados={}
    def __init__(self,ladoA,ladoB,ladoC):
        # self.ladoA=ladoA
        # self.ladoB=ladoB
        # self.ladoC=ladoC
        self.lados={
            'ladoA':ladoA,
            'ladoB':ladoB,
            'ladoC':ladoC
        }
    def calcularPerimetro(self):
        # self.perimetro=self.ladoA+self.ladoB+self.ladoC
        # self.perimetro=self.lados[1]+self.lados[2]+self.lados[3]
        self.perimetro=0
        for p in self.lados:
            self.perimetro+=self.lados[p]
        print(self.perimetro)
    def getMaiorLado(self):
        self.maiorLado=0
        for p in self.lados:
            if self.lados[p]>self.maiorLado:
                self.maiorLado,qualLado=self.lados[p],p
        print(f"O maior lado é o {qualLado}: {self.maiorLado}")
calculo1=Triangulo(5,30,10)
calculo1.calcularPerimetro()
calculo1.getMaiorLado()
