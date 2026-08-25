class ContaCorrente:

    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor


conta1 = ContaCorrente(12345, "Taissa")

print("Número da conta:", conta1.numero)
print("Nome do correntista:", conta1.nome)
print("Saldo:", conta1.saldo)

conta1.deposito(500)

print("\nApós depósito:")
print("Saldo:", conta1.saldo)

conta1.saque(200)

print("\nApós saque:")
print("Saldo:", conta1.saldo)

conta1.alterarNome("Taissa Sahado")

print("\nApós alterar o nome:")
print("Nome do correntista:", conta1.nome)