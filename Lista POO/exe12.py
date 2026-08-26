class ContaInvestimento:

    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionarJuros(self):
        juros = self.saldo * self.taxaJuros
        self.saldo += juros


conta = ContaInvestimento(1000, 0.10)

conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()

print(f"Saldo final: R$ {conta.saldo:.2f}")