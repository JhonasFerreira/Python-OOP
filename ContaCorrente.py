class ContaCorrete:
    def __init__(self,numero):
        self.numero=numero
        self.saldo=0.0
    def debitar(self,valor):
        self.saldo=self.saldo-valor
    def creditar(self,valor):
        self.saldo=self.saldo+valor

conta1=ContaCorrete('1234')
print(conta1.numero)

conta1.debitar(1000)
print(conta1.saldo)
conta1.creditar(4050)
print(conta1.saldo)